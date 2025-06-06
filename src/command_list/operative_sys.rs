use std::fs::{self, File};
use std::io::{self, BufRead, BufReader};

pub fn get_os() -> io::Result<()>{
    let content: File = fs::File::open("/etc/os-release")?;
    let content: BufReader<File> = BufReader::new(content);

    for line in content.lines(){
        if line.as_ref().unwrap().starts_with("NAME="){
            // println!("Distro: {:?}", line.unwrap().replace("NAME=", "").replace("\"", ""));
            println!("Distro: {}", line.unwrap()
                .replace("NAME=", "")
                .replace("\"", "")
            );
        }
    }
    Ok(())
}

