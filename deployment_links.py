from selenium import webdriver
from time import sleep
import json

class TranslnBot:
	def __init__(self):

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


		self.driver = webdriver.Chrome()
		self.driver.get(url)
		sleep(2)

		# Closing file
		f.close()

		field_user = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[1]/input[3]').send_keys(user)
		field_pass = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[2]/input').send_keys(pasw)

		# Actually logging in 
		self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[4]/input').click()

		sleep(4)

		self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[43]/td[3]/a').click()
		sleep(100)

TranslnBot()
