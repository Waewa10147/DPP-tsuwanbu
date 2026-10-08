#!/usr/bin/env python3
import sys
if len(sys.argv) == 2:
    text = sys.argv[1]
    count = text.count('z')
    
    if count > 0:
        print("z" * count)
    else:
        print("none")
else:
    print("none")