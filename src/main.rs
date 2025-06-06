// STANDARD LIBRARIES
use std::io;

//MODULES
mod command_list;
use command_list::{
    battery, cpu, gpu, hardware,
    operative_sys, packages
};

//PROGRAM
fn input() -> String {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    input.trim().to_string()
}

fn main() {
    battery::get_battery_perc();
    cpu::get_cpu();
    gpu::get_gpu;
    hardware::get_hardware();
    operative_sys::get_os();
    packages::get_packages();
}

/*  EXAMPLE OF OUTPUTS
 *  Less than 15% of snakes are venemous
    (\ /)    (\ /)       Distro:   NixOS
    ( O O)   ( -v-)    󰙀  Desk:     gnome
    c(")(")  c(")(")   󰳣  User:     gwyne
                       󰒔  Kernel:   6.12.31
    (\ /)    (\ /)       Shell:    /run/current-system/sw/bin/zsh
    ( T_T)   ( Uwu)      Ram:      4.5Gb / 11Gb
    c(")(")  c(")(")   󱑂  Uptime:   1 hours, 57 minutes
                       󰾆  Cpu:      Intel(R) Core(TM) i5-1035G1 CPU
                       󰘚  Graphs:   
                         Host:     nixos
                         Device:   VivoBook_ASUSLaptop X712JA_X712JA
                       󰀎  Owner:    nixos gwyne
                       󰏓  Pkgs:     
 * */
