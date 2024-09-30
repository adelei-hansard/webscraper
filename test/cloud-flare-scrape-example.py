import requests
from bs4 import BeautifulSoup

# website URL with contribution ID https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber#contribution-15052828000532
# creating a URL variable to add URL as a string
url = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber"

# requesting url, accept argument is creating a dictionary that only takes in the HTML

response = requests.get(url, headers={"Accept": "text/html"})

# parsing using HTML parser

parsed_response = BeautifulSoup(response.text, "html.parser")

# calling prettify so that it is easier to use

print(parsed_response.prettify())