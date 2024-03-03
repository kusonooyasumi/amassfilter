import re
import argparse

def extract_fqdns(input_file, output_file):
    # Read input file
    with open(input_file, 'r') as file:
        input_text = file.read()

    # Define regex pattern
    pattern = r'(?:\d+m)?(\w+(\.\w+)*\.trammellcrow\.com)'
    
    # Extract FQDNs
    fqdns = list(set(match.group(1) for match in re.finditer(pattern, input_text)))

    # Write unique FQDNs to the output file
    with open(output_file, 'w') as file:
        for fqdn in fqdns:
            file.write(fqdn + '\n')

if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Extract unique FQDNs ending with "trammellcrow.com" from a text file.')
    parser.add_argument('-f', '--input-file', required=True, help='Input file name')
    parser.add_argument('-o', '--output-file', required=True, help='Output file name')

    # Parse command line arguments
    args = parser.parse_args()

    # Extract unique FQDNs and write to the output file
    extract_fqdns(args.input_file, args.output_file)

    print(f"Unique FQDNs extracted from '{args.input_file}' and saved to '{args.output_file}'.")
