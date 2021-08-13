import sys
import os

#trap the situation where Morpheus is Launching the script via <stdin> and add cwd to path
if (__file__ == "<stdin>"):
    sys.path.append(os.path.join(os.getcwd(),"python"))

from winrmpwsh.winrm_pwsh import run_winrm
from morpheuscypher import Cypher

try:
    morpheus
except NameError:
    morpheus = None

server = morpheus['server']['fqdn']
password = Cypher(morpheus=morpheus).get('secret/spotts')

try:
    output=run_winrm(server,"Test\spotts",password,"")
    print(output)
    sys.exit(0)
except Exception as err:
    print(f"winRm Exception {err}")
    sys.exit(1)
