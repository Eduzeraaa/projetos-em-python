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

## Verão 1.0.0 - 05/08/2025

### Adicionado
Criei um arquivo .env pra guardar minha key do Groq. 
### Alterado
Fiz algumas alterações:
- Removi a parte de vídeos do YouTube. Explicarei o por quê na seção _Frustrações_;
- Alterei as instruções do Öyko, agora ele é um assistente expert em qualquer assunto;
### Frustrações
Após mais de 12 horas pesquisando o motivo de não rodar a parte de ver vídeos do YouTube, cheguei em uma conclusão: o problema não era o código, nem a biblioteca. É algo que transcende o Python. Atualizei as bibliotecas, criei um ambiente virtual (venv), fiz alterações e substituí a biblioteca "_youtube-transcript-ai_" pelo "_pytube_", e os erros persistiram. Portanto, acabei desistindo por hora. Mas ainda sim, apesar de tamanha frustração, não descartei a ideia. Talvez em versões futuras eu consiga adicioná-lo.