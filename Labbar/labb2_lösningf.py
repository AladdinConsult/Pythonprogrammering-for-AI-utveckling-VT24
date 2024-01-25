text_strängar = ["Hej", "på", "dig", "!", "Hur", "mår", "du", "?"]
gräns = 7
sammanslagen_sträng = ""


for i in range(gräns + 1):
    sammanslagen_sträng += text_strängar[i] + " "


print(sammanslagen_sträng)