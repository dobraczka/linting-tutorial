from abc import abstractmethod

VOLUME_WHISPER = 0
VOLUME_QUIET = 1
VOLUME_NORMAL = 2
VOLUME_LOUD = 3
VOLUME_SHOUT = 4


class Animal:
    voice: str
    volumes: frozenset[int] = frozenset(
        [VOLUME_WHISPER, VOLUME_QUIET, VOLUME_NORMAL, VOLUME_LOUD]
    )

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
        if volume == VOLUME_WHISPER:
            return "purrrrr"
        if volume == VOLUME_QUIET:
            return self.voice.lower()
        if volume == VOLUME_NORMAL:
            return self.voice
        return "HISSSS"


class Dog(Animal):
    voice: str = "Bark Woof"
    volumes: frozenset[int] = frozenset(
        [VOLUME_QUIET, VOLUME_NORMAL, VOLUME_LOUD, VOLUME_SHOUT]
    )

    def regulate_voice(self, volume: int) -> str:
        if volume == VOLUME_QUIET:
            return self.voice.lower()
        if volume == VOLUME_NORMAL:
            return self.voice
        if volume == VOLUME_LOUD:
            return self.voice.upper()
        return "GRRR!!! WOOF!!"


if __name__ == "__main__":
    print("Let's hear some animal sounds!")
    my_dog = Dog()
    my_dog.use_voice(2)

    my_cat = Cat()
    for vol in my_cat.volumes:
        my_cat.use_voice(vol)
