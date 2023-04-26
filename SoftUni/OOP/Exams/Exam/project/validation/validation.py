class Validation:
	@staticmethod
	def check_empty_value(value, item_name):
		if value == "" or value.isspace():
			raise ValueError(f"{item_name} cannot be empty!")
		
	@staticmethod
	def check_more_than_zero(value, item_name, _number):
		if value <= 0.0:
			raise ValueError(f"{item_name} cannot be less than or equal to {_number}!")
		
	# @staticmethod
	# def check_valid_capacity(value, item_name):
	# 	if value <= 0:
	# 		raise ValueError(f"{item_name} cannot be less than or equal to 0!")