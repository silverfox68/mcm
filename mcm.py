import os
import argparse

def lxd(args):
    print(args)
    os.system('lxc exec minecraft -- docker ps -a --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Minecraft Container Manager')
    parser.add_argument('-t', '--type', default='lxd', help='container system')
    parser.add_argument('-c', '--container', default='minecraft', help='name of container holding the servers')

    args = parser.parse_args()

    if args.type == 'lxd':
        # Use lxd
        lxd(args)
    else:
        print('Invalid container system')
