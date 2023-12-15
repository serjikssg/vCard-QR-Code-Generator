import pytest
from project import qr_file, qr_gen, vcart



test_data = f"""BEGIN:VCARD
VERSION:4.0
FN:
EMAIL;TYPE=EMAIL:
TEL;TYPE=MOBILE:
ADR;TYPE=HOME:;;;;;;
ORG:
TITLE:
URL:
NOTE:
BDAY:
END:VCARD"""

def test_vcart():
    assert vcart() == test_data

# def test_qr_file():
#     assert qr_file(data, "file") == None

# def test_qr_file():
#     with pytest.raises(TypeError):
#         qr_file(1, "file")


def test_qr():
    with pytest.raises(OSError):
        qr_file(test_data, "?")


def test_qr_gen():
    assert qr_gen(test_data) == None


def test_qr_gen_err():
    with pytest.raises(TypeError):
        qr_gen()
