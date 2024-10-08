# from generate_model_classes.ctrl_table_value import _CtrlTableValue

class _CtrlTableValue():

    def __init__(self, address, length_bytes, access):

        def validate_address(address):
            if not isinstance(address, int):
                raise ValueError(f'The given address {address} is not of type int')

        def valididate_len_bytes(length_bytes):
            if not isinstance(length_bytes, int):
                raise ValueError(f'The given length_bytes {length_bytes} is not of type int')
            valid_lengths_bytes = {1,2,4}
            if not(length_bytes in valid_lengths_bytes):
                raise ValueError(f'The given length_bytes {length_bytes} is not valid. Must be in {valid_lengths_bytes}')
            
        def validate_access(access):
            valid_access_strings= {'RW',"W","R"}
            if not (access in valid_access_strings):
                raise ValueError(f'The given access {access} is not valid. Must be in {valid_access_strings}')

        validate_address(address)
        valididate_len_bytes(length_bytes)
        validate_access(access)

        self.address = address 
        self.length_bytes = length_bytes
        self.access = access 

class _DynamixelModel():
	# This class is to ensure that all created new classes are the same class
	# and that type checking can happen correctly in the Motor Class in motor.py
	pass

class XL430W250(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	ModelInformation = _CtrlTableValue(2,4,'R')
	FirmwareVersion = _CtrlTableValue(6,1,'R')
	ID = _CtrlTableValue(7,1,'RW')
	BaudRate = _CtrlTableValue(8,1,'RW')
	ReturnDelayTime = _CtrlTableValue(9,1,'RW')
	DriveMode = _CtrlTableValue(10,1,'RW')
	OperatingMode = _CtrlTableValue(11,1,'RW')
	SecondaryShadowID = _CtrlTableValue(12,1,'RW')
	ProtocolType = _CtrlTableValue(13,1,'RW')
	HomingOffset = _CtrlTableValue(20,4,'RW')
	MovingThreshold = _CtrlTableValue(24,4,'RW')
	TemperatureLimit = _CtrlTableValue(31,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(32,2,'RW')
	MinVoltageLimit = _CtrlTableValue(34,2,'RW')
	PWMLimit = _CtrlTableValue(36,2,'RW')
	VelocityLimit = _CtrlTableValue(44,4,'RW')
	MaxPositionLimit = _CtrlTableValue(48,4,'RW')
	MinPositionLimit = _CtrlTableValue(52,4,'RW')
	StartupConfiguration = _CtrlTableValue(60,1,'RW')
	Shutdown = _CtrlTableValue(63,1,'RW')
	TorqueEnable = _CtrlTableValue(64,1,'RW')
	LED = _CtrlTableValue(65,1,'RW')
	StatusReturnLevel = _CtrlTableValue(68,1,'RW')
	RegisteredInstruction = _CtrlTableValue(69,1,'R')
	HardwareErrorStatus = _CtrlTableValue(70,1,'R')
	VelocityIGain = _CtrlTableValue(76,2,'RW')
	VelocityPGain = _CtrlTableValue(78,2,'RW')
	PositionDGain = _CtrlTableValue(80,2,'RW')
	PositionIGain = _CtrlTableValue(82,2,'RW')
	PositionPGain = _CtrlTableValue(84,2,'RW')
	Feedforward2ndGain = _CtrlTableValue(88,2,'RW')
	Feedforward1stGain = _CtrlTableValue(90,2,'RW')
	BusWatchdog = _CtrlTableValue(98,1,'RW')
	GoalPWM = _CtrlTableValue(100,2,'RW')
	GoalVelocity = _CtrlTableValue(104,4,'RW')
	ProfileAcceleration = _CtrlTableValue(108,4,'RW')
	ProfileVelocity = _CtrlTableValue(112,4,'RW')
	GoalPosition = _CtrlTableValue(116,4,'RW')
	RealtimeTick = _CtrlTableValue(120,2,'R')
	Moving = _CtrlTableValue(122,1,'R')
	MovingStatus = _CtrlTableValue(123,1,'R')
	PresentPWM = _CtrlTableValue(124,2,'R')
	PresentLoad = _CtrlTableValue(126,2,'R')
	PresentVelocity = _CtrlTableValue(128,4,'R')
	PresentPosition = _CtrlTableValue(132,4,'R')
	VelocityTrajectory = _CtrlTableValue(136,4,'R')
	PositionTrajectory = _CtrlTableValue(140,4,'R')
	PresentInputVoltage = _CtrlTableValue(144,2,'R')
	PresentTemperature = _CtrlTableValue(146,1,'R')
	BackupReady = _CtrlTableValue(147,1,'R')
	IndirectAddress1 = _CtrlTableValue(168,2,'RW')
	IndirectAddress2 = _CtrlTableValue(170,2,'RW')
	IndirectAddress3 = _CtrlTableValue(172,2,'RW')
	IndirectAddress26 = _CtrlTableValue(218,2,'RW')
	IndirectAddress27 = _CtrlTableValue(220,2,'RW')
	IndirectAddress28 = _CtrlTableValue(222,2,'RW')
	IndirectData1 = _CtrlTableValue(224,1,'RW')
	IndirectData2 = _CtrlTableValue(225,1,'RW')
	IndirectData3 = _CtrlTableValue(226,1,'RW')
	IndirectData26 = _CtrlTableValue(249,1,'RW')
	IndirectData27 = _CtrlTableValue(250,1,'RW')
	IndirectData28 = _CtrlTableValue(251,1,'RW')
	IndirectAddress29 = _CtrlTableValue(578,2,'RW')
	IndirectAddress30 = _CtrlTableValue(580,2,'RW')
	IndirectAddress31 = _CtrlTableValue(582,2,'RW')
	IndirectAddress54 = _CtrlTableValue(628,2,'RW')
	IndirectAddress55 = _CtrlTableValue(630,2,'RW')
	IndirectAddress56 = _CtrlTableValue(632,2,'RW')
	IndirectData29 = _CtrlTableValue(634,1,'RW')
	IndirectData30 = _CtrlTableValue(635,1,'RW')
	IndirectData31 = _CtrlTableValue(636,1,'RW')
	IndirectData54 = _CtrlTableValue(659,1,'RW')
	IndirectData55 = _CtrlTableValue(660,1,'RW')
	IndirectData56 = _CtrlTableValue(661,1,'RW')

class XL430(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	ModelInformation = _CtrlTableValue(2,4,'R')
	FirmwareVersion = _CtrlTableValue(6,1,'R')
	ID = _CtrlTableValue(7,1,'RW')
	BaudRate = _CtrlTableValue(8,1,'RW')
	ReturnDelayTime = _CtrlTableValue(9,1,'RW')
	DriveMode = _CtrlTableValue(10,1,'RW')
	OperatingMode = _CtrlTableValue(11,1,'RW')
	SecondaryShadowID = _CtrlTableValue(12,1,'RW')
	ProtocolType = _CtrlTableValue(13,1,'RW')
	HomingOffset = _CtrlTableValue(20,4,'RW')
	MovingThreshold = _CtrlTableValue(24,4,'RW')
	TemperatureLimit = _CtrlTableValue(31,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(32,2,'RW')
	MinVoltageLimit = _CtrlTableValue(34,2,'RW')
	PWMLimit = _CtrlTableValue(36,2,'RW')
	VelocityLimit = _CtrlTableValue(44,4,'RW')
	MaxPositionLimit = _CtrlTableValue(48,4,'RW')
	MinPositionLimit = _CtrlTableValue(52,4,'RW')
	StartupConfiguration = _CtrlTableValue(60,1,'RW')
	Shutdown = _CtrlTableValue(63,1,'RW')
	TorqueEnable = _CtrlTableValue(64,1,'RW')
	LED = _CtrlTableValue(65,1,'RW')
	StatusReturnLevel = _CtrlTableValue(68,1,'RW')
	RegisteredInstruction = _CtrlTableValue(69,1,'R')
	HardwareErrorStatus = _CtrlTableValue(70,1,'R')
	VelocityIGain = _CtrlTableValue(76,2,'RW')
	VelocityPGain = _CtrlTableValue(78,2,'RW')
	PositionDGain = _CtrlTableValue(80,2,'RW')
	PositionIGain = _CtrlTableValue(82,2,'RW')
	PositionPGain = _CtrlTableValue(84,2,'RW')
	Feedforward2ndGain = _CtrlTableValue(88,2,'RW')
	Feedforward1stGain = _CtrlTableValue(90,2,'RW')
	BusWatchdog = _CtrlTableValue(98,1,'RW')
	GoalPWM = _CtrlTableValue(100,2,'RW')
	GoalVelocity = _CtrlTableValue(104,4,'RW')
	ProfileAcceleration = _CtrlTableValue(108,4,'RW')
	ProfileVelocity = _CtrlTableValue(112,4,'RW')
	GoalPosition = _CtrlTableValue(116,4,'RW')
	RealtimeTick = _CtrlTableValue(120,2,'R')
	Moving = _CtrlTableValue(122,1,'R')
	MovingStatus = _CtrlTableValue(123,1,'R')
	PresentPWM = _CtrlTableValue(124,2,'R')
	PresentLoad = _CtrlTableValue(126,2,'R')
	PresentVelocity = _CtrlTableValue(128,4,'R')
	PresentPosition = _CtrlTableValue(132,4,'R')
	VelocityTrajectory = _CtrlTableValue(136,4,'R')
	PositionTrajectory = _CtrlTableValue(140,4,'R')
	PresentInputVoltage = _CtrlTableValue(144,2,'R')
	PresentTemperature = _CtrlTableValue(146,1,'R')

class MX28(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	ModelInformation = _CtrlTableValue(2,4,'R')
	FirmwareVersion = _CtrlTableValue(6,1,'R')
	ID = _CtrlTableValue(7,1,'RW')
	BaudRate = _CtrlTableValue(8,1,'RW')
	ReturnDelayTime = _CtrlTableValue(9,1,'RW')
	DriveMode = _CtrlTableValue(10,1,'RW')
	OperatingMode = _CtrlTableValue(11,1,'RW')
	SecondaryShadowID = _CtrlTableValue(12,1,'RW')
	ProtocolType = _CtrlTableValue(13,1,'RW')
	HomingOffset = _CtrlTableValue(20,4,'RW')
	MovingThreshold = _CtrlTableValue(24,4,'RW')
	TemperatureLimit = _CtrlTableValue(31,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(32,2,'RW')
	MinVoltageLimit = _CtrlTableValue(34,2,'RW')
	PWMLimit = _CtrlTableValue(36,2,'RW')
	AccelerationLimit = _CtrlTableValue(40,4,'RW')
	VelocityLimit = _CtrlTableValue(44,4,'RW')
	MaxPositionLimit = _CtrlTableValue(48,4,'RW')
	MinPositionLimit = _CtrlTableValue(52,4,'RW')
	Shutdown = _CtrlTableValue(63,1,'RW')
	TorqueEnable = _CtrlTableValue(64,1,'RW')
	LED = _CtrlTableValue(65,1,'RW')
	StatusReturnLevel = _CtrlTableValue(68,1,'RW')
	RegisteredInstruction = _CtrlTableValue(69,1,'R')
	HardwareErrorStatus = _CtrlTableValue(70,1,'R')
	VelocityIGain = _CtrlTableValue(76,2,'RW')
	VelocityPGain = _CtrlTableValue(78,2,'RW')
	PositionDGain = _CtrlTableValue(80,2,'RW')
	PositionIGain = _CtrlTableValue(82,2,'RW')
	PositionPGain = _CtrlTableValue(84,2,'RW')
	Feedforward2ndGain = _CtrlTableValue(88,2,'RW')
	Feedforward1stGain = _CtrlTableValue(90,2,'RW')
	BUSWatchdog = _CtrlTableValue(98,1,'RW')
	GoalPWM = _CtrlTableValue(100,2,'RW')
	GoalVelocity = _CtrlTableValue(104,4,'RW')
	ProfileAcceleration = _CtrlTableValue(108,4,'RW')
	ProfileVelocity = _CtrlTableValue(112,4,'RW')
	GoalPosition = _CtrlTableValue(116,4,'RW')
	RealtimeTick = _CtrlTableValue(120,2,'R')
	Moving = _CtrlTableValue(122,1,'R')
	MovingStatus = _CtrlTableValue(123,1,'R')
	PresentPWM = _CtrlTableValue(124,2,'R')
	PresentLoad = _CtrlTableValue(126,2,'R')
	PresentVelocity = _CtrlTableValue(128,4,'R')
	PresentPosition = _CtrlTableValue(132,4,'R')
	VelocityTrajectory = _CtrlTableValue(136,4,'R')
	PositionTrajectory = _CtrlTableValue(140,4,'R')
	PresentInputVoltage = _CtrlTableValue(144,2,'R')
	PresentTemperature = _CtrlTableValue(146,1,'R')

class MX106(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	ModelInformation = _CtrlTableValue(2,4,'R')
	FirmwareVersion = _CtrlTableValue(6,1,'R')
	ID = _CtrlTableValue(7,1,'RW')
	BaudRate = _CtrlTableValue(8,1,'RW')
	ReturnDelayTime = _CtrlTableValue(9,1,'RW')
	DriveMode = _CtrlTableValue(10,1,'RW')
	OperatingMode = _CtrlTableValue(11,1,'RW')
	SecondaryShadowID = _CtrlTableValue(12,1,'RW')
	ProtocolType = _CtrlTableValue(13,1,'RW')
	HomingOffset = _CtrlTableValue(20,4,'RW')
	MovingThreshold = _CtrlTableValue(24,4,'RW')
	TemperatureLimit = _CtrlTableValue(31,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(32,2,'RW')
	MinVoltageLimit = _CtrlTableValue(34,2,'RW')
	PWMLimit = _CtrlTableValue(36,2,'RW')
	CurrentLimit = _CtrlTableValue(38,2,'RW')
	AccelerationLimit = _CtrlTableValue(40,4,'RW')
	VelocityLimit = _CtrlTableValue(44,4,'RW')
	MaxPositionLimit = _CtrlTableValue(48,4,'RW')
	MinPositionLimit = _CtrlTableValue(52,4,'RW')
	Shutdown = _CtrlTableValue(63,1,'RW')
	TorqueEnable = _CtrlTableValue(64,1,'RW')
	LED = _CtrlTableValue(65,1,'RW')
	StatusReturnLevel = _CtrlTableValue(68,1,'RW')
	RegisteredInstruction = _CtrlTableValue(69,1,'R')
	HardwareErrorStatus = _CtrlTableValue(70,1,'R')
	VelocityIGain = _CtrlTableValue(76,2,'RW')
	VelocityPGain = _CtrlTableValue(78,2,'RW')
	PositionDGain = _CtrlTableValue(80,2,'RW')
	PositionIGain = _CtrlTableValue(82,2,'RW')
	PositionPGain = _CtrlTableValue(84,2,'RW')
	Feedforward2ndGain = _CtrlTableValue(88,2,'RW')
	Feedforward1stGain = _CtrlTableValue(90,2,'RW')
	BUSWatchdog = _CtrlTableValue(98,1,'RW')
	GoalPWM = _CtrlTableValue(100,2,'RW')
	GoalCurrent = _CtrlTableValue(102,2,'RW')
	GoalVelocity = _CtrlTableValue(104,4,'RW')
	ProfileAcceleration = _CtrlTableValue(108,4,'RW')
	ProfileVelocity = _CtrlTableValue(112,4,'RW')
	GoalPosition = _CtrlTableValue(116,4,'RW')
	RealtimeTick = _CtrlTableValue(120,2,'R')
	Moving = _CtrlTableValue(122,1,'R')
	MovingStatus = _CtrlTableValue(123,1,'R')
	PresentPWM = _CtrlTableValue(124,2,'R')
	PresentCurrent = _CtrlTableValue(126,2,'R')
	PresentVelocity = _CtrlTableValue(128,4,'R')
	PresentPosition = _CtrlTableValue(132,4,'R')
	VelocityTrajectory = _CtrlTableValue(136,4,'R')
	PositionTrajectory = _CtrlTableValue(140,4,'R')
	PresentInputVoltage = _CtrlTableValue(144,2,'R')
	PresentTemperature = _CtrlTableValue(146,1,'R')

class XL320(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	FirmwareVersion = _CtrlTableValue(2,1,'R')
	ID = _CtrlTableValue(3,1,'RW')
	BaudRate = _CtrlTableValue(4,1,'RW')
	ReturnDelayTime = _CtrlTableValue(5,1,'RW')
	CWAngleLimit = _CtrlTableValue(6,2,'RW')
	CCWAngleLimit = _CtrlTableValue(8,2,'RW')
	ControlMode = _CtrlTableValue(11,1,'RW')
	TemperatureLimit = _CtrlTableValue(12,1,'RW')
	MinVoltageLimit = _CtrlTableValue(13,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(14,1,'RW')
	MaxTorque = _CtrlTableValue(15,2,'RW')
	StatusReturnLevel = _CtrlTableValue(17,1,'RW')
	Shutdown = _CtrlTableValue(18,1,'RW')
	TorqueEnable = _CtrlTableValue(24,1,'RW')
	LED = _CtrlTableValue(25,1,'RW')
	DGain = _CtrlTableValue(27,1,'RW')
	IGain = _CtrlTableValue(28,1,'RW')
	PGain = _CtrlTableValue(29,1,'RW')
	GoalPosition = _CtrlTableValue(30,2,'RW')
	MovingSpeed = _CtrlTableValue(32,2,'RW')
	TorqueLimit = _CtrlTableValue(35,2,'RW')
	PresentPosition = _CtrlTableValue(37,2,'R')
	PresentSpeed = _CtrlTableValue(39,2,'R')
	PresentLoad = _CtrlTableValue(41,2,'R')
	PresentVoltage = _CtrlTableValue(45,1,'R')
	PresentTemperature = _CtrlTableValue(46,1,'R')
	RegisteredInstruction = _CtrlTableValue(47,1,'R')
	Moving = _CtrlTableValue(49,1,'R')
	HardwareErrorStatus = _CtrlTableValue(50,1,'R')
	Punch = _CtrlTableValue(51,2,'RW')

class MX64(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	FirmwareVersion = _CtrlTableValue(2,1,'R')
	ID = _CtrlTableValue(3,1,'RW')
	BaudRate = _CtrlTableValue(4,1,'RW')
	ReturnDelayTime = _CtrlTableValue(5,1,'RW')
	CWAngleLimit = _CtrlTableValue(6,2,'RW')
	CCWAngleLimit = _CtrlTableValue(8,2,'RW')
	TemperatureLimit = _CtrlTableValue(11,1,'RW')
	MinVoltageLimit = _CtrlTableValue(12,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(13,1,'RW')
	MaxTorque = _CtrlTableValue(14,2,'RW')
	StatusReturnLevel = _CtrlTableValue(16,1,'RW')
	AlarmLED = _CtrlTableValue(17,1,'RW')
	Shutdown = _CtrlTableValue(18,1,'RW')
	MultiTurnOffset = _CtrlTableValue(20,2,'RW')
	ResolutionDivider = _CtrlTableValue(22,1,'RW')
	TorqueEnable = _CtrlTableValue(24,1,'RW')
	LED = _CtrlTableValue(25,1,'RW')
	DGain = _CtrlTableValue(26,1,'RW')
	IGain = _CtrlTableValue(27,1,'RW')
	PGain = _CtrlTableValue(28,1,'RW')
	GoalPosition = _CtrlTableValue(30,2,'RW')
	MovingSpeed = _CtrlTableValue(32,2,'RW')
	TorqueLimit = _CtrlTableValue(34,2,'RW')
	PresentPosition = _CtrlTableValue(36,2,'R')
	PresentSpeed = _CtrlTableValue(38,2,'R')
	PresentLoad = _CtrlTableValue(40,2,'R')
	PresentVoltage = _CtrlTableValue(42,1,'R')
	PresentTemperature = _CtrlTableValue(43,1,'R')
	Registered = _CtrlTableValue(44,1,'R')
	Moving = _CtrlTableValue(46,1,'R')
	Lock = _CtrlTableValue(47,1,'RW')
	Punch = _CtrlTableValue(48,2,'RW')
	RealtimeTick = _CtrlTableValue(50,2,'R')
	Current = _CtrlTableValue(68,2,'RW')
	TorqueCtrlModeEnable = _CtrlTableValue(70,1,'RW')
	GoalTorque = _CtrlTableValue(71,2,'RW')
	GoalAcceleration = _CtrlTableValue(73,1,'RW')

class XM540W150(_DynamixelModel):
	ModelNumber = _CtrlTableValue(0,2,'R')
	ModelInformation = _CtrlTableValue(2,4,'R')
	FirmwareVersion = _CtrlTableValue(6,1,'R')
	ID = _CtrlTableValue(7,1,'RW')
	BaudRate = _CtrlTableValue(8,1,'RW')
	ReturnDelayTime = _CtrlTableValue(9,1,'RW')
	DriveMode = _CtrlTableValue(10,1,'RW')
	OperatingMode = _CtrlTableValue(11,1,'RW')
	SecondaryShadowID = _CtrlTableValue(12,1,'RW')
	ProtocolType = _CtrlTableValue(13,1,'RW')
	HomingOffset = _CtrlTableValue(20,4,'RW')
	MovingThreshold = _CtrlTableValue(24,4,'RW')
	TemperatureLimit = _CtrlTableValue(31,1,'RW')
	MaxVoltageLimit = _CtrlTableValue(32,2,'RW')
	MinVoltageLimit = _CtrlTableValue(34,2,'RW')
	PWMLimit = _CtrlTableValue(36,2,'RW')
	CurrentLimit = _CtrlTableValue(38,2,'RW')
	VelocityLimit = _CtrlTableValue(44,4,'RW')
	MaxPositionLimit = _CtrlTableValue(48,4,'RW')
	MinPositionLimit = _CtrlTableValue(52,4,'RW')
	ExternalPortMode1 = _CtrlTableValue(56,1,'RW')
	ExternalPortMode2 = _CtrlTableValue(57,1,'RW')
	ExternalPortMode3 = _CtrlTableValue(58,1,'RW')
	StartupConfiguration = _CtrlTableValue(60,1,'RW')
	Shutdown = _CtrlTableValue(63,1,'RW')
	TorqueEnable = _CtrlTableValue(64,1,'RW')
	LED = _CtrlTableValue(65,1,'RW')
	StatusReturnLevel = _CtrlTableValue(68,1,'RW')
	RegisteredInstruction = _CtrlTableValue(69,1,'R')
	HardwareErrorStatus = _CtrlTableValue(70,1,'R')
	VelocityIGain = _CtrlTableValue(76,2,'RW')
	VelocityPGain = _CtrlTableValue(78,2,'RW')
	PositionDGain = _CtrlTableValue(80,2,'RW')
	PositionIGain = _CtrlTableValue(82,2,'RW')
	PositionPGain = _CtrlTableValue(84,2,'RW')
	Feedforward2ndGain = _CtrlTableValue(88,2,'RW')
	Feedforward1stGain = _CtrlTableValue(90,2,'RW')
	BusWatchdog = _CtrlTableValue(98,1,'RW')
	GoalPWM = _CtrlTableValue(100,2,'RW')
	GoalCurrent = _CtrlTableValue(102,2,'RW')
	GoalVelocity = _CtrlTableValue(104,4,'RW')
	ProfileAcceleration = _CtrlTableValue(108,4,'RW')
	ProfileVelocity = _CtrlTableValue(112,4,'RW')
	GoalPosition = _CtrlTableValue(116,4,'RW')
	RealtimeTick = _CtrlTableValue(120,2,'R')
	Moving = _CtrlTableValue(122,1,'R')
	MovingStatus = _CtrlTableValue(123,1,'R')
	PresentPWM = _CtrlTableValue(124,2,'R')
	PresentCurrent = _CtrlTableValue(126,2,'R')
	PresentVelocity = _CtrlTableValue(128,4,'R')
	PresentPosition = _CtrlTableValue(132,4,'R')
	VelocityTrajectory = _CtrlTableValue(136,4,'R')
	PositionTrajectory = _CtrlTableValue(140,4,'R')
	PresentInputVoltage = _CtrlTableValue(144,2,'R')
	PresentTemperature = _CtrlTableValue(146,1,'R')
	BackupReady = _CtrlTableValue(147,1,'R')
	ExternalPortData1 = _CtrlTableValue(152,2,'RW')
	ExternalPortData2 = _CtrlTableValue(154,2,'RW')
	ExternalPortData3 = _CtrlTableValue(156,2,'RW')
	IndirectAddress1 = _CtrlTableValue(168,2,'RW')
	IndirectAddress2 = _CtrlTableValue(170,2,'RW')
	IndirectAddress3 = _CtrlTableValue(172,2,'RW')
	IndirectAddress26 = _CtrlTableValue(218,2,'RW')
	IndirectAddress27 = _CtrlTableValue(220,2,'RW')
	IndirectAddress28 = _CtrlTableValue(222,2,'RW')
	IndirectData1 = _CtrlTableValue(224,1,'RW')
	IndirectData2 = _CtrlTableValue(225,1,'RW')
	IndirectData3 = _CtrlTableValue(226,1,'RW')
	IndirectData26 = _CtrlTableValue(249,1,'RW')
	IndirectData27 = _CtrlTableValue(250,1,'RW')
	IndirectData28 = _CtrlTableValue(251,1,'RW')
	IndirectAddress29 = _CtrlTableValue(578,2,'RW')
	IndirectAddress30 = _CtrlTableValue(580,2,'RW')
	IndirectAddress31 = _CtrlTableValue(582,2,'RW')
	IndirectAddress54 = _CtrlTableValue(628,2,'RW')
	IndirectAddress55 = _CtrlTableValue(630,2,'RW')
	IndirectAddress56 = _CtrlTableValue(632,2,'RW')
	IndirectData29 = _CtrlTableValue(634,1,'RW')
	IndirectData30 = _CtrlTableValue(635,1,'RW')
	IndirectData31 = _CtrlTableValue(636,1,'RW')
	IndirectData54 = _CtrlTableValue(659,1,'RW')
	IndirectData55 = _CtrlTableValue(660,1,'RW')
	IndirectData56 = _CtrlTableValue(661,1,'RW')

