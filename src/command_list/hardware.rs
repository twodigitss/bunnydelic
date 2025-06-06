use std::{
    io::{self, Read},
    process::{Command, Stdio}
};

//GOAL: cat /sys/class/dmi/id/product_name

pub fn get_hardware() -> io::Result<()>{
    let cat = Command::new("cat")
        .arg("/sys/class/dmi/id/product_name")
        .stdout(Stdio::piped())
        .spawn()?;

    let mut result = String::new();
    cat.stdout.unwrap().read_to_string(&mut result);

    println!("Physical Machine {}", result);
    Ok(())
}
