# --------------------------------------------------------------------
class SBBFactory(object):
	"""docstring for SBBFactory"""
	def __init__(self, arg):
		super(SBBFactory, self).__init__()
		self.arg = arg

	@staticmethod
	def loadLib(*args):
		import name

# --------------------------------------------------------------------
class SBBAplication(object):
	"""docstring for SBB"""
	def __init__(self, arg):
		super(SBB, self).__init__()
		self.arg = arg
		
# --------------------------------------------------------------------
class SBBLearning(object):
	"""docstring for SBBLearning"""
	def __init__(self, arg):
		super(SBBLearning, self).__init__()
		self.arg = arg
		
# --------------------------------------------------------------------
class SBBCommunication(object):
	"""docstring for SBBCommunication"""
	def __init__(self, arg):
		super(SBBCommunication, self).__init__()
		self.arg = arg

# --------------------------------------------------------------------
# Iteraction with other data soucre
class SBBInterface(object):
	"""docstring for SBBInterface"""
	def __init__(self, arg):
		super(SBBInterface, self).__init__()
		self.arg = arg

class SBBInterfaceWeb(SBBInterface):
	"""docstring for SBBInterfaceWeb"""
	def __init__(self, arg):
		super(SBBInterfaceWeb, self).__init__()
		self.arg = arg

class SBBInterfaceWebBs4(SBBInterfaceWeb):
		"""docstring for SBBInterfaceWebBs4"""
		lib = 'bs4'

		def __init__(self, arg):
			SBBFactory.loadLib(self.lib)
			super(SBBInterfaceWebBs4, self).__init__()
			self.arg = arg
				

class SBBInterfaceCSV(SBBInterface):
	"""docstring for SBBInterfaceCSV"""
	def __init__(self, arg):
		super(SBBInterfaceCSV, self).__init__()
		self.arg = arg

# --------------------------------------------------------------------
# Data class
class SBBSource(object):
	"""docstring for SBBSource"""
	def __init__(self, arg):
		super(SBBSource, self).__init__()
		self.data = arg
		
class SBBSourceWeb(SBBSource):
	"""docstring for SBBSourceWeb"""
	def __init__(self, arg):
		super(SBBSourceWeb, self).__init__(arg)

class SBBSourceWebBs4(SBBSourceWeb):
	lib = 'bs4'

	"""docstring for SBBSourceWebBs4"""
	def __init__(self, arg):
		SBBFactory.loadLib(self.lib)
		super(SBBSourceWebBs4, self).__init__(arg)		

class SBBSourceCsv(SBBSource):
	"""docstring for SBBSourceCsv"""
	def __init__(self, arg):
		super(SBBSourceCsv, self).__init__()
		self.arg = arg

# --------------------------------------------------------------------
# Date class

class SBBDate(object):
	"""docstring for SBBDate"""
	lib = {
		'from': '',
		'import' : '',
		'as': ''
	}
	monthRus = {
		'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'
	}

	def __init__(self, arg):
		super(SBBDate, self).__init__()
		self.arg = arg
		
	def fromStringToUnix():
		pass

class SBBDateVk(SBBDate):
	"""docstring for SBBDateVk"""
	def __init__(self, arg):
		super(SBBDateVk, self).__init__()
		self.arg = arg