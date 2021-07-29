from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium import webdriver



PROXY = "91.218.229.103:3128"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome = webdriver.Chrome(executable_path=CM().install(), chrome_options=chrome_options)
chrome.get("http://whatismyipaddress.com/")
print()
