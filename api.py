import requests, json, time

from settings import json_api_url, height, width, first_pixel_by_row

on_color = "FFFFFF"
off_color = "000000"


def xy_to_pixel(x,y):
    direction = 1 if y % 2 == 0 else -1
    return first_pixel_by_row[y] + x * direction

def display_pixel(x,y, color=on_color):
    msg = pixels_to_msg([(x,y)], color)
    send_post(msg)

def pixels_to_msg(pixels, color=on_color):
    seq = []
    for pixel in pixels:
        seq.append(xy_to_pixel(pixel[0], pixel[1]))
        seq.append(color)
    return {"seg":{"i":seq}}

def display_character(character, color=on_color):
    send_post({"seg":{"i":[0,149,off_color]}})
    for x, column in enumerate(character):
        pixels = []
        for y, pixel in enumerate(column):
            if pixel:
                pixels.append((x, y))
        msg = pixels_to_msg(pixels, on_color)
        time.sleep(0.01)
        send_post(msg)
        

def display_list_of_cols(cols, align = 'center'):
    match align:
        case 'center':
            x = (width - len(cols))//2
        case 'right':
            x = (width - len(cols))
        case _:
            x = 0
    

def send_post(payload_dict):
    json_payload = json.dumps(payload_dict)
    requests.post(json_api_url, json_payload)
