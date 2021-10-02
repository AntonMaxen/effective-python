import sys
import os

for p in sys.path:
    if 'mimslade' in p.lower():
        print(p)


for k, v in os.environ.items():
    if 'env' in v.lower():
        print(f'{k}: {v}')
