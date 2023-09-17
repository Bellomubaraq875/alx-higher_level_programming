#!/usr/bin/python3
"""this is for the base file"""
import json
import csv
import turtle


class Base:
    """The class tcalled Base with various attributes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is a class constructor"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """this returns the JSON string representaion opf the given input"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """this is a class method that writes the JSON string representation
        of a given list to a file"""
        afile = cls.__name__ + ".json"
        with open(afile, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                listDict = [b.to_dictionary() for b in list_objs]
                jsonfile.write(Base.to_json_string(listDict))

    @staticmethod
    def from_json_string(json_string):
        """This static method retutns the list
        represented in JSON format"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newClass = cls(1, 1)
            else:
                newClass = cls(1)
        newClass.update(**dictionary)
        return newClass

    @classmethod
    def load_from_file(cls):
        """This returns a list of instances"""
        afile = str(cls.__name__) + ".json"
        try:
            with open(afile, "r") as jsonfile:
                listDict = Base.from_json_string(jsonfile.read())
                return [cls.create(**b) for b in listDict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """20th task"""
        afile = cls.__name__ + ".csv"
        with open(afile, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for ob in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
                else:
                    writer.writerow([ob.id, ob.size, ob.x, ob.y])

    @classmethod
    def load_from_file_csv(cls):
        ob = []
        afile = cls.__name__ + ".csv"
        with open(afile, 'r', newline='') as csvf:
            reader = csv.reader(csvf)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                else:
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                objects = cls.create(**dic)
                ob.append(objects)
        return ob
