import requests
from bs4 import BeautifulSoup as bs
print("londiyo ki dp download ker ne wala")
github_user = input("User name bta bosdike : ")
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Avatar'})['src']
print("horhe hy download hawasi ..................")
print(profile_image)

print('Maderchod link per click ker ke dp download ker le')