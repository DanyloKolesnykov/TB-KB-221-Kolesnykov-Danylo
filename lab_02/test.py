import pytest
from lab_01 import LoadBackFile, GetNewParams, addNewElement, deleteElement, updateElement, SaveAllData

# Fixture для тестування
@pytest.fixture
def sample_data():
    data = [
        {'name': 'Alice', 'phone': '123456'},
        {'name': 'John', 'phone': '789012'},
        
    ]
    params = ('name', 'phone')
    return data, params


def test_LoadBackFile(sample_data):
    data, params = sample_data
    loaded_data, loaded_params = LoadBackFile("test_lab2.csv")
    assert loaded_data == data
    assert loaded_params == params


def test_GetNewParams():
    with pytest.raises(TypeError):
        GetNewParams(('name', 'phone'))


def test_addNewElement(sample_data):
    data, params = sample_data
    new_item = {'name': 'Bob', 'phone': '345678'}
    addNewElement(data, params, new_item)


    assert data[1] == new_item



def test_deleteElement(sample_data):
    data, _ = sample_data
    name_to_delete = 'John'
    deleteElement(data, name_to_delete)
    assert all(item['name'] != name_to_delete for item in data)


def test_updateElement(sample_data):
    data, params = sample_data
    updated_item = {'name': 'John', 'phone': '987654'}
    updateElement(data, params, updated_item)
    assert any(item == updated_item for item in data)


def test_SaveAllData(sample_data, tmp_path):
    data, params = sample_data
    file_path = tmp_path / "test_lab2_out.csv"
    SaveAllData(data, params, file_path)
    assert file_path.exists()

    loaded_data, loaded_params = LoadBackFile(file_path)
    assert loaded_data == data
    assert loaded_params == params



