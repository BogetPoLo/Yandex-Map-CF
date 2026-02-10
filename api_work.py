import arcade.key
import requests

def up_down_map(delta1, delta2, key):
    print(delta2, delta2)
    if key == arcade.key.PAGEUP:
        if float(delta1) >= 40.0 and float(delta2) >= 40.0:
            print(1)
        elif float(delta1) <= 0.0005:
            print(2)
            delta1 = str(float(delta1) + 0.0005)
            delta2 = str(float(delta2) + 0.0005)
        elif float(delta1) <= 0.005:
            print(3)
            delta1 = str(float(delta1) + 0.005)
            delta2 = str(float(delta2) + 0.005)
        elif float(delta1) <= 0.01:
            print(4)
            delta1 = str(float(delta1) + 0.02)
            delta2 = str(float(delta2) + 0.02)
        elif float(delta1) <= 0.05:
            print(5)
            delta1 = str(float(delta1) + 0.05)
            delta2 = str(float(delta2) + 0.05)
        elif float(delta1) <= 0.4:
            print(6)
            delta1 = str(float(delta1) + 0.5)
            delta2 = str(float(delta2) + 0.5)
        elif float(delta1) <= 1.4:
            print(7)
            delta1 = str(float(delta1) + 2)
            delta2 = str(float(delta2) + 2)
        elif float(delta1) <= 3.4:
            print(8)
            delta1 = str(float(delta1) + 5)
            delta2 = str(float(delta2) + 5)
        elif float(delta1) <= 8.4:
            print(9)
            delta1 = str(float(delta1) + 15)
            delta2 = str(float(delta2) + 15)
        elif float(delta1) <= 23.4:
            print(10)
            delta1 = str(float(delta1) + 20)
            delta2 = str(float(delta2) + 20)
        return f"{delta1},{delta2}"

    if key == arcade.key.PAGEDOWN:
        if float(delta1) <= 0.0005 and float(delta2) <= 0.0005:
            delta1 = 0.0005
            delta2 = 0.0005
            print(1)
        elif 0.0005 >= float(delta1) <= 0.005:
            print(2)
            delta1 = str(float(delta1) - 0.0005)
            delta2 = str(float(delta2) - 0.0005)
        elif 0.005 >= float(delta1) <= 0.01:
            print(3)
            delta1 = str(float(delta1) - 0.005)
            delta2 = str(float(delta2) - 0.005)
        elif 0.01 >= float(delta1) <= 0.05:
            print(4)
            delta1 = str(float(delta1) - 0.02)
            delta2 = str(float(delta2) - 0.02)
        elif 0.05 >= float(delta1) <= 0.4:
            print(5)
            delta1 = str(float(delta1) - 0.05)
            delta2 = str(float(delta2) - 0.05)
        elif 0.4 >= float(delta1) <= 1.4:
            print(6)
            delta1 = str(float(delta1) - 0.5)
            delta2 = str(float(delta2) - 0.5)
        elif 1.4 >= float(delta1) <= 3.4:
            print(7)
            delta1 = str(float(delta1) - 2)
            delta2 = str(float(delta2) - 2)
        elif 3.4 >= float(delta1) <= 8.4:
            print(8)
            delta1 = str(float(delta1) - 5)
            delta2 = str(float(delta2) - 5)
        elif 8.4 >= float(delta1) <= 23.4:
            print(9)
            delta1 = str(float(delta1) - 15)
            delta2 = str(float(delta2) - 15)
        elif float(delta1) >= 23.4:
            print(10)
            delta1 = str(float(delta1) - 20)
            delta2 = str(float(delta2) - 20)
        return f"{delta1},{delta2}"


def movement(longitude, latitude, key):
    if key == arcade.key.UP:
        latitude = str(float(latitude) + 0.05)
    elif key == arcade.key.DOWN:
        latitude = str(float(latitude) - 0.05)
    elif key == arcade.key.LEFT:
        longitude = str(float(longitude) - 0.05)
    elif key == arcade.key.RIGHT:
        longitude = str(float(longitude) + 0.05)
    return f"{longitude},{latitude}"


def color_map(color):
    if color == "light":
        return "dark"
    else:
        return "light"