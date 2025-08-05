# CHANGELOG PROJETO ÖYKO
## Versão 0.1.0 - 02/08/2025
Primeira versão funcional do assistente Öyko. Feito com LangChain, usando API da Groq, que disponibilizou o modelo LlaMA 3.3-70b que estou usando atualmente. Inicialmente, Öyko é um assistente produzido "exclusivamente" para falar sobre malwares, porém, penso em mudar sua instrução futuramente, para ser um assistente geral, que ajuda em qualquer assunto.
## Versão 0.1.1 - 03/08/2025
### Adicionado
Consegui adicionar um sistema de leitura de sites no Öyko. Basta o usuário inserir a URL do site e fazer um comando. Funcionou perfeitamente e, como já dito, ele pode falar sobre quaisquer assuntos.
### Alterado
Alterei coisas básicas nas instruções do Öyko, para ele conseguir conversar sobre o site escolhido. Também fiz uma alteração no código, onde o usuário aperta 1 para enviar a URL de um site, 2 para um vídeo no YouTube (em desenvolvimento), 3 para falar com o assistente, e 4 para desligar. Caso o usuário tenha escolhido uma das 3 opções (com exceção da opção desligar), e queira trocar (exemplo: estava na opção de conversar com Öyko e agora quer ver sobre um site), o usuário envia "x", que ele voltará para a tela de seleção.
### Frustrações
Por algum motivo, não estou conseguindo integrar vídeos do YouTube. Ao selecionar a opção 2, eu envio a URL do vídeo, porém, acontece um bug. Já tentei mudar a versão da biblioteca, fiz mudanças no código, pesquisei, porém não funcionou. Decidi tentar novamente amanhã, já que apesar da frustração, foi um dia produtivo.
