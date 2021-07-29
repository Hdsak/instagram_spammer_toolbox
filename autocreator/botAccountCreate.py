from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import autocreator.accountInfoGenerator as account
import autocreator.getVerifCode as verifiCode
from selenium import webdriver
import autocreator.fakeMail as email
import time
from webdriver_manager.chrome import ChromeDriverManager as CM

import argparse


ua = UserAgent()
userAgent = ua.random
print(userAgent)

# if args.firefox:
#     profile = webdriver.FirefoxProfile()
#     profile.set_preference("general.useragent.ovrride", userAgent)
#     driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"your gecko driver here")

if 1:
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--proxy-server=%s' % "91.218.229.103:3128")
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(options=options, executable_path=CM().install())

driver.get("https://www.instagram.com/accounts/emailsignup/")
time.sleep(2)
try:
    cookie = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
except:
    pass
name = account.username()

# Fill the email value
email_field = driver.find_element_by_xpath('//body/div[@id="react-root"]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/label[1]/input[1]')
fake_email = email.getFakeMail()
email_field.send_keys(fake_email)
print(fake_email)

# Fill the fullname value
fullname_field = driver.find_element_by_name('fullName')
fullname_field.send_keys(account.generatingName())
print(account.generatingName())
# Fill username value
username_field = driver.find_element_by_name('username')
username_field.send_keys(name)
print(name)
# Fill password value
password_field = driver.find_element_by_name('password')
password_field.send_keys('kazan2012')  # You can determine another password here.
print(account.generatePassword())
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()

time.sleep(8)

# Birthday verification
driver.find_element_by_xpath(
    "//button[contains(text(),'Регистрация')]").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            "//button[contains(text(),'Регистрация')]"))).click()

driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

driver.find_element_by_xpath(
    "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,
                                                            "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
time.sleep(3)
#
fMail = fake_email[0].split("@")
mailName = fMail[0]
domain = fMail[1]
instCode = verifiCode.getInstVeriCode(mailName, domain, driver)
driver.find_element_by_name('email_confirmation_code').send_keys(instCode, Keys.ENTER)
time.sleep(10)
try:
    not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
    if (not_valid.text == 'That code isn\'t valid. You can request a new one.'):
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
        time.sleep(10)
        instCodeNew = verifiCode.getInstVeriCodeDouble(mailName, domain, driver, instCode)
        confInput = driver.find_element_by_name('email_confirmation_code')
        confInput.send_keys(Keys.CONTROL + "a")
        confInput.send_keys(Keys.DELETE)
        confInput.send_keys(instCodeNew, Keys.ENTER)
except:
    pass
