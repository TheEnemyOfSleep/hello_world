import argparse

parser = argparse.ArgumentParser(description="Flip a switch by setting a flag")
parser.add_argument('-d', '--data', nargs='+', help=r'list data with resourses', required=True)

args = parser.parse_args()

print(args.data)
