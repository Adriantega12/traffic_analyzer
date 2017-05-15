import struct

def formatIPv4(address):
	'Get properly formatted IPv4 Address.'
	return '.'.join( map( str, address ) )

def formatIPv6(address):
	'Get properly formatted IPv6 Address.'
	trueAddress = struct.unpack('! H H H H H H H H', address)
	listBytes = list(map('{:04x}'.format, trueAddress))
	i = 0
	for it in listBytes:
		listBytes[i] = cleanSection(it)
		i += 1

	cleanBlocks(listBytes)
	return ':'.join(listBytes)

def cleanSection(section):
	'Clean a section of the IPv6 address (deprepend zeroes)'
	dontIgnore = False

	ret = ''

	for i in section:
		if i != '0':
			ret += i
			dontIgnore = True
		elif dontIgnore:
			ret += i

	if (not dontIgnore):
		ret = '0'

	return ret

def cleanBlocks(listBytes):
	'Clean blocks of zeroes'

	i = 0
	init = 0
	count = 0
	triplets = []
	for it in listBytes:
		if it == '0' and count == 0:
			init = i
		elif it == '0' and count > 0:
			count += 1
		elif it != '0' and count > 0:
			triplets += [[init, i, count]]
			count = 0

		i += 1

	print(triplets)

def formatMACAddress(address):
	'Get properly formatted MAC Address'
	rawBytesStr = map('{:02X}'.format, address)		
	return ':'.join(rawBytesStr)