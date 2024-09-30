# installing relevant packages 
# https://pypi.org/project/chromedriver-py/
from chromedriver_py import binary_path
from selenium import webdriver
from time import sleep
# import requests
from bs4 import BeautifulSoup

# this is so that the program can find the chrome driver path and know how to open it
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)

# URL for scraping
url = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber"

driver.get(url)

# this is selenium method for getting from the current page
html = driver.page_source

# using beautiful soup to parse don't forget the beautiful soup feature argument html.parser
parsed_response = BeautifulSoup(html, "html.parser")


f = open("hansard.txt", "w")
f.write(parsed_response.prettify())

# pause the program for 5 seconds to view the results
sleep(5)

# close the driver
driver.quit()



# ------- below doesnt work because content is JS loaded, need to load in a local browser first - try selenium -------

# import requests
# from bs4 import BeautifulSoup

# website URL with contribution ID https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber#contribution-15052828000532
# creating a URL variable to add URL as a string
# url = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber"

# requesting url, accept argument is creating a dictionary that only takes in the HTML

# response = requests.get(url, headers={"Accept": "text/html"})

# parsing using HTML parser

# parsed_response = BeautifulSoup(response.text, "html.parser")

# calling prettify so that it is easier to use

# print(parsed_response.prettify())

# # ------- below is selnium, doesnt work because have not downloaded a chromedriver going to try using pip install instead -------

# import relevant libraries
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from time import sleep

# url = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber"

# instantiate webdriver and open a chrome browser 
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
# driver.maximize_window()

# load the webpage
# driver.get(url)

# response = requests.get(url, headers={"Accept": "text/html"})

# parsing using HTML parser

# parsed_response = BeautifulSoup(response.text, "html.parser")

# calling prettify so that it is easier to use

# print(parsed_response.prettify())


# pause the program for 5 seconds to view the results
# sleep(5)

# close the driver
# driver.quit()