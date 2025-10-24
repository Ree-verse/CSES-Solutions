use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: u64 = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let sequence = input.split_whitespace();

    let mut sum = 0;
    for s in sequence {
        let x: u64 = s.parse().unwrap();
        sum += x;
    }

    let result: u64 = (n + 1) * n / 2;
    println!("{}", result - sum);
}
