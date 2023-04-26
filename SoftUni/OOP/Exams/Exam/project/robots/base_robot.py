from abc import ABC, abstractmethod

from project.validation.validation import Validation


class BaseRobot(ABC):
	
	def __init__(self, name: str, kind: str, price: float, weight: int):
		self.name = name
		self.kind = kind
		self.price = price
		self.weight = weight
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value: str):
		Validation.check_empty_value(value, 'Robot name')
		self.__name = value
	
	@property
	def kind(self):
		return self.__kind
	
	@kind.setter
	def kind(self, value: str):
		Validation.check_empty_value(value, 'Robot kind')
		self.__kind = value
	
	@property
	def price(self):
		return self.__price
	
	@price.setter
	def price(self, value: float):
		Validation.check_more_than_zero(value, 'Robot price', '0.0')
		self.__price = value
	
	@abstractmethod
	def eating(self):
		...
	
	@abstractmethod
	def service_type(self):
		...
