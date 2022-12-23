import json

with open("package.json") as f:
    data = json.load(f)
    dependencies = data["dependencies"]
    for key, value in dependencies.items():
        print(f'          - "{key}@{value}"')
