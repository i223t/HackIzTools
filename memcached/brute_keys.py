#!/usr/bin/env python3

__author__      = "Maksim Chudakov aka Izzet"

import argparse
import sys
import bmemcached

def banner():
    print ('')

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -h 127.0.0.1 -p 11211 -w /usr/share/wordlist/all.txt")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-H', '--host', help="memcached server host", required=True)
    parser.add_argument('-p', '--port', help="memcached server port", type=int, default = 11211)
    parser.add_argument('-U', '--user', help="username", required=True)
    parser.add_argument('-P', '--password', help="password", required=True)
    parser.add_argument('-w', '--wordlist', help="wordlist", required=True)
    return parser.parse_args()
    
def main():
    args = parse_args()
    client = bmemcached.Client(('{0}:{1}'.format(args.host,args.port)), args.user,args.password)

    with open (args.wordlist) as f:
        try:
            word = f.readline()
        
            while word:
                response = client.get(word.strip())
                if response:
                    print ('Key Found: {0}\nValues:\n{1}\n\n'.format(word,response))
                word = f.readline()

        except Exception as err:
            print (err)

if __name__ == '__main__':
    main()
