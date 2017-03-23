# Ethernet Frame class

# Contiene el desempaquetamiento de la clase Ethernet.
# La longitud de los campos de Ethernet son como siguen:
# Receiver MAC Address: 6 bytes
# Sender MAC Address: 6 bytes
# Type: 2 bytes

# Ninguno de los campos recibe algún tratamiento de bits. Si acaso el campo "Type" que pasa por htons 
# para realizar un cambio en el orden de los octetos. Si lee 0x0800 para decir que es IPv4 entonces lo 
# cambia a 00 08, es entonces cuando lo podemos interpretar como "8" en decimal.

# Por cierto, entre los protocolos que nos interesan:
# TYPE:
# 	0x0800 = IPv4 						8 en decimal
# 	0x0806 = ARP Request or response 	1,544 en decimal
# 	0x86DD = IPv6						56,710 en decimal

import struct
import socket
import ipv4
import formatFunctions

class Ethernet:
	'Ethernet Frame class'

	def __init__(self, rawData):
		'Unpack ethernet frame'
		
		_recMac, _sendMac, _type = struct.unpack('! 6s 6s H', rawData[ : 14 ])

		self.recMac = formatFunctions.formatMACAddress(_recMac)
		self.sendMac = formatFunctions.formatMACAddress(_sendMac)
		self.protocol = socket.htons(_type)
		self.ethPayload = rawData[ 14 : ]