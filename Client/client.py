from clientCommands import Commands
import threading
import socket
import json
import sys

class Client:

    def __init__(self, config_dir):
        self._ip_server, self._port_server = self._read_config(config_dir)
        self._client_commands = Commands()
        self._connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def _read_config(self, config_dir):
        try:
            with open(config_dir, "r") as archive:
                config_data = json.load(archive)
            return config_data["ip"], config_data["port"]
        except Exception as e:
            print("ERRO - Erro ao ler o documento \"" + str(config_dir) + "\"\nDescrição do erro: " + str(e))
    
    def _close_connect(self):
        try:
            self._connection.close()
            print("Conexão fechada com sucesso ;)")
        except Exception as e:
            print("ERRO - Erro ao fechar a conexão com o servidor.\nDescrição do erro: " + str(e))
    
    def connect(self):
        try:
            self._connection.connect((self._ip_server, self._port_server))
            print("Conecção com o servidor '" + str(self._ip_server) + "' estabelecida!")
            self._start()
        except Exception as e:
            print("ERRO - Erro ao estabelecer conexão com o servidor.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()
    
    def _start(self):
        try:
            threading.Thread(target = self._receive_message).start()
            self._console()
        except Exception as e:
            print("ERRO - Erro ao iniciar as operações.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()
    
    def _receive_message(self):
        try:
            while True:
                message = self._connection.recv(1024)
                print(message + "\n")
        except Exception as e:
            print("ERRO - Erro ao gerenciar o envio de mensagens.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()
    
    def _console(self):
        try:
            while True:
                command = self._get_command()
                if command is not None:
                    self._send_command(command)
                    if command["command"] == "exit":
                        self._close_connect()
                        break
        except Exception as e:
            print("ERRO - Erro ao gerenciar o envio de mensagens.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()
            
    def _get_command(self):
        try:
            return self._client_commands.onecmd(input())
        except Exception as e:
            print("ERRO - Erro ao ler o comando digitado.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()

    def _send_command(self, command):
        try:
            self._connection.send(bytes(command, encoding="utf-8"))
        except Exception as e:
            print("ERRO - Erro ao enviar o comando.\nDescrição do erro: " + str(e))
        finally:
            self._close_connect()

if __name__ == "__main__":
    client = Client(sys.argv[1] if len(sys.argv) > 1 else "../Config/config.json")
    client.connect()
    