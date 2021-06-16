from pathlib import Path

path = Path("")

# check existence
print(path.exists())

# make new folder (directory)
# path.mkdir()

# remove new folder (directory)
# path.rmdir()

# find folders/files (directories)
# print(path.glob("*.*"))
for file in path.glob("*"):
    print(file)