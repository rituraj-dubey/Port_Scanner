import socket
import termcolor

top = ''' _______  _______  _______ _________     _______  _______  _______  _        _        _______  _______ 
(  ____ )(  ___  )(  ____ )\__   __/    (  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )
| (    )|| (   ) || (    )|   ) (       | (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|
| (____)|| |   | || (____)|   | |       | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|
|  _____)| |   | ||     __)   | |       (_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)
| (      | |   | || (\ (      | |             ) || |      | (   ) || | \   || | \   || (      | (\ (   
| )      | (___) || ) \ \__   | |       /\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__
|/       (_______)|/   \__/   )_(       \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/'''
print('\n')
print(termcolor.colored((top), 'blue'),"\n")
print()


def scan(target, ports):
	print('\n' + termcolor.colored((' Starting Scan For ' + str(target)), 'green'))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ipaddress, port):
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan: ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
	print('\n' + termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
elif ' ' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(' '):
		scan(ip_addr.strip(' '),ports)
else:
	scan(targets,ports)
