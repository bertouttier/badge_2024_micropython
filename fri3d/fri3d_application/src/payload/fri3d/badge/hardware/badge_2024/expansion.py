from .pinout import hardware_pinout


class HardwareExpansion:
    def __init__(self):
        self.pinout = hardware_pinout.pinout_expansion


hardware_expansion = HardwareExpansion()