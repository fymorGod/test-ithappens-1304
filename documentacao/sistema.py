'''
Autor: Luiz Fylip Viana
Date: 03/04/2020
From: Brazil, Ma
Language: Python
Libary: time

Document:: Based in challenger from Ithappens corporate tech of SuperMarket Mateus.
Link by Github:
    -- github.com/users/fymor-god --
'''
#importações
from cliente import Cliente
from usuario import Usuario
import time
#listas principais de dados
base_cliente = []
base_usuario = []
total_p = []
#dados = quantidade dos produtos ilimitada, dados estáticos
estoque_produtos = [(
    {'arroz 1KG':'3,99R$'},
    {'feijao 1KG':'4,49R$'},
    {'farinha 1KG':'3,39R$'},
    {'açucar 1kg':'4,49R$'},
    {'doritos 300g':'5,99R$'},
    {'CocaCola 2L':'6,99R$'}
    )]

#escopo de entrada do cliente e do funcionario
client = str(input("Digite o nome do Cliente: "))
cpf_client = input("Digite o cpf do Cliente: ")

base_cliente.append(Cliente(client, cpf_client))

user = str(input("Digite o nome do Usuário: "))
user_idade = input('Digite a idade do Usuário: ')
user_cpf = input('Digite o cpf do Usuário: ')

base_usuario.append(Usuario(user,user_idade,user_cpf))
print()
#inicio do sistema de escolha do produto
print('Escolha seu Produto\n')

for i in range(len(estoque_produtos)):
    valor_p = estoque_produtos[i]
    print("Produto {} posição = {}".format(valor_p,i))

resposta = input('Deseja escolher um produto?').strip().upper()[0]

while(resposta =='S'):
    pedido = int(input('Digite a posição indicada do seu produto: '))
    total_p.append(estoque_produtos[pedido])
    resposta = input('Deseja escolher mais um produto ?[S/N]')

print('Carregando sua Compra\n')
time.sleep(2)

print('Os Produtos da sua Compra\n')
for o in range(len(total_p)):
    compra = total_p[o]
    print(compra)

print('Finish Buy')