from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

# This is where the actual execution of the web driver starts.
driver.get("https://hcpscanvasproject.azurewebsites.net/")
currentUrl = driver.current_url
print(currentUrl)  

driver.quit()
