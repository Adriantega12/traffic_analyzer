# TCP Segment Class

# Contiene el desempaquetamiento de la clase TCP.

# Los campos de TCPv4 son los siguientes:
#  - Source Port: 2 bytes
#  - Destination Port: 2 bytes
#  - Sequence Number: 4 bytes
#  - Acknowledgement Number: 4 bytes
#  - Offset: 4 bits
#  - Reserved: 4 bits
#  - TCP Flags: 1 byte
#  	- C: Reduced (0x80)
#  	- E: ECN Echo (0x40)
#  	- U: Urgent (0x20)
#  	- A: Ack (0x10)
#  	- P: Push (0x08)
#  	- R: Reset (0x04)
#  	- S: Syn (0x02)
#  	- F: Fin (0x01)
#  - Window: 2 bytes
#  - Checksum: 2 bytes
#  - Urgent Pointer: 2 bytes
#  - Total: 20 bytes

class TCP:
	'TCP Segment class'

	def __init__(self, ipPayload):
		'Unpack IP Payload'
		_srcPort, _destPort, _seqNum, _ackNum, _offsetRes, _tcpFlags, \
		_window, _checksum, _urgPointer = struct.unpack("! H H L L B B H H H", ipPayload[ : 20 ])

		self.srcPort = _srcPort
		self.destPort = _destPort
		self.seqNum = _seqNum
		self.ackNum = _ackNum
		self.offsetRes = _offsetRes # Se debe desglosar
		self.tcpFlags = _tcpFlags # Desglosar en banderas
		self.window = _tcpFlags
		self.checksum = _checksum
		self.urgPointer = _urgPointer

	def getOffset(self, offsetRes):
		'Separate the 4 bits of Offset from the full byte'