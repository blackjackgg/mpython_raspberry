"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
class Descriptor(object):
	def __init__(self, uuid, flags):
		self.__uuid = uuid
		self.__flags = flags

	def get_descriptor(self):
		return self.__uuid, self.__flags
