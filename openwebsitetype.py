from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

driver.get('https://www.glassdoor.co.in/index.htm')

driver.find_element_by_xpath(".//*[@id='KeywordSearch']").send_keys("Software Tester")

driver.find_element_by_xpath('//*[@id="HeroSearchButton"]').click()

jobs_list = driver.find_elements_by_xpath("//*[@class='jlGrid hover']/li")

txt)

jobs_outfiles.close()