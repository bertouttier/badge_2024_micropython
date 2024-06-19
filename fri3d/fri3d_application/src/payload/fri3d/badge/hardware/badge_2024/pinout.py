from micropython import const
from fri3d.badge.hardware.pin import HardwarePinInput


class HardwarePinout:
    class PinoutExpansion:
        def __init__(self):
            self.uart = const(0)
            self.uart_tx = const(43)
            self.uart_rx = const(44)
            self.i2c = const(0)
            self.i2c_sda = const(9)
            self.i2c_scl = const(18)
            self.i2s = const(1)
            self.i2s_sck = const(2)
            self.i2s_ws = const(47)
            self.i2s_sd = const(16)

    class PinoutLEDS:
        def __init__(self):
            self.pin = const(12)

    class PinoutSPI:
        def __init__(self):
            self.pin_mosi = const(6)
            self.pin_miso = const(8)
            self.pin_sck = const(7)

    class PinoutDisplay:
        def __init__(self):
            self.pin_rst = const(48)
            self.pin_dc = const(4)
            self.pin_cs = const(5)

    class PinoutSAO:
        def __init__(self, leds):
            self.gpio1 = leds.pin
            self.gpio2 = const(13)

    class PinoutOnboardButtons:
        def __init__(self):
            self.pin_a = HardwarePinInput(const(39), True)
            self.pin_b = HardwarePinInput(const(40), True)
            self.pin_x = HardwarePinInput(const(38), True)
            self.pin_y = HardwarePinInput(const(41), True)
            self.pin_menu = HardwarePinInput(const(45), True)
            self.pin_start = HardwarePinInput(const(0), False)

    class PinoutJoystick:
        def __init__(self):
            self.pin_joystick_x = const(1)
            self.pin_joystick_y = const(3)

    def __init__(self):
        self.pinout_expansion = self.PinoutExpansion()
        self.pinout_leds = self.PinoutLEDS()
        self.pinout_spi = self.PinoutSPI()
        self.pinout_display = self.PinoutDisplay()
        self.pinout_sao = self.PinoutSAO(self.pinout_leds)
        self.pinout_onboard_buttons = self.PinoutOnboardButtons()
        self.pinout_joystick = self.PinoutJoystick()


hardware_pinout = HardwarePinout()
