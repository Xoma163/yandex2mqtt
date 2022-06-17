from enum import Enum


class Instance(Enum):
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
