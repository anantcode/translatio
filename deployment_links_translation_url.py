from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

import json

class TranslnBot:
	def __init__(self):

		# Loading account data ------------------- 
		# Opening JSON file
		f = open('data\login.json',)

		# returns JSON object as
		# a dictionary
		data = json.load(f)

		url = data['url']
		user = data['user']
		pasw = data['pass']
		answer = data['answer']
		account_id = data['account_id_ss2_test']
		deployment_id = data['deployment_id_ss2_bundler_ei_prefs']
		xp_account_chosen = data['xp_account_my_ss2_ac']

		print(user)


		# --------------------------------------------------
		xp_field_question = '/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr[2]/td[2]'
		xp_field_nickname = '/html/body/div[2]/div[2]/form/table/tbody/tr[3]/td/table/tbody/tr[3]/td[2]/input'
		xp_btn_submit = '/html/body/div[2]/div[2]/form/table/tbody/tr[4]/td/input'

		xp_account_my_ss2_ac = '/html/body/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[43]/td[3]/a'
		xp_account_qa_bundler = '/html/body/div[2]/div[3]/table/tbody/tr[2]/td/table/tbody/tr[90]/td[3]/a'

		xp_menu_script_deployment = '/html/body/div[1]/div[1]/div[2]/ul[4]/li[8]/ul/li[4]/ul/li[2]/a'
		
		xp_deployment_links_tab = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[1]/td/div/table/tbody/tr/td[4]/a'
		xp_deployment_links_translation_center1 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[6]/table/tbody/tr[2]/td[5]'
		xp_center1_chinese1 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[7]/div/div/div/span/div/table/tbody/tr[1]/td[2]/span/input'
		xp_center1_chinese2 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[7]/div/div/div/span/div/table/tbody/tr[2]/td[2]/span/input'

		xp_done_btn = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[7]/div/div/div/input'

		xp_deployment_links_translation_center2 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[6]/table/tbody/tr[4]/td[5]'
		xp_center2_chinese1 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[7]/div/div/div/span/div/table/tbody/tr[1]/td[2]/span/input'
		xp_center2_chinese2 = '/html/body/div[1]/div[2]/div[3]/table[1]/tbody/tr[2]/td/div/div[9]/div/form/div[7]/div/div/div/span/div/table/tbody/tr[2]/td[2]/span/input'

		xp_save_record_btn = '/html/body/div[1]/div[2]/div[3]/table[2]/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td[2]/input'

		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get(url)

		# Closing file
		f.close()

		field_user = self.driver.find_element("xpath", '/html/body/div[3]/div[1]/form/div/div[1]/input[3]').send_keys(user)
		field_pass = self.driver.find_element("xpath", '/html/body/div[3]/div[1]/form/div/div[2]/input').send_keys(pasw)

		# Actually logging in 
		self.driver.find_element("xpath", '/html/body/div[3]/div[1]/form/div/div[4]/input').click()

		# Choosing the account/role
		self.driver.find_element("xpath", xp_account_chosen).click()

		# security question answer
		self.driver.find_element("xpath", xp_field_nickname).send_keys(answer)
		self.driver.find_element("xpath", xp_btn_submit).click()

		# URL of Deployment in edit mode:
		url_deployment_prefs = f'https://{account_id}.app.netsuite.com/app/common/scripting/scriptrecord.nl?id={deployment_id}&e=T'

		# Login is done, directly navigating to required suitelet deployment by ID: 378
		self.driver.get(url_deployment_prefs)
		self.driver.find_element("xpath", xp_deployment_links_tab).click()
		sleep(2)

		# First Center
		self.driver.find_element("xpath", xp_deployment_links_translation_center1).click()
		sleep(2)
		self.driver.find_element("xpath", xp_center1_chinese1).send_keys('abc')
		self.driver.find_element("xpath", xp_center1_chinese2).send_keys('def')
		self.driver.find_element("xpath", xp_done_btn).click()

		# Second Center
		self.driver.find_element("xpath", xp_deployment_links_translation_center2).click()
		sleep(2)
		self.driver.find_element("xpath", xp_center2_chinese1).send_keys('abcd')
		self.driver.find_element("xpath", xp_center2_chinese2).send_keys('deff')
		self.driver.find_element("xpath", xp_done_btn).click()
		sleep(2)

		# Save Deployment Record
		self.driver.find_element("xpath", xp_save_record_btn).click()

		sleep()


TranslnBot()
