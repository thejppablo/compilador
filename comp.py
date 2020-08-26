import string
#contadores de quantidade de espaços, caracteres e tamanho da frase, respectivamente.
ct_espaço = 0
ct_char = 0
ct_len = 0

'''
função para dividir cada elemento de uma string e colocalos separados em uma lista
tudo antes do for é appended pra lista que é criada com []  
e em seguida indica se que esse elemento esta dentro do array palavra
'''

def dividir(palavra):
    return [char for char in palavra]

'''
string.printable é uma variavel local da biblioteca string que contem todos os 
chars da tabela ascii + caracteres especiais como pontuação, cifrões, etc.
'''
lista_asc = dividir(string.printable)

espaço = " "

palavra = input("insira ")

lista_palavra = dividir(palavra)

print(lista_palavra)

'''
um loop for que adciona +1 cada vez que n roda o array para no final pegar o tamanho da lista.
Em seguida ele checa se o conteúdo da string contém espaços e caracteres e 
subsequentemente adciona +1 a seus respectivos contadores.
'''
for n in lista_palavra:
    ct_len+=1
    if n in espaço:
        ct_espaço += 1
    elif n in lista_asc:
        ct_char += 1
print("total de chars e espaços: ", ct_len,
      "\nespaços em branco: ", ct_espaço, "\ncaracteres: ", ct_char)

'''
TODO:
-Consertar o bug onde o programa não reconhece o espaço caso eu volte  
a escrita (fase de input no terminal) e de o espaço.
-Criar uma classe pai para o compilador pra facilitar minha vida durante a disciplina

'''


