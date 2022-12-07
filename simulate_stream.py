import csv
import requests
import sys


def simulate_data_streaming(row_limit):
    n = 0
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = next(reader)
        for row in reader:
            raw_row = ";".join(row)
            requests.post(f'http://localhost:8000/new/{raw_row}')
            print(f"sent row {raw_row}")

            n += 1
            if n >= row_limit:
                break


if len(sys.argv) != 2:
    print("Pass number of rows to simulate as parameter")
    exit(-1)

simulate_data_streaming(int(sys.argv[1]))
