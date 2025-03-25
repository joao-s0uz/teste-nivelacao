import requests
from bs4 import BeautifulSoup
import pdfkit

response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

link1 = site.find('a', attrs={'data-mce-href': 'resolveuid/f710899c6c7a485ea62a1acc75d86c8c'})
link2 = site.find('a', attrs={'data-mce-href': 'resolveuid/85adaa3de5464d8aadea11456bfb4f94'})

links = [
  link1.get('href'),
  link2.get('href')
]
print(links)

