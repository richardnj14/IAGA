from random import randint

i = 1
jogo = []

while i <=6:
    nmr = randint(1, 60)
    if nmr not in jogo:
        jogo.append(nmr)
        i += 1

jogo.sort()

print(jogo)