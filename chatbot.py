import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv


load_dotenv()


chat = ChatGroq(model= 'llama-3.3-70b-versatile')


def resposta_bot(mensagens, documento):
    mensagens_padrao = [('system', '''Você é um assistente chamado Öyko. Você é expert em malwares de computador. 
Você é prestativo, amigável, e sempre responde perguntas de forma clara, e resumida.
Se necessário, você usa as seguintes informações para formular as suas respostas: {informacoes}.''')]
    mensagens_padrao += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_padrao)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content


def site():
    url_site = input('Digite a url do site: ')
    loader = WebBaseLoader(url_site) 
    lista_docs = loader.load() 
    documento = ''
    for doc in lista_docs:
        documento += doc.page_content
    return documento



documento = ''

def padrao():
    global documento
    while True:
        escolha = int(input('''Com o que deseja conversar hoje?
[1] Site
[2] Öyko
[3] Sair
'''))
        if escolha == 1:
            documento = site()
            break
            break
        elif escolha == 2:
            break
        elif escolha == 3:
            print('Desligando...')
            exit()
        else:
            print('Erro. Valor não incluso. Tente novamente')


padrao()

mensagens = []

while True:
    pergunta = input('User: ')
    if pergunta == 'x':
        mensagens = []
        documento = ''
        padrao() 
        continue 
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print(mensagens)








