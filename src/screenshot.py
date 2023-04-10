import os
from selenium import webdriver

def screenshot(name, site_url):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Remote(
        command_executor='http://192.168.0.3:4444',
        options=options
    )
    driver.set_window_size(1920, 1165)
    driver.get(site_url)
    driver.save_screenshot(name + ".png")
    driver.quit()
