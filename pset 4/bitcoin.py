import requests
import sys
import json

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    elif len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            response_json = response.json()
            a = response_json["bpi"]
            b = a["USD"]
            c = b["rate_float"]
            print(f"${c*float(sys.argv[1]):,.4f}")

        except ValueError:
            sys.exit("Command-line argument is not a number")

except requests.RequestException:
    sys.exit("There was an exception while handling the request")
