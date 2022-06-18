from django.db.models import TextChoices

from apps.yandex.consts import DeviceType, CapabilityType, RangeInstance, RangeUnit, ModeInstance, Mode, ToggleInstance, \
    ColorModel, Protocol

ColorModelChoices = [
    (ColorModel.RGB, "RGB"),
    (ColorModel.HSV, "HSV"),
]

ProtocolChoices = [
    (Protocol.HLS, "HLS"),
    (Protocol.PROGRESSIVE_MP4, "PROGRESSIVE_MP4"),
]


DeviceTypeChoices = [
    (DeviceType.LIGHT, 'LIGHT. Устройство, которое имеет управляемые светящиеся элементы'),
    (DeviceType.SOCKET, 'SOCKET. Розетка'),
    (DeviceType.SWITCH, 'SWITCH. Выключатель'),
    (DeviceType.THERMOSTAT, 'THERMOSTAT. Устройство с возможностью регулирования температуры'),
    (DeviceType.THERMOSTAT_AC, 'THERMOSTAT_AC. Устройство, управляющее микроклиматом в помещении, с возможностью регулирования температуры и режима работы'),
    (DeviceType.MEDIA_DEVICE, 'MEDIA_DEVICE. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео'),
    (DeviceType.TV, 'TV. Устройство для просмотра видеоконтента. На устройстве можно изменять громкость и переключать каналы'),
    (DeviceType.TV_BOX, 'TV_BOX. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно управлять громкостью воспроизведения и переключать каналы'),
    (DeviceType.RECEIVER, 'RECEIVER. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно изменять громкость, переключать каналы и источники аудио-/видеосигнала'),
    (DeviceType.COOKING, 'COOKING. Различная умная кухонная техника'),
    (DeviceType.COFFEE_MAKER, 'COFFEE_MAKER. Устройство, которое умеет делать кофе'),
    (DeviceType.KETTLE, 'KETTLE. Устройство, которое умеет кипятить воду и/или делать чай.'),
    (DeviceType.MULTICOOKER, 'MULTICOOKER. Устройство, которое выполняет функции мультиварки — приготовление пищи по заданным программам'),
    (DeviceType.OPENABLE, 'OPENABLE. Устройство, которое умеет открываться и/или закрываться'),
    (DeviceType.CURTAIN, 'CURTAIN. Устройство, которое выполняет функцию штор'),
    (DeviceType.HUMIDIFIER, 'HUMIDIFIER. Устройство, которое умеет изменять влажность в помещении'),
    (DeviceType.PURIFIER, 'PURIFIER. Устройство с функцией очистки воздуха'),
    (DeviceType.VACUUM_CLEANER, 'VACUUM_CLEANER. Устройство, которое выполняет функцию пылесоса'),
    (DeviceType.WASHING_MASHINE, 'WASHING_MASHINE. Устройство для стирки белья'),
    (DeviceType.DISHWASHER, 'DISHWASHER. Устройство для мытья посуды'),
    (DeviceType.IRON, 'IRON. Устройство, которое выполняет функции утюга'),
    (DeviceType.SENSOR, 'SENSOR. Устройство, которое передает данные со свойств'),
    (DeviceType.OTHER, 'OTHER. Остальные устройства, не подходящие под типы выше')
              ]

CapabilityTypeChoices = [
    (CapabilityType.ON_OFF, "ON_OFF. Удаленное включение и выключение устройства"),
    (CapabilityType.COLOR_SETTING, "COLOR_SETTING. Управление цветом для светящихся элементов в устройстве"),
    (CapabilityType.MODE, "MODE. Переключение режимов работы устройства, например, переключение между температурными режимами работы кондиционера"),
    (CapabilityType.RANGE, "RANGE. Управление параметрами устройства, которые имеют диапазон"),
    (CapabilityType.TOGGLE, "TOGGLE. Управление параметрами устройства, которые могут находиться только в одном из двух состояний"),
    (CapabilityType.VIDEO_STREAM, "VIDEO_STREAM. Получение видеопотока с камеры")
]

ModeChoices = [
    (Mode.AUTO, "AUTO. Автоматический режим"),
    (Mode.ECO, "ECO. Экономичный режим"),
    (Mode.TURBO, "TURBO. Турбо"),
    (Mode.COOL, "COOL. Охлаждение"),
    (Mode.DRY, "DRY. Режим осушения"),
    (Mode.FAN_ONLY, "FAN_ONLY. Вентиляция"),
    (Mode.HEAT, "HEAT. Обогрев"),
    (Mode.PREHEAT, "PREHEAT. Подогрев, [разогрев, предварительный нагрев, предварительный разогрев]"),
    (Mode.HIGH, "HIGH. Высокая скорость"),
    (Mode.LOW, "LOW. Низкая скорость"),
    (Mode.MEDIUM, "MEDIUM. Средняя скорость"),
    (Mode.MAX, "MAX. Максимальный, [максимум]"),
    (Mode.MIN, "MIN. Минимальный, [минимум]"),
    (Mode.FAST, "FAST. Быстрый"),
    (Mode.SLOW, "SLOW. Медленный"),
    (Mode.EXPRESS, "EXPRESS. Экспресс"),
    (Mode.NORMAL, "NORMAL. Нормальный, [обычный]"),
    (Mode.QUIET, "QUIET. Тихий, [ночной]"),
    (Mode.HORIZONTAL, "HORIZONTAL. Горизонтальный"),
    (Mode.STATIONARY, "STATIONARY. Неподвижный, [статичный, фиксированный]"),
    (Mode.VERTICAL, "VERTICAL. Вертикальный"),
    (Mode.ONE, "ONE. Первый"),
    (Mode.TWO, "TWO. Второй"),
    (Mode.THREE, "THREE Третий"),
    (Mode.FOUR, "FOUR. Четвёртый"),
    (Mode.FIVE, "FIVE. Пятый"),
    (Mode.SIX, "SIX. Шестой"),
    (Mode.SEVEN, "SEVEN. Седьмой"),
    (Mode.EIGHT, "EIGHT. Восьмой"),
    (Mode.NINE, "NINE. Девятый"),
    (Mode.TEN, "TEN. Десятый"),
    (Mode.AMERICANO, "AMERICANO. Американо"),
    (Mode.CAPPUCCINO, "CAPPUCCINO. Капучино"),
    (Mode.DOUBLE_ESPRESSO, "DOUBLE_ESPRESSO. Двойной эспрессо"),
    (Mode.ESPRESSO, "ESPRESSO. Эспрессо"),
    (Mode.LATTE, "LATTE. Латте"),
    (Mode.BLACK_TEA, "BLACK_TEA. Черный чай"),
    (Mode.FLOWER_TEA, "FLOWER_TEA. Цветочный чай"),
    (Mode.GREEN_TEA, "GREEN_TEA. Зеленый чай"),
    (Mode.HERBAL_TEA, "HERBAL_TEA. Травяной чай"),
    (Mode.OOLONG_TEA, "OOLONG_TEA. Чай улун"),
    (Mode.PUERH_TEA, "PUERH_TEA. Чай пуэр"),
    (Mode.RED_TEA, "RED_TEA. Красный чай"),
    (Mode.WHITE_TEA, "WHITE_TEA. Белый чай"),
    (Mode.GLASS, "GLASS. Мойка стекла"),
    (Mode.INTENSIVE, "INTENSIVE. Интенсивный"),
    (Mode.PRE_RINSE, "PRE_RINSE. Ополаскивание"),
    (Mode.ASPIC, "ASPIC. Холодец"),
    (Mode.BODY_FOOD, "BODY_FOOD. Детское питание"),
    (Mode.BAKING, "BAKING. Выпечка"),
    (Mode.BREAD, "BREAD. Хлеб"),
    (Mode.BOOLING, "BOOLING. Варка"),
    (Mode.CEREALS, "CEREALS. Крупы"),
    (Mode.CHEESECAKE, "CHEESECAKE. Чизкейк"),
    (Mode.DEEP_FRYER, "DEEP_FRYER. Фритюр"),
    (Mode.DESSERT, "DESSERT. Десерты"),
    (Mode.FOWL, "FOWL. Дичь"),
    (Mode.FRYING, "FRYING. Жарка"),
    (Mode.MACARONI, "MACARONI. Макароны"),
    (Mode.MILK_PORRIDGE, "MILK_PORRIDGE. Молочная каша"),
    (Mode.MULTICOOKER, "MULTICOOKER. Мультиповар"),
    (Mode.PASTA, "PASTA. Паста"),
    (Mode.PILAF, "PILAF. Плов"),
    (Mode.PIZZA, "PIZZA. Пицца"),
    (Mode.SAUCE, "SAUCE. Соус"),
    (Mode.SLOW_COOK, "SLOW_COOK. Томление"),
    (Mode.SOUP, "SOUP. Суп"),
    (Mode.STEAM, "STEAM. Пар"),
    (Mode.STEWING, "STEWING. Тушение"),
    (Mode.VACUUM, "VACUUM. Вакуум"),
    (Mode.YOGURT, "YOGURT. Йогурт"),
]

ModeInstanceChoices = [
    (ModeInstance.CLEANUP_MODE, "CLEANUP_MODE. Установка режима уборки"),
    (ModeInstance.DISHWASHING, "DISHWASHING. Установка режима мытья посуды"),
    (ModeInstance.FAN_SPEED, "FAN_SPEED. Установка режима работы скорости вентиляции, например, в кондиционере, вентиляторе или обогревателе"),
    (ModeInstance.HEAT, "HEAT. Установка режима нагрева"),
    (ModeInstance.INPUT_SOURCE, "INPUT_SOURCE. Установка источника сигнала"),
    (ModeInstance.PROGRAM, "PROGRAM. Установка какой-либо программы работы"),
    (ModeInstance.SWING, "SWING. Установка направления воздуха в климатической технике"),
    (ModeInstance.TEA_MODE, "TEA_MODE. Установка режима приготовления чая"),
    (ModeInstance.THERMOSTAT, "THERMOSTAT. Установка температурного режима работы климатической техники, например, в кондиционере"),
    (ModeInstance.WORK_SPEED, "WORK_SPEED. Установка скорости работы"),
]

RangeInstanceChoices = [
    (RangeInstance.BRIGHTNESS, "BRIGHTNESS. Изменение яркости световых элементов"),
    (RangeInstance.CHANNEL, "CHANNEL. Изменение канала, например телевизионного"),
    (RangeInstance.HUMIDITY, "HUMIDITY. Изменение влажности"),
    (RangeInstance.OPEN, "OPEN. Открывание чего-либо (открывание штор, окна)"),
    (RangeInstance.TEMPERATURE, "TEMPERATURE. Изменение температуры. Может обозначать температуру нагрева чайника, обогревателя или температуру кондиционера в каком-либо его режиме"),
    (RangeInstance.VOLUME, "VOLUME. Изменение громкости устройства")
]

RangeUnitChoices = [
    (RangeUnit.PERCENT, "Проценты"),
    (RangeUnit.CELSIUS, "Цельсий"),
    (RangeUnit.KELVIN, "Кельвины"),
]

ToggleInstanceChoices = [
    (ToggleInstance.BACKLIGHT, "BACKLIGHT. Подсветка"),
    (ToggleInstance.CONTROLS_LOCKED, "CONTROLS_LOCKED. Детский режим"),
    (ToggleInstance.IONIZATION, "IONIZATION. Ионизация"),
    (ToggleInstance.KEEP_WARM, "KEEP_WARM. Поддержание тепла"),
    (ToggleInstance.MUTE, "MUTE. Выключение звука"),
    (ToggleInstance.OSCILLATION, "OSCILLATION. Вращение"),
    (ToggleInstance.PAUSE, "PAUSE. Пауза"),
]
