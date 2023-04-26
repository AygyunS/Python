from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
	@property
	def initial_weight(self):
		return 7
	
	@property
	def service_type(self):
		return "Secondary Service"
	
	def __init__(self, name: str, kind: str, price: float):
		super().__init__(name, kind, price, self.initial_weight)
		
	def eating(self):
		self.weight += 1
