def process_char(char, data, pointer):
    if char == 'O':
        return ("", (pointer + 1) % 69_000)
    elif char == 'o':
        return ("", (pointer - 1) % 69_000)
    elif char == 'Ø':
        data[pointer] += 1
        return ("", pointer)
    elif char == 'ø':
        data[pointer] -= 1
        return ("", pointer)
    elif char == '0':
        pass
    elif char == '.':
        pass
    elif char == "®":
        input_string = str(input("input: "))
        data[pointer] = ord(input_string[0])
        return ("", pointer)
    elif char == "©":
        return (str(chr(data[pointer])), pointer)

    return ("", pointer)

def main():
    data = [0] * 69_000
    pointer = 0
    output = ""

    file_path = str(input("Enter Relative File Path: "))

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the first character
        char = file.read(1)

        # Continue reading characters until the end of the file
        while char:
            # Process the current character
            added_output, new_pointer = process_char(char, data, pointer)
            output += added_output
            pointer = new_pointer

            # Read the next character
            char = file.read(1)

    print(output)


if __name__ == "__main__":
    main()