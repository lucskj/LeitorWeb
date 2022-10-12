import requests
from bs4 import BeautifulSoup
import spacy


# Função responsável por filtrar e remover partes específicas da página.
def removerTags(soup):
    for data in soup(['style', 'script', 'head', 'header', 'meta', '[document]', 'title', 'footer', 'iframe', 'nav']):
        data.decompose()
        
    # Retornando todas as expressões em uma string, separando por espaço.
    return ' '.join(soup.stripped_strings)   


# Carregando a biblioteca Spacy, baseando-se na língua inglesa.
nlp = spacy.load("en_core_web_sm")

# Variáveis para armazenar o link de cada página.
url1 = 'https://hbr.org/2022/04/the-power-of-natural-language-processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
url4 = 'https://monkeylearn.com/natural-language-processing/'
url5 = 'https://en.wikipedia.org/wiki/Natural_language_processing'

# Salvando os links em uma lista.
urls = [url1, url2, url3, url4, url5]

# Definindo arrays para armazenar o resultado de todos os textos.
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []

# Loop para passar por cada url.
for url in urls:
  urlAtual = urls.index(url)                        # Salvando o índice da url em questão.
  html = requests.get(url).text                     # Armazenando o conteúdo de toda a página.
  soup = BeautifulSoup(html, 'html.parser')         # Removendo parte da estrutura HTML do texto.
  texts = removerTags(soup)                         # Enviando o texto para filtrar.
  page = nlp(texts)

  # Armazenando as sentenças em suas respectivas listas.
  for sentence in page.sents:
    if urlAtual == 0:
      t1.append(sentence.text)
    elif urlAtual == 1:
      t2.append(sentence.text)
    elif urlAtual == 2:
      t3.append(sentence.text)
    elif urlAtual == 3:
      t4.append(sentence.text)
    elif urlAtual == 4:
      t5.append(sentence.text)

# Printando o resultado das listas, para checagem.
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
