# FilterDomain Tool

```
 ____                        _         _____ _ _ _            
|  _ \  ___  _ __ ___   __ _(_)_ __   |  ___(_) | |_ ___ _ __ 
| | | |/ _ \| '_ ` _ \ / _` | | '_ \  | |_  | | | __/ _ \ '__|
| |_| | (_) | | | | | | (_| | | | | | |  _| | | | ||  __/ |   
|____/ \___/|_| |_| |_|\__,_|_|_| |_| |_|   |_|_|\__\___|_|   
```

A professional tool for filtering domains and removing matching lines from files.

## Features

✨ **Easy to Use**: Simple and clear command-line interface  
🚀 **Fast and Efficient**: Uses Sets for optimal performance  
📊 **Detailed Information**: Displays statistics about the filtering process  
💾 **Flexible Output**: Print to screen or save to file  
🛡️ **Error Handling**: Clear and helpful error messages  
🤫 **Quiet Mode**: For scripts and automation  

## Quick Installation

### On Linux

```bash
# Make the file executable
chmod +x filterdomain.py

# Use the tool
./filterdomain.py file1.txt file2.txt -o output.txt

# (Optional) Move to system path
sudo cp filterdomain.py /usr/local/bin/filterdomain
```

### On Windows

```powershell
python filterdomain.py file1.txt file2.txt -o output.txt
```

## Usage

### General Syntax
```bash
filterdomain MAIN_FILE FILTER_FILE [-o OUTPUT_FILE] [-q] [-v] [-h]
```

### Options

| Option | Description |
|--------|-------------|
| `MAIN_FILE` | Main input file to be filtered |
| `FILTER_FILE` | Filter file containing lines to remove |
| `-o, --output` | Save output to file (optional) |
| `-q, --quiet` | Quiet mode - suppress messages and show results only |
| `-v, --version` | Show version number |
| `-h, --help` | Show complete help message |

## Quick Examples

### 1. Print to Screen
```bash
filterdomain domains.txt blacklist.txt
```

### 2. Save to File
```bash
filterdomain domains.txt blacklist.txt -o clean_domains.txt
```

### 3. Quiet Mode (for Scripts)
```bash
filterdomain domains.txt blacklist.txt -q > output.txt
```

## Practical Example

### Content of file1.txt:
```
google.com
facebook.com
youtube.com
twitter.com
instagram.com
linkedin.com
```

### Content of file2.txt:
```
facebook.com
twitter.com
```

### Execution:
```bash
filterdomain file1.txt file2.txt -o file3.txt
```

### Result in file3.txt:
```
google.com
instagram.com
linkedin.com
youtube.com
```

## Complete Help

To view complete instructions and advanced examples:
```bash
filterdomain -h
```

Or read the [Complete Usage Guide](USAGE.md)

## How Does It Work?

1. 📂 Reads the main file (file1)
2. 📂 Reads the filter file (file2)  
3. 🔍 Removes all lines from file2 that exist in file1
4. 💾 Displays or saves the result

## Use Cases

- ✅ Remove blacklisted domains from a list
- ✅ Clean duplicate entries from lists
- ✅ Filter unwanted content
- ✅ Compare and subtract content between two files

## Requirements

- Python 3.6 or higher
- Works on: Linux, macOS, Windows

## Included Files

- `filterdomain.py` - Main program
- `README.md` - This file
- `USAGE.md` - Complete usage guide in Arabic
- `example_file1.txt` - Test file for testing
- `example_file2.txt` - Test filter file

## Test the Program

Try the program with the example files:
```bash
python filterdomain.py example_file1.txt example_file2.txt
```

## Version

**Current Version:** 1.0.0  
**Date:** October 2025

## License

This program is free and open source.

## Developer

Developed with ❤️ using Mo7amed Atef

---

**For Help and Support:**
```bash
filterdomain --help
```

