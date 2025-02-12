def int32_to_ip(int32: int) -> str:
    to_binary = bin(int32)[2:].zfill(32)
    ip= []
    for i in range(8, 33, 8):
       ip.append((str(int(to_binary[i-8:i], 2))))
    return '.'.join(ip)

def with_library(int32: int) -> str:
    import ipaddress
    return str(ipaddress.IPv4Address('192.168.0.264'))

# verify if is a ipV4
def verify_ip(ip: str) -> bool:
    import ipaddress
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError as Error:
        print(Error)
        return False

verify_ip('192.168.0.264')