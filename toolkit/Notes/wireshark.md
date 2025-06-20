# Wireshark Notes

## What is Wireshark?
Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, and protocol development.

## Installation
- On Kali Linux: `sudo apt install wireshark`
- On Ubuntu: `sudo apt install wireshark`
- On Windows/macOS: Download from https://www.wireshark.org/

## Basic Usage
- Start Wireshark and select a network interface to capture packets.
- Stop the capture and analyze the traffic.

## Useful Filters
- Show only HTTP traffic:
  ```
  http
  ```
- Show only traffic to/from an IP:
  ```
  ip.addr == 192.168.1.1
  ```
- Show only TCP traffic:
  ```
  tcp
  ```
- Show only DNS queries:
  ```
  dns
  ```

## Notes / Experiments
- [ ] Capture and analyze your own network traffic
- [ ] Try filtering by protocol or IP
- [ ] Document interesting findings 