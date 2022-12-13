import csv
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

simulator_url = 'http://simulator:' + os.environ['SIMULATOR_PORT']

def simulate_data_streaming(row_limit):
    n = 0
    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        headers = next(reader)
        for row in reader:
            lat_a, lat_b, lat_c, cpu_a, ram_a, cpu_b, ram_b, cpu_c, ram_c, x_c, y_c = row
            payload = [
                {
                    "id": 0,
                    "lat": lat_a,
                    "cpu": cpu_a,
                    "ram": ram_a,
                    "x": 0,
                    "y": 0,
                },
                {
                    "id": 1,
                    "lat": lat_b,
                    "cpu": cpu_b,
                    "ram": ram_b,
                    "x": 1,
                    "y": 2,
                },
                {
                    "id": 2,
                    "lat": lat_c,
                    "cpu": cpu_c,
                    "ram": ram_c,
                    "x": x_c,
                    "y": y_c,
                },
            ]
            requests.post(simulator_url + '/new', json=payload)
            print(f"sent row {payload}")

            n += 1
            if n >= row_limit:
                break


if len(sys.argv) != 2:
    print("Pass number of rows to simulate as parameter")
    exit(-1)

simulate_data_streaming(int(sys.argv[1]))
