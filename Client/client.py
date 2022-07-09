from clientCommands import Commands
import threading
import socket
import json
import sys

"""
Classe Client
classe responsável pela criação do client e sua gestão, além de ministrar o envio e recebimento de mensagens.
"""
class Client:

    ## Construtor da classe Server
    def __init__(self, config_dir):
        self._ip_server, self._port_server = self._read_config(config_dir)
        self._client_commands = Commands() ## Cria um objeto da classe Commands
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP e IP 
    
    ## Ler as configurações de ip e porta que serão utilizadas pelo servidor 
    def _read_config(self, config_dir):
        try:
            with open(config_dir, "r") as archive:
                config_data = json.load(archive)
            return config_data["ip"], config_data["port"]
        except Exception as e:
            print("ERRO - Erro ao ler o documento \"" + str(config_dir) + "\"\nDescrição do erro: " + str(e))
    
    ## Fecha a conexão do cliente
    def _close_connect(self):
        try:
            self._connection.close() ## Fecha a conexão do cliente
            print("Conexão fechada com sucesso ;)")
        except Exception as e:
            print("ERRO - Erro ao fechar a conexão com o servidor.\nDescrição do erro: " + str(e))
    
    ## Conecta-se ao servidor
    def connect(self):
        try:
            self._connection.connect((self._ip_server, self._port_server)) ## Conecta-se ao servidor
            print("Conecção com o servidor '" + str(self._ip_server) + "' estabelecida!")
            print("Obs: Para se comunicar basta esta conectado em algum canal, para isso saber mais use o comando \"help\"")
            self._start()
        except Exception as e:
            print("ERRO - Erro ao estabelecer conexão com o servidor.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()
    
    ## Inicia as operações do cliente que é enviar e receber mensagens, sendo que receber é uma thread 
    def _start(self):
        try:
            threading.Thread(target = self._receive_message).start() ## Inicia a thread para receber mensagens
            self._console() ## Chama metodo responsável por enviar mensagens
        except Exception as e:
            print("ERRO - Erro ao iniciar as operações.\nDescrição do erro: " + str(e))
    
    ## Recebe a mensagem e exibe na tela
    def _receive_message(self):
        try:
            while True:
                message = self._connection.recv(1024) ## Recebe mensagem
                message = message.decode("utf-8") ## Decodifica a mensagem
                print(message)
        except Exception as e:
            print("ERRO - Erro ao receber uma mensagem.\nDescrição do erro: " + str(e))
    
    ## Responsável por controlar o envio de mensagem
    def _console(self):
        try:
            while True:
                command = self._get_command()
                if command is not None:
                    self._send_command(command)
                    if command["command"] == "exit":
                        break
        except Exception as e:
            print("ERRO - Erro ao gerenciar o envio de mensagens.\nDescrição do erro: " + str(e))
    
    ## Recebe o comando do usuário
    def _get_command(self):
        try:
            return self._client_commands.onecmd(input())
        except Exception as e:
            print("ERRO - Erro ao ler o comando digitado.\nDescrição do erro: " + str(e))
    
    ## Envia o comando ao servidor
    def _send_command(self, command):
        try:
            self._connection.send(bytes(json.dumps(command), encoding="utf-8")) ## Transforma o dict de comando em json, para pode codificar e enviar os bytes ao servidor.
        except Exception as e:
            print("ERRO - Erro ao enviar o comando.\nDescrição do erro: " + str(e))

if __name__ == "__main__":
    client = Client(sys.argv[1] if len(sys.argv) > 1 else "../Config/config.json")
    client.connect()
    