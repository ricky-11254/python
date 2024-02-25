import telnetlib
import time

host = '192.168.56.2 24'
username = 'ricky'
password = '1234'

tn = telnetlib.Telnet(host)

tn.read_until(b"Username:")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password:")
tn.write(password.encode('ascii')+b"\n")
time.sleep(1)
tn.write(b'system-view\n')
time.sleep(1)
tn.write(b' interface GigabitEthernet0/0/1 \n')
tn.write(b'ip add 192.168.56.2 24 \n')
tn.write(b'dis ip int br \n')
tn.write(b'vlan batch 10 to 20 \n')
tn.write(b'sysname Router \n')
tn.write(b'display this \n')
