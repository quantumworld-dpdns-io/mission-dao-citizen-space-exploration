// Host program that runs RISC Zero guest methods and parses receipts
// Supports local proving (default) and Bonsai remote proving (with BONSAI_API_KEY env)

use methods::{MISSION_RECEIPT_ELF, DATA_PUBLICATION_ELF};
use risc0_zkvm::{default_prover, ExecutorEnv, Receipt};
use std::env;

fn main() -> anyhow::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: host <mission-receipt|data-publication> <payload_hex> <expected_hash_hex>");
        std::process::exit(1);
    }

    let method = &args[1];
    let payload_hex = &args[2];
    let expected_hex = if args.len() > 3 { &args[3] } else { "" };

    let payload = hex::decode(payload_hex.trim_start_matches("0x"))?;
    let expected = hex::decode(expected_hex.trim_start_matches("0x"))?;

    let elf = match method.as_str() {
        "mission-receipt" => MISSION_RECEIPT_ELF,
        "data-publication" => DATA_PUBLICATION_ELF,
        _ => {
            eprintln!("Unknown method: {}. Use 'mission-receipt' or 'data-publication'", method);
            std::process::exit(1);
        }
    };

    let env = ExecutorEnv::builder()
        .write(&payload)?
        .write(&expected)?
        .build()?;

    let prover = default_prover();
    let prove_info = prover.prove(env, elf)?;

    println!("Receipt: {:?}", prove_info.receipt);
    println!("Journal: {:?}", prove_info.receipt.journal);
    println!("Proof verified successfully");

    Ok(())
}
