import json
import os
import signal
import time
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver import DesiredCapabilities, Firefox, FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

loop_count = 0
player_locator = (By.XPATH, "//button[contains(@data-test,'player-')]")
player_skip_locator = (By.CSS_SELECTOR, "button[data-test='player-skip']")
continue_locator = (By.XPATH, "//span[text() = 'Continue']")
check_locator = (By.XPATH, "//span[text() = 'Check']")
player_practice_again_locator = (By.CSS_SELECTOR, "button[data-test='player-practice-again']")

translations_filename = "translations.json"
start = time.time()
translations = json.load(open(translations_filename, "r"))
end = time.time()
print("Loaded {} translations from disk in {} seconds.".format(len(translations), end - start))

# setup
profile_path = '/Users/alaileon/Library/Application Support/Firefox/Profiles/ld5n6nou.default-esr'
profile = FirefoxProfile(profile_path)
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference('detach', True)
profile.update_preferences()
desired = DesiredCapabilities.FIREFOX
driver = Firefox(firefox_profile=profile, desired_capabilities=desired, service_log_path=os.devnull)

# rate of challenge solving
main_throttle = 0.5

def keyboardInterruptHandler(sig, frame):
	start = time.time()
	json.dump(translations, open(translations_filename, "w"))
	end = time.time()
	print("Wrote {} translations to disk in {} seconds.".format(len(translations), end - start))
	exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

def input_translate():
	global loop_count
	print("parsing hint tokens")
	original_tokens = driver.find_elements(By.CSS_SELECTOR, "[data-test='hint-token']")
	try:
		original_sentence = ' '.join(elem.text for elem in original_tokens)
	except StaleElementReferenceException:
		return
	print("looking for " + original_sentence)
	if original_sentence in translations:
		print("found " + original_sentence)
		try:
			driver.find_element(By.CSS_SELECTOR, "textarea[data-test='challenge-translate-input']").send_keys(translations[original_sentence], Keys.RETURN)
		except ElementNotInteractableException:
			print("can't type into the input box, probably waiting for the end screen")
			loop_count = loop_count + 1
			driver.implicitly_wait(10)
			driver.find_element(*player_practice_again_locator)
			return
	else:
		loop_count = 0
		try:
			driver.find_element(*player_skip_locator).click()
			translated_sentence=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution')]/following-sibling::div").text
			translations[original_sentence] = translated_sentence
			print("New translation: " + original_sentence + " => " + translated_sentence)
		except NoSuchElementException:
			pass
	print("clicking continue after input challenge")
	driver.find_element(*continue_locator).click()


def assist_translate():
	original_question = driver.find_element(By.CSS_SELECTOR, "h1[data-test='challenge-header'] > span").text
	print("original question: " + original_question)
	original_word = original_question.split('"')[1]
	print("original word: " + original_word)
	print("looking for " + original_word)
	if original_word in translations:
		translation = translations[original_word]
		if isinstance(translation, str):
			print("found translation for " + original_word + ": " + translation)
			try:
				driver.find_element(By.XPATH, "//div[text() = '"+translation+"']").click()
				driver.find_element(*check_locator).click()
			except NoSuchElementException as e:
				driver.find_element(*player_skip_locator).click()
				translated_word=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution:')]/following-sibling::div").text
				translations[original_word] = [translation, translated_word]
		else:
			print("found translations for " + original_word + ": " + str(translation))
			for i in translation:
				try:
					driver.find_element(By.XPATH, "//div[text() = '"+i+"']").click()
					driver.find_element(*check_locator).click()
				except NoSuchElementException as e:
					print("better luck next time" + i)
	else:
		print("did not find translation for " + original_word + ", picking first")
		random_pick = driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge-judge-text']")
		random_pick_text = random_pick.text.strip()
		random_pick.click()
		driver.find_element(*check_locator).click()
		try:
			print("looking for blame-correct")
			driver.find_element(By.XPATH, "//div[contains(@data-test,'blame-correct')]")
			print("found blame-correct")
			translations[original_word] = random_pick_text
			print("New translation: " + original_word + " => " + random_pick_text)
			driver.implicitly_wait(10)
		except NoSuchElementException as e:
			driver.implicitly_wait(10)
			try:
				translated_word=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution:')]/following-sibling::div").text
				translations[original_word] = translated_word
				print("New translation: " + original_word + " => " + translated_word)
			except NoSuchElementException:
				pass
	driver.find_element(*continue_locator).click()


def judge_translate():
	original_question = driver.find_element(By.CSS_SELECTOR, "h1[data-test='challenge-header'] > span").text
	print("original question: " + original_question)
	original_word = original_question.split('"')[1]
	print("original word: " + original_word)
	print("looking for " + original_word)
	if original_word in translations:
		translation = translations[original_word]
		if isinstance(translation, str):
			print("found translation for " + original_word + ": " + translation)
			try:
				driver.find_element(By.XPATH, "//div[text() = '"+translation+"']").click()
				driver.find_element(*check_locator).click()
			except NoSuchElementException as e:
				driver.find_element(*player_skip_locator).click()
				translated_word=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution:')]/following-sibling::div").text
				translations[original_word] = [translation, translated_word]
		else:
			print("found translations for " + original_word + ": " + str(translation))
			for i in translation:
				try:
					driver.find_element(By.XPATH, "//div[text() = '"+i+"']").click()
					driver.find_element(*check_locator).click()
				except NoSuchElementException as e:
					print("better luck next time" + i)
	else:
		print("did not find translation for " + original_word + ", picking first")
		random_pick = driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge-judge-text']")
		random_pick_text = random_pick.text.strip()
		random_pick.click()
		driver.find_element(*check_locator).click()
		try:
			print("looking for blame-correct")
			driver.find_element(By.XPATH, "//div[contains(@data-test,'blame-correct')]")
			print("found blame-correct")
			translations[original_word] = random_pick_text
			print("New translation: " + original_word + " => " + random_pick_text)
			driver.implicitly_wait(10)
		except NoSuchElementException as e:
			driver.implicitly_wait(10)
			try:
				translated_word=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution:')]/following-sibling::div").text
				translations[original_word] = translated_word
				print("New translation: " + original_word + " => " + translated_word)
			except NoSuchElementException:
				pass
	driver.find_element(*continue_locator).click()


def name_translate():
	original_question = driver.find_element(By.CSS_SELECTOR, "h1[data-test='challenge-header'] > span").text
	print("original question: " + original_question)
	original_question = original_question.replace('“', '"')
	original_question = original_question.replace('”', '"')
	original_phrase = original_question.split('"')[1]
	print("original phrase: " + original_phrase)
	if original_phrase in translations:
		translation = translations[original_phrase]
		print("found answer for " + original_phrase + ": " + str(translation))
		if isinstance(translation, str):
			print("finding input box")
			driver.find_element(By.CSS_SELECTOR, "input[data-test='challenge-text-input']").send_keys(translation, Keys.RETURN)
			print("found input box")
		else:
			try:
				driver.find_element(By.XPATH, "//div[text() = '"+translation[0]+"']").click()
				driver.find_element(By.CSS_SELECTOR, "input[data-test='challenge-text-input']").send_keys(translation[1], Keys.RETURN)
			except NoSuchElementException:
				driver.find_element(By.CSS_SELECTOR, "input[data-test='challenge-text-input']").send_keys(" ".join(translation), Keys.RETURN)
		driver.find_element(*check_locator).click()
	else:
		print("did not find answer for " + original_phrase + ", skipping")
		driver.find_element(*player_skip_locator).click()
		answers = driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution')]/following-sibling::div").text
		answer = answers.split(",")[0]
		if len(answer.split(" ")) > 1:
			article = answer.split(" ")[0]
			text = " ".join(answer.split(" ")[1:])
			translations[original_phrase] = [article, text]
		else:
			translations[original_phrase] = answer
	driver.find_element(*continue_locator).click()


def gapfill_translate():
	print("parsing hint tokens")
	original_tokens = driver.find_elements(By.CSS_SELECTOR, "[data-test='hint-token']")
	original_sentence = ' '.join(elem.text for elem in original_tokens)
	print("looking for " + original_sentence)
	if original_sentence in translations:
		translation = translations[original_sentence]
		print("found answer for " + original_sentence + ": " + translation)
		driver.find_element(By.XPATH, "//div[text() = '"+translation+"']").click()
		driver.find_element(*check_locator).click()
	else:
		print("did not find answer for " + original_sentence + ", picking first")
		random_pick = driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge-judge-text']")
		random_pick_text = random_pick.text.strip()
		random_pick.click()
		driver.find_element(*check_locator).click()
		try:
			print("looking for blame-correct")
			driver.find_element(By.XPATH, "//div[contains(@data-test,'blame-correct')]")
			print("found blame-correct")
			translations[original_sentence] = random_pick_text
			print("New translation: " + original_sentence + " => " + random_pick_text)
			driver.implicitly_wait(10)
		except NoSuchElementException as e:
			driver.implicitly_wait(10)
			try:
				translated_word=driver.find_element(By.XPATH, "//h2[contains(text(), 'Correct solution:')]/following-sibling::div").text
				translations[original_sentence] = translated_word
				print("New translation: " + original_sentence + " => " + translated_word)
			except NoSuchElementException:
				pass
	driver.find_element(*continue_locator).click()

driver.maximize_window()
driver.get("https://www.duolingo.com/practice")

while True:
	try:
		if loop_count > 5:
			# just nuke everything if we detect a loop, protecting against network issues or other strange problems
			driver.get("https://www.duolingo.com/practice")
			loop_count = 0
		while True:
			driver.implicitly_wait(10)
			print("looking for any player-* button")
			driver.find_element(*player_locator)
			time.sleep(main_throttle)
			driver.implicitly_wait(0)
			try:
				print("looking for player-practice-again")
				driver.find_element(*player_practice_again_locator).click()
				print("clicked player-practice-again")
				continue
			except NoSuchElementException as e:
				pass
			try:
				print("looking for challenge type:")
				print(driver.find_element(By.XPATH, "//div[contains(@data-test,'challenge')]").get_attribute("data-test"))
			except NoSuchElementException as e:
				print("did not find a challenge type:")
				pass
			try:
				print("looking for challenge-translate")
				driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge challenge-translate']")
				print("found challenge-translate")
				input_translate()
				driver.implicitly_wait(10)
				break
			except NoSuchElementException as e:
				pass
			try:
				print("looking for challenge-assist")
				driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge challenge-assist']")
				print("found challenge-assist")
				assist_translate()
				driver.implicitly_wait(10)
				break
			except NoSuchElementException as e:
				pass
			try:
				print("looking for challenge-name")
				driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge challenge-name']")
				print("found challenge-name")
				name_translate()
				driver.implicitly_wait(10)
				break
			except NoSuchElementException as e:
				pass
			try:
				print("looking for challenge-gapFill")
				driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge challenge-gapFill']")
				print("found challenge-gapFill")
				gapfill_translate()
				driver.implicitly_wait(10)
				break
			except NoSuchElementException as e:
				pass
			try:
				print("looking for challenge-judge")
				driver.find_element(By.CSS_SELECTOR, "div[data-test='challenge challenge-judge']")
				print("found challenge-judge")
				judge_translate()
				driver.implicitly_wait(10)
				break
			except NoSuchElementException as e:
				pass
			try:
				print("clicking player-skip")
				driver.find_element(*player_skip_locator).click()
			except NoSuchElementException as e:
				print("didn't find player-skip")
				pass
			print("clicking continue")
			try:
				driver.find_element(*continue_locator).click()
			except ElementClickInterceptedException:
				continue
	except Exception as e:
		# ignore literally everything else, get back on that rat wheel
		print(e)
		driver.get("https://www.duolingo.com/practice")
