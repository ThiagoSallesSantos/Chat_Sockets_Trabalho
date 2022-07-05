import cmd
import json

class Commands(cmd.Cmd):
    
    def do_list(self):
        return self._modelResponse('list', None)
    
    def do_exit(self):
        return self._modelResponse('exit', None)
        
    def help_list(self):
        print('\n' + 'list' + '\n' + 'Lista os comandos disponiveis.' + '\n')
        
    def help_exit(self):
        print('\n' + 'list' + '\n' + 'Finaliza o servidor.' + '\n')
    
    ## Utilies Methods
    def default(self, line):
        print('\n' + 'comando inválido "' + str(line) + '", use o comando "help" para ver a lista de comandos disponiveis.' + '\n')
        
    def _model_response(self, command, id):
        return json.dumps({'command': str(command), 'param': str(id)})
