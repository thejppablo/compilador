import string
import time
import random


times2run = 100
def get_random_string(length):
    letters = string.ascii_letters
    letters += "              "
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str



totalTime1 = []
totalTime2 = []

def dividir(palavra):
        return [char for char in palavra]

minus = dividir(string.ascii_lowercase)
maius = dividir(string.ascii_uppercase)

key_minus = dict(zip(minus,maius))
key_maius = dict(zip(maius,minus))

keys = dict(zip(maius,minus))
keys.update(dict(zip(minus,maius)))


for CurrentRun in range(0, times2run):
    entrada = get_random_string(25000000)

    # Metodo 1
    start1 = time.time()

    newWord = []
    palavra = ""

    for leter in entrada:
        if leter in key_minus:
            letramin = key_minus.get(leter)
            newWord.append(letramin)
        elif leter in key_maius:
            letramai = key_maius.get(leter)
            newWord.append(letramai)
        else: # Adicionei esse else para o resto dos caracteres que não estão nas tabelas como por exemplo o espaço.
            newWord.append(leter)

    for x in newWord:
        palavra+=x

    end1 = time.time()
    totalTime1.append(end1 - start1)

    # Metodo 2
    start2 = time.time()
    newWordM2 = []

    for n in entrada:
        if n in keys:
            letra = keys.get(n)
            newWordM2.append(letra)
        else: # Adicionei esse else para o resto dos caracteres que não estão nas tabelas como por exemplo o espaço.
            newWordM2.append(n)

    palavraM1 = "".join(newWordM2) #https://www.bernardi.cloud/2012/11/06/python-string-concatenation-vs-list-join/

    end2 = time.time()
    totalTime2.append( end2 - start2)
    entrada = ""
    print(CurrentRun)

print("Time1:", sum(totalTime1)/len(totalTime1))
print("Time2:", sum(totalTime2)/len(totalTime2))





