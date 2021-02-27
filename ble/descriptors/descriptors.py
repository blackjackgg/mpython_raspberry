"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
import ubluetooth as bt
from ble.const import BLEConst
from .__descriptor import Descriptor


class CharacteristicAggregateFormat(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.CHARACTERISTIC_AGGREGATE_FORMAT)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class CharacteristicExtendedProperties(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.CHARACTERISTIC_EXTENDED_PROPERTIES)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class CharacteristicPresentationFormat(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.CHARACTERISTIC_PRESENTATION_FORMAT)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class CharacteristicUserDescription(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.CHARACTERISTIC_USER_DESCRIPTION)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ClientCharacteristicConfiguration(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.CLIENT_CHARACTERISTIC_CONFIGURATION)
	FLAGS = bt.FLAG_READ | bt.FLAG_WRITE

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class EnvironmentalSensingConfiguration(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.ENVIRONMENTAL_SENSING_CONFIGURATION)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class EnvironmentalSensingMeasurement(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.ENVIRONMENTAL_SENSING_MEASUREMENT)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class EnvironmentalSensingTriggerSetting(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.ENVIRONMENTAL_SENSING_TRIGGER_SETTING)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ExternalReportReference(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.EXTERNAL_REPORT_REFERENCE)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class NumberOfDigitals(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.NUMBER_OF_DIGITALS)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ReportReference(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.REPORT_REFERENCE)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ServerCharacteristicConfiguration(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.SERVER_CHARACTERISTIC_CONFIGURATION)
	FLAGS = bt.FLAG_READ | bt.FLAG_WRITE

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class TimeTriggerSetting(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.TIME_TRIGGER_SETTING)
	FLAGS = bt.FLAG_READ | bt.FLAG_WRITE

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ValidRange(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.VALID_RANGE)
	FLAGS = bt.FLAG_READ

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)


class ValueTriggerSetting(Descriptor):
	UUID = bt.UUID(BLEConst.Descriptors.VALUE_TRIGGER_SETTING)
	FLAGS = bt.FLAG_READ | bt.FLAG_WRITE

	def __init__(self):
		Descriptor.__init__(self, self.UUID, self.FLAGS)
