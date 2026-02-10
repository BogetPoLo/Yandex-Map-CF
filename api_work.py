import arcade.key
import requests

def up_down_map(delta1, delta2, key):
    print(delta2, delta2)
    if key == arcade.key.PAGEUP:
        if float(delta1) >= 50.0 and float(delta2) >= 50.0:
            print(1)
            return f"{delta1},{delta2}"
        else:
            print(2)
            delta1 = str(float(delta1) + 0.5)
            delta2 = str(float(delta2) + 0.5)
            return f"{delta1},{delta2}"

    if key == arcade.key.PAGEDOWN:
        if delta1 == "0.0005" and delta2 == "0.0005":
            print(3)
            return f"{delta1},{delta2}"
        else:
            print(4)
            delta1 = str(float(delta1) - 0.0005)
            delta2 = str(float(delta2) - 0.0005)
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
