import json
import os
import subprocess

output = subprocess.check_output(["gitversion"])
json_output = json.loads(output.decode("utf-8"))

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    for key, value in json_output.items():
        print(f"{key}::{value}", file=file)
