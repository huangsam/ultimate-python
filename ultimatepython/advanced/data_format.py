import json
from dataclasses import dataclass
from io import StringIO
from xml.etree import ElementTree as ETree

# Module-level constants
_JSON_FILE = StringIO("""
[
    {
        "author": "John",
        "title": "Summer",
        "body": "Summer time is hot"
    },
    {
        "author": "Jane",
        "title": "Winter",
        "body": "Winter time is cold"
    }
]
""")
_XML_FILE = StringIO("""
<notepad>
    <note>
        <author>John</author>
        <title>Summer</title>
        <body>Summer time is hot</body>
    </note>
    <note>
        <author>Jane</author>
        <title>Winter</title>
        <body>Winter time is cold</body>
    </note>
</notepad>
""")


@dataclass
class Note:
    """Note model."""
    author: str
    title: str
    body: str

    @classmethod
    def from_data(cls, data):
        """Create note from dictionary data."""
        return cls(**data)


def main():
    # Let's use `json.load` to parse note data from the JSON file
    json_content = json.load(_JSON_FILE)
    assert isinstance(json_content, list)
    assert all(isinstance(item, dict) for item in json_content)

    # It's simple to convert note data to class instances
    json_notes = [Note.from_data(data) for data in json_content]
    assert all(isinstance(note, Note) for note in json_notes)

    # Let's use `Etree.parse` to parse note data from the XML file
    tree = ETree.parse(_XML_FILE)
    assert isinstance(tree, ETree.ElementTree)

    # XML tree hierarchies start with a root element
    root_el = tree.getroot()
    assert ETree.iselement(root_el)
    assert root_el.tag == "notepad"

    # It's not simple to convert note data to class instances
    xml_notes = []
    for note_el in root_el:
        assert isinstance(note_el, ETree.Element)
        assert note_el.tag == "note"
        xml_notes.append(Note.from_data({
            attr_name: note_el.findtext(attr_name)
            for attr_name in ("author", "title", "body")
        }))

    # Note data is still the same between JSON and XML formats
    for json_note, xml_note in zip(json_notes, xml_notes):
        assert json_note == xml_note


if __name__ == "__main__":
    main()
