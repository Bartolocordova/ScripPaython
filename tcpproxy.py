import sys
import socket
import threading

HEX_FILTER = ''.join(
    [(len(repr(chr(1))) == 3) and chr(1) or '.' for i in range(256)])

def hexdump(src, length=16, show=True):
    if isinstance(src. bytes):
        src= src.decoede()
    results = list()
    for i in range(0, len(src), length):
        word= str(src[i:i+length])
        printable = word.translate(HEX_FILTER)
        hexa = ''.join([f'{ord(c):02X}' for c in word])
        hexwitdh = length*3
        results.append(f'{i:04x}{hexa<{hexwitdh}} {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results

def receive_from(connection):
    buffer = b""
    connection.settimeout(10)
    try:
        while True:
            data = connection.recv(4096)
            if not data:
                break

            buffer += data
    except Exception as e:
        print('error',e)
        pass

    return buffer

    def request_handler(buffer):
        # pefrorm packet modifications (e.g. fuzzinf, testing for auth issues, finding creds, etc.)
        return buffer
    
    def response_handler(buffer):
         # pefrorm packet modifications (e.g. fuzzinf, testing for auth issues, finding creds, etc.)
         return buffer
    
    # def proxy_handler(client_socket, remote_host, remote_port, receive_first):     
    
    # def server_loop(local_host, local_port, remote_host, remote_port, receive_first)

    def main():
        if len(sys.argv[1:]) != 5:
            print("Usage: ./proxy.py [Localhost] [localport]", end='')
            print("[remotehost] [remoteport] [receivefirst]")
            print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
            sys.exit(0)
        
        local_host = sys.argv[1]
        local_port = int(sys.argv[2])

        remote_host = sys.argv[3]
        remote_port = int(sys.argv[4])

        receive_first = sys.argv[5]

        if "True" in receive_first:
                receive_first = True
        else:
                receive_first = Fals

        Server_loop(local_host, local_port, remote_host, remote_port, receive_first)        
        
        if __name__ == '__main__':
           main()