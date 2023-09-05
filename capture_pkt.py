# import pyshark
# import sys

# # get the network interface from the command line arguments
# interface = sys.argv[1]

# # create a capture object
# capture = pyshark.LiveCapture(interface=interface)

# # iterate over captured packets
# for packet in capture.sniff_continuously():
#     # print the captured packet
#     print(packet)


import pyshark
import threading

# specify the network interface to capture packets from
interface = 'wlan0'

# create a capture object
capture = pyshark.LiveCapture(interface=interface)

def capture_packets():
    # iterate over captured packets
    for packet in capture.sniff_continuously():
        # print the captured packet
        print(packet)

# create and start a thread to run the packet capture and processing code
t = threading.Thread(target=capture_packets)
t.start()



### save as a script and call that script in my project.ipnb
###  see in bing chat straight