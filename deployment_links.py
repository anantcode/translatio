from selenium import webdriver
from time import sleep

class TranslnBot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://google.com")
		sleep(2)
		
		f = open("data\login.json", "r")
		print(f.read())


TranslnBot()
