import struct

class UDP:
	'UDP Class'

	def __init__(self, ipPayload):
		
		_srcPort, _destPort, _length, _checksum = struct.unpack("! H H H H", ipPayload[ : 8 ])

		self.srcPort = _srcPort
		self.destPort = _destPort
		self.length = _length
		self.checksum = _checksum
		self.payload = ipPayload[ 8 : ] 

	def getInfo(self):
		info = 'Source Port: {} Destination Port: {}\n'.format(self.srcPort, self.destPort)
		info += 'Length: {}\n'.format(self.length)
		info += 'Payload: ' + str(self.payload) + '\n'
		return info