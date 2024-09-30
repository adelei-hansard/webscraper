# installing relevant packages 
# https://pypi.org/project/chromedriver-py/
from chromedriver_py import binary_path
from selenium import webdriver
from selenium.webdriver.common.by import By  
from time import sleep
from bs4 import BeautifulSoup

# this is so that the program can find the chrome driver path and know how to open it
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

# URL for scraping
url = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber"

external_id = "contribution-150528280005322"

driver.get(url)
elem = driver.find_element(By.ID, external_id)

# using beautiful soup to parse don't forget the beautiful soup feature argument html.parser
parsed_response = BeautifulSoup(elem, "html.parser")

f = open("hansard-web-scrape-id.txt", "w")
f.write(parsed_response.prettify())

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()