# ARP Packet

# Contiene el desempaquetamiento de la clase ARP
# Campos de ARP Packet:

# - Hardware Type: 2 bytes
# - Protocol Type: 2 bytes
# - *Hardware Address Length: 1 byte
# - **Protocol Address Length: 1 byte
# - Operation Code: 2 bytes
# - Source Hardware Address: *
# - Source Protocol Address: **
# - Target Hardware Addres: *
# - Target Protocol Address: **
# Total: 28 - 32

# En esta clase hay que ser un poco cauteloso, específicamente con los campos marcados.
# Primero se tiene que extraer la longitud de la dirección de hardware y de protocolo y proceder desde ahí.
# Nada del otro mundo, pero aún así. Ya sabiendo esto se procede como siempre.
# La clase de momento está incompleto puesto que debería tomar en cuenta cuando es IPv4 o IPv6,
# algún día haré una solución elegante, hoy no es ese día.

import struct
import formatFunctions

ARP_OPCODE_TABLE = {
					1 : "ARP Request",
					2 : "ARP Reply",
					3 : "RARP Request",
					4 : "RARP Reply",
					5 : "DRARP Request",
					6 : "DRARP Reply",
					7 : "DRARP Error",
					8 : "InARP Request",
					9 : "InARP Reply"
					}

class ARP:
	'ARP Message class:'

	seARP_OPCODE_TABLE = {
					1 : "ARP Request",
					2 : "ARP Reply",
					3 : "RARP Request",
					4 : "RARP Reply",
					5 : "DRARP Request",
					6 : "DRARP Reply",
					7 : "DRARP Error",
					8 : "InARP Request",
					9 : "InARP Reply"
					}

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
												 ehtPayload[ 8 : 8 + (2 * _hardAddrLength + 
												 					  2 * _protoAddrLength) ] )


		self.hardType = _hardType
		self.protoType = _protoType
		self.hardAddrLength = _hardAddrLength
		self.protoAddrLength = _protoAddrLength
		self.opCode = _opCode
		self.srcHardAddr = formatFunctions.formatMACAddress(_srcHardAddr)
		self.srcProtoAddr = formatFunctions.formatIPv4(_srcProtoAddr)
		self.targetHardAddr = formatFunctions.formatMACAddress(_targetHardAddr)
		self.targetProtoAddr = formatFunctions.formatIPv4(_targetProtoAddr)

	def getInfo(self):
		info = 'Hardware Type: {} Protocol Type: {}\n'.format(
				self.hardType, self.protoType)
		info += 'Hardware Address Length: {} Prototype Address Length: {}\n'.format(
				self.hardAddrLength, self.protoAddrLength)
		info += 'Operation Code: {} Message Type: {}\n'.format(self.opCode, ARP_OPCODE_TABLE[self.opCode])
		info += 'Source Hardware Address: {}\nSource Protocol Address: {}\n'.format(
				self.srcHardAddr, self.srcProtoAddr)
		info += 'Target Hardware Address: {}\nTarget Protocol Address: {}\n'.format(
				self.targetHardAddr, self.targetProtoAddr)
		return info;

	def getMessage(self):
		return ARP_OPCODE_TABLE[self.opCode]