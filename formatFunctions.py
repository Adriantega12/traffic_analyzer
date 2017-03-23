def formatIPv4(address):
	'Return properly formatted IPv4 Address. I.E. 192.168.0.0'
	return '.'.join( map( str, address ) )

def formatMACAddress(address):
	'Format to readable Mac Address'
	rawBytesStr = map('{:02x}'.format, address)		
	return ':'.join(rawBytesStr).upper()