import random

"""
Classe ClientServer
classe responsável por fornecer uma estrutura de dado, para melhor gestão do cliente no servidor.
"""
class ClientServer:
    
    def __init__(self, connection):
        self._connection = connection
        self._name = random.choice(["Brasil", "EUA", "Argentina", "México", "Chile", "Canada", "Bolivia", "Equador", "Colombia", "Guiana", "Jamaica", "Cuba", "Uruguai", "Paraguai", "Venezuela"])
        self.channel = None
        
    def get_connection(self):
        return self._connection
        
    def get_name(self):
        return self._name
    
    def set_channel(self, channel):
        self.channel = channel
        
    def get_channel(self):
        return self.channel