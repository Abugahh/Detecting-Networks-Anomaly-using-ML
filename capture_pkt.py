# # import pyshark
# # import sys

# # # get the network interface from the command line arguments
# # interface = sys.argv[1]

# # # create a capture object
# # capture = pyshark.LiveCapture(interface=interface)

# # # iterate over captured packets
# # for packet in capture.sniff_continuously():
# #     # print the captured packet
# #     print(packet)


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



# ### save as a script and call that script in my project.ipnb
# ###  see in bing chat straight




# import pyshark
# import threading
# import datetime
# import math

# # specify the network interface to capture packets from
# interface = 'wlan0'

# # create a capture object
# capture = pyshark.LiveCapture(interface=interface)

# # create a dictionary to store the features for each packet
# features = {}

# # create some helper functions to calculate some features

# def get_rate(packet):
#     # get the rate of packets per second
#     # assuming that the packets are ordered by time
#     # rate = 1 / interarrival time
#     global prev_time # keep track of the previous packet time
#     if prev_time is None:
#         # first packet, rate is zero
#         rate = 0
#     else:
#         # calculate the interarrival time in seconds
#         delta = packet.sniff_time - prev_time
#         interarrival = delta.total_seconds()
#         if interarrival == 0:
#             # avoid division by zero, rate is infinity
#             rate = math.inf
#         else:
#             # calculate the rate
#             rate = 1 / interarrival
#     # update the previous packet time
#     prev_time = packet.sniff_time
#     return rate

# def get_smean(packet):
#     # get the mean size of packets sent by source IP address
#     # assuming that the packets are grouped by source IP address
#     global src_size # keep track of the total size of packets sent by source IP address
#     global src_count # keep track of the number of packets sent by source IP address
#     if src_size is None or src_count is None:
#         # first packet, initialize the variables
#         src_size = int(packet.length)
#         src_count = 1
#     else:
#         # update the variables
#         src_size += int(packet.length)
#         src_count += 1
#     # calculate the mean size
#     smean = src_size / src_count
#     return smean

# def get_tcprtt(packet):
#     # get the TCP round trip time (RTT)
#     # assuming that the packets are TCP packets with SYN and ACK flags set
#     global syn_time # keep track of the time when SYN flag is set
#     global ack_time # keep track of the time when ACK flag is set
#     if syn_time is None or ack_time is None:
#         # first packet, initialize the variables
#         syn_time = None
#         ack_time = None
#     # check if SYN flag is set
#     if packet.tcp.flags_syn == '1':
#         # update syn_time with current packet time
#         syn_time = packet.sniff_time
#     # check if ACK flag is set
#     if packet.tcp.flags_ack == '1':
#         # update ack_time with current packet time
#         ack_time = packet.sniff_time
    
#     if syn_time is not None and ack_time is not None:
#         # calculate RTT in seconds as difference between ack_time and syn_time 
#         delta = ack_time - syn_time 
#         tcprtt = delta.total_seconds()
#         # reset syn_time and ack_time for next RTT calculation 
#         syn_time = None 
#         ack_time = None 
#     else: 
#         # RTT cannot be calculated yet 
#         tcprtt = None 
#     return tcprtt

# def capture_packets():
#     # iterate over captured packets 
#     for packet in capture.sniff_continuously(): 
#         # print the captured packet 
#         print(packet) 
        
#         # extract the features from each packet 
#         # check if the packet is a TCP packet
#         if packet.transport_layer == 'TCP':
#             features['dload'] = float(packet.tcp.window_size_value) * 8 / float(packet.tcp.analysis_ack_rtt) * 1000 / 1024 / 1024 
#             features['ct_state_ttl'] = int(packet.ip.ttl) + int(packet.tcp.flags) 
#             features['rate'] = get_rate(packet) 
#             features['sttl'] = int(packet.ip.ttl) 
#             features['sload'] = float(packet.length) * 8 / float(packet.sniff_timestamp) * 1000 / 1024 / 1024 
#             features['dinpkt'] = float(packet.sniff_timestamp) - float(packet.tcp.time_relative) 
#             features['smean'] = get_smean(packet) 
#             features['tcprtt'] = get_tcprtt(packet) 
#             features['state'] = packet.tcp.state 
#             features['dbytes'] = int(packet.ip.len) - int(packet.ip.hdr_len) - int(packet.tcp.hdr_len) 
        
#         # print the features for each packet 
#         print(features)


# # initialize some global variables
# prev_time = None
# src_size = None
# src_count = None
# syn_time = None
# ack_time = None

# # create and start a thread to run the packet capture and processing code
# t = threading.Thread(target=capture_packets)
# t.start()

