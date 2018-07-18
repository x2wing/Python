from collections import defaultdict
import json
 

Vgb=11
Smbs=25
secinminute=60

print(Vgb*1024/Smbs/secinminute)

print(49790-7595.08)
print(2.87*170)

def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    """
    return defaultdict(tree)
 
root = tree()
# print(type(root))
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None
 
# print(json.dumps(root, indent=4))