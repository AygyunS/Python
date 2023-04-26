from project.services.base_service import BaseService


class SecondaryService(BaseService):
	@property
	def initial_capacity(self):
		return 15
	
	@property
	def service_type(self):
		return 'Secondary Service'
	
	def __init__(self, name: str):
		super().__init__(name, self.initial_capacity)
