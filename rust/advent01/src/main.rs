use std::env;
use std::fs;

fn main() {
    env::set_var("RUST_BACKTRACE", "full");
    let file = fs::read_to_string("././././inputs/input01").unwrap();
    
    let result = file.split("\n\n");

    for r in result {
        println!("{}", r);
    }

}