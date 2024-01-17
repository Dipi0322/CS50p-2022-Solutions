import re
import sys

def main():
    print(convert(input("Hours: ")))

def format_hour(hr,x):
    new_hr = None
    if hr == "12":
        if x == "AM":
            new_hr = "0"
        elif x == "PM":
            new_hr = "12"

    elif hr != "12":
        if x == "AM":
            new_hr = hr
        elif x == "PM":
            new_hr = int(hr) + 12
            new_hr = str(new_hr)

    if len(new_hr) < 2:
        new_hr = "0" + new_hr

    return new_hr


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)

    if match:
        x = s.index("A")
        y = s.index("P")
        time = re.search(r"^(.{1,5})\s(AM|PM)\sto\s(.{1,5})\s(AM|PM)$",s)

        if ":" in time.group(1) and ":" in time.group(3):
            modify_start = re.search(r"^([^:]+):?([^:]+)$",time.group(1))
            modify_end = re.search(r"^([^:]+):?([^:]+)$",time.group(3))

            start_hr, start_min = modify_start.group(1), modify_start.group(2)
            end_hr, end_min = modify_end.group(1), modify_end.group(2)

        else:
            start_hr, start_min = time.group(1), "00"
            end_hr, end_min = time.group(3), "00"

        starting_hour = format_hour(start_hr,time.group(2))
        ending_hour = format_hour(end_hr,time.group(4))

        return f"{starting_hour}:{start_min} to {ending_hour}:{end_min}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()