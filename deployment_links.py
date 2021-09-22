from selenium import webdriver
from time import sleep

class TranslnBot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.netsuite.com")


TranslnBot()