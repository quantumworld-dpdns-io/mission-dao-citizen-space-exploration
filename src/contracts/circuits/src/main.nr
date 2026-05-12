// Telemetry Integrity Circuit
// Proves hash(payload) == onchain_commitment without revealing raw telemetry data

fn main(payload: Field, commitment: pub Field) -> pub Field {
    let computed = std::hash::pedersen([payload]);
    assert(computed[0] == commitment);
    commitment
}
