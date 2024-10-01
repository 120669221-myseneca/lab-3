#!/usr/bin/env python3
'''Lab 3 Inv 3 function free_space '''
# Author ID: 120669221

import subprocess

def free_space():
    # Run the Linux command: df -h | grep '/$' | awk '{print $4}'
    result = subprocess.run(
        "df -h | grep '/$' | awk '{print $4}'", 
        shell=True, capture_output=True, text=True
    )
    # Return the result, ensuring it's in utf-8 and stripped of newlines
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())
