
# import pyshark
# import threading

# # Create a packet capture object (you can choose an interface or read from a file)
# capture = pyshark.LiveCapture(interface='wlan0')  # Replace 'eth0' with your desired interface

# # Process each packet and extract relevant features
# for packet in capture.sniff_continuously():
#     try:
#         dload = float(packet.ip.len)  # Extract total packet length (downlink)
#         ct_state_ttl = int(packet.tcp.flags)  # Extract TCP flags (connection state)
        
#         rate = float(packet.ip.ds_field)  # Extract Differentiated Services (DSCP) field
#         sttl = int(packet.ip.ttl)  # Extract source TTL
#         sload = float(packet.ip.src)  # Extract source IP address (load)
#         dinpkt = int(packet.ip.packets)  # Extract number of incoming packets
#         smean = float(packet.ip.src_port)  # Extract source port (mean)
#         tcprtt = float(packet.tcp.time_relative)  # Extract TCP relative timestamp
#         state = packet.tcp.flags_str  # Extract TCP connection state (e.g., SYN, ACK)
#         dbytes = int(packet.ip.src_oui)  # Extract destination OUI (Organizationally Unique Identifier)

#         # Now use these extracted features for classification
#         # ...
#     except AttributeError:
#         pass  # Skip packets that don't have all required fields

# # Close the capture when done
# # capture.close()

# t = threading.Thread(target=capture_packets)
# t.start()

import pyshark
import threading

# specify the network interface to capture packets from
interface = 'wlan0'

# create a capture object
capture = pyshark.LiveCapture(interface=interface)

syn_time = None  # keep track of the time when SYN flag is set
ack_time = None  # keep track of the time when ACK flag is set

def get_tcprtt(packet):
    global syn_time, ack_time
    if packet.tcp.flags_syn == '1':
        syn_time = packet.sniff_time
    if packet.tcp.flags_ack == '1':
        ack_time = packet.sniff_time
    if syn_time is not None and ack_time is not None:
        delta = ack_time - syn_time 
        tcprtt = delta.total_seconds()
        syn_time = None 
        ack_time = None 
    else: 
        tcprtt = None 
    return tcprtt

def capture_packets():
    # iterate over captured packets
    for packet in capture.sniff_continuously():
        # Extract TCP RTT from packet
        try:
            tcprtt = get_tcprtt(packet)
            if tcprtt is not None:
                print(f'TCP RTT: {tcprtt} seconds')
        except AttributeError:
            pass  # Not all packets will have TCP flags, so we just skip if an attribute is not present

# create and start a thread to run the packet capture and processing code
t = threading.Thread(target=capture_packets)
t.start()
