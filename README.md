# Chat_Sockets_Trabalho
Trabalho Prático 1 - Chat - Sistemas Distribuídos (GCC129)<br/>
Membros:
- Arthur Silveira Franco
- Thiago Salles Santos
## Descrição:
Chat de comunicação, usando a ideias de canais, para que computadores em uma mesma rede possam comunicar, utilizando de sockets, feito em python 3, com objetivo de obtenção de pontos na matéria Sistemas Distribuidos da Universidade Federal de Lavras.
## Instruções:
### Execução:
Necessário ter o python 3 instalado, preferencialmente a versão 3.9 ou superior. (Sistema desenvolvido na versão 3.9.2) <br/>
Para executar basta executar o código server.py (./Server/server.py) primeiro, passando o diretório onde se encontra a configuração de ip e porta que serão utilizadas, por padrão o arquivo será config.json (./Config/config.json), para que desta maneira o servidor seja inicializado. <br/>Posterior executar o código do client.py (./Client/client.py), passando o diretório onde se encontra a configuração de ip e porta que serão utilizadas, por padrão o arquivo será config.json (./Config/config.json), o limite de clientes no servidor é 5 por padrão. <br/>
Comandos:
- python3 server.py
- python3 client.py
<br/>
ou
- python3 server.py [dir_configurações]
- python3 client.py [dir_configurações]
<br/>
OBS: em caso de mudança do arquivo config.json ou criação de outro arquivo, deve ser seguido a seguinte estrutura: <br/>
{"ip":<ip_escolhido>, "port":<porta_escolhida>}
### Bibliotecas:
Todas as bibliotecas utilizadas no projeto, são bibliotecas padrões do python 3, são elas: <br/>
- cmd 
- sys
- sockets
- threading
- json
## Estrutura:
- Server
	- server.py
	- clientServer.py
- Config
	- config.json
- Client
	- client.py
	- clientCommands
## Funcionamento:
Ao se conectar o servidor o cliente deve inicialmente adentrar em algum canal de comunicação ou criar um novo canal, pelos comandos:
<br/>
- connect [nome_canal]
<br/>
ou
- create [nome_canal]
<br/>
Caso não conheça o nome do canal que deseja adentrar basta, usar o comando "list", que irá listar os canais e os membros que estão nestes canais. Em caso de dúvida basta utilizar o comando "help". As mensagens são todos os input's que não são considerados comandos.