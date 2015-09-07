#!/usr/bin/env python3
import sys

def main():
  if len(sys.argv) != 2:
    print('Usage: golfstats.py program.py')
    sys.exit(1)

  with open(sys.argv[1]) as f:
    print(stats(f.read()))

def stats(code):
  code = code.strip()
  # (characters, newlines, semicolons)
  return len(code), code.count('\n'), code.count(';')

if __name__ == '__main__':
  main()
