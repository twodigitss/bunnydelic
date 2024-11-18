''' //--// TOGGLEABLES
=================================='''
#Enables/disables phrases
show_phrase = True

#Indent phrases to left instead right on custom ascii
phraseToLeft = True

#Enable/disable color randomization
randomize_colors = True

#Enables/Disables icons from NerdFonts.com
show_icons = True

#Shows your distro icon instead the stock one in "icons" list
override_distro_icon = True


''' //--// STYLES
=================================='''
#Values: off, default, custom
show_ascii = "default"

#Values: "random" (as string) or any number (as integer) as an index inside an array
#Examples: custom_ascii = "random" / custom_ascii = 1 / custom_ascii = 2 / etc.
custom_ascii = "random"

#Values "off", "left", "bottom", "random"
color_block_position = "random"

#this is the phrase style, the entire line will be formated to:
#values: normal, italic, bold, underline 
phraseStyle = "normal"

#this is the prefixes of each line, like Kerner, Distro, etc.
#values: normal, italic, bold, underline
prefixStyle = "normal"

#this is the output after prefixStyle, like your current OS, pkg count, etc.
#values: normal, italic, bold, underline
informationStyle = "normal"


''' //--// INFORMATION SETS
=================================='''
#Displays set information of your choose in this specific order
#Items: cpu,de,distro,gpu,host,kernel,model,owner,pkg,ram,shell,uptime,user
display = [
    "distro",
    "de",
    "user",
    "kernel",
    "shell",
    "ram",
    "uptime",
    #"cpu",
    #"gpu",
    #"host",
    #"model",
    #"owner",
    #"pkg",
]

#Icons that are shown alsongside display variable 󰞅
icons = ["󰟀","󰀎","󰒔","󰙀","󰏓","","󱑂","","󰾆","","󰘚","󰳣",""]

#Set the color order if randomize_colors is false.
#You can repeat colors, also make sure this list is at least 4 elements long
static_color_set = ["purple","red","black","blue","green","white","cyan","yellow"]

#some random phrases to launch every time its executed
somephrases = [
    "Hellow r/Unixporn! look at this!!",
    "Energy(e) = milk(m) * coffe(c) ^ 2",
    "Welcome back!! hope you enjoy today (:",
    "Keep calm and be happy today c:",
    "Fridays I go painting in the Louvre!!",
    "Inspired in bunnyfetch!! check it out!",
    "Peace and love for everyone <3",
    "This fetch is owned now by Microsoft",
    "Rest in Peace ArchLabs, we will miss you",
    "Lorem ipsum dolor sit amet, consectetur",
    "Less than 15% of snakes are venemous",
    "There are 32 muscles in a cat's ear",
    "Jesse... we have to rice",
    "Now playing: Clouds as witnesses",
]

ascii_list=[
#this ascii is index 0
r'''
⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⠄
⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⡄
⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⡇
⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⡇
⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⠃
⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⠄
⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄
⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄
''',
#this ascii is index 1
r'''
⣿⣿⣿⣿⠋⠀⠀⠀⠀⣀⠀⠀⠈⠙
⣿⣿⣿⢳⣿⡇⠀⠀⠸⣿⡏⠀⠀⠀
⣿⣿⡿⠿⠈⣀⠀⠀⠀⠀⠹⣷⡀⠀
⣿⣿⣦⠀⣜⣿⡄⠀⠀⢤⣶⣿⠇⢸
⣿⣿⣿⡃⠈⠉⠁⠀⠀⠈⠛⠁⠀⠸
⣿⣿⣿⠃⠠⠴⠒⠂⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣇⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿
⣿⣿⣿⣿⣷⣤⣶⣶⠀⣿⣿⣿⣿⣿
''',
#this ascii is index 2
r'''
⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤
⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿
⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿
⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿
⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿
⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿
''',
]
