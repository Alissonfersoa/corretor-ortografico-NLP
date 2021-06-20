# Corretor ortografico
import nltk

# abrir arquivo
with open('C:\\Users\\batis\\OneDrive\\Documents\\GitHub\\corretor-ortografico-NLP\\treinamento.txt', encoding="utf8",mode='r') as f:
    treinamento = f.read()

# print(treinamento[:500])

exemplo_texto = ('ortografia, texto para corrigir')

exemplo_palavra = ('linguaem')

palavras_separadas = nltk.tokenize.word_tokenize(exemplo_texto)

lista_tokens = nltk.tokenize.word_tokenize(treinamento)

# Criando uma função para separar as palavras
def separa_palavras(lista_tokens):
    
    # Criando uma lista vázia
    lista_palavras = []
    
    for token in lista_tokens:
        
        if token.isalpha():
            
            lista_palavras.append(token)
    
    return lista_palavras

# Chamando a função e passando o parâmetro
# print(separa_palavras(palavras_separadas))

def normalizacao(lista_palavras):
    
    lista_normalizada = []
    
    for palavra in lista_palavras:
        
        lista_normalizada.append(palavra.lower())
        
    return lista_normalizada

def insere_letras(fatias):
    
    novas_palavras =[]
    
    letras = 'abcedfghijklmnopqrstuvwxyzáâàãéêèíîìóôòõúûùç'
    
    for esquerdo, direito in fatias:
        
        for letra in letras:
            
            novas_palavras.append(esquerdo + letra + direito)
    
    return novas_palavras


def gerador_palavras(palavra):
    
    fatias = []
    
    for i in range(len(palavra) + 1):
        
        fatias.append((palavra[:i], palavra[i:]))
    
    palavras_geradas = insere_letras(fatias)
    
    return palavras_geradas


def probabilidade(palavra_gerada):

    frequencia = nltk.FreqDist(lista_normalizada)
    total_palavras = len(lista_normalizada)
    
    return frequencia[palavra_gerada] / total_palavras

def corretor(palavra_errada):
    
    palavras_geradas = gerador_palavras(palavra_errada)
    
    palavra_correta = max(palavras_geradas, key=probabilidade)
    
    # Retorna a palavra já corrigida
    return palavra_correta

# Chamando a função e passando os parâmetros
# Imprimindo uma amostra do resultado


# ---------------------------------------------------------------------------
# Chamando a função e passando o corpus como parâmetro
lista_palavras = separa_palavras(lista_tokens)

# Chamando a função e passando os parâmetros
lista_normalizada = normalizacao(lista_palavras)

# Imprimindo uma amostra do resultado
# print(lista_normalizada[:10])
# print(insere_letras([('o', 'tografia')])[:10])

palavras_geradas = gerador_palavras(exemplo_palavra)

# Imprimindo a palavra de exemplo com uma amostra do resultado
# print(palavras_geradas[:5])

print(corretor(exemplo_palavra))


# ---------------------------------------------------------------------------

