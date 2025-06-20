# Cybersecurity Toolkit

A beginner-friendly Python toolkit for basic cybersecurity tasks. This project is designed to help you learn and practice cybersecurity concepts as you prepare for certifications like CompTIA Security+.

## Features
- **Log Analyzer**: Analyze log files, count lines, and search for keywords (e.g., 'error').
- **Port Scanner**: Scan a target host for open TCP ports in a specified range.

## Getting Started

### Requirements
- Python 3.7+
- No external dependencies required for basic tools

### Usage

#### Log Analyzer
```
python log_analyzer.py /path/to/logfile.log --keyword error
```
- Replace `/path/to/logfile.log` with your log file path.
- Use `--keyword` to search for a specific word (optional).

#### Port Scanner
```
python port_scanner.py 127.0.0.1 --start 1 --end 1024
```
- Replace `127.0.0.1` with the target IP or hostname.
- Use `--start` and `--end` to specify the port range (optional).

## Project Structure
```
toolkit/
  log_analyzer.py
  port_scanner.py
  utils.py
  requirements.txt
  README.md
```

## Expanding the Toolkit
- Add new tools as you learn (e.g., password hash cracker, vulnerability scanner).
- Document your code and findings for each new module.
- Consider adding a unified CLI (`main.py`) in the future.

## Future Modules
- Password Hash Cracker
- Vulnerability Scanner
- Unified CLI Launcher
- GUI Frontend (long-term goal)

---

*Happy learning and hacking!* 