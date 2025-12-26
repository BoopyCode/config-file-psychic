#!/usr/bin/env python3
"""
Config File Psychic - Because your config files are hiding secrets from you.
"""

import os
import sys
import json
import configparser
from pathlib import Path

def psychic_read(filepath):
    """Reads config files with psychic powers (or basic parsing)."""
    path = Path(filepath)
    
    if not path.exists():
        return f"Psychic vision: File doesn't exist. Are you editing a dream?"
    
    try:
        content = path.read_text()
    except Exception as e:
        return f"Psychic blocked: {e}"
    
    # The psychic part: guessing what's wrong
    issues = []
    
    # Check 1: Empty file
    if not content.strip():
        issues.append("File is emptier than your promises to document code")
    
    # Check 2: Common syntax issues
    if content.count('{') != content.count('}'):
        issues.append("JSON/object braces don't match. It's like dating, needs balance")
    
    if content.count('[') != content.count(']'):
        issues.append("Array brackets mismatched. Your arrays are escaping")
    
    # Check 3: Suspicious patterns
    if 'localhost' in content and 'production' in content.lower():
        issues.append("Found 'localhost' in 'production' config. Bold strategy!")
    
    if 'password' in content.lower() and '123' in content:
        issues.append("Password contains '123'. Hackers love predictable psychics")
    
    # Check 4: Duplicate sections (INI files)
    if filepath.endswith(('.ini', '.cfg')):
        try:
            parser = configparser.ConfigParser()
            parser.read(filepath)
            sections = parser.sections()
            if len(sections) != len(set(sections)):
                issues.append("Duplicate sections found. Your config is having an identity crisis")
        except:
            pass
    
    # The psychic reading
    if issues:
        reading = f"\n🔮 PSYCHIC READING for {filepath}:\n"
        reading += "=" * 50 + "\n"
        for i, issue in enumerate(issues, 1):
            reading += f"{i}. {issue}\n"
        reading += "=" * 50 + "\n"
        reading += f"File exists: ✓ ({path.stat().st_size} bytes)\n"
        reading += f"First 3 lines:\n"
        for line in content.split('\n')[:3]:
            reading += f"  {line[:80]}\n"
        return reading
    else:
        return f"\n✨ File looks fine! (But I'm only psychic, not perfect)"

def main():
    """Main function - because every script needs one."
    if len(sys.argv) != 2:
        print("Usage: python config_psychic.py <config_file>")
        print("Example: python config_psychic.py ~/project/config.json")
        sys.exit(1)
    
    result = psychic_read(sys.argv[1])
    print(result)

if __name__ == "__main__":
    main()
