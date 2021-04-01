# função 1
def calcula_soma(lista_de_numeros):
   soma_dos_numeros=0
   for numeros in lista_de_numeros:
       soma_dos_numeros = soma_dos_numeros + int(numeros)
   return soma_dos_numeros

print(calcula_soma([1,3,5]))
print(soma_dos_numeros)

# função 2
texto_entrada="1 2 3 4 5 4 8"
lista=[]
texto_convertido=0
def converte_entrada(texto_entrada):
      texto_convertido= texto_entrada.split()
      lista.append(texto_convertido)

print(converte_entrada(texto_entrada))
print(lista)

# função 3
lista_de_numeros = [0,6,9,8]
soma_dos_numeros = 0
numero_de_elementos = 0
def processa_numeros (lista_de_numeros):
  numero_de_elementos= len(lista_de_numeros) 
for numeros in lista_de_numeros:
       soma_dos_numeros = soma_dos_numeros + int(numeros)
   return( soma_dos_numeros, numero_de_elementos)

print(processa_numeros(lista_de_numeros))
print(f"A soma é {soma_dos_numeros} e o número de elementos é {numero_de_elementos}")

# função main do problema
media_dos_valores=0
lista_do_usuario=[]
def main(entrada_do_usuario):
  entrada_convertida= entrada_do_usuario.split()
  lista_do_usuario.append(entrada_convertida)
  soma_dos_valores=0
  for i in lista_do_usuario:
     soma_dos_valores= soma_dos_valores + int(i)
  media_dos_valores=soma_dos_valores/ len(lista_do_usuario)
  return (media_dos_valores)

print(main(entrada_do_usuario = [1 2 4]))
print(media_dos_valores)
