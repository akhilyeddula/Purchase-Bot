from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time as t
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

inStock = False

disabled_button_hex = "#C5CBD5"

purchase_bot_options = Options()
purchase_bot_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(chrome_options=purchase_bot_options)
driver.maximize_window()


waiter = WebDriverWait(driver, 10)

graphics_card_link = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"

test_link = "https://www.bestbuy.com/site/pny-geforce-gt-710-2gb-pci-express-2-0-graphics-card-black/5092306.p?skuId=5092306"
 
driver.get(graphics_card_link)
add_to_cart_button_xpath = "/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[7]/div[1]/div/div/div/button"
add_to_cart_button = driver.find_element_by_xpath(add_to_cart_button_xpath)

def add_to_cart():
	global inStock 

	add_to_cart_button_rgb = add_to_cart_button.value_of_css_property('background-color')
	add_to_cart_button_hex = Color.from_string(add_to_cart_button_rgb).hex
		
	if add_to_cart_button_hex.lower() == disabled_button_hex.lower():
		inStock = False
	
	if inStock:
		add_to_cart_button.click()
	else:
		check_for_stock()
	
def check_for_stock():
	global inStock
	while not inStock:
		waiter.until(EC.presence_of_element_located((By.XPATH, add_to_cart_button_xpath)))

		print("checking for stock")
		add_to_cart_button_rgb = add_to_cart_button.value_of_css_property('background-color')
		add_to_cart_button_hex = Color.from_string(add_to_cart_button_rgb).hex
		
		if not add_to_cart_button_hex.lower() == disabled_button_hex.lower():
			inStock = True
		else:
			print("not in stock yet")
			t.sleep(5)
			driver.refresh()
	
	print("found stock")
	add_to_cart()

check_for_stock()
	
		