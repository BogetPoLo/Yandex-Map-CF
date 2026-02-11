import arcade
from arcade.gui import UIManager, UITextureButton, UIAnchorLayout, UIBoxLayout, UIInputText
import requests
import os
import logging
from api_work import *

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Яндекс карты"
MAP_FILE = "map.png"
ALL_KEY = [
    arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT,
    arcade.key.PAGEUP, arcade.key.PAGEDOWN
]

class OutputMap(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)
        logging.info("Окно инициализировано: %dx%d, '%s'", width, height, title)

        self.press_keys = []
        self.up_im = False
        self.response = None

        self.api_serv = "https://static-maps.yandex.ru/v1"
        self.apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
        self.ll = '37.621351,55.753349'
        self.spn = "0.2,0.2"
        self.theme = "light"

        self.manager = UIManager()

    def setup(self):
        try:
            logging.info("Начало загрузки карты...")
            self.update_image()
            self.manager.enable()
            self.setup_widgets()
            logging.info("Инициализация интерфейса завершена.")
        except Exception as e:
            logging.error("Ошибка при setup(): %s", e)

    def setup_widgets(self):
        try:
            # Кнопка смены темы
            texture_normal = arcade.load_texture(":resources:/gui_basic_assets/button/red_normal.png")
            texture_hovered = arcade.load_texture(":resources:/gui_basic_assets/button/red_hover.png")
            texture_pressed = arcade.load_texture(":resources:/gui_basic_assets/button/red_press.png")
            theme_button = UITextureButton(
                texture=texture_normal,
                texture_hovered=texture_hovered,
                texture_pressed=texture_pressed,
                scale=1.0,
                text="тема",
                x=10,
                y=10
            )
            theme_button.on_click = self.color_map_button
            self.manager.add(theme_button)
            logging.info("Кнопка 'тема' добавлена.")

            # Поле ввода
            input_line = UIInputText(x=0, y=540, width=400, height=50, text="")
            self.manager.add(input_line)
            logging.info("Поле ввода добавлено.")

            # Кнопка поиска
            search_button = UITextureButton(
                texture=texture_normal,
                texture_hovered=texture_hovered,
                texture_pressed=texture_pressed,
                scale=1.0,
                text="Искать",
                x=410,
                y=540,
                width=1000,
                height=1000
            )
            self.manager.add(search_button)
            logging.info("Кнопка 'Искать' добавлена.")

        except Exception as e:
            logging.error("Ошибка при создании виджетов: %s", e)

    def on_draw(self):
        try:
            self.clear()
            self.manager.draw()
            if hasattr(self, 'background'):
                arcade.draw_texture_rect(
                    self.background,
                    arcade.LBWH(
                        (self.width - self.background.width) // 2,
                        (self.height - self.background.height) // 2,
                        self.background.width,
                        self.background.height
                    ),
                )
            else:
                logging.warning("Карта ещё не загружена, пропуск отрисовки.")
        except Exception as e:
            logging.error("Ошибка при отрисовке: %s", e)

    def on_update(self, delta_time):
        try:
            for key in ALL_KEY:
                if key in self.press_keys:
                    if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT]:
                        longitude, latitude = self.ll.split(",")
                        delta1, delta2 = self.spn.split(",")
                        self.ll = movement(longitude, latitude, delta1, delta2, key)
                        logging.info("Перемещение: новая координата (%s, %s)", *self.ll.split(","))
                        self.up_im = True
                    elif key == arcade.key.PAGEUP or key == arcade.key.PAGEDOWN:
                        delta1, delta2 = self.spn.split(",")
                        self.spn = up_down_map(delta1, delta2, key)
                        logging.info("Масштаб изменён: spn=%s", self.spn)
                        self.up_im = True

            if self.up_im:
                self.update_image()
        except Exception as e:
            logging.error("Ошибка при обновлении: %s", e)

    def color_map_button(self, event):
        try:
            self.theme = color_map(self.theme)
            logging.info("Смена темы: %s", self.theme)
            self.up_im = True
        except Exception as e:
            logging.error("Ошибка при смене темы: %s", e)

    def update_image(self):
        try:
            params = {
                "ll": self.ll,
                "spn": self.spn,
                "apikey": self.apikey,
                "size": "650,450",
                "theme": self.theme
            }
            logging.info("Запрос к API: %s с параметрами %s", self.api_serv, params)
            response = requests.get(self.api_serv, params, timeout=10)

            if response.status_code == 200:
                with open(MAP_FILE, "wb") as f:
                    f.write(response.content)
                self.background = arcade.load_texture(MAP_FILE)
                logging.info("Карта успешно загружена и сохранена.")
            else:
                logging.error("Ошибка API: %d — %s", response.status_code, response.text)

            self.up_im = False
        except requests.exceptions.Timeout:
            logging.error("Таймаут при запросе к API.")
        except requests.exceptions.RequestException as e:
            logging.error("Ошибка сети при запросе к API: %s", e)
        except Exception as e:
            logging.error("Неизвестная ошибка при обновлении изображения: %s", e)

    def on_key_press(self, key, modifiers):
        if key not in self.press_keys:
            self.press_keys.append(key)
            key_name = {
                arcade.key.UP: "UP", arcade.key.DOWN: "DOWN",
                arcade.key.LEFT: "LEFT", arcade.key.RIGHT: "RIGHT",
                arcade.key.PAGEUP: "PAGEUP", arcade.key.PAGEDOWN: "PAGEDOWN"
            }.get(key, f"KEY_{key}")
            logging.debug("Клавиша нажата: %s", key_name)

    def on_key_release(self, key, modifiers):
        if key in self.press_keys:
            self.press_keys.remove(key)
            key_name = {
                arcade.key.UP: "UP", arcade.key.DOWN: "DOWN",
                arcade.key.LEFT: "LEFT", arcade.key.RIGHT: "RIGHT",
                arcade.key.PAGEUP: "PAGEUP", arcade.key.PAGEDOWN: "PAGEDOWN"
            }.get(key, f"KEY_{key}")
            logging.debug("Клавиша отпущена: %s", key_name)


def setup_game(width=800, height=600, title="Space Race"):
    try:
        game = OutputMap(width, height, title)
        game.setup()
        logging.info("Карта настроена успешно.")
        return game
    except Exception as e:
        logging.critical("Ошибка при инициализации карты: %s", e)
        raise


def main():
    try:
        logging.info("Запуск приложения...")
        setup_game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()
        logging.info("Приложение завершено.")
    except Exception as e:
        logging.critical("Критическая ошибка в main(): %s", e)
    finally:
        if os.path.exists(MAP_FILE):
            try:
                os.remove(MAP_FILE)
                logging.info("Файл %s удалён.", MAP_FILE)
            except PermissionError:
                logging.error("Не удалось удалить %s: файл используется.", MAP_FILE)


if __name__ == "__main__":
    main()