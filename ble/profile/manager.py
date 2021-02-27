"""
The MIT License (MIT)
Copyright © 2020 Walkline Wang (https://walkline.wang)
Gitee: https://gitee.com/walkline/ESP32-BLE-Remote_Controller
"""
class ProfileManager(object):
	def __init__(self):
		self.__services = []

	def add_services(self, *services):
		for service in tuple(services):
			self.__services.append(service)

	def get_services(self) -> tuple:
		return tuple([service.get_service() for service in self.__services])

	def get_services_uuid(self) -> list:
		return [service.UUID for service in self.__services]
