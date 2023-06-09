class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        self.__setattr__("pet_type", pet_type)  #you're accessing the pet_type method, this is how the value is validated
        self.all.append(self)

    # semi baffles my mind. still used to variable name = property(fgetter, fsetter)
    @property
    def pet_type(self):   #fgetter
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, ptype):
        if ptype in self.PET_TYPES:
            self._pet_type = ptype
        else:
            raise Exception


class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        else:
            pet.owner = self


    def get_sorted_pets(self):
        return sorted(Pet.all, key = lambda x: x.name )