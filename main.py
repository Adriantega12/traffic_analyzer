import socket
import struct
import textwrap
import signal
import sys

import ethernet
import ipv4
import icmpv4
import ipv6
import icmpv6
import arp
import tcp
import udp

etherFrameCount = 0
ipv4Count = 0
ipv6Count = 0
icmpv4Count = 0
icmpv6Count = 0
arpMsgCount = 0
tcpSegCount = 0
udpSegCount = 0

def signal_handler(signal, frame):
	print ("\nSe capturaron:\n Ethernet Frames: {}\nIPv4 Packets: {}\nIPv6 Packets: {}\nICMPv4 Packets: {}\nICMPv6 Packets: {}\nARP Message: {}\nTCP Segments: {}\nUDP Segments: {}\n".format(
			etherFrameCount, ipv4Count, ipv6Count, icmpv4Count, icmpv6Count, arpMsgCount, tcpSegCount, udpSegCount))
	sys.exit(0)

#def main():
op = input('¿Iniciar ciclo de captura? (S/N) ')
	
if (op == 'S'):
	conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

	while (op == 'S'):

		printable = ""

		rawData, addr = conn.recvfrom(65535)
		eth = ethernet.Ethernet(rawData)

		etherFrameCount += 1

		printable += "\033[93mReciever MAC:\033[0m {} \033[93mSender MAC:\033[0m {}\n".format(
		eth.recMac, eth.sendMac)
		if (getattr(eth, 'type') == 8):
			'Is IPv4'
			ipv4Packet = ipv4.IPv4( getattr(eth, 'ethPayload') )

			ipv4Count += 1

			printable += '\033[92mSource IP:\033[0m {} \033[92mDestination IP:\033[0m {}\n'.format(
				ipv4Packet.srcAddress, ipv4Packet.destAddress)

			if (getattr(ipv4Packet, 'protocol') == 1):
				'Is ICMPv4'
				icmpv4Packet = icmpv4.ICMPv4( getattr(ipv4Packet, 'ipv4Payload') )

				icmpv4Count += 1
					
				printable += "\033[95mICMP Message Code:\033[0m {}".format(icmpv4Packet.code)

			elif (getattr(ipv4Packet, 'protocol') == 6):
				'Is TCP'
				tcpSegment = tcp.TCP( getattr(ipv4Packet, 'ipv4Payload') )

				tcpSegCount += 1
					
				printable += "\033[91mTCP: Source Port:\033[0m {} \033[91mDestination Port:\033[0m {}".format(
							tcpSegment.srcPort, tcpSegment.destPort)

			elif (getattr(ipv4Packet, 'protocol') == 17):
				'Is UDP'
				udpSegment = udp.UDP( getattr(ipv4Packet, 'ipv4Payload') )

				udpSegCount += 1
					
				printable += "\033[96mUDP: Source Port:\033[0m {} \033[96mDestination Port:\033[0m {}".format(
					udpSegment.srcPort, udpSegment.destPort)

		elif (getattr(eth, 'type') == 1544):
			'Is ARP'
			arpPacket = arp.ARP( getattr(eth, 'ethPayload') )
			arpMsgCount += 1
				
			printable += "\033[95mARP Message: Operation Code:\033[0m {} \033[95mMessage:\033[0m {}\n".format(
				arpPacket.opCode, arpPacket.getMessage())
			printable += "\033[95mSource HDW:\033[0m {} \033[95mTarget HDW:\033[0m {}\n".format(
				arpPacket.srcHardAddr, arpPacket.targetHardAddr)
			printable += "\033[95mSource Protocol Address:\033[0m {} \033[95mTarget Protocol Address:\033[0m {}".format(
				arpPacket.srcProtoAddr, arpPacket.targetProtoAddr)

		elif (getattr(eth, 'type') == 56710):
			'Is IPv6'
			ipv6Packet = ipv6.IPv6( getattr(eth, 'ethPayload') )

			ipv6Count += 1
				
			printable += "\033[94mSource IP:\033[0m {} \033[94mDestination IP:\033[0m {}\n".format(
					ipv6Packet.sourceAddress, ipv6Packet.destinationAddress
					)

			if (getattr(ipv6Packet, 'nextHeader') == 58):
				'Is ICMPv6'
				icmpv6Packet = icmpv6.ICMPv6( getattr(ipv6Packet, 'ipv6Payload') )

				icmpv6Count += 1
					
				printable += "\033[95mICMP Message Code:\033[0m {}".format(icmpv6Packet.code)

			elif (getattr(ipv6Packet, 'nextHeader') == 6):
				'Is TCP'
				tcpSegment = tcp.TCP( getattr(ipv6Packet, 'ipv6Payload') )

				tcpSegCount += 1
					
				printable += "TCP: Source Port: {} Destination Port: {}".format(
					tcpSegment.srcPort, tcpSegment.destPort)

			elif (getattr(ipv6Packet, 'nextHeader') == 17):
				'Is UDP'
				udpSegment = udp.UDP( getattr(ipv6Packet, 'ipv6Payload') )

				udpSegCount += 1
					
				printable += "UDP: Source Port: {} Destination Port: {}".format(
					udpSegment.srcPort, udpSegment.destPort)

		printable += '\n'
		print(printable)

		signal.signal(signal.SIGINT, signal_handler)