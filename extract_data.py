import zipfile
from pathlib import Path
from subprocess import run

out_path = Path("./sebi_tree_solution")
out_path.mkdir(exist_ok=True)

run(["inv", "get-test-pack"])

with zipfile.ZipFile("pack.zip") as zip_path:
    zip_path.extractall(out_path)
