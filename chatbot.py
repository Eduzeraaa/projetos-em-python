import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader

if not os.path.exists(".env"):
    chave = input("Digite sua GROQ_API_KEY: ").strip()
    with open(".env", "w") as f:
        f.write(f"GROQ_API_KEY={chave}")


load_dotenv()



api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("Erro: chave da API não encontrada.")
    exit()
os.environ["GROQ_API_KEY"] = api_key



chat = ChatGroq(model='llama-3-3-70b-versatile')




def resposta_bot(mensagens, documento):
    mensagens_padrao = [('system', '''Você é um assistente chamado Öyko. Você é expert em malwares de computador. 
Você é prestativo, amigável, e sempre responde perguntas de forma clara, e resumida.
Se necessário, você usa as seguintes informações para formular as suas respostas: {informacoes}.''')]
    mensagens_padrao += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_padrao)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content





def site():
    while True:
        url_site = input('Digite a URL do site (ou x para voltar): ').strip()
        if url_site.lower() == 'x':
            return None  # sinal para voltar
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
            print('URL inválida. Digite uma URL começando com http:// ou https://, ou x para voltar.')





def padrao():
    while True:
        escolha = input('''Com o que deseja conversar hoje?
[1] Site
[2] Öyko
[3] Sair
(x para sair)
''').strip().lower()

        if escolha == 'x' or escolha == '3':
            print('Desligando...')
            exit()

        if escolha == '1':
            documento = site()
            if documento is None:  # usuário digitou x pra voltar
                continue  # volta pro menu
            return documento
        elif escolha == '2':
            return ''  # sem documento externo
        else:
            print('Entrada inválida. Digite 1, 2, 3 ou x.')




def main():
    while True:
        documento = padrao()
        mensagens = []

        while True:
            pergunta = input('User: ').strip()
            if pergunta.lower() == 'x':
                print("Voltando para o menu principal...")
                break  # volta para o menu principal

            mensagens.append(('user', pergunta))
            resposta = resposta_bot(mensagens, documento)
            mensagens.append(('assistant', resposta))
            print(f'Bot: {resposta}')

if __name__ == "__main__":
    main()
