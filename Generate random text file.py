import tempfile
import os
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_empty_random_text_file():
    temp_dir = tempfile.gettempdir()  # Get the system's temporary directory
    random_filename = "randomTextFile" + generate_random_string(10) + ".txt"  # Generate a random file name

    file_path = os.path.join(temp_dir, random_filename)

    with open(file_path, "w") as file:
        pass  # Create an empty file

    return file_path

if __name__ == "__main__":
    random_file_path = create_empty_random_text_file()
    print(f"Empty text file created with random name: {random_file_path}")
