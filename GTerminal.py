#-*- coding:utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup
cont = 0
search = raw_input("Escreva sua pesquisa:")
print(search)
resultado_quant = raw_input("Quantos resultados você quer?\nEscreva um numero:")
path = raw_input("Onde deseja salvar o arquivo?Escreva um local ou nome:")
with open('caracteres.csv') as f:
	f_csv = csv.DictReader(f)
	for row in f_csv:
		search = search.replace(row['simb'], row['ASC'])
print(search)
numlinks = 0

trabalho = True
while trabalho == True:
	cont = cont+10
	page = req = requests.request('GET', "https://www.google.com.br/search?q="+search+"&oq="+search+"&start="+str(cont))
	soup = BeautifulSoup(page.content, 'html.parser')
	print(page.status_code)
	resultado = soup.find_all('h3', class_='r')
	arquivo = open(path+'.html', 'a+')

	for x in resultado:
		x = str(x)+"\n"
		x = x.replace('/url?q=', "")
		x1 = x.split("&amp", 1)
		x2 = x1[1].split(">", 1)
		print(x1, x2)
		x = x1[0]+"\">"+x2[1]
		arquivo.write(x)
		numlinks = numlinks+1
		if numlinks == int(resultado_quant):
			break
	if numlinks == int(resultado_quant):
		break
	if int(resultado_quant) < int(cont):
		trabalho = False
