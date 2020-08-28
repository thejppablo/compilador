import string

palavra = input("insira: ")

chars2Count = [" "]
charsCounter = []
for index, char in enumerate(chars2Count):
    charsCounter.append(palavra.count(chars2Count[index]))

print("total de chars e espaços: ", len(palavra),
        "\nespaços em branco: ", charsCounter[0], "\ncaracteres: ", len(palavra) - charsCounter[0])

