class Door:
	def __init__(self, **kwargs):
		self.position = kwargs.get('position', None)

		for key, value in kwargs.items():
			setattr(self, key, value)
