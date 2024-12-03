use std::{collections::HashMap, fs::File, io::Read};

fn read_file() -> String {
    let mut file = File::open("input.txt").unwrap();
    let mut buf = String::new();
    file.read_to_string(&mut buf).unwrap();
    buf
}

fn main() {
    let input = read_file();
    let lines = input.split('\n');
    let mut l1 = Vec::new();
    let mut l2 = Vec::new();
    for line in lines {
        let l: Vec<&str> = line.split(' ').collect();
        if l.len() < 2 {
            continue;
        }
        l1.push(l[0]);
        l2.push(*l.last().unwrap());
    }

    l1.sort();
    l2.sort();

    let mut score_map: HashMap<&str, i32> = HashMap::new();
    let mut l2_index = 0;
    let mut sim_score = 0;

    for c in 0..l1.len() {
        while l2[l2_index] < l1[c] {
            l2_index += 1;
        }

        if l2_index >= l2.len() {
            break;
        }

        if score_map.get(l1[c]).is_none() {
            let mut instances = 0;
            while l2[l2_index] == l1[c] {
                instances += 1;
                l2_index += 1;
                if l2_index >= l2.len() {
                    break;
                }
            }
            score_map.insert(l1[c], instances);
        }

        sim_score += l1[c].parse::<i32>().unwrap() * score_map[l1[c]];
    }

    println!("{}", sim_score);
}
