# install requests
# install bs4 import BeautifulSoup

#to create a virtual Environment 
# python -m venv --name the new venv--

#to activate it 
# source --name the new venv--/bin/activate

import requests
from bs4 import BeautifulSoup

res = requests.get("https://knbs.ng/")

soup = BeautifulSoup(res.content, 'html.parser')

s = soup.find_all('a', class_='text-sm')

for data in s:
    print(data.text)