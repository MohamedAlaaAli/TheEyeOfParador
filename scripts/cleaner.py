import os

def remove_files_with_index(directory):
    """
    Remove files where the character at index -5 is '1' in the given directory.
    """
    files = os.listdir(directory)
    
    for file in files:
        if len(file) >= 5 and file[-5] == '1' and file[-6]=="_":
            os.remove(os.path.join(directory, file))
            print(f"File '{file}' removed.")

def main():
    directory = input("Enter the directory path: ")
    
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return
    
    remove_files_with_index(directory)

if __name__ == "__main__":
    main()
