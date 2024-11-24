from scapy.all import *
import base64

payload = b"/etc/passwd/"
encoded_payload = base64.b64encode(payload).decode()
pkt = IP(dst="192.168.112.129")/TCP(dport=80, flags="PA")/Raw(load=f"GET /?q={encoded_payload} HTTP/1.1\r\nHost: target.com\r\n\r\n")

i = 0
while i < 10:
        send(pkt)
        i=i+1

