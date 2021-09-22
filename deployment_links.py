from selenium import webdriver
from time import sleep
import json

class TranslnBot:
	def __init__(self):

		xp_field_question = '/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]'
		xp_field_nickname = '/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/input'
		xp_btn_submit = '/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td/input'

		xp_account_my_ss2_ac = '/html/body/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[43]/td[3]/a'
		xp_account_qa_bundler = '/html/body/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[90]/td[3]/a'


		# Opening JSON file
		f = open('data\login.json',)

		# returns JSON object as
		# a dictionary
		data = json.load(f)

		url = data['url']
		user = data['user']
		pasw = data['pass']
		answer = data['answer']

		print(user)

		self.driver = webdriver.Chrome()
		self.driver.get(url)

		# Closing file
		f.close()

		field_user = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[1]/input[3]').send_keys(user)
		field_pass = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[2]/input').send_keys(pasw)

		# Actually logging in 
		self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div/div[4]/input').click()


		# sleep(100)
		# Choosing the account/role
		self.driver.find_element_by_xpath(xp_account_qa_bundler).click()

		# security question answer
		self.driver.find_element_by_xpath(xp_field_nickname).send_keys(answer)
		self.driver.find_element_by_xpath(xp_btn_submit).click()

		sleep(100)

		

TranslnBot()
