#atividade1
def maior_variavel(num1,num2,num3):
  if num1 > num2 and num1> num3:
    print(num1)
  elif num2 > num1 and num2> num3:
    print(num2)
  elif num3 > num2 and num3 > num1:
    print(num3)
#atividade2
def converte_em_lista(texto):
  return texto.split()
#atividade3
def soma_lista(lista):
  soma=0
  i=0
  while i < len(lista):
    soma += lista[1]
    i += 1
  return soma
#atividade4
def converte_em_frase(lista):
  return " ".join(lista)
