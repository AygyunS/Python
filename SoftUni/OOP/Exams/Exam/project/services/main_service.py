from project.services.base_service import BaseService


class MainService(BaseService):
	@property
	def initial_capacity(self):
		return 30
	
	@property
	def service_type(self):
		return 'Main Service'
	
	def __init__(self, name: str):
		super().__init__(name, self.initial_capacity)
