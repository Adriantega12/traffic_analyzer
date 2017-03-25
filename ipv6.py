# IPv6 Header class

# Contiene el desempaquetamiento de la clase IPv6.
# Campos del IPv6 Header:

# - Version: 4 bits
# - Traffic Class: 8 bits
# - Flow Label: 20 bits
# - Payload Length: 16 bits
# - Next Header: 8 bits
# - Hop Limit: 8 bits
# - Source Address: 128 bits (16 bytes)
# - Destination Address: 128 bits (16 bytes)

# Los únicos campos que reciben algún tipo de tratamiento especial de bits son Version, Traffic Class,
# porque se encuentra divido en el primer y segundo byte; y Flow Label por la misma razón que el anterior,
# en el segundo, tercer y cuarto byte.

# Cabe destacar que Next Header es similar al campo "protocol" de IPv4 porque representa ya sea el PDU
# de la capa superior o el "Extension Header" de IPv6. En dado caso, en el código nos interesa lo siguiente
# de momento:
# 	0x3A = ICMPv6	58 en decimal.

import struct
import formatFunctions

class IPv6:
	'IPv6 class'

	def __init__(self, ethPayload):
		'Initialize IPv6 class'

		self.getVerTrafClassAndFlowLabel(ethPayload[0 : 4])

		_payloadLen, _nxt, _hop, _srcAddr, _destAddr = struct.unpack('! H c B 16s 16s', ethPayload[4 : 40])
		
		self.payloadLength = _payloadLen
		self.nextHeader = _nxt
		self.hopLimit = _hop
		self.sourceAddress = formatFunctions.formatIPv6(_srcAddr)
		self.destinationAddress = formatFunctions.formatIPv6(_destAddr)
		self.ipv6Payload = ethPayload[40 : ]


	def getVerTrafClassAndFlowLabel(self, fourBytes):
		'Get version, traffic class and flow label from first four bytes of the ethernet payload'

		twoBytes = struct.unpack('! H', fourBytes[2 : ])

		self.version = fourBytes[0] >> 4
		self.trafficClass = ( ( fourBytes[0] & 15 ) << 4 ) + ( ( fourBytes[1] & 240 ) >> 4 )
		self.flowLabel = ((fourBytes[1] & 15) << 16) + twoBytes[0]


	def getInfo(self):
		'Print the IPv6 Packet information'

		info = 'Version: {} Traffic Class: {} Flow Label: {}\n'.format(
				self.version, self.trafficClass, self.flowLabel)
		info += 'Payload Length: {} Next Header: {} Hop Limit: {}\n'.format(
				self.payloadLength, self.nextHeader, self.hopLimit)
		info += 'Source Address: {}\nDestination Address: {}\n'.format(
				self.sourceAddress, self.destinationAddress)

		return info


		