import requests
from bs4 import BeautifulSoup, Comment
import spacy

# Carregando a biblioteca Spacy, baseando-se na língua inglesa.
nlp = spacy.load("en_core_web_sm")


# Função responsável por filtrar e selecionar partes específicas da página.
def selecionarTexto(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


# Variáveis para armazenar o link de cada página.
url1 = 'https://hbr.org/2022/04/the-power-of-natural-language-processing'
url2 = 'https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html'
url3 = 'https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP'
url4 = 'https://monkeylearn.com/natural-language-processing/'
url5 = 'https://en.wikipedia.org/wiki/Natural_language_processing'

# Salvando os links em uma lista.
urls = [url1, url2, url3, url4, url5]

# Definindo arrays para armazenar o resultado de todos os textos.
frases1 = []
frases2 = []
frases3 = []
frases4 = []
frases5 = []

qtdLinks = len(urls)
i = 0

# Loop para passar por cada url.
while i < qtdLinks:
  html = requests.get(urls[i]).text                 # Armazenando o conteúdo de toda a página.
  soup = BeautifulSoup(html, 'html.parser')         # Removendo parte das tags HTML para estruturar o texto.
  texts = soup.findAll(text=True)
  textFiltrado = filter(selecionarTexto, texts)     # Enviando o texto para a filtragem.
  text = " ".join(t.strip() for t in textFiltrado)  # Armazenando todas as expressões em uma string, separando por espaço.
  page = nlp(text)

  # Armazenando as sentenças em suas respectivas listas.
  for sentence in page.sents:
    if i == 0:
      frases1.append(sentence.text)
    elif i == 1:
      frases2.append(sentence.text)
    elif i == 2:
      frases3.append(sentence.text)
    elif i == 3:
      frases4.append(sentence.text)
    elif i == 4:
      frases5.append(sentence.text)

  i += 1

# Printando o resultado das listas, para checagem.
print(frases1)
print(frases2)
print(frases3)
print(frases4)
print(frases5)
