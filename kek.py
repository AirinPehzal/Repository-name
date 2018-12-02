import pymorphy2
import sys

text = "становлении советской власти Брестском мире экономике и политическом режиме в период гражданской войны"
text_split = text.split(" ")

morph = pymorphy2.MorphAnalyzer()

for a in text_split:
    pars = morph.parse(a)[0]  # метод morph.analyzer возвращает все разборы, с [0] главное
    result = pars.normalized  # нормальная форма, не работает без [0] выше
    sklon = pars.inflect({"gent"})
    lex = pars.lexeme
    text = open("text.txt", "w")
    text.write(str(pars))
    text.write(str(result))
    text.write(str(sklon))
    text.write(str(lex))
text.write("#################")
text.close()