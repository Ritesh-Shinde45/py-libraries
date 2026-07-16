import subprocess

opt=subprocess.run(["python", "--version"], capture_output=True, text=True)
print(opt.stdout)
print("Return Code:", opt.returncode)