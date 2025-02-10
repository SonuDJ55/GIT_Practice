class House(object):

    def __init__(self, property_type, property_siz):
        self.property_type = property_type
        self.property_size = property_siz
    
    def display_info(self):
        print("Property Type: " + self.property_type)
        print("Property Size: " + str(self.property_size))

