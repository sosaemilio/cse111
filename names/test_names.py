from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Sosa; Emilio") == "Sosa"
    assert extract_family_name("Espinoza; Veronica") == "Espinoza"

def test_extract_given_name():
    assert extract_given_name("Sosa; Emilio") == "Emilio"
    assert extract_given_name("Brown; Sally B") ==  "Sally B"
    assert extract_given_name("Organa; Leia") != "Organa"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])