import socket
import threading

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def scan_ip(ip, port, results):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, port))
        if result == 0:
            results.append(ip)
        sock.close()
    except Exception:
        pass

def scan_network_for_servers(port=5000, subnet=None):
    local_ip = get_local_ip()
    if subnet is None:
        subnet = '.'.join(local_ip.split('.')[:3])
    threads = []
    results = []
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        t = threading.Thread(target=scan_ip, args=(ip, port, results))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return results