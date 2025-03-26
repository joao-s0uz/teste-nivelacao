# Importando bibliotecas
import requests
from bs4 import BeautifulSoup

# Pegando o url e armazenando em uma váriavel
response = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/')

# Pegando todo o conteúdo do url e armazenando na váriavel content
content = response.content

# Deixando o conteúdo da váriavel content mais legivel
site = BeautifulSoup(content, 'html.parser')

# Pegando apenas os links de PDF dos Anexos I e II
link1 = site.find('a', attrs={'data-mce-href': 'resolveuid/f710899c6c7a485ea62a1acc75d86c8c'})
link2 = site.find('a', attrs={'data-mce-href': 'resolveuid/85adaa3de5464d8aadea11456bfb4f94'})

# Transformando em uma única váriavel
links = [
  link1.get('href'),
  link2.get('href')
]

print(links)