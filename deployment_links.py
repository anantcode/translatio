from selenium import webdriver
from time import sleep
import json

class TranslnBot:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://google.com")
		sleep(2)

		# Opening JSON file
		f = open('data\login.json',)

		# returns JSON object as
		# a dictionary
		data = json.load(f)

		url = data['url']
		user = data['user']
		pasw = data['pass']

		print(url)
		print(user)
		print(pasw)


		# Closing file
		f.close()


TranslnBot()
