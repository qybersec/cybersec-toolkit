import argparse  # For command-line argument parsing
import os  # For file path operations

# Function to analyze a log file
# file_path: path to the log file
# keyword: optional keyword to search for in the log

def analyze_log(file_path, keyword=None):
    if not os.path.isfile(file_path):  # Check if the file exists
        print(f"File not found: {file_path}")
        return
    with open(file_path, 'r') as f:
        lines = f.readlines()  # Read all lines from the log file
    print(f"Total lines in log: {len(lines)}")  # Print total number of lines
    if keyword:
        # Find lines containing the keyword (case-insensitive)
        matches = [line for line in lines if keyword.lower() in line.lower()]
        print(f"Lines containing '{keyword}': {len(matches)}")
        for line in matches:
            print(line.strip())  # Print each matching line

# Main function to handle command-line arguments
def main():
    parser = argparse.ArgumentParser(description='Simple Log Analyzer')
    parser.add_argument('logfile', help='Path to the log file')
    parser.add_argument('--keyword', help='Keyword to search for in the log')
    args = parser.parse_args()
    analyze_log(args.logfile, args.keyword)

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main() 