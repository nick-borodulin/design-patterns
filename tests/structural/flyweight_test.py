import pytest
from design_patterns.structural.flyweight import InvalidLetter, LetterFactory

def test_flyweight_factory() -> None:
    factory = LetterFactory()
    for character in 'abcdefghijklmnopqrstuvwxyz':
        letter_object = factory.create_letter(character)
        assert letter_object.draw() == f"drawing_character_{character}"

@pytest.mark.parametrize("character", ["abc", 1, None])
def test_invalid_character(character: str) -> None:
    factory = LetterFactory()
    with pytest.raises(InvalidLetter):
        _ = factory.create_letter(character)