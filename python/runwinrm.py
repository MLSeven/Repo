from .winrm_pwsh import run_winrm
from morpheuscypher import Cypher
import sys

server = morpheus['server']['fqdn']
password = Cypher(morpheus=morpheus).get('secret/spotts')

try:
    output=run_winrm(server,"Test\spotts",password,"")
    print(output)
    sys.exit(0)
except Exception as err:
    print(f"winRm Exception {err}")
    sys.exit(1)
