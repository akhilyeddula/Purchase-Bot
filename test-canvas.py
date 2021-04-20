from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Firefox(options=Options)

# This is where the actual execution of the web driver starts.
driver.maximize_window()
driver.get("https://hcpscanvasproject.azurewebsites.net/")
login = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/a")
login.click()

original_window = driver.current_window_handle
wait = WebDriverWait(driver, 10)

wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Wait for the new tab to finish loading content
wait.until(EC.title_is("Sign In"))
print(driver.current_url)


#driver.quit()

    