#!/usr/bin/env python3
import functools
import re
import subprocess
from contextlib import suppress
from pathlib import Path
import yaml

automation_files = sorted(list(Path("automation/").glob("*yaml")))
text = []

for fname in automation_files:
    print(fname)