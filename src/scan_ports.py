import socket
import threading


def scan_port(ip, port):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(0.5)
  try:
     connect = sock.connect((ip, port))
     print('Port :', port, ' its open.')
     sock.close()
  except:
     pass


if __name__ == '__main__':
    for port in ():
        thread = threading.Thread(target=scan_port, args=(ip, i))
        thread.start()
        thread.join()