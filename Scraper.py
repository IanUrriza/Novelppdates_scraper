

import undetected_chromedriver.v2 as uc
import selenium
from selenium.webdriver.common.by import By
class Scraper:
    driver = None

    def __init__(self):
        self.driver = uc.Chrome()

    def search_titles(self,page:int):
        self.driver.get(f'https://www.novelupdates.com/novelslisting/?sort=7&order=1&status=1&pg={page}')
        content = self.driver.find_elements(By.CLASS_NAME,'search_title')
        return content



scraper = Scraper()
content = scraper.search_titles(1)
for i in content:
    print(i.text)
for i in content:
    link = i.find_element(By.TAG_NAME,'a')
    print(link.get_attribute('href'))