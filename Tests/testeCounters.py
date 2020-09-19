import string
import time
import random



times2Run = 100

def get_random_string(length):
    letters = string.ascii_letters
    letters += "              "
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def dividir(palavra):
    return [char for char in palavra]
for x in range (0, times2Run):
  print("Test:",x)
  ct_espaço = 0
  ct_char = 0
  ct_len = 0

  palavra = get_random_string(250000)
  # print("Metodo 1")
  start1 = time.time() #Start is the intial time for total run time of the code 
  espaço = " "
  lista_palavra = dividir(palavra) #Sorting out the letters in the phrase to create an array with all the letters in it.
  lista_asc = dividir(string.printable) #An array of the printable chars

  # Counter of different chars contained in the phrase.
  for n in lista_palavra: 
    ct_len+=1
    if n in espaço:
        ct_espaço += 1
    elif n in lista_asc:
        ct_char += 1

  print("total de chars e espaços: ", ct_len,"\nespaços em branco: ", ct_espaço, "\ncaracteres: ", ct_char)
  end1 = time.time()


  #---------------------------------------------------------------------------------------------
  time1 = []
  time2 = []
  start2 = time.time()
  # print("Metodo 2")

  chars2Count = [" "]
  charsCounter = []
  for index, char in enumerate(chars2Count):
    charsCounter.append(palavra.count(chars2Count[index]))

  # print("total de chars e espaços: ", len(palavra),
  #       "\n espaços em branco: ", charsCounter[0], "\n caracteres: ", len(palavra) - charsCounter[0])
  end2 = time.time()

  time2.append(end2 - start2)
  time1.append(end1 - start1)

print(f"Time 1 = {sum(time1)/len(time1)}\nTime 2 = {sum(time2)/len(time2)}") 