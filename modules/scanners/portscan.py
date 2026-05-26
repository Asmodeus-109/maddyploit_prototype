import socket

class Module:

    def __init__(self):
        pass

    def run(self, target):

        print(f"Scanning {target}")

        common_ports = [21, 22, 23,25,53, 80,110,139, 143, 443, 445, 3306, 3389, 5900, 8080]

        for port in range(1, 1000):

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print(f"[+] Port {port} OPEN")

            s.close()