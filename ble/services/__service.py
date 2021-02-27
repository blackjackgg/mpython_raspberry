"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
class Service(object):
	def __init__(self, uuid):
		self.__uuid = uuid
		self.__characteristics = []

	def add_characteristics(self, *characteristics):
		for characteristic in tuple(characteristics):
			self.__characteristics.append(characteristic)
		
		return self

	def get_service(self):
		return (self.__uuid, tuple([char.get_characteristic() for char in self.__characteristics]),)
