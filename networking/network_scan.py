import socket
import threading
import requests

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

def scan_ip(ip, port, results, lock):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            # Try to get device name
            try:
                r = requests.get(f"http://{ip}:{port}/whoami", timeout=0.5)
                device_name = r.json().get('device_name', ip)
            except Exception:
                device_name = ip
            with lock:
                results.append({'ip': ip, 'device_name': device_name})
    except Exception:
        pass

def scan_network_for_servers(port=5000, subnet=None):
    local_ip = get_local_ip()
    if subnet is None:
        subnet = '.'.join(local_ip.split('.')[:3])
    threads = []
    results = []
    lock = threading.Lock()
    for i in range(1, 255):
        ip = f"{subnet}.{i}"
        t = threading.Thread(target=scan_ip, args=(ip, port, results, lock))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return results  # List of dicts: {'ip': ..., 'device_name': ...}