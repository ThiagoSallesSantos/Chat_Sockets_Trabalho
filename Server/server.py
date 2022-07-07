from clientServer import ClientServer
import threading
import socket
import json
import sys

class Server:
    
    def __init__(self, config_dir):
        self._ip, self._port = self._read_config(config_dir)
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._dict_connections = dict({})
        self._dict_channel = dict({})

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
            self._server.listen(5)
            print("Server está online!")
            self._operations()
        except Exception as e:
            print("ERRO - Erro ao iniciar o servidor.\nDescrição do erro: " + str(e))
        finally:
            self._close()

    def _operations(self):
        try:
            while True:
                connection, address = self._server.accept()
                self._dict_connections.update(dict({connection : ClientServer(connection)}))
                threading.Thread(target=self._receive_message, args=[connection, address]).start()
        except Exception as e:
            print("ERRO - Erro durante as chamadas de operações do server.\nDescrição do erro: " + str(e))
    
    def _receive_message(self, connection, address):
        try:
            print("O cliente portador do endereço: " + str(address[0]) + ":" + str(address[1]) + ". se conectou no servidor!")
            self._send_message(connection, "Server: Seja bem-vindo, seu nick no chat é: \"" + str(self._dict_connections[connection].get_name()) + "\"")
            while True:
                message = connection.recv(1024)
                message = json.loads(message.decode("utf-8"))
                self._process_command(connection, message)
        except Exception as e:
            print("ERRO - Erro durante o recebimento da mensagem.\nDescrição do erro: " + str(e))
    
    def _process_command(self, connection, command):
        try:
            if command["command"] == "msg":
                self._process_command_msg(connection, command["param"])
            elif command["command"] == "create":
                self._process_command_create(connection, command["param"])
            elif command["command"] == "connect":
                self._process_command_connect(connection, command["param"])
            elif command["command"] == "list":
                self._process_command_list(connection)
            elif command["command"] == "exit":
                self._process_command_exit(connection)
            else:
                self._send_message(connection, "Erro - Comando enviado não consta como comando aceito no servidor!")
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando do cliente.\nDescrição do erro: " + str(e))
    
    def _process_command_msg(self, connection, param):
        try:
            if self._dict_connections[connection].get_channel() in self._dict_channel.keys():
                for client in self._dict_channel[self._dict_connections[connection].get_channel()]:
                    if client.get_connection() is not connection:
                        self._send_message(client.get_connection(), str(self._dict_connections[connection].get_name()) + ": " + str(param))
            else:
                self._send_message(connection, "Server: Você não se encontra em um canal de mensagem ou o canal não existe mais!")
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando msg.\nDescrição do erro: " + str(e))
    
    def _process_command_create(self, connection, param):
        try:
            if param not in self._dict_channel.keys():
                self._dict_channel.update(dict({param : list([])}))
                self._send_message(connection, "Server: O canal \"" + str(param) + "\" foi criado!")
                self._process_command_connect(connection, param)
            else:
                self._send_message(connection, "Server: O canal " + str(param) + " já existe")
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando create.\nDescrição do erro: " + str(e))
    
    def _process_command_connect(self, connection, param):
        try:
            if param in self._dict_channel.keys():
                if self._dict_connections[connection] not in self._dict_channel[param]:
                    self._dict_channel[param].append(self._dict_connections[connection])
                    self._dict_connections[connection].set_channel(param)
                    self._send_message(connection, "Server: Você foi conectado no canal \"" + str(param) + "\"")
                    for client in self._dict_channel[param]:
                        if client.get_connection() is not connection:
                            self._send_message(client.get_connection(), "Server: O cliente " + str(self._dict_connections[connection].get_name()) + " se conectou no canal!")
                else:
                    self._send_message(connection, "Server: Você já se encontra conectado no canal \"" + str(param) + "\"")
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando connect.\nDescrição do erro: " + str(e))
    
    def _process_command_list(self, connection):
        try:
            message = "Lista de canais:\n"
            if self._dict_channel.keys():
                for canal in self._dict_channel.keys():
                    message += str(canal) + ": (membros no canal)\n"
                    if self._dict_channel[canal]:
                        for client in self._dict_channel[canal]:
                            message += "\t- " + str(client.get_name()) + "\n"
                    else:
                        message += "(Não possui membros onlines no canal)\n"
                    message += "-------------------------------\n"
            else:
                message += "(Não possui canais abertos)\n"
            self._send_message(connection, message)
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando list.\nDescrição do erro: " + str(e))
            
    def _process_command_exit(self, connection):
        try:
            client = self._dict_connections[connection]
            self._dict_channel[client.get_channel()].remove(client)
            del self._dict_connections[connection]
            for client_others in self._dict_channel[client.get_channel()]:
                if client_others.get_connection() is not connection:
                    self._send_message(client_others.get_connection(), "O cliente " + str(client.get_name()) + " se desconectou!")
        except Exception as e:
            print("ERRO - Erro durante o processamento do comando exit.\nDescrição do erro: " + str(e))
    
    def _send_message(self, connection, message):
        try:
            connection.send(bytes(message, encoding="utf-8"))
        except Exception as e:
            print("ERRO - Erro durante o envio de mensagem ao cliente.\nDescrição do erro: " + str(e))

if __name__ == "__main__":
    server = Server(sys.argv[1] if len(sys.argv) > 1 else "../Config/config.json")
    server.start()