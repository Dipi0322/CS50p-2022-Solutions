import sys
from PIL import Image,ImageOps

def main():
    if check_command_line(sys.argv):
        fix_image(sys.argv[1],sys.argv[2])

def check_command_line(argv):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3:
        supported_file = ".jpg.jpeg.png"
        format1 = ""
        format2 = ""

        for i in sys.argv[1][sys.argv[1].index(".")+1::]:
            format1 += i

        for j in sys.argv[2][sys.argv[2].index(".")+1::]:
            format2 += j

        format1 = format1.lower()
        format2 = format2.lower()

        if format1 != format2:
            sys.exit("Input and output have different extensions")
        elif format1 not in supported_file:
            sys.exit("Invalid Input")
        elif format2 not in supported_file:
            sys.exit("Invalid Output")

    return True


def fix_image(input_image, output_image):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(input_image) as base_image:
                base_image = ImageOps.fit(base_image, shirt.size)
                base_image.paste(shirt, shirt)
                base_image.save(output_image)


    except FileNotFoundError:
        sys.exit("Input does not exist")
    except OSError:
        sys.exit(f"Can not convert {input_image}")


if __name__ == "__main__":
    main()
