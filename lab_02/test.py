import os
import csv
import pytest
from lab_01 import LoadBackFile, SaveAllData, main

@pytest.fixture
def sample_data():
    # You can modify this data for your specific test case
    return [
        {"name": "John", "phone": "123-456-7890"},
        {"name": "Alice", "phone": "987-654-3210"}
    ]

def test_load_back_file(tmpdir, sample_data):
    # Create a temporary directory for testing
    temp_file = os.path.join(tmpdir, "test_lab2.csv")

    # Save sample data to the temporary file
    with open(temp_file, "w", newline="") as csvfile:
        fieldnames = sample_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_data)

    # Load the data using LoadBackFile
    loaded_data, params = LoadBackFile(temp_file)

    # Perform assertions
    assert loaded_data == sample_data
    assert params == tuple(sample_data[0].keys())

def test_main(tmpdir, capsys, monkeypatch):
    # Create a temporary directory for testing
    temp_file = os.path.join(tmpdir, "test_lab2.csv")

    # Mock user input for testing main function
    monkeypatch.setattr('builtins.input', lambda _: 'X')  # Simulate 'X' to exit

    # Call main function with sample data
    main([], ("name", "phone"))

    # Capture printed output
    captured = capsys.readouterr()

    # Perform assertions on the output
    assert "Exit()" in captured.out

def test_save_all_data(tmpdir, sample_data):
    # Create a temporary directory for testing
    temp_file = os.path.join(tmpdir, "test_lab2_out.csv")

    # Call SaveAllData with sample data
    SaveAllData(sample_data, ("name", "phone"), temp_file)

    # Check if the file was created and has the correct content
    assert os.path.isfile(temp_file)

    with open(temp_file, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        saved_data = [row for row in reader]

    assert saved_data == sample_data
