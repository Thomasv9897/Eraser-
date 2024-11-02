import os

def remove_file(filename):
    """Remove a file and handle potential errors."""
    try:
        os.remove(filename)
        print(f"{filename} has been removed successfully.")
    except FileNotFoundError:
        print(f"Error: {filename} does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to delete {filename}.")
    except Exception as e:
        print(f"An error occurred while removing {filename}: {e}")

if __name__ == "__main__":
    try:
        from c1 import get_run_count
        from c2 import add_and_subtract
        from c3 import self_destruct

        # Call functions
        get_run_count()
        add_and_subtract()
        self_destruct()

        # Remove the first module
        remove_file('c1.py')
    except ImportError as e:
        print(f"Import error: {e}. Attempting to remove c2.py and c3.py.")

        try:
            from c2 import add_and_subtract
            from c3 import self_destruct

            # Call functions
            add_and_subtract()
            self_destruct()

            # Remove the second module
            remove_file('c2.py')
        except ImportError as e:
            print(f"Import error: {e}. Attempting to remove c3.py.")

            try:
                from c3 import self_destruct

                # Call function
                self_destruct()

                # Remove the third module
                remove_file('c3.py')
            except ImportError:
                print("Error: The file 'c3.py' is not present in the current directory.")
                exit(1)
