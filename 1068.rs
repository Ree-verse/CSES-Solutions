fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    let mut n: u64 = input.trim().parse().unwrap();

    print!("{}", n);

    while n != 1 {
        if n % 2 == 0 {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
        print!(" {}", n);
    }
}
