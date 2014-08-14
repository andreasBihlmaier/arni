from Status import Status
import psutil

class HostStatus(Status):

	"""
	Extension of Status , to store 
	additional information used by hosts. 
	"""
	
	def __init__(self):
		
		super(HostStatus, self).__init__()
		
		#: CPU temp in celsius.
		self.__cpu_temp =  []
		

		#: CPU temp by core in celsius.
		self.__cpu_temp_core = [[] for x in range(self._cpu_count)]
		
		#: GPU temp by card in celsius.
		self.__gpu_temp = []
		
		self.__network_interfaces = psutil.net_io_counters(pernic = True)		


		#: Dictionary holding sets of Network interface - bandwidth in bytes
		self.__bandwidth = {}
		
		#: Dictionary holding sets of 
		#: Network interface - frequency of network calls in hertz.
		self.__msg_frequency = {}

		#: Dictionary holding sets of drive name - free space.
		self.__drive_space = {}
		
		#: Dictionary holding sets of drive name - bytes/s written.
		self.__drive_write = {}
		
		#: Dictionary holding sets of drive name - bytes/s read.
		self.__drive_read = {}
		
	
	def add_cpu_temp(self, temp):
		"""
		Adds another measured value to cpu_temp. 
		
		:param temp: measured temperature in celsius
		:type temp: int
		"""
		self.__cpu_temp.append(temp)
		
	def add_cpu_temp_core(self, temps):
		"""
		Adds another set of measured values to cpu_temp_core.
		
		:param temps: measured temperatures in celsius
		:type temp: int[]
		"""
		for x in range(self._cpu_count):
			self.__cpu_temp_core[x].append(temps[x])
		
	def add_gpu_temp(self, temps):
		"""
		Adds another set of measured values to gpu_temp.
		
		:param temp: measured temperatures in celsius
		:type temp: int[]
		"""
		pass
		
	def add_bandwidth(self, interface, bytes):
		"""
		Adds another  measured value, in bytes, to bandwidth belonging 
		to the given network interface.
		
		:param interface: name of the network interface
		:type interface: string
		:param bytes: measured bytes
		:type bytes: int		
		"""
		if interface not in self.__bandwidth:
			self.__bandwidth[interface] = []

		self.__bandwidth[interface].append(bytes)


		
	def add_msg_frequency(self, interface, freq):
		"""
		Adds another  measured value, in hertz, to msg_frequency belonging 
		to the given network interface.
		
		:param interface: name of the network interface
		:type interface: string
		:param freq: measured frequency
		:type freq: int	
		"""
		if interface not in self.__msg_frequency:
			self.__msg_frequency[interface] = []

		self.__msg_frequency[interface].append(freq)

		
	def add_drive_write(self, disk, byte):
		"""
		Adds another  measured value, in bytes, to drive_write belonging 
		to the given disk.
		
		:param disk: name of the disk
		:type disk: string
		:param byte: bytes written
		:type byte: int	
		"""
		if disk not in self.__drive_write:
			self.__drive_write[disk] = []

		self.__drive_write[disk].append(byte)
		
	def add_drive_read(self, disk, byte):
		"""
		Adds another  measured value, in bytes, to drive_read belonging 
		to the given disk.
		
		:param disk: name of the disk
		:type disk: string
		:param byte: bytes read
		:type byte: int	
		"""
		if disk not in self.__drive_read:
			self.__drive_read[disk] = []

		self.__drive_read[disk].append(byte)
		


	def add_drive_space(self, disk, space):
		"""
		Adds the free space of a drive to the Dictionary
		
		:param disk: name of the disk
		:type disk: string
		:param space: free space
		:type byte: int	
		"""
		self.__drive_space[disk] = space



	def reset_specific(self):
		""" 
		Resets the values specific to Host or Nodes
		"""
		del self.__cpu_temp[:]
		del self.__cpu_temp_core[:]
		del self.__gpu_temp[:]

		self.__bandwidth.clear()
		self.__drive_read.clear()
		self.__drive_write.clear()
		self.__msg_frequency.clear()



	@property 
	def cpu_temp(self):
		return self.__cpu_temp

	@property 
	def cpu_temp_core(self):
		return self.__cpu_temp_core

	@property
	def gpu_temp(self):
		return self.__gpu_temp

	@property
	def bandwidth(self):
		return self.__bandwidth

	@property 
	def msg_frequency(self):
		return self.__msg_frequency

	@property 
	def drive_space(self):
		return self.__drive_space

	@property 
	def drive_write(self):
		return self.__drive_write

	@property 
	def drive_read(self):
		return self.__drive_read

	@cpu_temp.setter
	def cpu_temp(self, value):
		self.__cpu_temp = value

	@cpu_temp_core.setter
	def cpu_temp_core(self, value):
		self.__cpu_temp_core = value

	@gpu_temp.setter
	def gpu_temp(self, value):
		self.__gpu_temp = value


	@bandwidth.setter
	def bandwidth(self, value):
		self.__bandwidth = value 

	@msg_frequency.setter
	def msg_frequency(self, value):
		self.__msg_frequency = value

	@drive_space.setter
	def drive_space(self, value):
		self.__drive_space = value

	@drive_read.setter
	def drive_read(self, value):
		self.__drive_read = value

	@drive_write.setter
	def drive_write(self, value):
		self.__drive_write = value
