def go(color, text):
    black = "0;30m";
    red = "1;31m";
    green = "1;32m";
    yellow = "1;33m";
    blue = "1;34m";
    purple = "1;35m";
    cyan = "1;36m";
    white = "1;37m";
    clr = "\033[";
    end = "\033[0m\n";
    if color == "black":
        print(clr + black + text + end)
    elif color == "red":
        print(clr + red + text + end)
    elif color == "green":
        print(clr + green + text + end)
    elif color == "yellow":
        print(clr + yellow + text + end)
    elif color == "blue":
        print(clr + blue + text + end)
    elif color == "purple":
        print(clr + purple + text + end)
    elif color == "cyan":
        print(clr + cyan + text + end)
    elif color == "white":
        print(clr + white + text + end)
    else:
        print('\033[1;31mcolorprint: \033[0mInvalid options')
        help()
def help():
    print('\033[1;32mUsable Colors:\033[0m\nblack\nred\ngreen\nyellow\nblue\npurple\ncyan\nwhite\ne.g.: colorprint.go(\'red\', \'text\')')
