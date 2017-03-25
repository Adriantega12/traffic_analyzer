# ICMPv6 class

# Contiene el desempaquetamiento de la clase ICMPv6
# Campos de ICMPv6:

# - Type: 8 bits
# - Code: 8 bits
# - Checksum: 16 bits
# - Cuerpo del mensaje: Tomado como Payload.

# Para nuestros fines, es lo mismo ICMPv4.

import struct

class ICMPv6:
	'ICMPv6 class'
	
	def __init__(self, ipv6Payload):
		_type, _code, _checksum = struct.unpack( '! B B H', ipv6Payload[ : 4 ] )

		self.type = _type
		self.code = _code
		self.checksum = _checksum
		self.messageBody = ipv6Payload[ 4 : ]