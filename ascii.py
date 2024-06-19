from random import randint

def getAscii(index):
    try:
        match index:
            case "random": return ascii_list[ randint(0,len(ascii_list)-1) ]
            case _: return ascii_list[index]
    except OSError as e:
        return ascii_list[0]

ascii_list=[
r'''#this ascii is index 0
⣿⣿⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣿⣿⠄
⣿⣿⠄⠄⠄⠄⠄⠄⠙⠿⣿⣿⣿⣿⣿⠄⢿⣿⣿⡄
⣦⡙⠳⠄⠄⠄⠄⠄⠄⢀⣠⣤⣀⣈⠙⠃⠄⠿⢇⡇
⣿⡇⠄⠄⠄⠄⠄⣠⣶⣿⣿⣿⣿⣿⣿⣷⣆⡀⣼⡇
⢿⣷⡀⠄⢀⣴⣾⣟⠉⠉⠉⠉⣽⣿⣿⣿⣿⠇⢹⠃
⣎⢻⣷⠰⣿⣿⣿⣿⣦⣀⣀⣴⣿⣿⣿⠟⢫⡾⢸⠄
⠿⣧⠙⢷⠙⠻⠿⢿⡿⠿⠿⠛⠋⠉⠄⠂⠘⠁⠞⠄
⠑⣠⣤⣴⡖⠄⠿⣋⣉⣉⡁⠄⢾⣦⠄⠄⠄⠄⠄⠄
''',

r'''#this ascii is index 1
⣿⣿⣿⣿⠋⠀⠀⠀⠀⣀⠀⠀⠈⠙
⣿⣿⣿⢳⣿⡇⠀⠀⠸⣿⡏⠀⠀⠀
⣿⣿⡿⠿⠈⣀⠀⠀⠀⠀⠹⣷⡀⠀
⣿⣿⣦⠀⣜⣿⡄⠀⠀⢤⣶⣿⠇⢸
⣿⣿⣿⡃⠈⠉⠁⠀⠀⠈⠛⠁⠀⠸
⣿⣿⣿⠃⠠⠴⠒⠂⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣇⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿
⣿⣿⣿⣿⣷⣤⣶⣶⠀⣿⣿⣿⣿⣿
''',
r'''#this ascii is index 2
⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤
⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰⢸⣿
⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞⣸⣿
⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻⣿⣿⣿
⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽⣿⣿⣿
⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙⢿
''',
r'''#and so on...
'''
]

