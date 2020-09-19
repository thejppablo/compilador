import string
def dividir(palavra):
    return [char for char in palavra]

entrada = input("insere ")

minus = dividir(string.ascii_lowercase)
maius = dividir(string.ascii_uppercase)

keys = dict(zip(maius,minus))
keys.update(dict(zip(minus,maius))) # Um dicionario para todas as palavras, para não precisar de 2 if.


newWord = []

for n in entrada:
    if n in keys:
        letra = keys.get(n)
        newWord.append(letra)
    else: # Adicionei esse else para o resto dos caracteres que não estão nas tabelas como por exemplo o espaço.
        newWord.append(n)

palavra = "".join(newWord) # https://www.bernardi.cloud/2012/11/06/python-string-concatenation-vs-list-join/

    
print(newWord)
print(palavra)







