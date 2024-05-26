#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name="Unknown", breed="Unknown"):
        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            print(f"Setting name to {name}.")
            self._name = name

    name = property(get_name, set_name)

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        if breed not in Dog.approved_breeds:
            print("Breed must be in list of approved breeds.")
        else:
            print(f"Setting breed to {breed}.")
            self._breed = breed

    breed = property(get_breed, set_breed)


