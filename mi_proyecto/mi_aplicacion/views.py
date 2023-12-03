from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from mi_aplicacion.models import PaginaWeb, Parrafo, AnalisisTexto

def analisis_texto(request):
    
    url = "https://www.elfinanciero.com.mx/economia/2023/12/01/salario-minimo-2024-como-se-integra-el-aumento-de-20-por-ciento-para-el-proximo-ano/"
    response = requests.get(url)
    html_content = response.text

    
    soup = BeautifulSoup(html_content, 'html.parser')

    
    paragraphs = soup.find_all('p')
    text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

   
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)

    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)  
    summary_text = ' '.join([str(sentence) for sentence in summary])

   
    context = {
        'mostrar_informacion_analisis': True, 
        'tokens': tokens,
        'text': text,
        'tagged': tagged,
        'summary': summary_text,
    }

    return render(request, 'mi_aplicacion/analisis_texto.html', context)
