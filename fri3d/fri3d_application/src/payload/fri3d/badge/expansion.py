from machine import UART, I2C, Pin
from fri3d.badge.hardware import hardware_capabilities


class Expansion:
    def _init_expansion(self, exp):
        self.uart = UART(
            exp.pinout.uart,
            rx=exp.pinout.uart_rx,
            tx=exp.pinout.uart_tx
        )
        self.i2c = I2C(
            exp.pinout.i2c,
            scl=Pin(exp.pinout.i2c_scl),
            sda=Pin(exp.pinout.i2c_sda)
        )
        # TODO: create a I2S audio-in/out object?

    def __init__(self):
        self.uart = None
        self.i2c = None
        # TODO: create a I2S audio-in/out object?

        if hardware_capabilities.expansion:
            from fri3d.badge.hardware import hardware_expansion
            self._init_expansion(hardware_expansion)


expansion = Expansion()
