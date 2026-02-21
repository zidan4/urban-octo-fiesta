def get_mac(ip_address):
  responses,unanswered = ¬
  srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),¬
  timeout=2,retry=10)
  # return the MAC address from a response
  for s,r in responses:
  return r[Ether].sr
