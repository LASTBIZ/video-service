import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def screenshot(name, site_url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    driver.set_window_size(1920, 1165)
    print(site_url)
    driver.get(site_url)
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "investors"))
    )
    driver.save_screenshot(name + ".png")
    driver.quit()
