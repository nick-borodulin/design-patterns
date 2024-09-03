from design_patterns.creation.builder import Client

def test_plaint_text():
    assert Client().generate_plain_text() == "Paragraph One Sentence One\n\nParagraph Two Sentence Two"


def test_html_text():
    assert Client().generate_html() == "<p>Paragraph One</p><br>Sentence One<br><p>Paragraph Two</p><br>Sentence Two<br>"