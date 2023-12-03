import requests
from bs4 import BeautifulSoup
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


url = "https://www.eluniversal.com.mx/nacion/ya-estas-grande-amlo-llega-a-los-70-anos-con-felicitaciones-de-su-familia-y-gabinete/"
response = requests.get(url)
html_content = response.text


soup = BeautifulSoup(html_content, 'html.parser')


paragraphs = soup.find_all('p')
text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])


tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)


print("Tokens:", tokens)
print("\nTexto Completo:\n", text)
print("\nEtiquetas gramaticales:", tagged)


parser = PlaintextParser.from_string(text, Tokenizer("spanish"))
summarizer = LsaSummarizer()
summary = summarizer(parser.document, 3)  

print("\nResumen:")
for sentence in summary:
    print(sentence)

