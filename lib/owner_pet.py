class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name:str, pet_type:str, owner: "Owner" = None):
        #PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
        if pet_type not in Pet.PET_TYPES:
            raise Exception("pet_type must be a type of PET_TYPES")
        #self._name
        #pass
        self._name = name
        self.pet_type = pet_type
        self._owner = None

        if owner is not None:
            self.owner = owner

        Pet.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("onwner must be of type Owner")
        
        self._owner = owner

        if self not in owner.pets():
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be a type of Pet")
        
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
        
    pass