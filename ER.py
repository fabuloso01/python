'''
for i in range(1,51):
    print(i)
'''
'''
for num in range(50,0,-1):
    print(num)
'''
'''
for i in range(150,201):
    print(i, end=" ")
'''
'''
for i in range(5,-1,-1):
    print(i)
'''
'''
i = 5

while i >=0:
    print(i)
    i -= 1
'''
'''
n =  int(input("Informe um número: "))

for i in range(1,n+1):
    print(i, end=" ")
    '''

'''
n = int(input("Informe um número: "))

for i in range(1,n+1):
    print(i)
'''
'''
num=int(input('Digite um número: '))  #receber número do usuário
x=1
while x<=num:
    print(x)
    x+=1
    '''
#Escreva um programa que mostre na tela os 20 primeiros múltiplos de 5.
'''
for i in range(1,101):
    if i%5==0:
       print(i, end=" ")
'''
'''
x=1
while x<=100:
    if x%5==0:
        print(x)
        x+=1
    x+=1
'''
'''
#Tabuada
n = int(input("Informe um número: "))

for i in range(1,11):
    print(f"{n}x{i} = {n*i}")
    '''
'''
for valor in range(1,11):
    	for numero in range(1,11):
    		print(f'{valor} x {numero} = {valor*numero}')
'''
'''
x=11
for a in range(0,4):
    for x in range(1, 11):
        print(x, end=" ")
'''
'''
num=0
while 0<=num<=10:
    num=int(input('Insira um número inteiro entre 0-10: '))
    if num<0 or num>10:
      print('Fim do programa.')
'''
'''
while True:
    num=int(input('Insira um número inteiro entre 0-10: '))
    if num<0 or num>10:
        print('Fim do programa.')
        break
'''
'''
for i in range(1,11):
    n = int(input("Informe um número de 0-10: "))
    if n < 0 or n > 10:
        print('Fim do programa.')
        break
'''
'''
lista_produtos = ["faca", "garfo", "panela", "frigideira"]

for produto in lista_produtos:
    print(produto.capitalize())
'''
"""
lista_precos = [10, 20, 30]
for preco in lista_precos:
    imposto = preco*0.1
    print(f"{imposto:.2f}")
"""

'''
#percorrer um dicionário
produtos = {
    "faca": 10,
    "garfo": 20,
}

for produto in produtos:
    print(produto)
    print(produtos[produto], end=" ")
'''
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''
'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")

  for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
'''
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
'''
'''
y = 6
for x in range(0,5):
    for y in range(0,6):
        print(y,end=" ")
else:
    print("Fim")
'''

n = 0
somar = 0
num_digitados = 0
for i in range(1,11):
    n = int(input("Informe um número de 0-10: "))
    if n < 0 or n > 10:
        print(f'Soma dos números digitados: {somar}')
        print(f'Quantidade de números digitados: {num_digitados}')
        print('Fim do programa.')
        break
    somar += n 
    print(somar)
    num_digitados += 1

    






