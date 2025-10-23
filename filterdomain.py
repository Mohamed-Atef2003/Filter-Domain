#!/usr/bin/env python3
"""
FilterDomain - A professional tool for filtering domains from files
Author: GitHub Copilot
Version: 1.0.0
"""

import sys
import argparse
from pathlib import Path


BANNER = r"""
 ____                        _         _____ _ _ _            
|  _ \  ___  _ __ ___   __ _(_)_ __   |  ___(_) | |_ ___ _ __ 
| | | |/ _ \| '_ ` _ \ / _` | | '_ \  | |_  | | | __/ _ \ '__|
| |_| | (_) | | | | | | (_| | | | | | |  _| | | | ||  __/ |   
|____/ \___/|_| |_| |_|\__,_|_|_| |_| |_|   |_|_|\__\___|_|   
                                                               
                    Domain Filter Tool Version 1.0.0
"""


class FilterDomain:
    """Main class for filtering domains"""
    
    def __init__(self, main_file, filter_file, output_file=None, quiet=False):
        self.main_file = Path(main_file)
        self.filter_file = Path(filter_file)
        self.output_file = Path(output_file) if output_file else None
        self.quiet = quiet
        
    def read_file(self, file_path):
        """Read file and return lines as a set"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Read lines, strip whitespace, and ignore empty lines
                lines = {line.strip() for line in f if line.strip()}
            return lines
        except FileNotFoundError:
            print(f"❌ Error: File '{file_path}' not found!", file=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print(f"❌ Error: Permission denied to read '{file_path}'!", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error reading file '{file_path}': {e}", file=sys.stderr)
            sys.exit(1)
    
    def filter_domains(self):
        """Filter domains from main file based on filter file"""
        if not self.quiet:
            print(f"📂 Reading main file: {self.main_file}")
        main_lines = self.read_file(self.main_file)
        if not self.quiet:
            print(f"   ✓ Loaded {len(main_lines)} unique lines")
        
        if not self.quiet:
            print(f"📂 Reading filter file: {self.filter_file}")
        filter_lines = self.read_file(self.filter_file)
        if not self.quiet:
            print(f"   ✓ Loaded {len(filter_lines)} filter patterns")
        
        if not self.quiet:
            print(f"🔍 Filtering domains...")
        # Remove lines that exist in filter file
        filtered_lines = main_lines - filter_lines
        removed_count = len(main_lines) - len(filtered_lines)
        
        if not self.quiet:
            print(f"   ✓ Removed {removed_count} matching lines")
            print(f"   ✓ Remaining: {len(filtered_lines)} lines")
        
        return sorted(filtered_lines)
    
    def write_output(self, filtered_lines):
        """Write filtered lines to output file or stdout"""
        if self.output_file:
            try:
                if not self.quiet:
                    print(f"💾 Writing output to: {self.output_file}")
                with open(self.output_file, 'w', encoding='utf-8') as f:
                    for line in filtered_lines:
                        f.write(f"{line}\n")
                if not self.quiet:
                    print(f"   ✓ Successfully wrote {len(filtered_lines)} lines to {self.output_file}")
            except PermissionError:
                print(f"❌ Error: Permission denied to write to '{self.output_file}'!", file=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print(f"❌ Error writing to file '{self.output_file}': {e}", file=sys.stderr)
                sys.exit(1)
        else:
            if not self.quiet:
                print("\n" + "="*60)
                print("📄 FILTERED RESULTS:")
                print("="*60)
            for line in filtered_lines:
                print(line)
            if not self.quiet:
                print("="*60)
                print(f"Total: {len(filtered_lines)} lines")
    
    def run(self):
        """Execute the filtering process"""
        filtered_lines = self.filter_domains()
        self.write_output(filtered_lines)
        if not self.quiet:
            print("\n✅ Done!")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        prog='filterdomain',
        description=r'''
 ____                        _         _____ _ _ _            
|  _ \  ___  _ __ ___   __ _(_)_ __   |  ___(_) | |_ ___ _ __ 
| | | |/ _ \| '_ ` _ \ / _` | | '_ \  | |_  | | | __/ _ \ '__|
| |_| | (_) | | | | | | (_| | | | | | |  _| | | | ||  __/ |   
|____/ \___/|_| |_| |_|\__,_|_|_| |_| |_|   |_|_|\__\___|_|   

Domain Filter Tool - A professional tool for filtering and cleaning domain lists
Version 1.0.0

DESCRIPTION:
  This tool filters domains/lines from a main file by removing all matching 
  lines found in a filter file. Perfect for cleaning domain lists, removing 
  duplicates, or filtering out unwanted entries.

HOW IT WORKS:
  1. Reads the main file (file1.txt)
  2. Reads the filter file (file2.txt) 
  3. Removes all lines from main file that exist in filter file
  4. Outputs the cleaned result to stdout or saves to a file
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
EXAMPLES:
  Basic usage - Print to screen:
    %(prog)s domains.txt blacklist.txt
    
  Save filtered output to file:
    %(prog)s domains.txt blacklist.txt -o clean_domains.txt
    
  Real world example:
    %(prog)s all_domains.txt spam_domains.txt -o filtered_domains.txt
    
USE CASES:
  • Remove blacklisted domains from a domain list
  • Clean up duplicate entries between two files
  • Filter out unwanted lines from any text file
  • Compare and subtract content between two files

NOTES:
  • Empty lines are automatically ignored
  • Lines are compared after trimming whitespace
  • Duplicate lines in files are automatically handled
  • Output is sorted alphabetically for consistency

AUTHOR:
  Created with GitHub Copilot

For bugs and feature requests, please contact the developer.
        '''
    )
    
    parser.add_argument('main_file', 
                        metavar='MAIN_FILE',
                        help='Main input file to be filtered (e.g., domains.txt)')
    parser.add_argument('filter_file',
                        metavar='FILTER_FILE', 
                        help='Filter file containing lines to remove (e.g., blacklist.txt)')
    parser.add_argument('-o', '--output', 
                        dest='output_file',
                        metavar='OUTPUT_FILE',
                        help='Save output to file instead of printing to stdout')
    parser.add_argument('-q', '--quiet',
                        action='store_true',
                        help='Quiet mode - suppress all messages except errors and results')
    parser.add_argument('-v', '--version', 
                        action='version',
                        version='Domain Filter Tool v1.0.0')
    
    # Show banner if not in quiet mode
    args = parser.parse_args()
    
    if not args.quiet:
        print(BANNER)
    
    # Create and run the filter
    filter_tool = FilterDomain(args.main_file, args.filter_file, args.output_file, args.quiet)
    filter_tool.run()


if __name__ == '__main__':
    main()
