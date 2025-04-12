import argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--pyexe')
args = parser.parse_args()
reqs = set([
    'Flask',
    'openpyxl',
    'pandas',
    'selenium'
])

pkgs = subprocess.getoutput("pip freeze").splitlines()
pkgs = {x if x.find("=") == -1 else x[:x.find("=")]  for x in pkgs}
need = reqs-pkgs
print("python exe:",args.pyexe)
if len(need):
    print("Installing missing packages", need)
    args.pyexe
    for n in need:
        if n == "Flask":
            subprocess.run(f"{args.pyexe} -m pip install flask")
        else :
            subprocess.run(f"{args.pyexe} -m pip install {n}")
else:
    print("All necessary packages already installed!")
