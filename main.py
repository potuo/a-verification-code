from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import randint
import os


def create_cardimg(cardtext, cardtext_color, cardfont="songti.ttf"):
    cardim = Image.new("RGBA", (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(cardim)
    font = ImageFont.truetype(font=cardfont, size=50)
    draw.text((6, 0), text=cardtext, fill=cardtext_color, font=font)
    cardim.save("card.png")


def card_to_main(cx, cy):
    mainim = Image.open("main.png")
    cardim = Image.open("card.png")
    cardim1 = cardim.rotate(randint(-50, 50))
    mainim.paste(cardim1, (cx, cy), cardim1)
    mainim.save("main.png", "PNG")


def create_mainimg(mode, lang, custom=None):
    global cardver

    """
        mode-1:only random numbers,
        mode-2:random numbers and letters,
        mode-3:custom verification cards
    """
    a = 0

    if mode == 1:
        for i in range(lang):
            cardtext_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            cardtext = str(randint(0, 9))
            create_cardimg(cardtext, cardtext_color)
            print(cardtext_color, cardtext)
            card_to_main(5+a, 24)
            a += 42
            cardver += cardtext
        return cardver

    elif mode == 2:
        vertext_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        for i in range(lang):
            cardtext_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            cardtext = vertext_list[randint(0, len(vertext_list)-1)]
            create_cardimg(cardtext, cardtext_color)
            print(cardtext_color, cardtext)
            card_to_main(5 + a, 24)
            a += 42
            cardver += cardtext
        return cardver

    elif mode == 3:
        for i in range(len(custom)):
            cardtext_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            cardtext = custom[i]
            create_cardimg(cardtext, cardtext_color)
            print(cardtext_color, cardtext)
            card_to_main(5 + a, 24)
            a += 42
            cardver += cardtext
        return cardver

    else:
        return "Parameter Error !!!"


def main(mode, lang=4, custom=None):
    global cardver
    cardver = ""
    if mode == 3:
        lang = len(str(custom))
    Image.new("RGBA", (45*lang, 100), (255, 255, 255, 255)).save("main.png")
    create_mainimg(mode, lang, str(custom))
    Image.open("main.png").filter(ImageFilter.EMBOSS).save("cardver.png")
    os.remove("card.png")
    os.remove("main.png")
    return cardver
