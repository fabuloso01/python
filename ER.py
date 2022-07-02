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
x=11
for a in range(1,4):
    for x in range(1, 11):
        print(x, end=" ")
