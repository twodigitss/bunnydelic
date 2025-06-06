use std::{io::Read, process::{Command, Stdio}};

//free -h | awk '/^Mem/ {print $3, $2}'
pub fn get_ram(){
    let free_output = Command::new("free")
        .arg("-h")
        .stdout(Stdio::piped())
        .spawn()
        .expect("Failed to execute free command");

    let awk_output = Command::new("awk")
        .arg("/^Mem/ {print $3, $2}")
        .stdin(free_output.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()
        .expect("Failed to execute awk command");

    let mut output = String::new();
    awk_output.stdout.unwrap().read_to_string(&mut output)
        .expect("Failed to read awk output");

    println!("Ram: {}", output.trim());

}
