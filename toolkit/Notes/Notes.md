# Notes

## Documentation Approach
- As your toolkit grows, create a separate notes file for each tool (e.g., nmap_notes.md, port_scanner_notes.md).
- Use these files to document commands, options, and findings for each tool.
- Keep this file for general notes and project-wide information.

## Important Commands

### Log Analyzer
Analyze a log file and search for a keyword:
```
python tools/log_analyzer.py logs/sample.log --keyword error
```

### Port Scanner
Scan localhost for open ports 1-1024 (default):
```
python tools/port_scanner.py 127.0.0.1
```
Scan a custom range:
```
python tools/port_scanner.py 127.0.0.1 --start 20 --end 100
```
Scan top 20 most common ports:
```
python tools/port_scanner.py 127.0.0.1 --top
```
Scan a custom list or range:
```
python tools/port_scanner.py 127.0.0.1 --ports 22,80,443
python tools/port_scanner.py 127.0.0.1 --ports 20-25
```
Scan all 65535 ports:
```
python tools/port_scanner.py 127.0.0.1 --full
```
UDP scan (basic):
```
python tools/port_scanner.py 127.0.0.1 --type udp --ports 53,123
```
Verbose output (show closed ports):
```
python tools/port_scanner.py 127.0.0.1 --top --verbose
```

### Vulnerability Scanner
Scan a host for common vulnerable ports:
```
python tools/vuln_scanner.py
```
(You will be prompted to enter the target host.)

---

## Nmap Cheatsheet (Most Used Commands)

- Quick scan (top 1000 TCP ports):
  ```
  nmap target
  ```
- Scan all ports:
  ```
  nmap -p- target
  ```
- Service/version detection:
  ```
  nmap -sV target
  ```
- OS detection:
  ```
  nmap -O target
  ```
- Aggressive scan (OS, version, script, traceroute):
  ```
  nmap -A target
  ```
- Scan specific ports:
  ```
  nmap -p 22,80,443 target
  ```
- UDP scan:
  ```
  nmap -sU target
  ```
- Save output to file:
  ```
  nmap -oN scan.txt target
  ```
- Stealth SYN scan (requires root):
  ```
  sudo nmap -sS target
  ```
- Top 100 ports:
  ```
  nmap --top-ports 100 target
  ```

Replace `target` with the IP or hostname you want to scan.

 What to Research Next
Hash Cracker: Learn about password hashes (MD5, SHA1, etc.) and how to brute-force or dictionary-attack them.
File Integrity Checker: Compare file hashes to detect tampering.
Network Sniffer: (More advanced) Capture and analyze network packets (e.g., with scapy).
Simple Password Generator: Create strong, random passwords.
Basic Encryption/Decryption: Try out Python's cryptography or hashlib modules.