import os
import subprocess


path = os.getcwd()
remove_original = True if input("remove original epub?(y/n)") == "y" else False

for file in os.listdir(path):
    if file[-5:] == ".epub":
        print(f"processing file {file}")
        name = file[: file.find(".epub")]
        out = subprocess.run(
            ["ebook-convert", file, f"{name}.mobi", "--dont-compress"],
            shell=True,
            capture_output=True,
        )
        (
            (print(f"removing {file}"), os.remove(os.path.join(path, file)))
            if remove_original
            else None,
            print("done."),
        ) if out.returncode == 0 else print("an error has occured.")
