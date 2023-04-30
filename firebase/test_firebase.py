from firebase import retrieve_data, import_data, convert_json
import pytest



def test_retrieve_data():
    
    assert isinstance(retrieve_data("ana"), dict)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])