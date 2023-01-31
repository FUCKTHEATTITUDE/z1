import os
from telegram.ext import Updater
from config import Config
from .restricted import restricted
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


try:
 
 updater = Updater(token = Config.BOT_TOKEN, use_context=True)
 dp = updater.dispatcher
 options = webdriver.ChromeOptions()
 options.add_argument("-profile")
 options.add_argument(s)
 #profile = FirefoxProfile()
 #profile.set_preference("dom.webdriver.enabled", False)
 #profile.set_preference('useAutomationExtension', False)
 #profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36")
 #profile.update_preferences()
 desired = DesiredCapabilities.Chrome
 options.add_argument("--disable-infobars")
 options.add_argument("--headless")
 #options.add_argument("--window-size=1200,800")
 options.add_argument("--disable-blink-features=AutomationControlled")
 browser = webdriver.Chrome(options=options, desired_capabilities=desired, service_args=["--marionette-port", "2828"])
 #browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
except Exception as e:
 print(e)
