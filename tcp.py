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

import struct

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
		self.offset = self.getOffset(_offsetRes)
		self.c, self.e, self.u, self.a, self.p, self.r, self.s, self.f = self.getTCPFlags(_tcpFlags)
		self.window = _tcpFlags
		self.checksum = _checksum
		self.urgPointer = _urgPointer
		self.payload = ipPayload [ 20 : ]

	def getOffset(self, _offsetRes):
		'Separate the 4 bits of Offset from the full byte'
		return (_offsetRes >> 4) & 0x0F

	def getTCPFlags(self, _tcpFlags):
		'Separate all TCP flags'
		_c = (_tcpFlags >> 8) & 0x80
		_e = (_tcpFlags >> 7) & 0x40
		_u = (_tcpFlags >> 6) & 0x20
		_a = (_tcpFlags >> 5) & 0x10
		_p = (_tcpFlags >> 4) & 0x08
		_r = (_tcpFlags >> 3) & 0x04
		_s = (_tcpFlags >> 2) & 0x02
		_f = (_tcpFlags >> 1) & 0x01

		return _c, _e, _u, _a, _p, _r, _s, _f

	def getInfo(self):
		'String of information of TCP Class'
		
		info = 'Source Port: {} Destination Port: {}\n'.format(
				self.srcPort, self.destPort )
		info += 'Sequence Number: {}\n'.format(
				self.seqNum )
		info += 'Acknowledgement Number: {}\n'.format(
				self.ackNum )
		info += 'Offset: {}\n'.format(self.offset)
		info += 'TCP Flags:\nC: {} E: {} U: {} A: {} P: {} R: {} S: {} F: {}\n'.format(
				self.c, self.e, self.u, self.a, self.p, self.r, self.s, self.f)
		info += 'Window Size: {}\n'.format(
				self.window )
		info += 'Urgent Pointer: {}\n'.format(
				self.urgPointer )

		return info
