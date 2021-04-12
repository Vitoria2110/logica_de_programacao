#atividade 1
def multiplo_de_5_impar():
  i=0
  num= int(input("Número: "))
  while i <= num:
    if i % 5 == 0 and i % 2 == 1:
      print(i)
    i += 1

multiplo_de_5_impar()

#atividade 2
def lista_do_usuario():
  num_entradas=int(input("Número de entradas da lista:  "))
  lista=[]
  for i in range(num_entradas):
    lista.append( input("Valores da lista:  ") )
  return(lista)

print(lista_do_usuario())

#atividade 3
def numeros_maiores_que_5(lista):
  i=0
  while i <= len(lista):
    if lista[i] >= 5:
      return(lista[i])
    i+=1

#atividade 4
def funcao_menu():
  menu = {
    'a':'PSG',
    'b':'BAYERN',
  }
  opcao=(input("Coloque aqui sua opção:  "))
  while opcao in menu:
      print(menu[opcao])
  else:
      print("Fim")
