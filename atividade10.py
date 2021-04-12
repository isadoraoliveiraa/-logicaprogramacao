def exercicio1():
  numero_n = int(input())
  i = 0
  while numero_n > i:
    if i % 5 == 0 and i % 2 != 0:
      print(i)
    i += 1
    
def exercicio2():
  numero = input("Digite seus numeros: \r\n")
  lista = []
  lista_n = numero.split()
  for numero in lista_n:
    lista.append(int(numero))
  return lista

def exercicio3():
  numeros = input("Digite seus numeros: \r\n")
  lista = []
  lista_n = numeros.split()
  soma_num = 0
  for numeros in lista_n:
    lista.append(int(numeros))
    if int(numeros) > 5:
      soma_num += 1
      return soma_num
      
def exercicio4():
  opcao = input()
  while opcao != 'd':
    if opcao == 'a':
      print("PSG")
    elif opcao == 'b':
      print("BAYER")
