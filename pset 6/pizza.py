import sys
from tabulate import tabulate

def main():
    if command_line(sys.argv):
        headers = check_file(sys.argv[1])[0]
        table = check_file(sys.argv[1])[1::]
        print(tabulate(table, headers, tablefmt="grid"))

def command_line(argv):
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    elif len(sys.argv) == 2 and ".csv" in sys.argv[1]:
        return True

def check_file(file_path):
    try:
        with open(file_path,"r") as file:
            lines = []
            for line in file:
                lines.append(line.strip().split(","))
        return lines

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()