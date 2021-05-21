#criar listas 1 linha
print([2*x+1 for x in range(10)])
print([2*x for x in range(10)])
#from random inport randint
#[valor(randint, input) for x in range(tam lista)]

#(EASY)Dados 3 números, crie uma função minimo_de_3 para calcular o menor dos 3
def minimo_de_3(n1, n2, n3):
  if n1 < n2 and n1 < n3:
    return n1
  elif n2 < n3:
    return n2
  return n3

#(EASY)Dada uma lista de números, crie uma função meu_minimo que retorna o menor deles
def meu_minimo (lista):
  minimo = lista[i]
  for elemento in lista:
    if elemento < minimo:
      minimo = elemento 
    return minimo
  
#(EASY)Dada uma lista de números, crie uma função minha_soma que retorne a soma deles
def minha_soma(lista):
  soma = 0
  for elemento in lista:
    soma += elemento
  return soma

 #(MEDIUM) Dada uma lista de números, crie uma função meu_sort para ordenar a lista (do menor para o maior) e retorná-la
def meu_sort(lista):
  for i in range(len(lista)):
    for j in ranage(i + 1, len(lista)):
      if lista[i] < lista[j]:
        temp = lista[i]
        lista[i] = lista[j]
        lista[j] = temp
      return lista
    
#(HARD) Agora, dada a lista [4,5,0,7,9,5], calcule a média dos dois maiores valores dessa lista.
# Para isso, use as funções que você criou acima - meu_minimo, minha_soma e meu_sort.
# Lembre-se de usar a estrutura [ inicio : fim ] para pegar esses dois valores mínimos.
lista = [4, 5, 0, 7, 9, 5]
sort = meu_sort(lista)
minimo = lista[ :2]
media = minha_soma(minimos) / 2
print(media)

#Em uma linha, imprima a lista de número pares
print(list(map(lambda x: int(x), filter(lambda x: int(x) % 2 == 0, lista_2))))

#Em um linha, imprima a lista de números maiores que 3
print(list(map(lambda x: int(x), filter(lambda x: int(x) > 3, lista_2))))

# Em uma linha, imprima a lista_1 com cada elemento separado por ponto e vírgula (;).
print(str.join(';', map(lambda x: str(x), lista_1)))

# Imprima a média dos valores da lista_2, se possível em uma linha
print((sum(map(lambda x: int(x), lista_2))) / len(lista_2))

# Dada a palavra: "Joao,3,4,8,5,4,10", imprima a média de notas do Joao.
palavra= "Joao, 3, 4, 8, 5, 4, 10"
palavra_com_split = palavra.split(',')
aluno = palavra_com_split[0]
notas = list(map(lambda nota: float(nota), palavra_com_split[1:]))
media = sum(notas)/len(notas)
print(media)

#filtrar a posição
print([lista[x] for x in [pos1, pos2]])

#cria matriz
from random import randint
def cria_matriz(num_linhas, num_colunas):
  matriz = []
  for i in range(num_linhas):
    linhas = []
    for j in range(num_colunas):
      linhas.append(randint(0, 9))
    matriz.append(linhas)
  return matriz
          
#imprime matriz
def imprime_matriz(matriz):
  for i in range(len(matriz)):
    linhas = matriz[i]
    for j in range(len(linhas)):
      print(matriz [i][j], end=" ")
    print()
    
def imprime_uns(num_linhas, num_colunas):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print('1', end=' ')
        print()    
    
def soma_matriz(matrizA, matrizB):
    matrizC = []
    for i in range(len(matrizA)):
        linha = matrizA[i]
        linha_resultado = []
        for j in range(len(linha)):
            linha_resultado.append( matrizA[i][j] * matrizB[i][j] )
        matrizC.append(linha_resultado)
    return matrizC

#easy segunda o professor
with open('./lista_precos.txt', 'r') as arquivo_de_entrada:
    try:
        linhas = arquivo_de_entrada.readlines()
        precos = list(map( lambda x: float(x), linhas))
    except:
        print('deu errado')
    arquivo_de_entrada.close()

with open('./nota_fiscal.txt', 'w') as nota_fiscal:
    linhas_da_nota = []
    for preco in precos:
        linhas_da_nota.append(f'tomate \t {preco}')
    linhas_da_nota.append('====================')
    linhas_da_nota.append(f'Total \t {sum(precos)}')
    # nota_fiscal.writelines(conteudo)
    nota_fiscal.write(str.join('\n', linhas_da_nota))
    nota_fiscal.close()
    
#medium segundo o filipe
produtos = []
precos = []
with open('./lista_de_compras.txt', 'r') as compras:
    try:
        linhas = compras.readlines()
        for linha in linhas:
            [produto, preco] = linha.split(',')
            produtos.append(produto)
            precos.append(float(preco))
    except:
        print('deu ruim')
    compras.close()

with open('./nota_fiscal_plus.txt', 'w') as nota_fiscal:
    linhas_da_nota = []
    for i in range(len(produtos)):
        linhas_da_nota.append(f'{produtos[i]} \t {precos[i]}')
    linhas_da_nota.append('===========')
    linhas_da_nota.append(f'Total \t {sum(precos)}')
    nota_fiscal.write( str.join('\n', linhas_da_nota) )
    nota_fiscal.close()

#hard e nessa eu concordo com o filipe
alunos = []
medias = []
with open('./alunos.txt', 'r') as arquivo_alunos:
    try:
        linhas = arquivo_alunos.readlines()
        for linha in linhas:
            linha_com_split = linha.split(',')
            alunos.append(linha_com_split[0])
            notas = list(map(lambda nota: float(nota), linha_com_split[1:]))
            media = sum(notas)/len(notas)
            medias.append(media)
        print(medias)
    except:
        print('deu ruim')
    arquivo_alunos.close()

with open('./boletim_classe.txt', 'w') as boletim:
    linhas_do_boletim = []
    for i in range(len(alunos)):
        linhas_do_boletim.append(f'{alunos[i]} \t {medias[i]}')
    linhas_do_boletim.append('================')
    aprovados =  len( list( filter(lambda media: media >= 6, medias) ) )

    linhas_do_boletim.append(f'Aprovados \t {aprovados}')
    boletim.write(str.join('\n', linhas_do_boletim))
