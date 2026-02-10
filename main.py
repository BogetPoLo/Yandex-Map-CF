import arcade
import requests
import os

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 450
SCREEN_TITLE = "Янедкс карты"
MAP_FILE = "map.png"


class OutputMap(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)

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

    def setup(self):
        api_serv = "https://static-maps.yandex.ru/v1"
        apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        ll = '37.621351,55.753349'
        spn = "0.2,0.2"

        params = {
            "ll": ll,
            "spn": spn,
            "apikey": apikey,
            "size": "650,450"
        }
        response = requests.get(api_serv, params)
        print(response)
        if response:
            with open(MAP_FILE, "wb") as f:
                f.write(response.content)
            print(123)
            self.background = arcade.load_texture(MAP_FILE)

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