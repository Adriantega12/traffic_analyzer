# IPv4 Header class

# Contiene el desempaquetamiento de la clase IPv4.
# Campos de IPv4 Header:

# - Version: 4 bits
# - Header Length: 4 bits
# - Type of Service: 8 bits
# - Total Length: 16 bits
# - Identification: 16 bits
# - IP Flags: 3 bits (1 para c/u)
# 	- x: Reserved
# 	- D: Do Not Fragment
# 	- M: More moreFragments
# - Fragment Offset: 13 bits
# - Time to Live: 8 bits
# - Protocol: 8 bits
# - Header Checksum: 16 bits
# - Source Address: 32 bits
# - Destination Addres: 32 bits
# - Opciones: Debe pesar la diferencia entre hlen y la suma de todos los otros campos. (HLen - 160)

# Hay mejores soluciones para el tratamiento de bits dado a todo esto. 
# Sobre todo para IP Flags y FragOffset.

# Campos de Protocol implementados
# - ICMP = 0x01
# - TCP = 0x06

import struct
import formatFunctions

class IPv4:
	'IPv4 Packet class'

	def __init__(self, ethPayload):
		'Unpack Ethernet payload in IPv4 Packet'

		self.getVersionAndHeaderLength( ethPayload[0] )
		
		_typeOfService, _totalLength, _id = struct.unpack( '! c H H', ethPayload[1 : 6] ) # Ignora 1, 1, 2, 2
		
		# Toma 2 bytes
		self.getIPFlagsAndOffset( ethPayload[ 6 : 8 ] )

		_timeToLive, _protocol, _headerChecksum, _srcAddress, _destAddress = struct.unpack( 
													'! B B H 4s 4s', ethPayload[ 8 : 20 ] ) # 1, 1, 2, 4, 4
		
		# Guardar todo en un atributo apropiado
		self.typeOfService = _typeOfService
		self.totalLength = _totalLength
		self.id = _id
		self.timeToLive = _timeToLive
		self.protocol = _protocol
		self.headerChecksum = _headerChecksum # Se suma con el complemento a 1 de todos los campos en trozos de 16 bits
		self.srcAddress = formatFunctions.formatIPv4(_srcAddress)
		self.destAddress = formatFunctions.formatIPv4(_destAddress)
		self.ipv4Payload = ethPayload[ self.headerLength : ]

 		# Nota: Los otros campos ya fueron guardados utilizando las funciones de "getXandY"

	def getVersionAndHeaderLength(self, firstByte):
		'Get Version and Header Length from the first byte of the ethernet payload'

		# El campo de Version es de 4 bits de largo y está en el primer byte del payload del ethernet frame.
		# Así que si quieres obtener los primeros 4 bits de este byte, se necesita realizar una rotación a la derecha.
		# Para que de XXXX XXXX quede a manera de 0000 XXXX.
		self.version = firstByte >> 4

		# El HLEN es un campo de 4 bits que está en los últimos bits del primer byte del payload del ethernet frame.
		# Para obtenerlo basta con hacer una puerta and con el número 15. (En binario esto es 0000 1111) 
		# Esto deberá resultar en el valor del HLEN contenido en el primer byte. Se multiplica por 4 porque
		# HLEN representa la cantidad de bytes que mide el encabezado en múltiplos de 4.
		self.headerLength = (firstByte & 15) * 4

	def getIPFlagsAndOffset(self, ethBytes):
		'Get IP Flags and Fragmentation Offset'
 
		# Los IP Flgas y el Frag Offset están contenidos en 2 bytes de información. El primer bit es ignorado
		# por lo que no se captura y ya. La bandera de Do Not Fragment, está ubicada en el segundo bit
		# del primer byte, por lo que lo extraemos con 0100 0000 (128 en decimal); la bandera More moreFragments está
		# en el tercer bit del primer byte.
		self.doNotFragment = (ethBytes[0] & 64) >> 6
		self.moreFragments = (ethBytes[0] & 32) >> 5

		# Todos los bits que restan entre los dos bytes (5 bits del primero y el segundo byte entero) forman
		# el Fragmentation Offset. Este está representado en múltiplos de 8 bytes.
		self.fragOffset = (	( ( ethBytes[0] & 16 ) 	>> 4 ) 	* 4096 
						  + ( ( ethBytes[0] & 8 ) 	>> 3) 	* 2048 
						  + ( ( ethBytes[0] & 4 ) 	>> 2) 	* 1024  
						  + ( ( ethBytes[0] & 2 ) 	>> 1) 	* 512
						  +   ( ethBytes[0] & 1 ) 			* 256
						  + ( ( ethBytes[1] & 128) 	>> 7 ) 	* 128
						  + ( ( ethBytes[1] & 64) 	>> 6 ) 	* 64
						  + ( ( ethBytes[1] & 32) 	>> 5 ) 	* 32
						  + ( ( ethBytes[1] & 16) 	>> 4 ) 	* 16
						  + ( ( ethBytes[1] & 8) 	>> 3 ) 	* 8
						  + ( ( ethBytes[1] & 4) 	>> 2 ) 	* 4
						  + ( ( ethBytes[1] & 2) 	>> 1 ) 	* 2
						  +   ( ethBytes[1] & 1) )

	def getInfo(self):
		info = 'Version: {} HLen: {} ToS: {} TLen: {}\n'.format(
				self.version, self.headerLength, self.typeOfService, self.totalLength)
		info += 'ID: {} IP Flags - D: {} M: {} Fragment Offset: {}\n'.format(
				self.id, self.doNotFragment, self.moreFragments, self.fragOffset)
		info += 'Time to Live: {} Protocol: {} Checksum: {}\n'.format(
				self.timeToLive, self.protocol, self.headerChecksum)
		info += 'Source Address: {}\nDestination Address: {}\n'.format(
				self.srcAddress, self.destAddress)

		return info;