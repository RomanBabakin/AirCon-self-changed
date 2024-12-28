from .properties import (AcWorkMode, AirFlow, Economy, FanSpeed, VertiSweep, FastColdHeat, Quiet, Power,
                         TemperatureUnit)


def clear_up_change_flags(control: int) -> int:
  return control & 2868817502


def get_fan_speed(control: int) -> FanSpeed:
  int_val = (control >> 1) & 15
  return FanSpeed(int_val)


def set_fan_speed(control: int, value: FanSpeed) -> None:
  int_val = value.value
  return (control & ~31) | ((int_val << 1) | 1)

def get_verti_sweep(control: int) -> VertiSweep:
  int_val = (control >> 1) & 15
  return VertiSweep(int_val)


def set_verti_sweep(control: int, value: VertiSweep) -> None:
  int_val = value.value
  return (control & ~31) | ((int_val << 1) | 1)


def get_power(control: int) -> Power:
  int_val = (control >> 6) & 1
  return Power(int_val)


def set_power(control: int, value: Power) -> None:
  int_val = value.value
  return (control & ~(3 << 5)) | (((int_val << 1) | 1) << 5)


def get_work_mode(control: int) -> AcWorkMode:
  int_val = (control >> 9) & 7
  return AcWorkMode(int_val)


def set_work_mode(control: int, value: AcWorkMode) -> None:
  int_val = value.value
  return (control & ~(15 << 8)) | (((int_val << 1) | 1) << 8)


def get_heat_cold(control: int) -> FastColdHeat:
  int_val = (control >> 13) & 1
  return FastColdHeat(int_val)


def set_heat_cold(control: int, value: FastColdHeat) -> None:
  int_val = value.value
  return (control & ~(3 << 12)) | (((int_val << 1) | 1) << 12)


def get_eco(control: int) -> Economy:
  int_val = (control >> 15) & 1
  return Economy(int_val)


def set_eco(control: int, value: Economy) -> None:
  int_val = value.value
  return (control & ~(3 << 14)) | (((int_val << 1) | 1) << 14)


def get_temp(control: int) -> int:
  return (control >> 17) & 63


def set_temp(control: int, value: int) -> None:
  return (control & ~(127 << 16)) | (((value << 1) | 1) << 16)


def get_fan_power(control: int) -> AirFlow:
  int_val = (control >> 25) & 1
  return AirFlow(int_val)


def set_fan_power(control: int, value: AirFlow) -> None:
  int_val = value.value
  return (control & ~(3 << 24)) | (((int_val << 1) | 1) << 24)


def get_fan_lr(control: int) -> AirFlow:
  int_val = (control >> 27) & 1
  return AirFlow(int_val)


def set_fan_lr(control: int, value: AirFlow) -> None:
  int_val = value.value
  return (control & ~(3 << 26)) | (((int_val << 1) | 1) << 26)


def get_fan_mute(control: int) -> Quiet:
  int_val = (control >> 29) & 1
  return Quiet(int_val)


def set_fan_mute(control: int, value: Quiet) -> None:
  int_val = value.value
  return (control & ~(3 << 28)) | (((int_val << 1) | 1) << 28)


def get_temptype(control: int) -> TemperatureUnit:
  int_val = (control >> 31) & 1
  return TemperatureUnit(int_val)


def set_temptype(control: int, value: TemperatureUnit) -> None:
  int_val = value.value
  return (control & ~(3 << 30)) | (((int_val << 1) | 1) << 30)
