class ColorsFore:
    """
    colors for the terminal foreground
    """
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37

class ColorsBack:
    """
    colors for the terminal background
    """
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47

class ColorsStyle:
    """
    Styles used for the terminal.
    """
    NONE = 0
    _BRIGHT = 1
    DARK = 2
    ITALIC =3 
    UNDERLINE = 4
    _LIGHTBACK = 5
    _LIGHTBACK2 = 6
    INVERT = 7

class ColorsCode:
    """
    Escape codes used on the terminal.
    """
    prefix = "\x1b["
    postfix = "\x1b[0m"

def colorstr(style="NONE", fore="WHITE", back="BLACK", text=""):
    """
    Formats a string with color codes and returns it.

    :param style: Use none, dark, italic, underline or invert.
    :param fore: Use Black, Red, Green, Yellow, Blue, Purple, Cyan, or White.
    :param back: Use Black, Red, Green, Yellow, Blue, Purple, Cyan, or White.
    :param text: This is the text you wish to format.
    :returns: Returns the text, formatted with the codes needed to produce the colors.
    """
    # Style, Fore, Back.  Set defaults.
    useStyle = ColorsStyle.NONE
    useFore = ColorsFore.WHITE
    useBack = ColorsBack.BLACK
    # make easier to decide.
    style = style.lower().strip()
    fore = fore.lower().strip()
    back = back.lower().strip()
    # figure out the style.
    if style == "dark":
        useStyle = ColorsStyle.DARK
    elif style=="italic":
        useStyle = ColorsStyle.ITALIC
    elif style == "underline":
        useStyle=ColorsStyle.UNDERLINE
    elif style == "invert":
        useStyle = ColorsStyle.INVERT
    #Figure out the foreground.
    if fore == "black":
        useFore = ColorsFore.BLACK
    elif fore == "green":
        useFore = ColorsFore.GREEN
    elif fore == "yellow":
        useFore = ColorsFore.YELLOW
    elif fore == "blue":
        useFore = ColorsFore.BLUE
    elif fore == "purple":
        useFore = ColorsFore.PURPLE
    elif fore == "cyan":
        useFore = ColorsFore.CYAN
    elif fore == "white":
        useFore = ColorsFore.WHITE
    elif fore == "red":
        useFore = ColorsFore.RED
    #Figure out the background.
    if back == "black":
        useBack = ColorsBack.BLACK
    elif back == "green":
        useBack = ColorsBack.GREEN
    elif back == "yellow":
        useBack = ColorsBack.YELLOW
    elif back == "blue":
        useBack = ColorsBack.BLUE
    elif back == "purple":
        useBack = ColorsBack.PURPLE
    elif back == "cyan":
        useBack = ColorsBack.CYAN
    elif back == "white":
        useBack = ColorsBack.WHITE
    elif back == "red":
        useBack = ColorsBack.RED
    colorsOut = ";".join([str(useStyle),str(useFore),str(useBack)])
    valOut = '%s%sm%s%s' % (ColorsCode.prefix,colorsOut,text,ColorsCode.postfix)
    return valOut

def colortxt(fore="WHITE", back="BLACK", text=""):
    """
    Formats a string with color codes and returns it using normal style.

    :param fore: Use Black, Red, Green, Yellow, Blue, Purple, Cyan, or White.
    :param back: Use Black, Red, Green, Yellow, Blue, Purple, Cyan, or White.
    :param text: This is the text you wish to format.
    :returns: Returns the text, formatted with the codes needed to produce the colors.
    """
    return colorstr("none",fore,back,text)

def foretxt(fore="WHITE", text = ""):
    """
    Formats a string with color foreground on black.

    :param fore: Use Black, Red, Green, Yellow, Blue, Purple, Cyan, or White.
    :param text: This is the text you wish to format.
    :returns: Returns the text, formatted with the codes needed to produce the colors.
    """
    return colorstr(fore=fore,text=text)
    