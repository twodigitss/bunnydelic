use std::{
    collections::HashMap, path::Path,
    process::{Command, Stdio},

};

pub fn get_packages(){
    // let packages: Vec<String> = Vec::new();

    //  TODO: manage a better encapsulation, adding the 
    //  commands even.
    let mut pm_files = HashMap::new();
    pm_files.insert("Apt", "/etc/apt/sources.list");
    pm_files.insert("Dnf", "/etc/dnf/dnf.conf");
    pm_files.insert("Pacman", "/etc/pacman.conf");
    pm_files.insert("Nixos", "/etc/nixos/configuration.nix");

    let mut os_pm = "";
    pm_files.iter().for_each(|(key, value)| {
        if Path::new(value).exists() {
            println!("Package Manager: {}", key);
            os_pm = key;
        }
    });


    if os_pm == "Apt" {
        let output = Command::new("dpkg")
            .arg("-l")
            .output()
            .expect("Failed to run dpkg command");

        //TODO: handle how to count without making a mess...
        let count = output.stdout;
        // let count_str = String::from_utf8_lossy(&count);

    } else if os_pm == "Dnf" {
        // Implement Dnf package manager logic here
        let output = Command::new("pacman")
            .arg("-Qq")
            .output()
            .expect("Failed to run pacman command");

    } else if os_pm == "Pacman" {
        // Implement Pacman package manager logic here
        let output = Command::new("pacman")
            .arg("-Qq")
            .output()
            .expect("Failed to run pacman command");

    } else if os_pm == "Nixos" {
        // Implement Nixos package manager logic here
    } else {
        println!("No supported package manager found.");
    } 



}
