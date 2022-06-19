from enum import Enum


class Status(Enum):
    DONE = "DONE"
    ERROR = "ERROR"


class ColorModel(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/color_setting.html
    """
    RGB = "rgb"
    HSV = "hsv"


class Protocol(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/video_stream.html
    """
    HLS = "hls"
    PROGRESSIVE_MP4 = "progressive_mp4"


class DeviceType(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/device-types.html
    """
    LIGHT = "devices.types.light"  # Устройство, которое имеет управляемые светящиеся элементы
    SOCKET = "devices.types.socket"  # Розетка
    SWITCH = "devices.types.switch"  # Выключатель
    THERMOSTAT = "devices.types.thermostat"  # Устройство с возможностью регулирования температуры
    THERMOSTAT_AC = "devices.types.thermostat.ac"  # Устройство, управляющее микроклиматом в помещении, с возможностью регулирования температуры и режима работы
    MEDIA_DEVICE = "devices.types.media_device"  # Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео
    TV = "devices.types.media_device.tv"  # Устройство для просмотра видеоконтента. На устройстве можно изменять громкость и переключать каналы
    TV_BOX = "devices.types.media_device.tv_box"  # Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно управлять громкостью воспроизведения и переключать каналы
    RECEIVER = "devices.types.media_device.receiver"  # Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно изменять громкость, переключать каналы и источники аудио-/видеосигнала
    COOKING = "devices.types.cooking"  # Различная умная кухонная техника
    COFFEE_MAKER = "devices.types.cooking.coffee_maker"  # Устройство, которое умеет делать кофе
    KETTLE = "devices.types.cooking.kettle"  # Устройство, которое умеет кипятить воду и/или делать чай.
    MULTICOOKER = "devices.types.cooking.multicooker"  # Устройство, которое выполняет функции мультиварки — приготовление пищи по заданным программам
    OPENABLE = "devices.types.openable"  # Устройство, которое умеет открываться и/или закрываться
    CURTAIN = "devices.types.openable.curtain"  # Устройство, которое выполняет функцию штор
    HUMIDIFIER = "devices.types.humidifier"  # Устройство, которое умеет изменять влажность в помещении
    PURIFIER = "devices.types.purifier"  # Устройство с функцией очистки воздуха
    VACUUM_CLEANER = "devices.types.vacuum_cleaner"  # Устройство, которое выполняет функцию пылесоса
    WASHING_MASHINE = "devices.types.washing_machine"  # Устройство для стирки белья
    DISHWASHER = "devices.types.dishwasher"  # Устройство для мытья посуды
    IRON = "devices.types.iron"  # Устройство, которое выполняет функции утюга
    SENSOR = "devices.types.sensor"  # Устройство, которое передает данные со свойств
    OTHER = "devices.types.other"  # Остальные устройства, не подходящие под типы выше


class CapabilityType(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/video_stream.html
    """
    ON_OFF = "devices.capabilities.on_off"  # Удаленное включение и выключение устройства
    COLOR_SETTING = "devices.capabilities.color_setting"  # Управление цветом для светящихся элементов в устройстве
    MODE = "devices.capabilities.mode"  # Переключение режимов работы устройства, например, переключение между температурными режимами работы кондиционера
    RANGE = "devices.capabilities.range"  # Управление параметрами устройства, которые имеют диапазон
    TOGGLE = "devices.capabilities.toggle"  # Управление параметрами устройства, которые могут находиться только в одном из двух состояний
    VIDEO_STREAM = "devices.capabilities.video_stream"  # Получение видеопотока с камеры


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
    ONE = "one"  # Первый
    TWO = "two"  # Второй
    THREE = "three"  # Третий
    FOUR = "four"  # Четвёртый
    FIVE = "five"  # Пятый
    SIX = "six"  # Шестой
    SEVEN = "seven"  # Седьмой
    EIGHT = "eight"  # Восьмой
    NINE = "nine"  # Девятый
    TEN = "ten"  # Десятый
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


class ModeInstance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/mode-instance-modes.html
    """
    CLEANUP_MODE = "cleanup_mode"  # Установка режима уборки
    DISHWASHING = "dishwashing"  # Установка режима мытья посуды
    FAN_SPEED = "fan_speed"  # Установка режима работы скорости вентиляции, например, в кондиционере, вентиляторе или обогревателе
    HEAT = "heat"  # Установка режима нагрева
    INPUT_SOURCE = "input_source"  # Установка источника сигнала
    PROGRAM = "program"  # Установка какой-либо программы работы
    SWING = "swing"  # Установка направления воздуха в климатической технике
    TEA_MODE = "tea_mode"  # Установка режима приготовления чая
    THERMOSTAT = "thermostat"  # Установка температурного режима работы климатической техники, например, в кондиционере
    WORK_SPEED = "work_speed"  # Установка скорости работы


class RangeInstance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range-instance.html
    """
    BRIGHTNESS = "brightness"  # Изменение яркости световых элементов
    CHANNEL = "channel"  # Изменение канала, например телевизионного
    HUMIDITY = "humidity"  # Изменение влажности
    OPEN = "open"  # Открывание чего-либо (открывание штор, окна)
    TEMPERATURE = "temperature"  # Изменение температуры. Может обозначать температуру нагрева чайника, обогревателя или температуру кондиционера в каком-либо его режиме
    VOLUME = "volume"  # Изменение громкости устройства


class RangeUnit(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/range-instance.html
    """
    PERCENT = "unit.percent"  # Проценты
    CELSIUS = "unit.temperature.celsius"  # Цельсий
    KELVIN = "unit.temperature.kelvin"  # Кельвины


class ToggleInstance(Enum):
    """
    https://yandex.ru/dev/dialogs/smart-home/doc/concepts/toggle-instance.html
    """
    BACKLIGHT = "backlight"  # Подсветка
    CONTROLS_LOCKED = "controls_locked"  # Детский режим
    IONIZATION = "ionization"  # Ионизация
    KEEP_WARM = "keep_warm"  # Поддержание тепла
    MUTE = "mute"  # Выключение звука
    OSCILLATION = "oscillation"  # Вращение
    PAUSE = "pause"  # Пауза


ALLOWED_RANGE_UNITS_BY_RANGE_INSTANCE = {
    RangeInstance.BRIGHTNESS: [RangeUnit.PERCENT],
    RangeInstance.CHANNEL: [],
    RangeInstance.HUMIDITY: [RangeUnit.PERCENT],
    RangeInstance.OPEN: [RangeUnit.PERCENT],
    RangeInstance.TEMPERATURE: [RangeUnit.KELVIN, RangeUnit.CELSIUS],
    RangeInstance.VOLUME: [RangeUnit.PERCENT]
}
