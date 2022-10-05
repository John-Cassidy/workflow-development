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

print(f"{statusFiles}")