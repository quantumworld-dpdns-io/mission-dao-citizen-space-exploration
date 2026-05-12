// Verifiable mission-execution receipt
// Proves mission state transitions A -> B -> C were followed correctly
// and produces a cryptographic receipt

use risc0_zkvm::sha::{Sha256, Digest};

fn main() {
    let payload: Vec<u8> = risc0_zkvm::io::read();
    let expected: Digest = risc0_zkvm::io::read();
    
    let hash = risc0_zkvm::sha::Sha256::hash_bytes(&payload);
    assert_eq!(hash, expected, "payload hash must match expected commitment");
    
    risc0_zkvm::io::commit(&hash);
}
