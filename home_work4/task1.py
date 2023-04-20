def read_magic_number(path: str) -> bool:
    with open (path,encoding = 'utf - 8', mode = 'r') as f:
        line = f.readline()
        try:
            line = int(line)
            return line >= 1 and line < 3
        except ValueError as error:
            print(error)
