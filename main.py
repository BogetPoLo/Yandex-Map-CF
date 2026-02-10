import arcade
import requests
import os
from api_work import *

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 450
SCREEN_TITLE = "Янедкс карты"
MAP_FILE = "map.png"
ALL_KEY = [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT, arcade.key.PAGEUP, arcade.key.PAGEDOWN]

class OutputMap(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)

        self.press_keys = []
        self.up_im = False
        self.response = None

        self.api_serv = "https://static-maps.yandex.ru/v1"
        self.apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        self.ll = '37.621351,55.753349'
        self.spn = "0.2,0.2"

    def setup(self):
        params = {
            "ll": self.ll,
            "spn": self.spn,
            "apikey": self.apikey,
            "size": "650,450"
        }
        self.response = requests.get(self.api_serv, params)
        self.update_image()

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(
                (self.width - self.background.width) // 2,
                (self.height - self.background.height) // 2,
                self.background.width,
                self.background.height
            ),
        )

    def on_update(self, delta_time):
        for key in ALL_KEY:
            if key in self.press_keys:
                if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT]:
                    longitude, latitude = self.ll.split(",")
                    self.ll = movement(longitude, latitude, key)
                    self.up_im = not(self.up_im)
                if key in [arcade.key.PAGEUP, arcade.key.PAGEDOWN]:
                    delta1, delta2 = self.spn.split(",")
                    self.spn = up_down_map(delta1, delta2, key)
                    self.up_im = not (self.up_im)

        if self.up_im:
            self.update_image()


    def update_image(self):
        params = {
            "ll": self.ll,
            "spn": self.spn,
            "apikey": self.apikey,
            "size": "650,450"
        }
        self.response = requests.get(self.api_serv, params)

        if self.response:
            with open(MAP_FILE, "wb") as f:
                f.write(self.response.content)
            self.background = arcade.load_texture(MAP_FILE)
        self.up_im = not(self.up_im)

    def on_key_press(self, key, modifiers):
        self.press_keys.append(key)

    def on_key_release(self, key, modifiers):
        self.press_keys.remove(key)


def setup_game(width=800, height=600, title="Space Race"):
    game = OutputMap(width, height, title)
    game.setup()
    return game


def main():
    setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
    os.remove(MAP_FILE)

if __name__ == "__main__":
    main()