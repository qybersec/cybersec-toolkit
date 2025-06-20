# Port Scanner Notes

## Usage Examples

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

## Output to File

Save results to a file:
```
python tools/port_scanner.py 127.0.0.1 --start 20 --end 100 --output results.txt
```

## Notes
- By default, only open ports are shown. Use `--verbose` to see closed ports.
- Use the `--output` option to save results for documentation or reporting. 