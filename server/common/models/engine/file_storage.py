#!/usr/bin/env python
''' Contain the FileStorage module '''

from json import dump, load

from common.models import storage
from common.models.book import Book
from common.models.user import User
from common.models.account import Account

classes = { 'Account': Account, 'Book': Book, 'User': User }


class FileStorage:
    ''' Serialize instances to a JSON file & deserialize back to instances '''

    # string - path to the JSON file
    __file_path = 'storage.json'
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        ''' Return the dictionary __objects '''
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        ''' Set in __objects the obj with key <obj class name>.id '''
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        ''' Serialize __objects to the JSON file (path: __file_path) '''
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as f:
            dump(json_objects, f)

    def reload(self):
        ''' Deserialize the JSON file to __objects '''
        try:
            with open(self.__file_path, 'r') as f:
                jo = load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]['__class__']](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        ''' Delete obj from __objects if it’s inside '''
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        ''' Call reload() method for deserializing the JSON file to objects '''
        self.reload()

    def get(self, cls, id):
        '''
        Return the object based on the class name and its ID, or
        None if not found
        '''
        if cls not in classes.values():
            return None

        all_cls = storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        ''' Count the number of objects in storage '''
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(storage.all(clas).values())
        else:
            count = len(storage.all(cls).values())

        return count