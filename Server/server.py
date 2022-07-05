from clientServer import ClientServer
from serverCommands import Commands
import threading
import socket
import json
import sys

class Server:
    
    def __init__(self, config_dir):
        self._ip, self._port = self._read_config(config_dir)
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_commands = Commands()
        self._dict_connections = dict({})

    def _read_config(self, config_dir):
        try:
            with open(config_dir, "r") as archive:
                config_data = json.load(archive)
            return config_data["ip"], config_data["port"]
        except Exception as e:
            print("ERRO - Erro ao ler o documento \"" + str(config_dir) + "\"\nDescrição do erro: " + str(e))

    def _desconnect_clients(self):
        try:
            pass
        except Exception as e:
            print("ERRO - Erro ao ler o documento \"" + str(config_dir) + "\"\nDescrição do erro: " + str(e))

    def _close(self):
        try:
            self._server.close()
            print("Servidor foi desligado com sucesso ;)")
        except Exception as e:
            print("ERRO - Erro ao desligar o servidor\nDescrição do erro: " + str(e))
    
    def start(self):
        try:
            self._server.bind((self._ip, self._port))
            self._server.listen(1)
            print("Server está online!")
            self._operations()
        except Exception as e:
            print("ERRO - Erro ao iniciar o servidor.\nDescrição do erro: " + str(e))
        finally:
            self._close()

    def _operations(self):
        try:
            threading.Thread(target=self._console).start()
            while True:
                connection, address = self._server.accept()
                self._dict_connections.update(dict({connection : ClientServer(connection)}))
                threading.Thread(target=self._receive_message, args=[connection, address]).start()
        except Exception as e:
            print("ERRO - Erro durante as chamadas de operações do server.\nDescrição do erro: " + str(e))
    
    def _console(self):
        try:
            while True:
                pass
        except Exception as e:
            print("ERRO - Erro durante a gerencia do console.\nDescrição do erro: " + str(e))
    
    def _get_command(self):
        try:
            return self._server_commands.onecmd(input())
        except Exception as e:
            print("ERRO - Erro ao ler o comando digitado.\nDescrição do erro: " + str(e))
    
    def _receive_message(self, connection, address):
        try:
            print("O cliente portador do endereço: " + str(address[0]) + ":" + str(address[1]) + ". se conectou no servidor!")
            while True:
                message = connection.recv(1024)
                message = json.loads(message.decode("utf-8"))
        except Exception as e:
            print("ERRO - Erro durante o recebimento da mensagem.\nDescrição do erro: " + str(e))
    
    def _process_command(self, command):
        try:
            
        except:
            print("ERRO - Erro durante o recebimento da mensagem.\nDescrição do erro: " + str(e))
    
    def _send_message(self, connection, command):
        try:
            connection.send(bytes(json.dumps(command), encoding="utf-8"))
        except Exception as e:
            print("ERRO - Erro durante as chamadas de operações do server.\nDescrição do erro: " + str(e))

if __name__ == "__main__":
    server = Server(sys.argv[1] if len(sys.argv) > 1 else "../Config/config.json")
    server.start()