from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from translations import translations

#setup

fp = webdriver.FirefoxProfile()

fp.set_preference("webdriver.load.strategy", "unstable");

driver = webdriver.Firefox(firefox_profile=fp)

driver.maximize_window()

#login
driver.get("https://www.duolingo.com")
driver.find_element_by_id("sign-in-btn").click()
driver.find_element_by_name("login").send_keys("USER")
driver.find_element_by_name("password").send_keys("PASS",Keys.RETURN)
WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/skill/de/Basics-1']")))
driver.get("https://www.duolingo.com/skill/de/Basics-1/practice")
while True:
	try:
		WebDriverWait(driver, 10, 0.05).until(EC.presence_of_element_located((By.ID, "start-button")))
		driver.find_element_by_id("start-button").click()
		for i in xrange(24):
			try:
			  WebDriverWait(driver, 3, 0.05).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='text-input' or @id='word-input' or @name='mediumSelect' or @id='sentence-0']")))
			except TimeoutException as e:
				pass
				#ActionChains(driver).send_keys("DEUTSCHLAND",Keys.RETURN).perform()
			if len(driver.find_elements_by_css_selector("div.text-to-translate")) > 0:
				line = driver.find_element_by_css_selector("div.text-to-translate").text.encode( "utf-8" ).replace('\n', ' ').replace('\r', '')
				try:
				  translation = translations[line]
				  ActionChains(driver).send_keys(translation).perform()
				except KeyError as e:
					with open("dictionary.py", "a") as myfile:
					  myfile.write("\n"+'"'+line+'":"",')
					print '"'+line+'":"",'
			driver.find_elements_by_xpath("//input[@id='sentence-0']")
			try:
				driver.find_element_by_xpath("//input[@id='sentence-0']").click()
			except:
				pass
			ActionChains(driver).send_keys(". 1",Keys.ARROW_DOWN,Keys.ARROW_LEFT,Keys.DELETE,Keys.RETURN).perform()
			WebDriverWait(driver, 5, 0.05).until(EC.visibility_of_element_located((By.ID, "next_button")))
			#WebDriverWait(driver, 5, 0.05).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='text-input' or @id='word-input']")))
			driver.find_element_by_id("next_button").click()
			#ActionChains(driver).send_keys(Keys.RETURN).perform()
		#ActionChains(driver).send_keys(Keys.RETURN,Keys.RETURN).perform()
		WebDriverWait(driver, 7, 0.05).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Practice again')]")))
		driver.find_element_by_xpath("//button[contains(text(),'Practice again')]").click()
	except Exception as e:
		#print e
		driver.get("https://www.duolingo.com/skill/de/Basics-1/practice")
		try:
		    WebDriverWait(driver, 3).until(EC.alert_is_present(),
		                                   'Timed out waiting for PA creation ' +
		                                   'confirmation popup to appear.')

		    alert = driver.switch_to_alert()
		    alert.accept()
		    print "alert accepted"
		except TimeoutException:
		    print "no alert"
#except TimeoutException as e:
	#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "skip_button")))
	#driver.find_element_by_id("skip_button").click()
	#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "next_button")))
	#driver.find_element_by_id("next_button").click()
#
#driver.quit()


