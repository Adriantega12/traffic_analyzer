# ICMPv4 class

# Contiene el desempaquetamiento de la clase ICMPv4
# Campos de ICMPv4:

# - Type: 8 bits
# - Code: 8 bits
# - Checksum: 16 bits
# - Información específica a partir del 4to byte. (No tomada en cuenta)

import struct

class ICMPv4:
	'ICMPv4 class'

	def __init__(self, ipv4Payload):
		_icmpType, _code, _checksum = struct.unpack( '! B B H', ipv4Payload[ : 4 ] )

		self.icmpType = _icmpType
		self.code = _code
		self.checksum = checksum
		self.payload = data[ 4 : ]