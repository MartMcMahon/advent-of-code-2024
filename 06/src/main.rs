use std::clone::CloneToUninit;
use std::fs::File;
use std::io::{self, BufRead, BufReader, Read};
use std::ops::Index;

fn main() -> io::Result<()> {
    let bytes = include_bytes!("test.txt");

    bytes.fi
    // let file = File::open("test.txt")?;
    // let reader = BufReader::new(file);
    // let lines = reader.lines();
    // let width = lines[0]

    // let mut map: Vec<Vec<String>> = Vec::with_capacity(bytes.count() % width);
    // let map = bytes.collect().chunks(width);

    Ok(())
}
// for (n, c) in bytes.enumerate() {
//     let c = c?;
//     match c {

//         let line_n = n % width;

//         _ => {map[line_n][n - (line_n)  ]}
//         // '.' => {}
//         // '#' => {map[n % width][]
//     }
// }

// for (line_number, line) in reader.lines().enumerate() {
//     let line = line?;
//     let width = line.chars().count();

//     line.find("^")
//     line

//     if line.contains("^") || line.contains(">") || line.contains(
//         "v"
//     ) || line.contains("<") {
//         line.g

//     }

//     map.push(vec![line.chars().collect()]);

//     // println!("Line {}: {} characters", line_number + 1, char_count);
// }

// Ok(())
// }
