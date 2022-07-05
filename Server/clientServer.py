import random

class ClientServer:
    
    def __init__(self, connection):
        self._connection = connection
        self._name = random.choice(["Brasil", "EUA", "Argentina", "México", "Chile", "Canada", "Bolivia", "Equador", "Colombia", "Guiana", "Jamaica", "Cuba", "Uruguai", "Paraguai", "Venezuela"])
        self._canal = None

    def __del__(self):
        return "O usuario " + str(self.get_name()) + " foi desconectado!"

    def get_connection(self):
        return self._connection
        
    def get_name(self):
        return self._name
    
    def set_canal(self, canal):
        self._canal = canal
        
    def get_canal(self):
        return self._canal