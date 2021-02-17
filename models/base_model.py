#!/usr/bin/python3
'''
BaseModel: defines all common attributes/methods for other classes
'''
from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''class BaseModel'''
    def __init__(self):
        '''construtor of class'''
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        '''overwrites the method __str__'''
        str_name = "[{:s}] ({}) {}"
        return str_name.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''update the updated_a attribute'''
        self.updated_at = datetime.today()

    def to_dict(self):
        '''return the dict of class'''
        dictionary = dict(self.__dict__)
        dictionary_update = {'created_at': self.created_at.isoformat(),
                             'updated_at': self.updated_at.isoformat()}
        dictionary.setdefault('__class__', self.__class__.__name__)
        dictionary.update(dictionary_update)
        return dictionary
