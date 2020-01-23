import ping3

pi_ip = '192.168.1.106'
r = ping3.ping(pi_ip, unit='ms')

print(r)