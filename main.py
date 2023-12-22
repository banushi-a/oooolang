def atomic_command(char, data, pointer):
    """
    Processes an atomic command

    Parameters:
    char     - A single character representing a command
    data     - An array representing the tapehead in the computation
    pointer  - Index on tape that computation is currenntly on

    Returns:
    The updated index of the pointer
    """
    if char == 'O':
        return (pointer + 1) % 69_000
    elif char == 'o':
        return (pointer - 1) % 69_000
    elif char == 'Ø':
        data[pointer] += 1
        return pointer
    elif char == 'ø':
        data[pointer] -= 1
        return pointer
    elif char == "®":
        input_string = str(input("input: "))
        data[pointer] = ord(input_string[0])
        return pointer
    elif char == "©":
        print(str(chr(data[pointer])), end="")
        return pointer

    return pointer

def get_loop_contents(string):
    """
    Get the contents of a loop given some string of commands

    Parameters:
    string - A string of commands starting with 0
    """

    # We use a stack to ensure we  get the corresponding .
    stack = ["0"]
    loop_contents = ""
    for char in string[1:]:
        if char == "0":
            stack.append("0")
        elif char == "." and stack[-1] == "0":
            stack.pop()
        elif char == ".":
            raise ValueError("A (.) is missing a corresponding (0)")
        
        loop_contents += char 

        if (len(stack)) == 0:
            return loop_contents[:-1]
        

def process_string(string, data, pointer, cond, breakWhenDone):
    """
    Process some string of commands

    Parameters:
    string        - String of commands
    data          - An array representing the tapehead in the computation
    pointer       - Index on tape that computation is currenntly on
    cond          - Conditional function that determines if the code is still running
    breakWhenDone - Should we break out of the loop after one iteration?
    """
    loopPointer = pointer
    while cond(loopPointer):
        for i, char in enumerate(string):
            if char == "0":
                inner_loop = get_loop_contents(string[i:])
                new_cond = lambda x: data[x] > 0
                process_string(inner_loop, data, pointer, new_cond, False)
            else:
                pointer = atomic_command(char, data, pointer)
        if breakWhenDone:
            break

def main():
    data = [0] * 69_000

    file_path = str(input("Enter Relative File Path: "))

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            process_string(file_content, data, 0, lambda _ : True, True)
            print()
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()