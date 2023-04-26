from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
	@property
	def initial_weight(self):
		return 9
	
	@property
	def service_type(self):
		return "Main Service"
	
	def __init__(self, name: str, kind: str, price: float):
		super().__init__(name, kind, price, self.initial_weight)
	
	def eating(self):
		self.weight += 3
