import argparse
import sys
from log_analyzer import analyze_log
from port_scanner import scan_ports

def main():
    parser = argparse.ArgumentParser(description="Cybersecurity Toolkit")
    subparsers = parser.add_subparsers(dest="command", help="Available tools")

    # Log Analyzer
    parser_log = subparsers.add_parser("log", help="Analyze a log file")
    parser_log.add_argument("logfile", help="Path to the log file")
    parser_log.add_argument("--keyword", help="Keyword to search for in the log", default=None)

    # Port Scanner
    parser_scan = subparsers.add_parser("scan", help="Scan open TCP ports on a host")
    parser_scan.add_argument("host", help="Target host (IP or domain)")
    parser_scan.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser_scan.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")

    args = parser.parse_args()

    if args.command == "log":
        analyze_log(args.logfile, args.keyword)
    elif args.command == "scan":
        scan_ports(args.host, args.start, args.end)
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 