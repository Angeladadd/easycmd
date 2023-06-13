#!/usr/bin/env python

import argparse
import platform
import os
from storage import Storage

def main():
    path = os.path.join(os.curdir, 'easycmd.csv')
    storage = Storage(path)

    parser = argparse.ArgumentParser(description='Quick save and find a frequently used command')
    subparsers = parser.add_subparsers(dest='command')
    cache_parser = subparsers.add_parser('cache', help='Cache a command')
    cache_parser.add_argument('value', help='The command needs to be cached')
    cache_parser.add_argument('-a', dest='alias', help='Alias of the command')
    parser.add_argument('-c', dest='value', help='Command to find')

    args = parser.parse_args()
    
    if args.command == 'cache':
        storage.cache(args.value, args.alias or None)
    else:
        matches = storage.match(args.value)
        for alias, cmd in matches.items():
            print('ALIAS:', alias, 'CMD:', cmd)


if __name__ == '__main__':
    main()