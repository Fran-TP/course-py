def int32_to_ip(int32: int) -> str:
    to_binary = bin(int32)[2:].zfill(32)
    ip= []
    for i in range(8, 32, 9):
        ip.append(str(int(to_binary[i-8:i], 2)))
    return '.'.join(ip)

print(int32_to_ip(2))