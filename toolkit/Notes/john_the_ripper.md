# John the Ripper Notes

## What is John the Ripper?
John the Ripper ("John") is a popular open-source password cracking tool. It can crack password hashes using dictionary attacks, brute force, and other methods.

## Installation
- On Kali Linux: `sudo apt install john`
- On Ubuntu: `sudo apt install john`
- On other systems: See https://www.openwall.com/john/

## Basic Usage
- Crack a simple password hash file:
  ```
  john hashes.txt
  ```
- Show cracked passwords:
  ```
  john --show hashes.txt
  ```

## Useful Commands
- List supported hash types:
  ```
  john --list=formats
  ```
- Use a custom wordlist:
  ```
  john --wordlist=rockyou.txt hashes.txt
  ```
- Incremental (brute force) mode:
  ```
  john --incremental hashes.txt
  ```

## Notes / Experiments
- [ ] Try cracking a sample hash file
- [ ] Document your findings and any errors 