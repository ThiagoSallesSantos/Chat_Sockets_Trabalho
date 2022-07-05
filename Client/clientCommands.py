import cmd
import json

class Commands(cmd.Cmd):

    ## Metodos - Comandos
    def do_msg(self, message):
        if message:
            return self._modelResponse('msg', message)
        print('\n' + 'comando inválido, não foi passado nenhuma mensagem para envio no canal, use o comando "help msg" para mais informações.' + '\n')
        
    def do_create(self, name):
        if name:
            return self._modelResponse('create', name)
        print('\n' + 'comando inválido, não foi passado nenhum nome para o canal a ser criado, use o comando "help create" para mais informações.' + '\n')
        
    def do_connect(self, name):
        if name:
            return self._modelResponse('connect', name)
        print('\n' + 'comando inválido, não foi passado nenhum nome de canal para se conectar, use o comando "help connect" para mais informações.' + '\n')
    
    def do_list(self):
        return self._modelResponse('list', None)
    
    def do_exit(self):
        return self._modelResponse('exit', None)
    
    ## Helpers Methods
    def help_msg(self):
        print('\n' + 'msg <message>' + '\n' + '<message> mensagem que deseja enviar no canal.' + '\n')
        
    def help_create(self):
        print('\n' + 'create <name>' + '\n' + '<name> nome do canal que deseja criar.' + '\n')
        
    def help_connect(self):
        print('\n' + 'connect <name>' + '\n' + '<name> nome do canal que deseja adentrar.' + '\n')
        
    def help_list(self):
        print('\n' + 'list' + '\n' + 'Lista os comandos disponiveis.' + '\n')
        
    def help_exit(self):
        print('\n' + 'list' + '\n' + 'Finaliza a conecção com o servidor.' + '\n')
    
    ## Utilies Methods
    def default(self, line):
        print('\n' + 'comando inválido "' + str(line) + '", use o comando "help" para ver a lista de comandos disponiveis.' + '\n')
        
    def _model_response(self, command, id):
        return json.dumps({'command': str(command), 'param': str(id)})
