#!/usr/bin/env python3

def secure_archive(file_name: str, action: str, text: str) -> tuple[bool, str]:
    result = True
    result_text = ""
    try:
        with open(file_name, action) as file:
            if action == 'r':
                result_text = file.read()
            elif action == 'w':
                file.write(text)
                result_text = 'Content succesfully written to file'
    except (FileNotFoundError, PermissionError) as e:
        result_text += str(e)
        result = False
        return (result, result_text)
    final = (result, result_text)
    return final


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    print(f"Using '{secure_archive.__name__}' "
          "to read from a nonexisting file:")
    print(secure_archive('test', 'r', 'Esto es una prueba'))
    print(f"Using '{secure_archive.__name__}' "
          "to read from a inaccessible file:")
    print(secure_archive('testo.txt', 'r', 'Esto es una prueba'))
    print(f"Using '{secure_archive.__name__}' to read from a regular file:")
    print(secure_archive('ancient_fragment.txt', 'r', 'Esto es una prueba'))
    print(f"Using '{secure_archive.__name__}' "
          "to write previous content to a new file:")
    print(secure_archive('new.txt', 'w', 'Esto es una prueba'))
