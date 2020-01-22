from . import _init_rev

# autogenerated by 'robotpy-build create-imports rev rev._rev'
from ._rev import (
    CANAnalog,
    CANBusScanner,
    CANDigitalInput,
    CANEncoder,
    CANError,
    CANPIDController,
    CANScanIdentifier,
    CANSensor,
    CANSparkMax,
    CANSparkMaxLowLevel,
    ControlType,
    SparkMax,
)

__all__ = [
    "CANAnalog",
    "CANBusScanner",
    "CANDigitalInput",
    "CANEncoder",
    "CANError",
    "CANPIDController",
    "CANScanIdentifier",
    "CANSensor",
    "CANSparkMax",
    "CANSparkMaxLowLevel",
    "ControlType",
    "SparkMax",
]

# backwards compat
MotorType = CANSparkMaxLowLevel.MotorType
IdleMode = CANSparkMax.IdleMode
LimitSwitch = CANDigitalInput.LimitSwitch
LimitSwitchPolarity = CANDigitalInput.LimitSwitchPolarity

__all__ += [
    "MotorType",
    "IdleMode",
    "LimitSwitch",
    "LimitSwitchPolarity",
]
