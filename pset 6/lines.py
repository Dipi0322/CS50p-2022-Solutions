import sys

def main():
    if command_line(sys.argv):
        print(check_lines(sys.argv[1]))

def command_line(argv):
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    elif len(sys.argv) == 2 and ".py" in sys.argv[1]:
        return True

def check_lines(file_path):
    try:
        with open(file_path,"r") as file:
            lines = file.readlines()

        count = 0
        for line in lines:
            line = line.strip()
            if line.startswith("#"):
                continue
            elif len(line) == 0:
                continue
            else:
                count += 1
        return count

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
