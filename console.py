#!/usr/bin/python3

'''
HBNBCommand: contain the entry point of the command
'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''use cmd to receive a command'''
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        '''it will be execute when press enter no arguments'''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
