from enum import Enum


class Mode(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/mode-instance.html
    """
    AUTO = "auto"  # Автоматический режим
    ECO = "eco"  # Экономичный режим
    TURBO = "turbo"  # Турбо
    #
    COOL = "cool"  # Охлаждение
    DRY = "dry"  # Режим осушения
    FAN_ONLY = "fan_only"  # Вентиляция
    HEAT = "heat"  # Обогрев
    PREHEAT = "preheat"  # Подогрев, [разогрев, предварительный нагрев, предварительный разогрев]
    #
    HIGH = "high"  # Высокая скорость
    LOW = "low"  # Низкая скорость
    MEDIUM = "medium"  # Средняя скорость
    #
    MAX = "max"  # Максимальный, [максимум]
    MIN = "min"  # Минимальный, [минимум]
    #
    FAST = "fast"  # Быстрый
    SLOW = "slow"  # Медленный
    #
    EXPRESS = "express"  # Экспресс
    NORMAL = "normal"  # Нормальный, [обычный]
    QUIET = "quiet"  # Тихий, [ночной]
    #
    HORIZONTAL = "horizontal"  # Горизонтальный
    STATIONARY = "stationary"  # Неподвижный, [статичный, фиксированный]
    VERTICAL = "vertical"  # Вертикальный
    #
    ONE = "one",  # Первый
    TWO = "two",  # Второй
    THREE = "three",  # Третий
    FOUR = "four",  # Четвёртый
    FIVE = "five",  # Пятый
    SIX = "six",  # Шестой
    SEVEN = "seven",  # Седьмой
    EIGHT = "eight",  # Восьмой
    NINE = "nine",  # Девятый
    TEN = "ten",  # Десятый
    #
    AMERICANO = "americano"  # Американо
    CAPPUCCINO = "cappuccino"  # Капучино
    DOUBLE_ESPRESSO = "double_espresso"  # Двойной эспрессо
    ESPRESSO = "espresso"  # Эспрессо
    LATTE = "latte"  # Латте
    #
    BLACK_TEA = "black_tea"  # Черный чай
    FLOWER_TEA = "flower_tea"  # Цветочный чай
    GREEN_TEA = "green_tea"  # Зеленый чай
    HERBAL_TEA = "herbal_tea"  # Травяной чай
    OOLONG_TEA = "oolong_tea"  # Чай улун
    PUERH_TEA = "puerh_tea"  # Чай пуэр
    RED_TEA = "red_tea"  # Красный чай
    WHITE_TEA = "white_tea"  # Белый чай
    #
    GLASS = "glass"  # Мойка стекла
    INTENSIVE = "intensive"  # Интенсивный
    PRE_RINSE = "pre_rinse"  # Ополаскивание
    #
    ASPIC = "aspic"  # Холодец
    BODY_FOOD = "baby_food"  # Детское питание
    BAKING = "baking"  # Выпечка
    BREAD = "bread"  # Хлеб
    BOOLING = "boiling"  # Варка
    CEREALS = "cereals"  # Крупы
    CHEESECAKE = "cheesecake"  # Чизкейк
    DEEP_FRYER = "deep_fryer"  # Фритюр
    DESSERT = "dessert"  # Десерты
    FOWL = "fowl"  # Дичь
    FRYING = "frying"  # Жарка
    MACARONI = "macaroni"  # Макароны
    MILK_PORRIDGE = "milk_porridge"  # Молочная каша
    MULTICOOKER = "multicooker"  # Мультиповар
    PASTA = "pasta"  # Паста
    PILAF = "pilaf"  # Плов
    PIZZA = "pizza"  # Пицца
    SAUCE = "sauce"  # Соус
    SLOW_COOK = "slow_cook"  # Томление
    SOUP = "soup"  # Суп
    STEAM = "steam"  # Пар
    STEWING = "stewing"  # Тушение
    VACUUM = "vacuum"  # Вакуум
    YOGURT = "yogurt"  # Йогурт
