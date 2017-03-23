class ICMPv4:
	"ICMP class, version 4"

	def __init__(self, ipv4Payload):
		_icmpType, _code, _checksum = struct.unpack( '! B B H', ipv4Payload[ : 4 ] )

		self.icmpType = _icmpType
		self.code = _code
		self.checksum = checksum
		self.payload = data[ 4 : ]