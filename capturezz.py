# import pyshark
# import threading

# # specify the network interface to capture packets from
# interface = 'wlan0'

# # create a capture object
# capture = pyshark.LiveCapture(interface=interface)

# def capture_packets():
#     # iterate over captured packets
#     for packet in capture.sniff_continuously():
#         # print the captured packet
#         print(packet)
        
#         # Extract features from packet
#         try:
#             dload = packet.ip.len  # Assuming 'dload' refers to IP datagram length
#             ct_state_ttl = packet.ip.ttl  # TTL value from IP header
#             rate = None  # This might need additional processing based on your specific requirements
#             sttl = packet.ip.ttl  # TTL value from IP header
#             sload = None  # This might need additional processing based on your specific requirements
#             dinpkt = None  # This might need additional processing based on your specific requirements
#             smean = None  # This might need additional processing based on your specific requirements
#             tcprtt = packet.tcp.analysis.ack_rtt if hasattr(packet.tcp, 'analysis') else None  # TCP round-trip time
#             state = packet.tcp.flags.syn == '1' and packet.tcp.flags.ack == '1'  # Check if it's a SYN-ACK packet
#             dbytes = len(packet.data.data) if hasattr(packet, 'data') else 0  # Data bytes size
            
#             print(f'dload: {dload}, ct_state_ttl: {ct_state_ttl}, rate: {rate}, sttl: {sttl}, sload: {sload}, dinpkt: {dinpkt}, smean: {smean}, tcprtt: {tcprtt}, state: {state}, dbytes: {dbytes}')
            
#         except AttributeError:
#             pass  # Not all packets will have all attributes, so we just skip if an attribute is not present

# # create and start a thread to run the packet capture and processing code
# t = threading.Thread(target=capture_packets)
# t.start()



# import pyshark
# import threading

# # specify the network interface to capture packets from
# interface = 'wlan0'

# # create a capture object
# capture = pyshark.LiveCapture(interface=interface)

# def capture_packets():
#     # iterate over captured packets
#     for packet in capture.sniff_continuously():
#         # Extract features from packet
#         try:
#             dload = packet.ip.len  # Assuming 'dload' refers to IP datagram length
#             ct_state_ttl = packet.ip.ttl  # TTL value from IP header
#             rate = None  # This might need additional processing based on your specific requirements
#             sttl = packet.ip.ttl  # TTL value from IP header
#             sload = None  # This might need additional processing based on your specific requirements
#             dinpkt = None  # This might need additional processing based on your specific requirements
#             smean = None  # This might need additional processing based on your specific requirements
#             tcprtt = packet.tcp.analysis.ack_rtt if hasattr(packet.tcp, 'analysis') else None  # TCP round-trip time
#             state = packet.tcp.flags.syn == '1' and packet.tcp.flags.ack == '1'  # Check if it's a SYN-ACK packet
#             dbytes = len(packet.data.data) if hasattr(packet, 'data') else 0  # Data bytes size
            
#             print(f'dload: {dload}, ct_state_ttl: {ct_state_ttl}, rate: {rate}, sttl: {sttl}, sload: {sload}, dinpkt: {dinpkt}, smean: {smean}, tcprtt: {tcprtt}, state: {state}, dbytes: {dbytes}')
            
#         except AttributeError:
#             pass  # Not all packets will have all attributes, so we just skip if an attribute is not present

# # create and start a thread to run the packet capture and processing code
# t = threading.Thread(target=capture_packets)
# t.start()





import pyshark
import threading

# Create a packet capture object (you can choose an interface or read from a file)
capture = pyshark.LiveCapture(interface='wlan0')  # Replace 'eth0' with your desired interface

# Process each packet and extract relevant features
for packet in capture.sniff_continuously():
    try:
        dload = float(packet.ip.len)  # Extract total packet length (downlink)
        ct_state_ttl = int(packet.tcp.flags)  # Extract TCP flags (connection state)
        
        rate = float(packet.ip.ds_field)  # Extract Differentiated Services (DSCP) field
        sttl = int(packet.ip.ttl)  # Extract source TTL
        sload = float(packet.ip.src)  # Extract source IP address (load)
        dinpkt = int(packet.ip.packets)  # Extract number of incoming packets
        smean = float(packet.ip.src_port)  # Extract source port (mean)
        tcprtt = float(packet.tcp.time_relative)  # Extract TCP relative timestamp
        state = packet.tcp.flags_str  # Extract TCP connection state (e.g., SYN, ACK)
        dbytes = int(packet.ip.src_oui)  # Extract destination OUI (Organizationally Unique Identifier)

        # Now use these extracted features for classification
        # ...
    except AttributeError:
        pass  # Skip packets that don't have all required fields

# Close the capture when done
# capture.close()

t = threading.Thread(target=capture_packets)
t.start()
