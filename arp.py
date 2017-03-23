import struct
import formatFunctions

"""
ARP Packet fields
Hardware Type: 2 bytes
Protocol Type: 2 bytes
*Hardware Address Length: 1 byte
**Protocol Address Length: 1 byte
Operation Code: 2 bytes
Source Hardware Address: *
Source Protocol Address: **
Target Hardware Addres: *
Target Protocol Address: **
Total: 28 - 32
"""

class ARP:
	'ARP Packet class:'

	def __init__(self, ehtPayload):
		'Unpack ARP packet'

		# Primero se tiene que determinar la longitud de la "Hardware Address" y "Protocol Address"
		# para poder desempaquetar todo
		(_hardType, _protoType, 
		 _hardAddrLength, _protoAddrLength, _opCode) = struct.unpack('! H H B B H', ehtPayload[ : 8] )

		# Una vez determinadas las longitudes entonces armamos el string para hacer unpack

		unpackString = '! {}s {}s {}s {}s'.format(_hardAddrLength, _protoAddrLength, 
												  _hardAddrLength, _protoAddrLength)
		(_srcHardAddr, _srcProtoAddr, 
			_targetHardAddr, _targetProtoAddr) = struct.unpack( unpackString, 
												 ehtPayload[ 8 : 8 + (2 *_hardAddrLength + 2 *_protoAddrLength) ] )


		self.hardType = _hardType
		self.protoType = _protoType
		self.hardAddrLength = _hardAddrLength
		self.protoAddrLength = _protoAddrLength
		self.opCode = _opCode
		self.srcHardAddr = formatFunctions.formatMACAddress(_srcHardAddr)
		self.srcProtoAddr = formatFunctions.formatIPv4(_srcProtoAddr)
		self.targetHardAddr = formatFunctions.formatMACAddress(_targetHardAddr)
		self.targetProtoAddr = formatFunctions.formatIPv4(_targetProtoAddr)