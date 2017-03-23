import struct
import socket
import formatFunctions

class Ethernet:
	'Ethernet Frame class'

	def __init__(self, rawData):
		'Unpack ethernet frame'
		
		_destMac, _srcMac, _type = struct.unpack('! 6s 6s H', rawData[ : 14 ])

		self.destMac = formatFunctions.formatMACAddress(_destMac)
		self.srcMac = formatFunctions.formatMACAddress(_srcMac)
		self.protocol = socket.htons(_type)
		self.ethPayload = rawData[ 14 : ]

	def printEthernetFrame(self):
		'Print a beautiful table of the Ethernet Frame fields'

		