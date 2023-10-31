#função recursiva
'''
def ourSum(lower, upper, margin= 0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + ourSum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
    
ourSum(1 , 4)

def factorial(n):
    def recurse(n, product):
        if n == 1: return product
        else: return recurse(n -1, n * product)
    return recurse()

def factorial(n, product = 1):
    if n == 1 : return product
    else: return factorial(n - 1, n * product)'''

'''import decimal

n1 = decimal.Decimal('0.1')
n2 = decimal.Decimal('0.7')
n3= n1 + n2
print(n3)
print(f'{n3:.2f}')#para formatar o tanto de casas decimais
print(round(n3, 3))

frase = "Olha só que, coisa interessante"
lista_frase_cruas = frase.split(',')

lista_palavras = []

for i, frase in enumerate(lista_frase_cruas):
    lista_palavras.append(lista_frase_cruas[i].strip())

##print(lista_frase_cruas)

frases_unidas = '*'.join(lista_palavras)
print(frases_unidas)

salas = [ 
    ['Maria', 'Helena', ],
     ['Elaine', ],
     ['Luis', 'Joao', 'Eduarda', (0,10,20,30,40)],
    ]

print(salas[0][1])
print(salas[2][2])
print(salas[2][3][3])

for sala in salas:
    print('A sala é :' ,len(sala))
    for aluno in sala:
        print(aluno)

def soma(*args):
    total= 0

    for numero in args:
        total =total + numero
        print('Total', total)
        total = total + numero
        print('total',total)
    print(total)

soma(1,2,3,4,5)


def mutiplica (*args):
    valor = 1

    for n in args:
        valor = valor * n 
        print("Total",valor)
mutiplica(1,2,3,4,5)

def par(n):
    
    if n % 2 == 0:
        return 'par'
    else:
        return 'impar'
n1 =10
n2 = 11

r1 = par(n1)
r2 = par(n2)
print(r1 , r2)

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao,'Bom Dia', 'Luis'))

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao},{nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

for nome in ['Maria','Joana','Luis']:
    print(falar_bomdia(nome)*4 )
    print(falar_boanoite(nome)*2)


#dict métodos úteis 

pessoa = { 'nome': 'Débora',
         'sobrenome':'silva'

}
print(pessoa.get('nome'))
pessoa.update({'nome':'Déby',
               'idade': 30,})

print(pessoa.items())


perguntas = [{
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1','3','4','5'],
    'Resposta': '4',
},
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25','55','10','51'],
    'Resposta': '25',
},
{
    'Pergunta':'Quanto é 10/2?',
    'Opções':['4','5','2','1'],
    'Resposta':'5',
},
]

#def p1(*args):
print('Pergunta:' , perguntas[0]['Pergunta'])
for i, opcao in enumerate(perguntas[0]['Opções']):
    print(f' {i})',opcao)

r1 = input('Escolha a opção certa: ' )

if r1 == '2':
    print('Certa Resposta')
else:
    print('Errou')

print(perguntas[1]['Pergunta'])
for i,opcao1 in enumerate(perguntas[1]['Opções']):
    print(f' {i})',opcao1)

r2 = input('Escolha a opção certa: ' )

if r2 == '0':
    print('Certa Resposta')
else:
    print('Errou')

print(perguntas[2]['Pergunta'])
for i, opcao2 in enumerate(perguntas[2]['Opções']):
    print(f' {i})', opcao2)

r3 = input('Escolha a opção certa: ' )

if r3 == '1':
    print('Certa Resposta')
else:
    print('Errou')

#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final,mostre a matriz na tela ,com a formatação correta


def main():
    a =[0,1,2,3,4]
    b = a
    b[1]=7 
    b[2]= 9
    print('a=', a ,'b=', b)

main()

 

linha_com_zeros = [0]*5
A = [ linha_com_zeros ] * 5
A[1][1] = 2

print(A)

A = []
for i in range(5):
    A = A + [[0]*5] # cria uma nova lista [0]*5
A[1][1] = 2
print(A)

s1 = set() #vazio
s1 = {'Deby',1,2,3}#com dados
print(s1)



ss1 = {1,2,3,3,3,3,3,3,1}#remove valores duplicados
print(ss1)

l1 = [1,2,3,3,3,3,3,3,1]
s2 = set(l1)
l2 = list(s2)
print(l2)

s3 = set()
s3.add('Deby')
s3.update(("Ola mundo",1,2,3,4))
s3.discard(3)
print(s3)

s4 = {1,2,3}
s5 = {2,3,4}
s6 = s4 | s5
s6 = s4 & s5
s6 = s4 - s5
s6 = s4 ^ s5
print(s6)


letras = set()
while True:
    letra = input("Digite ")
    letras.add(letra.lower())

    if "l" in letras:
        print("PARABENS")
        break

    print(letras)


a, b = 1 , 2
a, b = b , a
print(a,b)

pessoa = {
    'nome': 'Déby',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade':16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa , **dados_pessoa}
print(pessoa_completa)

#argumentos variados
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave,valor)
    

mostro_argumentos_nomeados(**pessoa_completa)

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)'''

#Mapeamento de dados em list compreehension

produtos = [
    {"nome": 'p1', 'preco': 20 ,},
    {'nome': 'p2', 'preco':10,},
    {'nome':'p3', 'preco': 30,},
]
novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
    
#Outra forma de fazer a mesma coisa
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)

numeros = [1,2,3,4,5,6,7,8,9,10]
novo_numeros = [numero for numero in numeros if numero > 5]
impares=[numero for numero in numeros if numero % 2 != 0]
outro_if = [numero if numero != 6 else 600 for numero in numeros if numero % 2 == 0]


print(numeros, '\n' ,novo_numeros,'\n',impares,'\n',outro_if )

string = 'Otavio Miranda'
numero_de_letras = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_letras]
    for indice in range(0, len(string), numero_de_letras)])
print(nova_string)

































































