// Verifiable data publication proof
// Proves that a dataset hash matches the published hash on-chain

use risc0_zkvm::sha::{Sha256, Digest};

fn main() {
    let dataset: Vec<u8> = risc0_zkvm::io::read();
    let published_hash: Digest = risc0_zkvm::io::read();
    
    let dataset_hash = risc0_zkvm::sha::Sha256::hash_bytes(&dataset);
    assert_eq!(dataset_hash, published_hash, "dataset hash must match published hash");
    
    risc0_zkvm::io::commit(&dataset_hash);
}
