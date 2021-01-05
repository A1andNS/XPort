import socket


def is_alive(ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((ip, 80))
        s.close()
        return True
    except socket.timeout:
        return False
    except ConnectionRefusedError:
        return True


if __name__ == "__main__":
    is_alive("192.168.3.3")
