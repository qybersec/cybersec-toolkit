import socket  # For network connections
import argparse  # For command-line argument parsing
import sys

# List of top 20 common ports (can be expanded)
TOP_PORTS = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]

# Function to scan a single TCP port using connect()
def tcp_connect_scan(host, port, verbose=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] TCP Port {port} is open.")
                return True
            elif verbose:
                print(f"[-] TCP Port {port} is closed.")
    except Exception as e:
        if verbose:
            print(f"[!] Error scanning TCP port {port}: {e}")
    return False

# Function to scan a single UDP port (limited, not always reliable)
def udp_scan(host, port, verbose=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(1)
            s.sendto(b"", (host, port))
            try:
                data, _ = s.recvfrom(1024)
                print(f"[+] UDP Port {port} is open or responding.")
                return True
            except socket.timeout:
                if verbose:
                    print(f"[-] UDP Port {port} is open|filtered (no response)")
            except Exception as e:
                if verbose:
                    print(f"[!] Error scanning UDP port {port}: {e}")
    except Exception as e:
        if verbose:
            print(f"[!] Error creating UDP socket for port {port}: {e}")
    return False

# Main scan function
def scan_ports(host, start_port, end_port, verbose=False):
    open_ports = []
    closed_ports = []
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open.")
                open_ports.append(port)
            elif verbose:
                print(f"[-] Port {port} is closed.")
                closed_ports.append(port)
    if not open_ports:
        print("No open ports found in the specified range.")
    return open_ports, closed_ports

# Helper to parse port arguments
def parse_ports(args):
    if args.top:
        return TOP_PORTS
    elif args.ports:
        # Custom list, e.g. "22,80,443" or "20-25"
        ports = []
        for part in args.ports.split(","):
            if "-" in part:
                start, end = part.split("-")
                ports.extend(range(int(start), int(end)+1))
            else:
                ports.append(int(part))
        return ports
    elif args.full:
        return list(range(1, 65536))
    else:
        # Default: 1-1024
        return list(range(1, 1025))

def write_output(filename, host, start_port, end_port, open_ports, closed_ports, verbose):
    with open(filename, 'w') as f:
        f.write(f"Scan results for {host} (ports {start_port}-{end_port}):\n")
        if open_ports:
            f.write("Open ports:\n")
            for port in open_ports:
                f.write(f"  {port}\n")
        else:
            f.write("No open ports found.\n")
        if verbose and closed_ports:
            f.write("Closed ports:\n")
            for port in closed_ports:
                f.write(f"  {port}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Simple TCP Port Scanner\n\n'
        'Examples:\n'
        '  python port_scanner.py 127.0.0.1 --start 20 --end 25\n'
        '  python port_scanner.py 192.168.1.1 --ports 22,80,443\n'
        '  python port_scanner.py scanme.nmap.org --full --type udp\n',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('host', help='Target host to scan (IP or hostname)')
    parser.add_argument('--start', type=int, default=1, help='Start port (default: 1)')
    parser.add_argument('--end', type=int, default=1024, help='End port (default: 1024)')
    parser.add_argument('--ports', help='Comma-separated list or range of ports (e.g., "22,80,443" or "20-25")')
    parser.add_argument('--top', action='store_true', help='Scan top 20 most common ports')
    parser.add_argument('--full', action='store_true', help='Scan all 65535 ports')
    parser.add_argument('--type', choices=['tcp', 'udp'], default='tcp', help='Scan type: tcp (default) or udp')
    parser.add_argument('--verbose', action='store_true', help='Show closed ports')
    parser.add_argument('--output', help='Write results to a file')
    args = parser.parse_args()

    # Determine port list
    if args.start or args.end:
        start = args.start if args.start else 1
        end = args.end if args.end else 1024
        ports = list(range(start, end+1))
    else:
        ports = parse_ports(args)

    open_ports, closed_ports = scan_ports(args.host, args.start, args.end, args.verbose)

    if args.output:
        write_output(args.output, args.host, args.start, args.end, open_ports, closed_ports, args.verbose)
        print(f"Results written to {args.output}")

    # Note: SYN scan (stealth scan) is not possible in pure Python without raw sockets and root/admin privileges.
    # For advanced scans, use nmap (see Notes.md for a cheatsheet).

if __name__ == '__main__':
    main() 