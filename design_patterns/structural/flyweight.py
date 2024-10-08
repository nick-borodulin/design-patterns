from abc import ABC, abstractmethod


class Glyph(ABC):
    @abstractmethod
    def draw(self) -> str: ...


class Letter(Glyph):
    def __init__(self, character: str) -> None:
        self._character = character

    def draw(self) -> str:
        return f"drawing_character_{self._character}"


class InvalidLetter(Exception):
    pass


class LetterFactory:
    def __init__(self) -> None:
        self._letters: dict[str, Letter] = dict()

    def create_letter(self, character: str) -> Letter:
        if (
            character is None
            or type(character) is not str
            or not character.isascii()
            or len(character) != 1
        ):
            raise InvalidLetter()

        if character not in self._letters.keys():
            self._letters[character] = Letter(character)

        return self._letters[character]
