import csv
import sys

def main():
    if command_line(sys.argv):
        create_new(sys.argv[1],sys.argv[2])

def command_line(argv):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit(f"Could not read {sys.argv[1]}")
    elif len(sys.argv) == 3 and ".csv" in sys.argv[1]:
        return True

def create_new(file_input,file_output):
    try:
        students = []
        with open(file_input,"r") as file:
            reader = csv.reader(file)
            for row in reader:
                name,house = row[0],row[1]
                if "," in name:
                    first, last = name.split(",")
                else:
                    continue

                student = {"first": last.strip(), "last": first.strip(), "house": house.strip()}
                students.append(student)

        field_names = ["first", "last", "house"]

        with open(file_output, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(students)

    except FileNotFoundError:
        sys.exit(f"Could not read {file_input}")

if __name__ == "__main__":
    main()