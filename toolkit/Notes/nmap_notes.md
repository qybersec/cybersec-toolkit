# Nmap Notes

## Example Command

```
nmap -sS -sV -O -T4 -Pn <target>
```

### Option Breakdown
- `-sS` : SYN scan (stealth scan, requires root/admin)
- `-sV` : Service/version detection (finds out what service/version is running on open ports)
- `-O`  : OS detection (tries to determine the operating system)
- `-T4` : Timing template (T4 is faster, but more detectable; T0 is slowest/stealthiest)
- `-Pn` : No ping (skip host discovery, treat all hosts as online)
- `<target>` : The IP address or hostname you want to scan

## Other Useful Nmap Options

- `-p <ports>` : Scan specific ports (e.g., `-p 22,80,443` or `-p 1-1000`)
- `-A` : Aggressive scan (enables OS detection, version detection, script scanning, and traceroute)
- `-sU` : UDP scan
- `-oN <file>` : Output results to a normal text file
- `-oX <file>` : Output results to XML file
- `-v` : Increase verbosity (can use `-vv` for even more)
- `--top-ports <N>` : Scan the top N most common ports
- `-F` : Fast scan (scans fewer ports)

## Example Scans

- Quick scan (top 1000 TCP ports):
  ```
  nmap <target>
  ```
- Full TCP port scan:
  ```
  nmap -p- <target>
  ```
- UDP scan:
  ```
  nmap -sU <target>
  ```
- Aggressive scan:
  ```
  nmap -A <target>
  ```
- Save output to file:
  ```
  nmap -oN scan.txt <target>
  ```

Replace `<target>` with the IP or hostname you want to scan. 