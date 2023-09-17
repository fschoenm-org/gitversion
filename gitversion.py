import json
import os
import subprocess
import sys

output = subprocess.check_output(["gitversion", sys.argv[1]])
json_output = json.loads(output.decode("utf-8"))

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    for key, value in json_output.items():
        print(f"{key}::{value}", file=file)
