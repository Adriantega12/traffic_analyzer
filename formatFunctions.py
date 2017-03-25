def formatIPv4(address):
	'Get properly formatted IPv4 Address.'
	return '.'.join( map( str, address ) )

def formatIPv6(address):
	'Get properly formatted IPv6 Address.'
	rawBytesStr = map('{:02x}'.format, address)	
	return ':'.join(rawBytesStr).upper()

def formatMACAddress(address):
	'Get properly formatted MAC Address'
	rawBytesStr = map('{:02x}'.format, address)		
	return ':'.join(rawBytesStr).upper()