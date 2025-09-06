#!/usr/bin/env python
from pathlib import Path
from yaml import safe_load_all, safe_load, load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

from splitstream import splitfile
import json

# file_path = Path('.sde_workspace/fsd/controlTowerResources.yaml')
file_path = Path('.sde_workspace/fsd/types.json')
# file_path = Path('.sde_workspace/bsd/invFlags.yaml')
with file_path.open('r') as f:
    for jsonstr in splitfile(f, format='json'):
        obj = json.loads(jsonstr)
        print('------------------------------------------------------')
        print(type(obj))
        print(obj)
    # for i in safe_load(f):
    #     print('------------------------------------------------------')
    #     print(type(i))
    #     # if isinstance(i, dict):
    #     #     for k, v in i.items():
    #     #         print(f'{k}: {v}')
    #     # if isinstance(i, list):
    #         # for j in i:
    #         #     print(j)
