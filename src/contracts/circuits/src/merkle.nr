// Merkle Membership Proof Circuit
// Proves a data hash is included in a published Merkle tree root
// without revealing the full tree

fn main(leaf: Field, index: Field, root: pub Field, proof: [Field; 8]) -> pub Field {
    let computed_root = std::merkle::compute_merkle_root(leaf, index, proof);
    assert(computed_root == root);
    root
}
