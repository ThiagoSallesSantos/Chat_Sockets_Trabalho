# Chat_Sockets_Trabalho
<p>Trabalho Prático 1 - Chat - Sistemas Distribuídos (GCC129)</p>
</p>Membros:</p>
- Arthur Silveira Franco
- Thiago Salles Santos
## Descrição:
<p>Chat de comunicação, usando a ideias de canais, para que computadores em uma mesma rede possam comunicar, utilizando de sockets, feito em python 3, com objetivo de obtenção de pontos na matéria Sistemas Distribuidos da Universidade Federal de Lavras.</p>
## Instruções:
### Execução:
<p>Necessário ter o python 3 instalado, preferencialmente a versão 3.9 ou superior. (Sistema desenvolvido na versão 3.9.2)</p>
<p>Para executar basta executar o código server.py (./Server/server.py) primeiro, passando o diretório onde se encontra a configuração de ip e porta que serão utilizadas, por padrão o arquivo será config.json (./Config/config.json), para que desta maneira o servidor seja inicializado.<br/> Posterior executar o código do client.py (./Client/client.py), passando o diretório onde se encontra a configuração de ip e porta que serão utilizadas, por padrão o arquivo será config.json (./Config/config.json), o limite de clientes no servidor é 5 por padrão.</p>
<p>Comandos:</p>
<p>
- python3 server.py <br/>
- python3 client.py <br/>
ou <br/>
- python3 server.py <dir_configurações> <br/>
- python3 client.py <dir_configurações> <br/>
</p>
<p>OBS: em caso de mudança do arquivo config.json ou criação de outro arquivo, deve ser seguido a seguinte estrutura:</p>
<p>{"ip":<ip_escolhido>, "port":<porta_escolhida>}</p>
### Bibliotecas:
<p>Todas as bibliotecas utilizadas no projeto, são bibliotecas padrões do python 3, são elas:</p>
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
<p>Ao se conectar o servidor o cliente deve inicialmente adentrar em algum canal de comunicação ou criar um novo canal, pelos comandos:</p>
<p>
- connect <nome_canal> <br/>
ou <br/>
- create <nome_canal> <br/>
</p>
<p>Caso não conheça o nome do canal que deseja adentrar basta, usar o comando "list", que irá listar os canais e os membros que estão nestes canais.<br/> Em caso de dúvida basta utilizar o comando "help".<br/> As mensagens são todos os input's que não são considerados comandos.</p>