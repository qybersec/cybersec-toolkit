import subprocess
import argparse

# Simple nmap scanner using subprocess

def run_nmap_scan(target, options, output):
    # Build the nmap command
    cmd = ["nmap"] + options.split() + [target]
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if output:
            with open(output, 'w') as f:
                f.write(result.stdout)
            print(f"Results saved to {output}")
    except subprocess.CalledProcessError as e:
        print("Error running nmap:")
        print(e.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run an nmap scan from Python.")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--options", default="-sS -T4", help="Nmap options (default: '-sS -T4')")
    parser.add_argument("--output", help="File to save nmap output")
    args = parser.parse_args()

    run_nmap_scan(args.target, args.options, args.output) 