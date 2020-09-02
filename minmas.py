import string
def dividir(palavra):
    return [char for char in palavra]

entrada = input("insere ")

minus = dividir(string.ascii_lowercase)
maius = dividir(string.ascii_uppercase)

key_minus = dict(zip(minus,maius))
key_maius = dict(zip(maius,minus))

newWord = []

for n in entrada:
    if n in key_minus:
        letramin = key_minus.get(n)
        newWord.append(letramin)
    elif n in key_maius:
        letramai = key_maius.get(n)
        newWord.append(letramai)

palavra = ""

for x in newWord:
    palavra+=x
print(newWord)
print(palavra)







