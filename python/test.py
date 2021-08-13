import sys
import os

try:
    morpheus
except NameError:
    morpheus = None

if morpheus:
    server = morpheus['server']['fqdn']
else:
    server ="No Morpheus Context"

#password = Cypher(morpheus=morpheus).get('secret/spotts')

print(f"Python Test running in the server context {server}")
print(f"__file__ {__file__}")


for path in sys.path:
    print(f"path = {path}")

for item, value in os.environ.items():
    print(f"Environment - {item}: {value}")

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#sys.path.append(BASE_PATH)
print(f"Base Path {BASE_PATH}")