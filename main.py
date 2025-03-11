import subprocess

if(!ScadInstalled()):
  return 1

def executeScad(scadFile):
  subprocess.run(["openscad"])
  return True