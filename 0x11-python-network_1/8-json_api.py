#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except ValueError:
        print("Not a valid JSON")
