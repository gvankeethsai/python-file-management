
from pathlib import Path


def show_files_folders():
    try:
        path = Path('')
        ls = list(path.rglob('*'))

        for index, item in enumerate(ls):
            print(f"{index + 1}: {item}")

        if not ls:
            print("No files or folders found")

    except Exception as e:
        print(f"Error displaying files and folders: {e}")


def create_file():
    try:
        file_name = input("Enter the name of the file: ").strip()

        if not file_name:
            print("File name cannot be empty")
            return

        path = Path(file_name)

        if path.exists():
            print("File already exists")
            return

        path.touch()
        print(f"File {file_name} created")

        choice1 = input(
            "Would you like to write into your file? (y/n): "
        ).strip().lower()

        if choice1 == "y":
            write_Into_file(file_name)
        else:
            print("Okay, you are done")

    except Exception as e:
        print(f"Invalid file name or operation failed: {e}")


def write_Into_file(file_name):
    try:
        path = Path(file_name)

        if not path.exists() or not path.is_file():
            print("File does not exist")
            return

        content = input("Enter the content: ")

        with open(file_name, 'a') as f:
            f.write(content + "\n")

        print(f"Content written into {file_name}")

    except Exception as e:
        print(f"Error writing to file: {e}")


def update_file():
    try:
        file_name = input("Enter the name of the file: ").strip()

        if not file_name:
            print("File name cannot be empty")
            return

        path = Path(file_name)

        print("Enter 1 to overwrite an existing file")
        print("Enter 2 to append to an existing file")
        print("Enter 3 to create a new file and write into it")
        print("Enter 4 to rename a file")

        enter = input("Enter your choice: ").strip()

        if enter not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            return

        if enter == "3":
            create_file()
            return

        if not path.exists() or not path.is_file():
            print("File does not exist")
            return

        if enter == "1":
            confirm = input(
                "This will erase existing content. Continue? (y/n): "
            ).strip().lower()

            if confirm != "y":
                print("Overwrite cancelled")
                return

            content = input("Enter the new content: ")

            with open(file_name, "w") as f:
                f.write(content + "\n")

            print("Content overwritten")

        elif enter == "2":
            content = input("Enter the content to append: ")

            with open(file_name, "a") as f:
                f.write(content + "\n")

            print("Content appended")

        elif enter == "4":
            new_name = input(
                "Enter the new name of the file: "
            ).strip()

            if not new_name:
                print("File name cannot be empty")
                return

            new_path = Path(new_name)

            if new_path.exists():
                print("A file with that name already exists")
                return

            path.rename(new_name)
            print("File renamed successfully")

    except Exception as e:
        print(f"Error updating file: {e}")


def read_file():
    try:
        file_name = input("Enter the name of the file: ").strip()
        path = Path(file_name)

        if path.exists() and path.is_file():
            with open(file_name, "r") as f:
                content = f.read()

            print(content)
        else:
            print("File does not exist")

    except Exception as e:
        print(f"Error reading file: {e}")


def delete_file():
    try:
        file_name = input("Enter the name of the file: ").strip()
        path = Path(file_name)

        if path.exists() and path.is_file():
            confirm = input(
                f"Are you sure you want to delete {file_name}? (y/n): "
            ).strip().lower()

            if confirm == "y":
                path.unlink()
                print(f"File {file_name} deleted")
            else:
                print("Deletion cancelled")

        else:
            print("File does not exist")

    except Exception as e:
        print(f"Error deleting file: {e}")


def main():
    while True:
        print("\n===== FILE MANAGEMENT SYSTEM =====")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update or rename a file")
        print("4. Delete a file")
        print("5. Show files and folders")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                create_file()

            elif choice == "2":
                read_file()

            elif choice == "3":
                update_file()

            elif choice == "4":
                delete_file()

            elif choice == "5":
                show_files_folders()

            elif choice == "6":
                print("Exiting the program")
                break

            else:
                print("Invalid choice. Enter a number from 1 to 6")

        except Exception as e:
            print(f"An error occurred: {e}")


main()
