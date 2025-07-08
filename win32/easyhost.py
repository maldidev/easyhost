import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(prog='easyhost', description='Host management tool')
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')
    
    # help command (implied by -h/--help, but we can add it explicitly)
    help_parser = subparsers.add_parser('help', help='show this help message and exit')
    
    # run command
    run_parser = subparsers.add_parser('run', help='run the host with given mapping')
    run_parser.add_argument('ip', help='IP address to map')
    run_parser.add_argument('sitelink', help='Site link/domain to map to the IP')
    
    # version command
    version_parser = subparsers.add_parser('version', help='show version information')
    
    # if no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()

    def run_host(iplink, site):
        print(f"port: 8000, ip: {iplink}, site (addon): {site}")
        os.system(f"python3 -m http.server 8000 --bind {iplink}")
    
    # handle commands
    if args.command == 'help':
        parser.print_help()
    elif args.command == 'run':
        run_host(args.ip, args.sitelink)
    elif args.command == 'version':
        print("EasyHost version 1.0")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()