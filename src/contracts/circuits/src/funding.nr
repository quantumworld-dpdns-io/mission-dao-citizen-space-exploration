// Funding Verification Circuit
// Proves sum of private contributions >= public funding threshold
// without revealing individual contribution amounts

fn main(contributions: [Field; 5], threshold: pub Field) -> pub Field {
    let mut total = 0;
    for i in 0..5 {
        total = total + contributions[i];
    }
    assert(total >= threshold);
    total
}
