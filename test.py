class BinaryTree:

    def __init__(self):

        self.__data=None;


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data