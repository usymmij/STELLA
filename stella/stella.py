#! /usr/bin/env python
import argparse


def main():
    parser = argparse.ArgumentParser(
                    prog='STELLA',
                    description='CARLA based autonomous agent',
                    epilog='')
    parser.add_argument('-ip', '--ip', default="localhost", 
                        help="CARLA ip")
    parser.add_argument('-p', '--port', default=2000, type=int,
                        help="CARLA port")

    args = parser.parse_args()

    print(args.port)
    print(args.ip)

if __name__=="__main__":
    main()
