from django.db.models import TextChoices

from apps.yandex.consts import DeviceType, CapabilityType, RangeInstance, RangeUnit, ModeInstance, Mode, ToggleInstance, \
    ColorModel, Protocol

ColorModelChoices = [
    (ColorModel.RGB.value, "RGB"),
    (ColorModel.HSV.value, "HSV"),
]

ProtocolChoices = [
    (Protocol.HLS.value, "HLS"),
    (Protocol.PROGRESSIVE_MP4.value, "PROGRESSIVE_MP4"),
]


DeviceTypeChoices = [
    (DeviceType.LIGHT.value, 'LIGHT. Устройство, которое имеет управляемые светящиеся элементы'),
    (DeviceType.SOCKET.value, 'SOCKET. Розетка'),
    (DeviceType.SWITCH.value, 'SWITCH. Выключатель'),
    (DeviceType.THERMOSTAT.value, 'THERMOSTAT. Устройство с возможностью регулирования температуры'),
    (DeviceType.THERMOSTAT_AC.value, 'THERMOSTAT_AC. Устройство, управляющее микроклиматом в помещении, с возможностью регулирования температуры и режима работы'),
    (DeviceType.MEDIA_DEVICE.value, 'MEDIA_DEVICE. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео. Аудио, видео, мультимедиа техника. Устройства, которые умеют воспроизводить звук и видео'),
    (DeviceType.TV.value, 'TV. Устройство для просмотра видеоконтента. На устройстве можно изменять громкость и переключать каналы'),
    (DeviceType.TV_BOX.value, 'TV_BOX. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно управлять громкостью воспроизведения и переключать каналы'),
    (DeviceType.RECEIVER.value, 'RECEIVER. Устройство, подключаемое к телевизору или дисплею, для просмотра видеоконтента. На устройстве можно изменять громкость, переключать каналы и источники аудио-/видеосигнала'),
    (DeviceType.COOKING.value, 'COOKING. Различная умная кухонная техника'),
    (DeviceType.COFFEE_MAKER.value, 'COFFEE_MAKER. Устройство, которое умеет делать кофе'),
    (DeviceType.KETTLE.value, 'KETTLE. Устройство, которое умеет кипятить воду и/или делать чай.'),
    (DeviceType.MULTICOOKER.value, 'MULTICOOKER. Устройство, которое выполняет функции мультиварки — приготовление пищи по заданным программам'),
    (DeviceType.OPENABLE.value, 'OPENABLE. Устройство, которое умеет открываться и/или закрываться'),
    (DeviceType.CURTAIN.value, 'CURTAIN. Устройство, которое выполняет функцию штор'),
    (DeviceType.HUMIDIFIER.value, 'HUMIDIFIER. Устройство, которое умеет изменять влажность в помещении'),
    (DeviceType.PURIFIER.value, 'PURIFIER. Устройство с функцией очистки воздуха'),
    (DeviceType.VACUUM_CLEANER.value, 'VACUUM_CLEANER. Устройство, которое выполняет функцию пылесоса'),
    (DeviceType.WASHING_MASHINE.value, 'WASHING_MASHINE. Устройство для стирки белья'),
    (DeviceType.DISHWASHER.value, 'DISHWASHER. Устройство для мытья посуды'),
    (DeviceType.IRON.value, 'IRON. Устройство, которое выполняет функции утюга'),
    (DeviceType.SENSOR.value, 'SENSOR. Устройство, которое передает данные со свойств'),
    (DeviceType.OTHER.value, 'OTHER. Остальные устройства, не подходящие под типы выше')
              ]

CapabilityTypeChoices = [
    (CapabilityType.ON_OFF.value, "ON_OFF. Удаленное включение и выключение устройства"),
    (CapabilityType.COLOR_SETTING.value, "COLOR_SETTING. Управление цветом для светящихся элементов в устройстве"),
    (CapabilityType.MODE.value, "MODE. Переключение режимов работы устройства, например, переключение между температурными режимами работы кондиционера"),
    (CapabilityType.RANGE.value, "RANGE. Управление параметрами устройства, которые имеют диапазон"),
    (CapabilityType.TOGGLE.value, "TOGGLE. Управление параметрами устройства, которые могут находиться только в одном из двух состояний"),
    (CapabilityType.VIDEO_STREAM.value, "VIDEO_STREAM. Получение видеопотока с камеры")
]

ModeChoices = [
    (Mode.AUTO.value, "AUTO. Автоматический режим"),
    (Mode.ECO.value, "ECO. Экономичный режим"),
    (Mode.TURBO.value, "TURBO. Турбо"),
    (Mode.COOL.value, "COOL. Охлаждение"),
    (Mode.DRY.value, "DRY. Режим осушения"),
    (Mode.FAN_ONLY.value, "FAN_ONLY. Вентиляция"),
    (Mode.HEAT.value, "HEAT. Обогрев"),
    (Mode.PREHEAT.value, "PREHEAT. Подогрев, [разогрев, предварительный нагрев, предварительный разогрев]"),
    (Mode.HIGH.value, "HIGH. Высокая скорость"),
    (Mode.LOW.value, "LOW. Низкая скорость"),
    (Mode.MEDIUM.value, "MEDIUM. Средняя скорость"),
    (Mode.MAX.value, "MAX. Максимальный, [максимум]"),
    (Mode.MIN.value, "MIN. Минимальный, [минимум]"),
    (Mode.FAST.value, "FAST. Быстрый"),
    (Mode.SLOW.value, "SLOW. Медленный"),
    (Mode.EXPRESS.value, "EXPRESS. Экспресс"),
    (Mode.NORMAL.value, "NORMAL. Нормальный, [обычный]"),
    (Mode.QUIET.value, "QUIET. Тихий, [ночной]"),
    (Mode.HORIZONTAL.value, "HORIZONTAL. Горизонтальный"),
    (Mode.STATIONARY.value, "STATIONARY. Неподвижный, [статичный, фиксированный]"),
    (Mode.VERTICAL.value, "VERTICAL. Вертикальный"),
    (Mode.ONE.value, "ONE. Первый"),
    (Mode.TWO.value, "TWO. Второй"),
    (Mode.THREE.value, "THREE Третий"),
    (Mode.FOUR.value, "FOUR. Четвёртый"),
    (Mode.FIVE.value, "FIVE. Пятый"),
    (Mode.SIX.value, "SIX. Шестой"),
    (Mode.SEVEN.value, "SEVEN. Седьмой"),
    (Mode.EIGHT.value, "EIGHT. Восьмой"),
    (Mode.NINE.value, "NINE. Девятый"),
    (Mode.TEN.value, "TEN. Десятый"),
    (Mode.AMERICANO.value, "AMERICANO. Американо"),
    (Mode.CAPPUCCINO.value, "CAPPUCCINO. Капучино"),
    (Mode.DOUBLE_ESPRESSO.value, "DOUBLE_ESPRESSO. Двойной эспрессо"),
    (Mode.ESPRESSO.value, "ESPRESSO. Эспрессо"),
    (Mode.LATTE.value, "LATTE. Латте"),
    (Mode.BLACK_TEA.value, "BLACK_TEA. Черный чай"),
    (Mode.FLOWER_TEA.value, "FLOWER_TEA. Цветочный чай"),
    (Mode.GREEN_TEA.value, "GREEN_TEA. Зеленый чай"),
    (Mode.HERBAL_TEA.value, "HERBAL_TEA. Травяной чай"),
    (Mode.OOLONG_TEA.value, "OOLONG_TEA. Чай улун"),
    (Mode.PUERH_TEA.value, "PUERH_TEA. Чай пуэр"),
    (Mode.RED_TEA.value, "RED_TEA. Красный чай"),
    (Mode.WHITE_TEA.value, "WHITE_TEA. Белый чай"),
    (Mode.GLASS.value, "GLASS. Мойка стекла"),
    (Mode.INTENSIVE.value, "INTENSIVE. Интенсивный"),
    (Mode.PRE_RINSE.value, "PRE_RINSE. Ополаскивание"),
    (Mode.ASPIC.value, "ASPIC. Холодец"),
    (Mode.BODY_FOOD.value, "BODY_FOOD. Детское питание"),
    (Mode.BAKING.value, "BAKING. Выпечка"),
    (Mode.BREAD.value, "BREAD. Хлеб"),
    (Mode.BOOLING.value, "BOOLING. Варка"),
    (Mode.CEREALS.value, "CEREALS. Крупы"),
    (Mode.CHEESECAKE.value, "CHEESECAKE. Чизкейк"),
    (Mode.DEEP_FRYER.value, "DEEP_FRYER. Фритюр"),
    (Mode.DESSERT.value, "DESSERT. Десерты"),
    (Mode.FOWL.value, "FOWL. Дичь"),
    (Mode.FRYING.value, "FRYING. Жарка"),
    (Mode.MACARONI.value, "MACARONI. Макароны"),
    (Mode.MILK_PORRIDGE.value, "MILK_PORRIDGE. Молочная каша"),
    (Mode.MULTICOOKER.value, "MULTICOOKER. Мультиповар"),
    (Mode.PASTA.value, "PASTA. Паста"),
    (Mode.PILAF.value, "PILAF. Плов"),
    (Mode.PIZZA.value, "PIZZA. Пицца"),
    (Mode.SAUCE.value, "SAUCE. Соус"),
    (Mode.SLOW_COOK.value, "SLOW_COOK. Томление"),
    (Mode.SOUP.value, "SOUP. Суп"),
    (Mode.STEAM.value, "STEAM. Пар"),
    (Mode.STEWING.value, "STEWING. Тушение"),
    (Mode.VACUUM.value, "VACUUM. Вакуум"),
    (Mode.YOGURT.value, "YOGURT. Йогурт"),
]

ModeInstanceChoices = [
    (ModeInstance.CLEANUP_MODE.value, "CLEANUP_MODE. Установка режима уборки"),
    (ModeInstance.DISHWASHING.value, "DISHWASHING. Установка режима мытья посуды"),
    (ModeInstance.FAN_SPEED.value, "FAN_SPEED. Установка режима работы скорости вентиляции, например, в кондиционере, вентиляторе или обогревателе"),
    (ModeInstance.HEAT.value, "HEAT. Установка режима нагрева"),
    (ModeInstance.INPUT_SOURCE.value, "INPUT_SOURCE. Установка источника сигнала"),
    (ModeInstance.PROGRAM.value, "PROGRAM. Установка какой-либо программы работы"),
    (ModeInstance.SWING.value, "SWING. Установка направления воздуха в климатической технике"),
    (ModeInstance.TEA_MODE.value, "TEA_MODE. Установка режима приготовления чая"),
    (ModeInstance.THERMOSTAT.value, "THERMOSTAT. Установка температурного режима работы климатической техники, например, в кондиционере"),
    (ModeInstance.WORK_SPEED.value, "WORK_SPEED. Установка скорости работы"),
]

RangeInstanceChoices = [
    (RangeInstance.BRIGHTNESS.value, "BRIGHTNESS. Изменение яркости световых элементов"),
    (RangeInstance.CHANNEL.value, "CHANNEL. Изменение канала, например телевизионного"),
    (RangeInstance.HUMIDITY.value, "HUMIDITY. Изменение влажности"),
    (RangeInstance.OPEN.value, "OPEN. Открывание чего-либо (открывание штор, окна)"),
    (RangeInstance.TEMPERATURE.value, "TEMPERATURE. Изменение температуры. Может обозначать температуру нагрева чайника, обогревателя или температуру кондиционера в каком-либо его режиме"),
    (RangeInstance.VOLUME.value, "VOLUME. Изменение громкости устройства")
]

RangeUnitChoices = [
    (RangeUnit.PERCENT.value, "Проценты"),
    (RangeUnit.CELSIUS.value, "Цельсий"),
    (RangeUnit.KELVIN.value, "Кельвины"),
]

ToggleInstanceChoices = [
    (ToggleInstance.BACKLIGHT.value, "BACKLIGHT. Подсветка"),
    (ToggleInstance.CONTROLS_LOCKED.value, "CONTROLS_LOCKED. Детский режим"),
    (ToggleInstance.IONIZATION.value, "IONIZATION. Ионизация"),
    (ToggleInstance.KEEP_WARM.value, "KEEP_WARM. Поддержание тепла"),
    (ToggleInstance.MUTE.value, "MUTE. Выключение звука"),
    (ToggleInstance.OSCILLATION.value, "OSCILLATION. Вращение"),
    (ToggleInstance.PAUSE.value, "PAUSE. Пауза"),
]
