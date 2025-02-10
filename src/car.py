class Car(object):

    def __init__(self, make, model):
        """Constructor for the class."""
        self._make = make
        self._model = model
    
    def information(self):
        return f"This is a car {self.make}."

   

  