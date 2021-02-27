"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
import ubluetooth as bt
from ble.const import BLEConst
from .__characteristic import Characteristic


class Characteristics(Characteristic):
	def __init__(self, uuid, flags):
		self.__uuid = bt.UUID(uuid)
		self.__flags = flags

		Characteristic.__init__(self, self.__uuid, self.__flags)
