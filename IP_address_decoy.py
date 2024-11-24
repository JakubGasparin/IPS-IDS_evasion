from scapy.all import *

payload = "/etc/passwd"
target_ip = "192.168.112.129"
target_port = 80
decoy_ips = ["192.168.1.100", "192.168.1.101", "192.168.1.102"]

for decoy in decoy_ips:
    packet = IP(src=decoy, dst=target_ip) / TCP(dport=target_port, flags="PA") / payload
    send(packet)
