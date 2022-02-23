import pyshark

capture = pyshark.LiveCapture(interface='en0')
capture.sniff(packet_count=5)
for packet in capture:
    print(packet)


#abc