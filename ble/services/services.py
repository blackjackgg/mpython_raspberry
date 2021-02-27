"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
import ubluetooth as bt
from ble.const import BLEConst
from .__service import Service


class GenericAccess(Service):
	UUID = bt.UUID(BLEConst.Services.GENERIC_ACCESS)

	def __init__(self):
		Service.__init__(self, self.UUID)


class AlertNotificationService(Service):
	UUID = bt.UUID(BLEConst.Services.ALERT_NOTIFICATION_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class AutomationIO(Service):
	UUID = bt.UUID(BLEConst.Services.AUTOMATION_IO)

	def __init__(self):
		Service.__init__(self, self.UUID)


class BatteryService(Service):
	UUID = bt.UUID(BLEConst.Services.BATTERY_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class BinarySensor(Service):
	UUID = bt.UUID(BLEConst.Services.BINARY_SENSOR)

	def __init__(self):
		Service.__init__(self, self.UUID)


class BloodPressure(Service):
	UUID = bt.UUID(BLEConst.Services.BLOOD_PRESSURE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class BodyComposition(Service):
	UUID = bt.UUID(BLEConst.Services.BODY_COMPOSITION)

	def __init__(self):
		Service.__init__(self, self.UUID)


class BondManagementService(Service):
	UUID = bt.UUID(BLEConst.Services.BOND_MANAGEMENT_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ContinuousGlucoseMonitoring(Service):
	UUID = bt.UUID(BLEConst.Services.CONTINUOUS_GLUCOSE_MONITORING)

	def __init__(self):
		Service.__init__(self, self.UUID)


class CurrentTimeService(Service):
	UUID = bt.UUID(BLEConst.Services.CURRENT_TIME_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class CyclingPower(Service):
	UUID = bt.UUID(BLEConst.Services.CYCLING_POWER)

	def __init__(self):
		Service.__init__(self, self.UUID)


class CyclingSpeedAndCadence(Service):
	UUID = bt.UUID(BLEConst.Services.CYCLING_SPEED_AND_CADENCE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class DeviceInformation(Service):
	UUID = bt.UUID(BLEConst.Services.DEVICE_INFORMATION)

	def __init__(self):
		Service.__init__(self, self.UUID)


class EmergencyConfiguration(Service):
	UUID = bt.UUID(BLEConst.Services.EMERGENCY_CONFIGURATION)

	def __init__(self):
		Service.__init__(self, self.UUID)


class EnvironmentalSensing(Service):
	UUID = bt.UUID(BLEConst.Services.ENVIRONMENTAL_SENSING)

	def __init__(self):
		Service.__init__(self, self.UUID)


class FitnessMachine(Service):
	UUID = bt.UUID(BLEConst.Services.FITNESS_MACHINE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class GenericAttribute(Service):
	UUID = bt.UUID(BLEConst.Services.GENERIC_ATTRIBUTE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class Glucose(Service):
	UUID = bt.UUID(BLEConst.Services.GLUCOSE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class HealthThermometer(Service):
	UUID = bt.UUID(BLEConst.Services.HEALTH_THERMOMETER)

	def __init__(self):
		Service.__init__(self, self.UUID)


class HeartRate(Service):
	UUID = bt.UUID(BLEConst.Services.HEART_RATE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class HTTPProxy(Service):
	UUID = bt.UUID(BLEConst.Services.HTTP_PROXY)

	def __init__(self):
		Service.__init__(self, self.UUID)


class HumanInterfaceDevice(Service):
	UUID = bt.UUID(BLEConst.Services.HUMAN_INTERFACE_DEVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ImmediateAlert(Service):
	UUID = bt.UUID(BLEConst.Services.IMMEDIATE_ALERT)

	def __init__(self):
		Service.__init__(self, self.UUID)


class IndoorPositioning(Service):
	UUID = bt.UUID(BLEConst.Services.INDOOR_POSITIONING)

	def __init__(self):
		Service.__init__(self, self.UUID)


class InsulinDelivery(Service):
	UUID = bt.UUID(BLEConst.Services.INSULIN_DELIVERY)

	def __init__(self):
		Service.__init__(self, self.UUID)


class InternetProtocolSupportService(Service):
	UUID = bt.UUID(BLEConst.Services.INTERNET_PROTOCOL_SUPPORT_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class LinkLoss(Service):
	UUID = bt.UUID(BLEConst.Services.LINK_LOSS)

	def __init__(self):
		Service.__init__(self, self.UUID)


class LocationAndNavigation(Service):
	UUID = bt.UUID(BLEConst.Services.LOCATION_AND_NAVIGATION)

	def __init__(self):
		Service.__init__(self, self.UUID)


class MeshProvisioningService(Service):
	UUID = bt.UUID(BLEConst.Services.MESH_PROVISIONING_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class NextDSTChangeService(Service):
	UUID = bt.UUID(BLEConst.Services.NEXT_DST_CHANGE_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ObjectTransferService(Service):
	UUID = bt.UUID(BLEConst.Services.OBJECT_TRANSFER_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class PhoneAlertStatusService(Service):
	UUID = bt.UUID(BLEConst.Services.PHONE_ALERT_STATUS_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class PulseOximeterService(Service):
	UUID = bt.UUID(BLEConst.Services.PULSE_OXIMETER_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ReconnectionConfiguration(Service):
	UUID = bt.UUID(BLEConst.Services.RECONNECTION_CONFIGURATION)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ReferenceTimeUpdateService(Service):
	UUID = bt.UUID(BLEConst.Services.REFERENCE_TIME_UPDATE_SERVICE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class RunningSpeedAndCadence(Service):
	UUID = bt.UUID(BLEConst.Services.RUNNING_SPEED_AND_CADENCE)

	def __init__(self):
		Service.__init__(self, self.UUID)


class ScanParameters(Service):
	UUID = bt.UUID(BLEConst.Services.SCAN_PARAMETERS)

	def __init__(self):
		Service.__init__(self, self.UUID)


class TransportDiscovery(Service):
	UUID = bt.UUID(BLEConst.Services.TRANSPORT_DISCOVERY)

	def __init__(self):
		Service.__init__(self, self.UUID)


class TxPower(Service):
	UUID = bt.UUID(BLEConst.Services.TX_POWER)

	def __init__(self):
		Service.__init__(self, self.UUID)


class UserData(Service):
	UUID = bt.UUID(BLEConst.Services.USER_DATA)

	def __init__(self):
		Service.__init__(self, self.UUID)


class WeightScale(Service):
	UUID = bt.UUID(BLEConst.Services.WEIGHT_SCALE)

	def __init__(self):
		Service.__init__(self, self.UUID)
