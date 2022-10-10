import json

repo_name = "workflow-development"
owner = "John-Cassidy"
owner_repo_name = f"{owner}/{repo_name}"

statusFiles = []

statusFiles.append("history/file1.csv")
statusFiles.append("history/file2.csv")
statusFiles.append("history/file3.csv")
statusFiles.append("history/file4.csv")
statusFiles.append("history/file5.csv")

# print(f"::set-output name=statusFiles::{statusFiles}")

target = {39: None, 44: None, 91: None, 93: None}
print(str(statusFiles).translate(target))

# print(f"{statusFiles}")

# print(json.dumps({"statusFiles": statusFiles}))