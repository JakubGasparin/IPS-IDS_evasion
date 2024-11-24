pkt1 = IP(dst="192.168.112.129", id=111, frag=0, flags=1)/TCP(dport=80, flags="S")
pkt2 = IP(dst="192.168.112.129", id=111, frag=2, flags=0)/Raw(load="/etc/passwd")
send(pkt1)
send(pkt2)
