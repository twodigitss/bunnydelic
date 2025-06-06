use std::fs;

pub fn get_battery_perc(){
    let path = "/sys/class/power_supply/BAT0/capacity";
    match fs::read_to_string(path){
        Ok(content) => println!("Battery capacity: {}%", content.trim()),
        Err(e) => eprintln!("Error reading battery capacity: {}", e),
    }
    // println!("{}", path);
}
