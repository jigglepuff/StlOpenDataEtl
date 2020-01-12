#!/usr/bin/env python3
# Python make file for repeated build functions

# Execute pip freeze to collect our dependencies to a requirements.txt file
import subprocess

print("Executing pip install against collected requirements.")
requirements = subprocess.Popen(
    ['pip', 'install', '-r', 'requirements.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = requirements.communicate()
print(stdout.decode('utf-8'))
