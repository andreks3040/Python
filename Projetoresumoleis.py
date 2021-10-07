
import re
import nltk
import string
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
texto_original = """Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios:

I - independência nacional;

II - prevalência dos direitos humanos;

III - autodeterminação dos povos;

IV - não-intervenção;

V - igualdade entre os Estados;

VI - defesa da paz;

VII - solução pacífica dos conflitos;

VIII - repúdio ao terrorismo e ao racismo;

IX - cooperação entre os povos para o progresso da humanidade;

X - concessão de asilo político.

Parágrafo único. A República Federativa do Brasil buscará a integração econômica, política, social e cultural dos povos da América Latina, visando à formação de uma comunidade latino-americana de nações."""
texto_original = re.sub(r'\n+', ' ', texto_original)

def preprocessamento(texto):
  texto_formatado = texto.lower()
  tokens = []
  for token in nltk.word_tokenize(texto_formatado):
    tokens.append(token)

  tokens = [palavra for palavra in tokens if palavra not in palavrascomuns ]
  texto_formatado = ' '.join([str(elemento) for elemento in tokens])

  return texto_formatado

palavrascomuns = [';',',','.','-','de', 'a', 'o', 'que', 'é', 'do', 'da', 'em', 'para', 'com', 'os', 'no', 'se', 'na', 'por', 'mais', 'as', 'dos', 'como', 'mas', 'ao', 'ele', 'das', 'à', 'seu', 'sua', 'ou', 'quando', 'muito', 'nos', 'já', 'eu', 'também', 'só', 'pelo', 'pela', 'até', 'isso', 'ela', 'entre', 'depois', 'sem', 'mesmo', 'aos', 'seus', 'quem', 'nas', 'me', 'esse', 'eles', 'você', 'essa', 'num', 'nem', 'suas', 'meu', 'às', 'minha', 'numa', 'pelos', 'elas', 'qual', 'nós', 'lhe', 'deles', 'essas', 'esses', 'pelas', 'este', 'dele', 'tu', 'te', 'vocês', 'vos', 'lhes', 'meus', 'minhas', 'teu', 'tua', 'teus', 'tuas', 'nosso', 'nossa', 'nossos', 'nossas', 'dela', 'delas', 'esta', 'estes', 'estas', 'aquele', 'aquela', 'aqueles', 'aquelas', 'isto', 'aquilo', 'estou', 'está', 'estamos', 'estão', 'estive', 'esteve', 'estivemos', 'estiveram', 'estava', 'estávamos', 'estavam', 'estivera', 'estivéramos', 'esteja', 'estejamos', 'estejam', 'estivesse', 'estivéssemos', 'estivessem', 'estiver', 'estivermos', 'estiverem', 'hei', 'há', 'havemos', 'hão', 'houve', 'houvemos', 'houveram', 'houvera', 'houvéramos', 'haja', 'hajamos', 'hajam', 'houvesse', 'houvéssemos', 'houvessem', 'houver', 'houvermos', 'houverem', 'houverei', 'houverá', 'houveremos', 'houverão', 'houveria', 'houveríamos', 'houveriam', 'sou', 'somos', 'são', 'era', 'éramos', 'eram', 'fui', 'foi', 'fomos', 'foram', 'fora', 'fôramos', 'seja', 'sejamos', 'sejam', 'fosse', 'fôssemos', 'fossem', 'for', 'formos', 'forem', 'serei', 'será', 'seremos', 'serão', 'seria', 'seríamos', 'seriam', 'tenho', 'tem', 'temos', 'tém', 'tinha', 'tínhamos', 'tinham', 'tive', 'teve', 'tivemos', 'tiveram', 'tivera', 'tivéramos', 'tenha', 'tenhamos', 'tenham', 'tivesse', 'tivéssemos', 'tivessem', 'tiver', 'tivermos', 'tiverem', 'terei', 'terá', 'teremos', 'terão', 'teria', 'teríamos', 'teriam']

texto_formatado = preprocessamento(texto_original)
texto_formatado

from nltk.tokenize import LineTokenizer


lista_sentencas = nltk.tokenize.line_tokenize(texto_original, blanklines='discard')

lista_palavras = nltk.word_tokenize(texto_formatado)

lista_sentencas2 =nltk.word_tokenize(texto_original)

from IPython.core.display import HTML
from IPython.display import display
texto = ' '
space = """  """
display(HTML(f'<h1>Resumo do Texto</h1>'))
for palavra2 in lista_sentencas2:
  if palavra2 in lista_palavras:
    texto += str(palavra2).replace(palavra2, f"<mark>{palavra2}</mark>")+' '
  else:
    texto += palavra2+' '
display(HTML(f"""{texto}"""))


