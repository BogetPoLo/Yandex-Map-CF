import arcade.key
import requests

def up_down_map(delta1, delta2, key):
    if arcade.key.PAGEUP:
        if delta1 == "50.0" and delta2 == "50.0":
            return delta1, delta2
        else:
            delta1 = str(float(delta1) + 0.0005)
            delta2 = str(float(delta2) + 0.0005)
            return delta1, delta2

    if arcade.key.PAGEDOWN:
        if delta1 == "0.0005" and delta2 == "0.0005":
            return delta1, delta2
        else:
            delta1 = str(float(delta1) - 0.0005)
            delta2 = str(float(delta2) - 0.0005)
            return delta1, delta2




