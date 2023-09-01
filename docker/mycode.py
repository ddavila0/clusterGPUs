#!/usr/bin/env python3
import os

def main():
    try:
        num = int(os.environ['NUM'])
    except:
        num = 3
    for i in range(0, num):
        print(i)

if __name__ == "__main__":
    main()
