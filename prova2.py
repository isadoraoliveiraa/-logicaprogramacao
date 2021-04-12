def exercicio1(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3) / 3
  return (f'Média do aluno foi {media}')

def exercicio2():
  numeros = input("Digite seus numeros: \r\n")
  lista = []
  lista_n = numeros.split()
  for numeros in lista_n:
    lista.append(int(numeros))
  return lista

def exercicio3():
  opcao = input()
  while opcao != 'z' and opcao != 'Z':
    if opcao == 'a':
      print("Globo")
    elif opcao == 'b':
      print("SBT")
    else:
      print("Inválido")
      
def exercicio4(lista_media):
   media = 0
   for elemento in lista_media:
     if elemento < 7:
       media += 1
   if media < 0.25:
     return "Professor Coxa"
   else:
     return "Profesor Padrão"
