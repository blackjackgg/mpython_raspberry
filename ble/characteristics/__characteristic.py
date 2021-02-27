"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
https://gitee.com/walkline/micropython-ble-library
"""
class Characteristic(object):
	def __init__(self, uuid, flags):
		self.__descriptors = []
		self.__uuid = uuid
		self.__flags = flags
	
	def add_descriptors(self, *descriptors):
		for descriptor in tuple(descriptors):
			self.__descriptors.append(descriptor)
		
		return self

	def get_characteristic(self):
		if self.__descriptors:
			return (self.__uuid, self.__flags,) + (tuple([descriptor.get_descriptor() for descriptor in self.__descriptors]),)
		else:
			return self.__uuid, self.__flags,
