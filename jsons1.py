import subprocess
from json import dumps

x = input()

out  = subprocess.getstatusoutput(x)
status = out[0]
output = out[1]

db = {"status":status, "output":output}

out1 = dumps(db)

print(out1)