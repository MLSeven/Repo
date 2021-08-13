import sys
import os

server = morpheus['server']['fqdn']
password = Cypher(morpheus=morpheus).get('secret/spotts')

print(f"Python Test running in the server context {server}")
for path in sys.path:
    print(path)

for item, value in os.environ.items():
    print(f"Environment - {item}: {value}")