import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv



if not os.path.exists(".env"):
    chave = input("Digite sua GROQ_API_KEY: ").strip()
    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={chave}")



load_dotenv()


chat = ChatGroq(model= 'llama-3.3-70b-versatile')


def resposta_bot(mensagens, documento):
    mensagens_padrao = [('system', '''Você é um assistente chamado Öyko. Você é expert em todos os assuntos. 
Você é prestativo, amigável, e sempre responde perguntas de forma clara, e resumida.
Se necessário, você usa as seguintes informações para formular as suas respostas: {informacoes}.''')]
    mensagens_padrao += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_padrao)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content



def site():
    while True:
        url_site = input('Digite a URL do site (ou "x" para voltar): ').strip()
        if url_site.lower() == 'x':
            return None 
        if url_site.startswith('http://') or url_site.startswith('https://'):
            try:
                loader = WebBaseLoader(url_site) 
                lista_docs = loader.load() 
                documento = ''
                for doc in lista_docs:
                    documento += doc.page_content
                return documento
            except Exception as e:
                print(f'Erro ao carregar o site: {e}')
        else:
            print('URL inválida. Tente novamente.')




documento = ''


def padrao():
    global documento
    while True:
        try:
            escolha = int(input('''Com o que deseja conversar hoje?
[1] Site
[2] Öyko
[3] Sair
'''))
        except ValueError:
            print('Entrada inválida. Tente novamente.')
            continue

        if escolha == 1:
            doc = site()
            if doc is None:
                continue
            documento = doc
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
