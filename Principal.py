#coding: utf-8

#Scripts simples utilizando a biblioteca turtle.Dicas e ajuda para o #melhor entendimento da biblioteca

#autor: José Ivan Geraldo da Silva
#data:27/03/2021
#local:Guarulhos-SP
###
import turtle ###importacao da biblioteca grafica turtle
t =  turtle.Turtle()##cria o objeto para trabalhar com

def square():##funcao square desenha um quadrado
	for i in range(4):#tem 4 lados quadrado
		t.forward(100)##vai 100 pixels para frente
		t.left(90)#vira 90 graus a esquerda
		#####vai fazer isto 4 vezes ate fechar o quadrado

###A chamada da funcao square excluir o comentario abaixo para executar a funcao.
#square()

###Agora fazer figuras mais complexas
###Vamos partir do racicionio que figuras geometricas estao inaceits no cieculo trigonometrico
###Entao o circulo tem 360 grais para desenhar uma figura com n ladoa,twteemo de dividir 360 pela qtd de laddia da figura
###Ex:Triangulo 3 lados:
###360/3.Temos de fazer a inclinacao de 120 graus : t.left(120).Fazendo um loop junto com t.forward,3 vezes

def triangle():
	for i in range(3):
		t.forward(100)
		t.left(120)
##Excluir o comentario abaixo para execucao da funcao
#triangle()

###Agora vamos criar funcao para qualquer poligono de n lados
###Uma variavel usa 360/n,onde n e o numero de lados do poligono,e tambem a quantidade de vezes que sera exwcutada o loop
###Abaixo a declaeacao da funcao
def poligono(lados):
	if lados  < 3: ##nao pode menoa que 3 lados
		print("Favor colocar um numeeo inteiro acima de 2")
	else:
		for i in range(lados):
			t.forward(100)###100 de avanco pode ser mudado livremente
			t.left(360.0/lados)###detalhe foi colocado uma divisão por float pois se não der um resutado inteiro ,na operação o circulo ficará imcompleto
			
##se quisee exexutar a funcao é só retirar os comentarios
poligono(11)




			
	
	
