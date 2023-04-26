from abc import ABC, abstractmethod
from typing import List

from project.robots.base_robot import BaseRobot
from project.validation.validation import Validation


class BaseService(ABC):
	def __init__(self, name: str, capacity: int):
		self.name = name
		self.capacity = capacity
		self.robots: List[BaseRobot] = []
	
	@property
	def count_of_robots(self):
		return len(self.robots)
	
	@property
	def price_of_all_robots(self):
		return sum([r.price for r in self.robots])
	
	@property
	@abstractmethod
	def service_type(self):
		...
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		Validation.check_empty_value(value, 'Service name')
		self.__name = value
	
	@property
	def capacity(self):
		return self.__capacity
	
	@capacity.setter
	def capacity(self, value):
		Validation.check_more_than_zero(value, 'Service capacity', '0')
		self.__capacity = value
	
	def has_capacity_for_robot(self):
		return len(self.robots) < self.capacity
	
	def feed_all_robots(self):
		for robot in self.robots:
			robot.eating()
	
	def details(self):
		result = [
			f"{self.name} {self.service_type}:",
			f"Robots: {' '.join([r.name for r in self.robots]) if self.robots else 'none'}"
		]
		
		return '\n'.join(result)
