#!/usr/bin/env python

import argparse
import platform
import os
from storage import Storage

def main():

    parser = argparse.ArgumentParser(description='Quick save and find a frequently used command')
    subparsers = parser.add_subparsers(dest='command')
    cache_parser = subparsers.add_parser('cache', help='Cache a command')
    cache_parser.add_argument('value', help='The command needs to be cached')
    cache_parser.add_argument('-a', dest='alias', help='Alias of the command')

    find_parser = subparsers.add_parser('find', help='Find a command by either entering part of it or its alias')
    find_parser.add_argument('keyword', help='Keyword to find a command')

    parser.add_argument('-s', dest='source', help='Source file path')

    args = parser.parse_args()

    path = os.path.join(args.source or os.curdir, 'easycmd.csv')
    storage = Storage(path)
    
    if args.command == 'cache':
        storage.cache(args.value, args.alias or None)
    elif args.command == 'find':
        matches = storage.match(args.keyword)
        for alias, cmd in matches.items():
            print('ALIAS:', alias, 'CMD:', cmd)
    else:
        print('Command unsupported: ', args.command)


if __name__ == '__main__':
    main()