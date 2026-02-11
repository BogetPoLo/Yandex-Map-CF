import arcade.key
import logging

# Словарь для преобразования клавиш в строки
KEY_NAMES = {
    arcade.key.UP: "UP",
    arcade.key.DOWN: "DOWN",
    arcade.key.LEFT: "LEFT",
    arcade.key.RIGHT: "RIGHT",
    arcade.key.PAGEUP: "PAGEUP",
    arcade.key.PAGEDOWN: "PAGEDOWN"
}

def get_key_name(key):
    return KEY_NAMES.get(key, f"KEY_{key}")

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def up_down_map(delta1, delta2, key):
    try:
        d1, d2 = float(delta1), float(delta2)
        key_name = get_key_name(key)
        logging.info("Масштаб: текущее значение spn=(%s, %s), клавиша: %s", d1, d2, key_name)

        if key == arcade.key.PAGEUP:  # Увеличение масштаба
            if d1 >= 40.0:
                logging.warning("Достигнут максимальный масштаб.")
                return f"{d1},{d2}"
            elif d1 <= 0.0005:
                d1 = d2 = d1 + 0.001
            elif d1 <= 0.005:
                d1 = d2 = d1 + 0.005
            elif d1 <= 0.01:
                d1 = d2 = d1 + 0.02
            elif d1 <= 0.05:
                d1 = d2 = d1 + 0.05
            elif d1 <= 0.4:
                d1 = d2 = d1 + 0.5
            elif d1 <= 1.4:
                d1 = d2 = d1 + 2.0
            elif d1 <= 3.4:
                d1 = d2 = d1 + 5.0
            elif d1 <= 8.4:
                d1 = d2 = d1 + 15.0
            elif d1 <= 23.4:
                d1 = d2 = d1 + 20.0
            else:
                d1 = d2 = d1 + 20.0
            logging.info("Увеличение масштаба: новый spn=(%s, %s)", d1, d2)
            return f"{d1},{d2}"

        elif key == arcade.key.PAGEDOWN:  # Уменьшение масштаба
            if d1 <= 0.0005:
                logging.warning("Достигнут минимальный масштаб.")
                return "0.0005,0.0005"
            elif d1 <= 0.0051:
                d1 = d2 = max(0.0005, d1 - 0.0005)
            elif d1 <= 0.021:
                d1 = d2 = d1 - 0.01
            elif d1 <= 0.051:
                d1 = d2 = d1 - 0.02
            elif d1 <= 0.41:
                d1 = d2 = d1 - 0.08
            elif d1 <= 1.41:
                d1 = d2 = d1 - 0.5
            elif d1 <= 3.41:
                d1 = d2 = d1 - 2.0
            elif d1 <= 8.41:
                d1 = d2 = d1 - 5.0
            elif d1 <= 23.41:
                d1 = d2 = d1 - 15.0
            else:
                d1 = d2 = d1 - 20.0
            d1 = max(0.0005, d1)
            d2 = max(0.0005, d2)
            logging.info("Уменьшение масштаба: новый spn=(%s, %s)", d1, d2)
            return f"{d1},{d2}"

        else:
            logging.warning("Неизвестная клавиша для масштабирования: %s", get_key_name(key))
            return f"{delta1},{delta2}"

    except ValueError as e:
        logging.error("Ошибка преобразования spn в число: delta1='%s', delta2='%s' — %s", delta1, delta2, e)
        return "0.2,0.2"
    except Exception as e:
        logging.error("Неизвестная ошибка в up_down_map: %s", e)
        return "0.2,0.2"


def movement(longitude, latitude, delta1, delta2, key):
    try:
        lon, lat = float(longitude), float(latitude)
        d1, d2 = float(delta1), float(delta2)
        logging.info("Перемещение: текущие координаты (%s, %s)", lon, lat)

        if d1 <= 0.0005:
            if key == arcade.key.UP:
                lat += 0.0002
            elif key == arcade.key.DOWN:
                lat -= 0.0002
            elif key == arcade.key.LEFT:
                lon -= 0.0002
            elif key == arcade.key.RIGHT:
                lon += 0.0002
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 0.01:
            if key == arcade.key.UP:
                lat += 0.001
            elif key == arcade.key.DOWN:
                lat -= 0.001
            elif key == arcade.key.LEFT:
                lon -= 0.001
            elif key == arcade.key.RIGHT:
                lon += 0.001
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 0.05:
            if key == arcade.key.UP:
                lat += 0.02
            elif key == arcade.key.DOWN:
                lat -= 0.02
            elif key == arcade.key.LEFT:
                lon -= 0.02
            elif key == arcade.key.RIGHT:
                lon += 0.02
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 0.4:
            if key == arcade.key.UP:
                lat += 0.05
            elif key == arcade.key.DOWN:
                lat -= 0.05
            elif key == arcade.key.LEFT:
                lon -= 0.05
            elif key == arcade.key.RIGHT:
                lon += 0.05
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 1.4:
            if key == arcade.key.UP:
                lat += 0.05
            elif key == arcade.key.DOWN:
                lat -= 0.05
            elif key == arcade.key.LEFT:
                lon -= 0.05
            elif key == arcade.key.RIGHT:
                lon += 0.05
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 3.4:
            if key == arcade.key.UP:
                lat += 0.05
            elif key == arcade.key.DOWN:
                lat -= 0.05
            elif key == arcade.key.LEFT:
                lon -= 0.05
            elif key == arcade.key.RIGHT:
                lon += 0.05
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 8.4:
            if key == arcade.key.UP:
                lat += 0.05
            elif key == arcade.key.DOWN:
                lat -= 0.05
            elif key == arcade.key.LEFT:
                lon -= 0.05
            elif key == arcade.key.RIGHT:
                lon += 0.05
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"
        elif d1 <= 23.4:
            if key == arcade.key.UP:
                lat += 0.05
            elif key == arcade.key.DOWN:
                lat -= 0.05
            elif key == arcade.key.LEFT:
                lon -= 0.05
            elif key == arcade.key.RIGHT:
                lon += 0.05
            else:
                logging.warning("Неизвестная клавиша перемещения: %s", get_key_name(key))
                return f"{longitude},{latitude}"


        lon = max(-180.0, min(180.0, lon))
        lat = max(-90.0, min(90.0, lat))

        logging.info("Новые координаты: (%s, %s)", lon, lat)
        return f"{lon},{lat}"

    except ValueError as e:
        logging.error("Ошибка преобразования координат: longitude='%s', latitude='%s' — %s", longitude, latitude, e)
        return "37.621351,55.753349"
    except Exception as e:
        logging.error("Неизвестная ошибка в movement: %s", e)
        return "37.621351,55.753349"


def color_map(color):
    try:
        if not isinstance(color, str):
            logging.error("Ожидался тип str для 'color', получено: %s", type(color))
            return "light"

        if color.strip().lower() == "light":
            logging.info("Смена темы: light → dark")
            return "dark"
        else:
            logging.info("Смена темы: dark → light")
            return "light"
    except Exception as e:
        logging.error("Ошибка при смене темы: %s", e)
        return "light"