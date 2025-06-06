use std::process::{Command, Stdio};
use std::io::{self, Read};

// goal: "lscpu | awk '/Model name/ {print $3, $4, $5, $6}'"

pub fn get_cpu() -> io::Result<()> {

    let lscpu = Command::new("lscpu")
        .stdout(Stdio::piped())
        .spawn()?;

    let awk = Command::new("awk")
        .arg(r#"/Model name/ {print $3, $4, $5, $6}"#)
        .stdin(lscpu.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()?;

    let mut output = String::new();
    awk.stdout.unwrap().read_to_string(&mut output)?;

    println!("CPU Model: {}", output.trim());
    Ok(())
}
