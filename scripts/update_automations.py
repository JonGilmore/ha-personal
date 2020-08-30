#!/usr/bin/env python3

#  _   _ ____  ____    _  _____ _____   ____  _____    _    ____  __  __ _____
# | | | |  _ \|  _ \  / \|_   _| ____| |  _ \| ____|  / \  |  _ \|  \/  | ____|
# | | | | |_) | | | |/ _ \ | | |  _|   | |_) |  _|   / _ \ | | | | |\/| |  _|
# | |_| |  __/| |_| / ___ \| | | |___  |  _ <| |___ / ___ \| |_| | |  | | |___
#  \___/|_|   |____/_/   \_\_| |_____| |_| \_\_____/_/   \_\____/|_|  |_|_____|
#
# - from github.com/basnijholt/home-assistant-config

# Run this script from the main repo root!
# It updates the table of devices and the list of automations.
# This code relies on the way I have structeded my files and named my automations.

# XXX: note that "security-%EF%B8%8F" is the anchor...

import functools
import re
import subprocess
from contextlib import suppress
from pathlib import Path

import yaml

from _readme_tables import html_table

URL = "https://github.com/jongilmore/ha-personal/blob/{commit_hash}/{fname}"


# @functools.lru_cache()
# def git_revision_hash():
#     """Get the git hash to save with data to ensure reproducibility."""
#     git_output = subprocess.check_output(["git", "rev-parse", "HEAD"])
#     return git_output.decode("utf-8").replace("\n", "")


@functools.lru_cache()
def git_latest_edit_hash(fname):
    """Get the git hash to save with data to ensure reproducibility."""
    git_output = subprocess.check_output(
        ["git", "rev-list", "-1", "master", str(fname)]
    )
    return git_output.decode("utf-8").replace("\n", "")


def line_number(fname, text, regex_check):
    assert isinstance(text, str)
    with fname.open() as f:
        for i, line in enumerate(f):
            if text in line:
                if regex_check and re.search(fr"\b{text}", line) is None:
                    break
                return i + 1
    raise ValueError(f"Text ({text}) doesn't exist in file {fname}.")


def permalink(fname):
    return URL.format(commit_hash=git_latest_edit_hash(fname), fname=fname)


def permalink_automation(fname, automation):
    from_line = line_number(fname, automation["alias"], False)
    return permalink(fname) + f"#L{from_line}"


def permalink_entity(x, yaml_fname):
    domain, name = x.split(".")
    fname = Path(yaml_fname or f"includes/{domain}s.yaml")
    from_line = line_number(fname, f"{name}:", True)
    return permalink(fname) + f"#L{from_line}"


def title_and_summary(automation):
    title, summary = automation["alias"].split(": ")
    # emoji = get_emoji(title.strip())
    # title = f"{title} {emoji}"
    summary = summary[0].upper() + summary[1:]
    return title, summary


def automations_as_dict(fname):
    with fname.open() as f:
        # return yaml.safe_load(f)
        return yaml.load(f, Loader=yaml.BaseLoader)


def find_inputs(s):
    pattern = "(input_(select|boolean|number|datetime|text)[.][a-z0-9_]+)"
    return {groups[0] for groups in re.findall(pattern, s)}


def find_entities(s, domain):
    pattern = f"({domain}[.][a-z0-9_]+)"
    return {groups for groups in re.findall(pattern, s)}


def get_dependencies(automation):
    deps = []
    inputs = find_inputs(str(automation))
    for input_entity in sorted(inputs):
        with suppress(ValueError):
            url = permalink_entity(input_entity, None)
            s = f"  - [{input_entity}]({url})"
            deps.append(s)

    for domain, yaml_file in [
        ("alert", "includes/alerts.yaml"),
        ("binary_sensor", "includes/binary_sensors.yaml"),
        ("camera", "includes/cameras.yaml"),
        ("climate", "includes/climate.yaml"),
        ("cover", "includes/covers.yaml"),
        ("fan", "includes/fans.yaml"),
        ("group", "includes/groups.yaml"),
        ("input_boolean", "includes/input_booleans.yaml"),
        ("rest_command", "includes/rest_commands.yaml"),
        ("script", "includes/scripts.yaml"),
        ("sensor", "includes/sensors.yaml"),
        ("shell_command", "includes/shell_commands.yaml"),
        ("switch", "includes/switches.yaml"),
        ("timer", "includes/timers.yaml"),
        ("zone", "includes/zones.yaml"),
    ]:
        entities = find_entities(str(automation), domain)
        for entity in sorted(entities):
            with suppress(ValueError):
                url = permalink_entity(entity, yaml_file)
                s = f"  - [{entity}]({url})"
                deps.append(s)

    text = "\n".join(deps)
    if deps:
        text = "  *which uses:*\n" + text + "\n"
    return text


def toc_entry(automations):
    title, _ = title_and_summary(automations[0])
    return f"1. [{title}](#{slugify(title)}) ({len(automations)} automations)"


def get_header(fname, automation):
    title, _ = title_and_summary(automation)
    return f"## [{title}]({permalink(fname)})"


def get_automation_line(fname, automation):
    _, summary = title_and_summary(automation)
    return f"### [{summary}]({permalink_automation(fname, automation)})"


def slugify(s):
    return s.lower().strip().replace(" ", "-").encode("ascii", "ignore").decode("ascii")


def get_description(automation):
    if "description" not in automation:
        return ""
    desc = automation["description"]
    return "\n  " + desc + "\n"


def remove_text(content, start, end):
    do_append = True
    new = []
    for line in content:
        if end in line:
            do_append = not do_append
        if do_append:
            new.append(line)
        if start in line:
            do_append = not do_append
    return new


# def get_emoji(title):
#     return {
#         "Alarm clock": "⏰",
#         "Apple Watch": "⌚️",
#         "Arriving": "👞",
#         "Climate": "🔥🥶",
#         "Control switches": "🎛",
#         "Cube": "∛",
#         "Doorbell": "🚪🔔",
#         "Frontend": "👨‍💻",
#         "KEF DSP": "🔈🎛",
#         "Leaving": "👞",
#         "Light": "💡",
#         "Lovelace": "👨‍💻",
#         "LSX": "🔈",
#         "Media player": "🔈📺",
#         "Music": "🎵",
#         "Night mode": "🌕🌑",
#         "Plant": "☘️",
#         "Rhasspy": "🤖",
#         "Security": "👮‍♂️🚨",
#         "System": "🖥",
#         "Utilities": "🧺👚🍽",
#         "Vacation mode": "🏝",
#         "Vacuum": "🧹",
#         "Work": "💼",
#     }[title]


def modify_lines(to_insert, lines, tag):
    MARKDOWN_COMMENT = "<!-- {} -->"
    start = MARKDOWN_COMMENT.format(f"start-{tag}")
    end = MARKDOWN_COMMENT.format(f"end-{tag}")
    new_lines = remove_text(lines, start, end)
    i = next((i for (i, line) in enumerate(new_lines) if start in line)) + 1
    return new_lines[:i] + [s + "\n" for s in to_insert] + new_lines[i:]


automation_files = sorted(list(Path("automation/").glob("*yaml")))
text = []

# Create TOC
toc_title = "Automations - Table of Content"
text.append(f"# {toc_title}")
total_automations = 0
for fname in automation_files:
    automations = automations_as_dict(fname)
    total_automations += len(automations)
    text.append(toc_entry(automations))
text.append("\n")
text.append(f"⚠️ Total number of automations: **{total_automations}** ⚠️\n")
back_to_toc = f"[^ toc](#{slugify(toc_title)})"

# List automations
for fname in automation_files:
    automations = automations_as_dict(fname)
    text.append(get_header(fname, automations[0]))
    for automation in automations:
        text.append(get_automation_line(fname, automation))
        text.append(get_description(automation))
        text.append(get_dependencies(automation))
    text.append(back_to_toc)
    text.append("\n")

# Modify automations.md
with open("automations.md") as f:
    lines = f.readlines()

lines = modify_lines(text, lines, "automations")
lines = modify_lines(html_table.split("\n"), lines, "table")

with open("automations.md", "w") as f:
    f.write("".join(lines))
