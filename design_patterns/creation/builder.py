from abc import abstractmethod, ABC


class TextBuilder(ABC):
    @abstractmethod
    def add_paragraph(self, paragraph: str) -> None: ...

    @abstractmethod
    def add_sentence(self, sentence: str) -> None: ...

    @property
    @abstractmethod
    def text(self) -> str: ...


class PlainTextBuilder(TextBuilder):
    def __init__(self) -> None:
        self._text = str()

    def add_paragraph(self, paragraph: str) -> None:
        if len(self._text) > 0:
            self._text += "\n\n"
        self._text += paragraph

    def add_sentence(self, sentence: str) -> None:
        if len(self._text) > 0:
            self._text += " "
        self._text += sentence

    @property
    def text(self) -> str:
        return self._text


class HTMLTextBuilder(TextBuilder):
    def __init__(self) -> None:
        self._html = str()

    def add_paragraph(self, paragraph: str) -> None:
        self._html += f"<p>{paragraph}</p>"

    def add_sentence(self, sentence: str) -> None:
        self._html += f"<br>{sentence}<br>"

    @property
    def text(self) -> str:
        return self._html


class TextGenerator:
    def generate_text(self, builder: TextBuilder) -> None:
        builder.add_paragraph("Paragraph One")
        builder.add_sentence("Sentence One")
        builder.add_paragraph("Paragraph Two")
        builder.add_sentence("Sentence Two")


class Client:
    def generate_plain_text(self) -> str:
        generator = TextGenerator()
        plain_text_builder = PlainTextBuilder()
        generator.generate_text(plain_text_builder)
        return plain_text_builder.text

    def generate_html(self) -> str:
        generator = TextGenerator()
        html_text_builder = HTMLTextBuilder()
        generator.generate_text(html_text_builder)
        return html_text_builder.text
