#-*- coding:utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup

class search():
	def __init__(self, search, nPage, proxies=None):
		"""
			@params str search
			@param int nPage
			@params dict proxies={'https': 'http://10.10.1.10:1080'}
		"""
		self.search = self.ReplaceChar(search)
		self.page = []
		self.nPage = int(nPage)*10
		self.result = []
		self.proxies = proxies

	def Run(self):
		count = 0
		while self.nPage >= count:

			if self.proxies != None:
				request = "http://www.google.com.br/search?q="+str(self.search)+"&oq="+str(self.search)+"&start="+str(count)
				r = requests.get(request,proxies=self.proxies)
				self.page.append(r.content)				
				count = count+10

			else:	
				request = "http://www.google.com.br/search?q="+str(self.search)+"&oq="+str(self.search)+"&start="+str(count)
				r = requests.get(request)
				self.page.append(r.content)
				count = count+10
			if count == 0: 
				count = count+1*10

		for x in range(0, len(self.page)):
			soup = BeautifulSoup(self.page.pop(),features="lxml")			
			self.result.append(soup.find_all("div",{"class":"g"}))
			

	def SaveInHtml(self, path):
		arquivo = open(path+'result.html', 'w+')
		for x in self.result:
			for y in x:
				arquivo.write(str(y))
		arquivo.close()


	def ReplaceChar(self, string):
		with open('caracteres.csv') as f:
			f_csv = csv.DictReader(f)
			for row in f_csv:
				string = string.replace(row['simb'], row['ASC'])
		return string





