import os

# directory = "/"  # Replace with the actual directory path
directory = os.path.dirname(os.path.abspath(__file__))

print(directory)
for filename in os.listdir(directory):
    print(filename)
    if "$" in filename:
        new_filename = filename.replace("$", "")
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_filename}")
