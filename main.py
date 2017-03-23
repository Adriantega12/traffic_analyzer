import socket
import struct
import textwrap

import ethernet
import ipv4
import arp

def main():
	op = input('¿Iniciar ciclo de captura? (S/N)')
	
	if (op == 'S'):
		conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

		while (op == 'S'):
			rawData, addr = conn.recvfrom(65535)
			eth = ethernet.Ethernet(rawData)
			print ('Ethernet Frame:')
			# print ('Destination MAC: {}\nSource MAC: {} \nProtocol: {}\n'.format(getattr(eth, 'destMac'), getattr(eth, 'srcMac'), getattr(eth, 'protocol')))	
			print(eth.getInfo())

			if (getattr(eth, 'type') == 8):
				'Is IPv4'
				
				ipv4Packet = ipv4.IPv4( getattr(eth, 'ethPayload') )

				print ('IPv4 Datagram:')
				print ('Version: {}, Header Length {}\
					\nType of Service: {},Total Length: {}, ID: {}\
					\nDo Not Fragment: {}, More Fragments {}, Frag Offset: {}\
					\nTime To Live: {}, Protocol: {}, Header Checksum: {}\
					\nSource IP: {} Destination IP: {}\n'.format(
					getattr(ipv4Packet, 'version'), getattr(ipv4Packet, 'headerLength'), 
					getattr(ipv4Packet, 'typeOfService'), getattr(ipv4Packet, 'totalLength'), 
					getattr(ipv4Packet, 'id'), getattr(ipv4Packet, 'doNotFragment'), 
					getattr(ipv4Packet, 'moreFragments'), getattr(ipv4Packet, 'fragOffset'),
					getattr(ipv4Packet, 'timeToLive'), getattr(ipv4Packet, 'protocol'),
					getattr(ipv4Packet, 'headerChecksum'), getattr(ipv4Packet, 'srcAddress'),
					getattr(ipv4Packet, 'destAddress') ) )

			elif (getattr(eth, 'protocol') == 1544):
				'Is ARP'

				arpPacket = arp.ARP( getattr(eth, 'ethPayload') )

				print ('ARP Packet:')
				print ('Hardware Type: {}, Protocol Type: {}\nHardware Length: {}, Protocol Length: {}\
					\nOperation Code: {}\
					\nSender Hardware Address: {}\nSender Protocol Address: {}\
					\nTarget Hardware Address: {}\nTarget Protocol Address: {}\n'.format(
					getattr(arpPacket, 'hardType'), getattr(arpPacket, 'protoType'),
					getattr(arpPacket, 'hardAddrLength'), getattr(arpPacket, 'protoAddrLength'),
					getattr(arpPacket, 'opCode'), getattr(arpPacket, 'srcHardAddr'),
					getattr(arpPacket, 'srcProtoAddr'), getattr(arpPacket, 'targetHardAddr'),
					getattr(arpPacket, 'targetProtoAddr') ) )

main()