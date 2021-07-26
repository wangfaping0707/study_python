import sys

print(sys.argv)
print(sys.modules)
print(sys.path)
print(sys.platform)
print(sys.stdin)
print(sys.stdout)
print(sys.stderr)


args = sys.argv[1:]
# print(args)
args.reverse()
print(' '.join(args))

