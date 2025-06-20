# Metasploit Notes

## What is Metasploit?
Metasploit is a powerful open-source penetration testing framework. It is used for developing, testing, and executing exploits against target systems.

## Installation
- On Kali Linux: Pre-installed
- On Ubuntu: `sudo apt install metasploit-framework`
- On other systems: See https://docs.metasploit.com/docs/using-metasploit/getting-started.html

## Basic Usage
- Start Metasploit console:
  ```
  msfconsole
  ```
- Search for an exploit:
  ```
  search vsftpd
  ```
- Use an exploit module:
  ```
  use exploit/unix/ftp/vsftpd_234_backdoor
  ```
- Set options:
  ```
  set RHOSTS 192.168.1.100
  set RPORT 21
  ```
- Run the exploit:
  ```
  run
  ```

## Useful Commands
- List all exploits:
  ```
  show exploits
  ```
- List all payloads:
  ```
  show payloads
  ```
- Get help:
  ```
  help
  ```

## Notes / Experiments
- [ ] Try exploiting Metasploitable 2 in a VM
- [ ] Document your process and results 