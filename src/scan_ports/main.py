import socket
import threading
import ipaddress
import re


PORT_FILE = 'port_list.txt'
SERVER_PORTS = (80, 443)
IP_RANGE = '185.228.168.9/24'


def get_server(sock, file):
    request = "GET / HTTP/1.1\r\n\r\n"
    sock.send(request.encode())
    response = sock.recv(4096).decode()
    result = re.search('Server:(.*)\r', response).group(1)
    file.write(f'Server:{result}')
    print(f'Server:{result}')


def scan_port(ip, port, file):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        file.write('test')
        connect = s.connect_ex((ip, port))
        print(connect)
        if connect == 0:
            file.write(f'IP:{ip}  port:{port} OPEN')
            print(f'IP:{ip}  port:{port} OPEN')
            if port in SERVER_PORTS:
                get_server(s, file)


if __name__ == '__main__':

    with open(PORT_FILE, 'r', encoding='UTF-8') as port_file, \
            open('output.dat', 'w', encoding='UTF-8') as output_file:

        output_file.truncate(0)
        for port in port_file:
            for ip in ipaddress.ip_network(IP_RANGE, False):
                print(ip, port)
                thread = threading.Thread(target=scan_port,
                                          args=(str(ip), int(port), output_file))
                thread.start()
                thread.join()
