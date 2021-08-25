import sys
import os

try:
    morpheus
except NameError:
    morpheus = None

print("Morpheus Python Test: GIT Branch Python")
if morpheus:
    print("Running Python in Morpheus from a Local source")
else:
    print("This script is not being run via Morpheus")
  
print("Current value of sys.path")  
for path in sys.path:
    print(f"sys.path = {path}")
    
print("Current Environment")
for item, value in os.environ.items():
    print(f"Environment - {item}: {value}")

print(f"__file__ is {__file__}")
print(f"os.getcwd() {os.getcwd()}")
print(f"os.path.abspath(__file__) = {os.path.abspath(__file__)}")
