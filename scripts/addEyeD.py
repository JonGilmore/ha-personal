#!/usr/bin/env python3

import re
from pathlib import Path

pattern = re.compile(r'^(- alias: )(".*: .*")$')
automation_files = sorted(list(Path("./").glob("*yaml")))

for fname in automation_files:
    inputfile = open(fname, 'r').readlines()
    write_file = open(f"new-{fname}",'w')
    for line in inputfile:
        write_file.write(line)
        match = pattern.search(line)
        if match:
            new_line = f"  id: {match.group(2)}"
            write_file.write(new_line + "\n") 
write_file.close()
