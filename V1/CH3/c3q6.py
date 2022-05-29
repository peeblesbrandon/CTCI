from collections import deque
from datetime import datetime
import unittest

class AnimalShelter:
    class Animal:
        def __init__(self, type, name):
            type = type.lower()
            if type not in {'dog', 'cat'}:
                raise Exception('animal type must be cat or dog')
            self.type = type
            self.name = name
            self.addedAt = datetime.now()

    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
    
    def enqueue(self, animalType, animalName):
        newAnimal = AnimalShelter.Animal(animalType, animalName)
        if newAnimal.type == 'dog':
            self.dogs.append(newAnimal)
        elif newAnimal.type == 'cat':
            self.cats.append(newAnimal)
    
    def dequeueCat(self):
        if not self.cats:
            raise Exception('no more cats')
        return self.cats.popleft()

    def dequeueDog(self):
        if not self.dogs:
            raise Exception('no more dogs :(')
        return self.dogs.popleft()

    def dequeueAny(self):
        if self.cats and self.dogs:
            if self.dogs[0].addedAt <= self.cats[0].addedAt:
                return self.dogs.pop()
            else:
                return self.cats.pop()
        elif self.dogs:
            return self.dogs.pop()
        elif self.cats:
            return self.cats.pop()
        else:
            raise Exception('no more animals :(')

class Test(unittest.TestCase):
    def test_dequeueDog(self):
        shelter = AnimalShelter()
        shelter.enqueue('dog', 'Ducky')
        shelter.enqueue('dog', 'Lucky')
        shelter.enqueue('cat', 'Scamper')
        self.assertEqual(shelter.dequeueDog().name, 'Ducky')
    
    def test_dequeueCat(self):
        shelter = AnimalShelter()
        shelter.enqueue('dog', 'Ducky')
        shelter.enqueue('dog', 'Lucky')
        shelter.enqueue('cat', 'Scamper')
        self.assertEqual(shelter.dequeueCat().name, 'Scamper')
    
    def test_dequeueAny(self):
        shelter = AnimalShelter()
        shelter.enqueue('cat', 'Scamper')
        shelter.enqueue('dog', 'Ducky')
        shelter.enqueue('dog', 'Lucky')
        self.assertEqual(shelter.dequeueAny().name, 'Scamper')

if __name__ == '__main__':
    unittest.main()
