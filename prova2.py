#atividade prática 1
def media_do_aluno():
  nota1=float(input("Coloque a nota 1: "))
  nota2=float(input("Coloque a nota 2: "))
  nota3=float(input("Coloque a nota 3: "))
  media_de_notas=0
  media_de_notas=(nota1+nota2+nota3)/3
  return (f"Média do aluno é {media_de_notas}")

print(media_do_aluno())

#atividade prática 2
def atividade2():
  num_entradas = int(input("Digite o numero de entradas: "))
  lista_de_saida = []
  for i in range(num_entradas):
    lista_de_saida.append( input("Digite a nova entrada:  ") )
  return(lista_de_saida)


print(atividade2())

#atividade prática 3
def atividade3():
  menu = {
    'a':'globo',
    'b':'sbt'
  }
  opcao=(input("Coloque aqui sua opção:  "))
  while opcao != 'z' or opcao !='Z':
   if opcao in menu:
       print(menu[opcao])
   return print("Fim")

atividade3()

#atividade prática 4
def atividade4(lista_media_do_aluno):
  i=0
  medias_inferiores_a_7=0
  if lista_media_do_aluno[i] < 7:
    medias_inferiores_a_7 += 1
  i +=1
  if medias_inferiores_a_7 < len(lista_media_do_aluno) * 0.25:
      return(print("Professor Coxa"))
  else:
      return (print("Professor Padrão"))

#exemplo de uma lista de média do aluno
lista_media_do_aluno=[8,2,4,6]
atividade4(lista_media_do_aluno)
