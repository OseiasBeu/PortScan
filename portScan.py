import socket 
import sys 
menu = "\n"
def scanner(ip,menu):
    print(menu+'[WARNING] - Scan Iniciado!\n\n')
    if 'https' in 'http' in ip:
        sobre_ip = ip.strip('https:/')
        ip = socket.gethostbyname(sobre_ip)
        
    for ports in range(0,3306):
        portas_encontradas = []
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP
        client.settimeout(0.03)
        code =client.connect_ex((ip,ports))
        if code == 0:
            portas_encontradas.append(ports)
            print("[STATUS] - Porta %s ABERTA! \n"%ports)
        else:
            pass
    print("[=>] Scan Finished! \n\n")
    print("[!] Total Portas [ABERTAS] - %s"%portas_encontradas)
    
if len(sys.argv) < 2:
    print("\nModo de uso:\n py portScan.py 127.0.0.1\n\n#############")
else:
    ip = sys.argv[1]
    scanner(ip,menu)
    