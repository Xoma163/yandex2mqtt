from enum import Enum


class Device(Enum):
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
