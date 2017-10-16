# --------------------------------------------------------------------
class SBBFactory(object):
	"""docstring for SBBFactory"""
	def __init__(self, arg):
		super(SBBFactory, self).__init__()
		self.arg = arg

# --------------------------------------------------------------------
class SBB(object):
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
		self.arg = arg
		
class SBBSourceWeb(SBBSource):
	"""docstring for SBBSourceWeb"""
	def __init__(self, arg):
		super(SBBSourceWeb, self).__init__()
		self.arg = arg

class SBBSourceCsv(SBBSource):
	"""docstring for SBBSourceCsv"""
	def __init__(self, arg):
		super(SBBSourceCsv, self).__init__()
		self.arg = arg