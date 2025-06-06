use std::{
    io::{self, Read}, 
    process::{Command, Stdio}
};

//GOAL: "lspci | grep -iE 'VGA|3D|Display' | awk -F '[:[:space:]]+' '{print $6,$7,$8,$9,$10}'", 

pub fn get_gpu() -> io::Result<()>{

    let lscpu = Command::new("lscpu")
        .stdout(Stdio::piped())
        .spawn()?;

    let grep = Command::new("grep")
        .arg(r#"-iE /Model name/ {print $3, $4, $5, $6}"#)
        .stdin(lscpu.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()?;

    let awk = Command::new("awk")
        .arg(r#"-F '[:[:space:]]+' '{print $6,$7,$8,$9,$10}'"#)
        .stdin(grep.stdout.unwrap())
        .stdout(Stdio::piped())
        .spawn()?;


    let mut output = String::new();
    awk.stdout.unwrap().read_to_string(&mut output)?;

    println!("GPU Model: {}", output.trim());
    Ok(())
}
