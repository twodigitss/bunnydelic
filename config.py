''' -- CONFIGURATION FILE (if it were not more obvious) --
    NOTES:
    1. MAKE SURE your custom ascii does not have weird escape chars. 
    2. Suggest and report bugs or whatever in discussions/issues on github
    
    EXTRA: if you are facing problems with blank spaces in custom ascii, take this
    empty chars made for filling some ascii arts, it will surely fix it
    emptychars="⠀⠀⠀⠀⠀⠀"

'''

#Enables/disables phrases
show_phrase=True

#Indent phrases to left instead right on custom ascii
phraseToLeft=False

#values: normal, italic, bold, underline 
phraseStyle = "normal"

#Items: cpu,de,distro,gpu,host,kernel,model,owner,pkg,ram,shell,uptime,user
display=["distro","user","kernel","shell","pkg","ram","uptime"]

#values: normal, italic, bold, underline
displayStyle = "normal"
informationStyle = "normal"

#Values: off, default, custom
show_ascii="default"

#Values "off" "left" "bottom" 
color_block_position="left"

#Enable/disable color randomization
randomize_colors=True

#Set the color order if randomize_colors is false.
#You can repeat colors, also make sure this list is at least 4 elements long
static_color_set=["purple","red","black","blue","green","white","cyan","yellow"]

#Enables/Disables icons from NerdFonts.com
show_icons=True

#Shows your distro icon instead the stock one in "icons" list
override_distro_icon=True

#Icons that are shown alsongside display variable 󰞅
icons=["󰟀","󰀎","󰒔","󰙀","󰏓","","󱑂","","󰾆","","󰘚","󰳣",""]

#Paste here your ascii
custom_ascii='''
⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⠛⠿⣿⣿
⣿⣿⣿⣿⠋⠀⠀⠀⠀⣀⠀⠀⠈⠙
⣿⣿⣿⢳⣿⡇⠀⠀⠸⣿⡏⠀⠀⠀
⣿⣿⡿⠿⠈⣀⠀⠀⠀⠀⠹⣷⡀⠀
⣿⣿⣦⠀⣜⣿⡄⠀⠀⢤⣶⣿⠇⢸
⣿⣿⣿⡃⠈⠉⠁⠀⠀⠈⠛⠁⠀⠸
⣿⣿⣿⠃⠠⠴⠒⠂⠀⠀⠀⠀⠀⠀
⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴
⣿⣿⣿⣇⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿
⣿⣿⣿⣿⣷⣤⣶⣶⠀⣿⣿⣿⣿⣿
'''

#some random phrases to launch every time its executed
somephrases=[
    "Hellow r/Unixporn! look at this!!",
    "Energy(e) = milk(m) * coffe(c) ^ 2",
    "Welcome back!! hope you enjoy today (:",
    "Hey there! Ready to dive into the day?",
    "Keep calm and be happy today c:",
    "Fridays I go painting in the Louvre!!",
    "Inspired in bunnyfetch!! check it out!",
    "Peace and love for everyone <3",
    "Hey ya!, ready to brighten up the day? (:", 
    "This fetch is owned now by Microsoft",
    "Stay high and spread positive energy!!",
    "Rest in Peace ArchLabs, we will miss you",
]
