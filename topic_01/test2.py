# Test functions for string manipulation

# Function to test strip()
def test_strip():
    original_string = "   Hello, World!   "
    stripped_string = original_string.strip()
    print("Original String:", original_string)
    print("Stripped String:", stripped_string)

# Function to test capitalize()
def test_capitalize():
    original_string = "hello, world!"
    capitalized_string = original_string.capitalize()
    print("Original String:", original_string)
    print("Capitalized String:", capitalized_string)

# Function to test title()
def test_title():
    original_string = "this is a title case example"
    title_case_string = original_string.title()
    print("Original String:", original_string)
    print("Title Case String:", title_case_string)

# Function to test upper()
def test_upper():
    original_string = "convert me to uppercase"
    uppercase_string = original_string.upper()
    print("Original String:", original_string)
    print("Uppercase String:", uppercase_string)

# Function to test lower()
def test_lower():
    original_string = "CONVERT ME TO LOWERCASE"
    lowercase_string = original_string.lower()
    print("Original String:", original_string)
    print("Lowercase String:", lowercase_string)

# Run the test functions
test_strip()
print("\n")
test_capitalize()
print("\n")
test_title()
print("\n")
test_upper()
print("\n")
test_lower()
