#Options to print this fetch
''' NOTES:
    1. DO NOT make the custom_ascii string into a f-string. It will
       still take care about the inner curly bracets and take them as 
       characters and therefore, will impact the identation for shorter lines.
    2. Due to 1st point, custom ascii arts are colorlesss 
    3. MAKE SURE your custom_ascii does not have weird escape chars. 
    
    EXTRA: if you are facing problems with blank spaces in custom ascii, take this
    empty char made for filling some ascii arts, it will surely fix it
    emptychar="⠀"

'''
#Enables/disables random phrases at the top of the fetch
show_phrase=True

#Enables/disables every ascii art
show_ascii=True

#Enables/Disables icons from NerdFonts.com
show_icons=True

#shows your distro icon instead the stock one in "icons" list
override_distro_icon=True

#Icons that are shown alsongside display variable
icons=["","","󰒔","󰙀","󰏓","",""]

#Shows in order what information is displayed
display=["os","host","kernel","de","pkg","shell","uptime"]

#Values: ["custom" or "default"]
prioritize_ascii="default"

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
    "Welcome back!! hope you enjoy today (:",
    "Hey there! Ready to dive into the day?",
    "Keep calm and be happy today c:",
    "Inspired in bunnyfetch!! check it out!",
    "Peace and love for everyone <3",
    "Hey ya!, ready to brighten up the day? (:", 
    "This fetch is owned now by Microsoft",
    "Stay high and spread positive energy!!",
]
