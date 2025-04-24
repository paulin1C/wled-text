import requests, json, time

from settings import json_api_url, height, width, first_pixel_by_row

on_color = "FFFFFF"
off_color = "000000"


def xy_to_pixel(x,y):
    direction = 1 if y % 2 == 0 else -1
    return first_pixel_by_row[y] + x * direction

def display_pixel(x,y, color=on_color):
    pixel = xy_to_pixel(x,y)
    send_post({"seg":{"i":[pixel, color]}})

def display_list_of_cols(cols, align = 'center'):
    match align:
        case 'center':
            x = (width - len(cols))//2
        case 'right':
            x = (width - len(cols))
        case _:
            x = 0
    

def send_post(payload_dict):
    requests.post(json_api_url, json.dumps(payload_dict))

