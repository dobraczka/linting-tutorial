from abc import abstractmethod
from typing import Set


class Animal:
    voice: str
    volumes: Set[int] = {0, 1, 2}

    @abstractmethod
    def regulate_voice(self, volume: int) -> str:
        pass

    def use_voice(self, volume: int):
        if volume not in self.__class__.volumes:
            raise ValueError(f"Volume can only be {Animal.volumes}")
        print(self.regulate_voice(volume))


class Cat(Animal):
    voice: str = "Meow Meow"

    def regulate_voice(self, volume: int) -> str:
        if volume == 0:
            return "purrrrr"
        if volume == 1:
            return self.voice.lower()
        if volume == 2:
            return self.voice
        return "HISSSS"


class Dog(Animal):
    voice: str = "Bark Woof"
    volumes: Set[int] = {0, 1, 2, 4}

    def regulate_voice(self, volume: int) -> str:
        if volume == 0:
            raise ValueError("Dogs cannot bark this quiet!")
        if volume == 1:
            return self.voice.lower()
        if volume == 2:
            return self.voice
        if volume == 3:
            return self.voice.upper()
        return "GRRR!!! WOOF!!"


if __name__ == "__main__":
    print("Let's hear some animal sounds!")
    my_dog = Dog()
    my_dog.use_voice(2)

    my_cat = Cat()
    for range in my_cat.volumes:
        my_cat.use_voice(range)
        my_cat.use_voice(range)
        my_cat.use_voice("loud")
