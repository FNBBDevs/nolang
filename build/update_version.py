import sys
import re

if len(sys.argv) != 2:
    print("""Problem with argument.\n
             Expected exactly one argument with new version number - e.g. '0.0.0'""")
    exit(1)

new_version = sys.argv[1]

if re.match(r"[0-9]+\.[0-9]+\.[0-9]+", new_version) == None:
    print("Wrong format of argument:", new_version,
          "\nRequired format: 0.0.0.0")
    exit(1)

"""
Update the version.yml file to change the version number
"""
with open(r"D:\a\nolang\nolang\build\version.yml", "r", encoding="utf8") as version_file:
    version_file_lines = version_file.readlines()
    version_file_lines[0] = f"Version: {new_version}\n"

with open(r"D:\a\nolang\nolang\build\version.yml", "w", encoding="utf8") as version_file:
    version_file.writelines(version_file_lines)

"""
Update the nolang.py file to change the version number
"""
with open(r"D:\a\nolang\nolang\nolang.py",  "r", encoding="utf8") as nolang_file:
    lines = nolang_file.readlines()
    for idx, line in enumerate(lines):
        if line[:2] == "__":
            line = line.split(" ")
            line[2] = f"\"{new_version}\""
            line = " ".join(line)
            lines[idx] = line+"\n"
            break
with open(r"D:\a\nolang\nolang\nolang.py", "w", encoding="utf8") as nolang_file:
    nolang_file.writelines(lines)
