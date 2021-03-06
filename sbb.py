# --------------------------------------------------------------------
class SBBFactory(object):
	"""docstring for SBBFactory"""
	def __init__(self, arg):
		super(SBBFactory, self).__init__()
		self.arg = arg

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
	_dt = 'datetime'
	_re = 're'

	lib = {
		'from': '',
		'import' : '',
		'as': ''
	}

	monthRus = {
		'янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'
	}

	import datetime as _dt
	import re as _re

	def __init__(self, arg):
		super(SBBDate, self).__init__()
		self.arg = arg

class SBBDateVk(SBBDate):
	"""docstring for SBBDateVk"""
	vkDateRegex = _re.compile('([0-9]{1,2})\W([а-я]{3})\W([0-9]{4})\Wв\W([0-9]{1,2}):([0-9]{1,2})', _re.IGNORECASE)

	def __init__(self, arg):
		super(SBBDateVk, self).__init__()
		self.arg = arg

	def getTimeFromVk(date):
		day, month, year, hours, minutes = self.vkDateRegex.findall(date)[0]
		date = _dt.datetime(int(year), monthRus.index(month)+1, int(day), int(hours), int(minutes), 0)

		return date

# --------------------------------------------------------------------
# Controllers

class SBBControllers(object):
	"""docstring for SBBControllers"""
	def __init__(self, arg):
		super(SBBControllers, self).__init__()
		self.arg = arg

# --------------------------------------------------------------------
# Controller

class SBBController(object):
	"""docstring for SBBController"""
	def __init__(self, arg):
		super(SBBController, self).__init__()
		self.arg = arg

class SBBControllerCommunication(SBBController):
	"""docstring for SBBControllerCommunication"""
	def __init__(self, arg):
		super(SBBControllerCommunication, self).__init__()
		self.arg = arg

class SBBControllerLearn(SBBController):
	"""docstring for SBBControllerLearn"""
	def __init__(self, arg):
		super(SBBControllerLearn, self).__init__()
		self.arg = arg