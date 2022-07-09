import cmd

"""
Classe Commands
classe responsável por gerenciar os comandos disponíveis pelos clientes.
"""
class Commands(cmd.Cmd):

    ## Metodos - Comandos
    def default(self, message):
        return self._model_response('msg', message)
    
    def do_create(self, name):
        if name:
            return self._model_response('create', name)
        print('\n' + 'comando inválido, não foi passado nenhum nome para o canal a ser criado, use o comando "help create" para mais informações.' + '\n')
        
    def do_connect(self, name):
        if name:
            return self._model_response('connect', name)
        print('\n' + 'comando inválido, não foi passado nenhum nome de canal para se conectar, use o comando "help connect" para mais informações.' + '\n')
    
    def do_list(self, _):
        return self._model_response('list', None)
    
    def do_exit(self, _):
        return self._model_response('exit', None)
    
    ## Helpers Methods
    def help_create(self):
        print('\n' + 'create <name>' + '\n' + '<name> nome do canal que deseja criar.' + '\n')
        
    def help_connect(self):
        print('\n' + 'connect <name>' + '\n' + '<name> nome do canal que deseja adentrar.' + '\n')
        
    def help_list(self):
        print('\n' + 'list' + '\n' + 'Lista os canais disponiveis.' + '\n')
        
    def help_exit(self):
        print('\n' + 'list' + '\n' + 'Finaliza a conecção com o servidor.' + '\n')
    
    ## Utilies Methods
    ## Metodos por transformar o comando digitado em um dict
    def _model_response(self, command, param):
        return dict({'command': str(command), 'param': str(param)})
