import socket  # For network connections

# List of common ports and their typical services
COMMON_PORTS = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    139: 'NetBIOS',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3389: 'RDP',
}

def scan_common_ports(host):
    print(f"Scanning {host} for common vulnerabilities (open ports)...")
    found = False
    for port, service in COMMON_PORTS.items():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} ({service}) is OPEN. Potential risk: {service} service exposed.")
                found = True
    if not found:
        print("No common vulnerable ports found open.")
    else:
        print("\nSecurity Tip: Close unused ports and restrict access to critical services.")

def main():
    host = input("Enter the target host (IP or hostname): ")
    scan_common_ports(host)

if __name__ == '__main__':
    main() 