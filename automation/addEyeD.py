#!/usr/bin/env python3

import functools
import re
import subprocess
from contextlib import suppress
from pathlib import Path
from collections import Counter
import yaml

def automations_as_dict(fname):
    with fname.open() as f:
        return yaml.load(f, Loader=yaml.BaseLoader)

automation_files = sorted(list(Path("./").glob("*yaml")))

for fname in automation_files:
    automations = automations_as_dict(fname)

    for automation in automations:
        print(automation['alias'])
        automation['id'] = automation['alias']
        # print(automation)
    
    print(yaml.dump(automations))
    exit(0)