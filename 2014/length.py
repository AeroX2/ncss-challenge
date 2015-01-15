#!/usr/bin/env python3
import sys
 
def main():
  if len(sys.argv) < 2:
    sys.exit('Usage: golfstats.py program.py')
 
  for i in range(1, len(sys.argv)):
    with open(sys.argv[i]) as f:
      print(i, stats(f.read()), sep='. ')
 
def stats(code):
  code = code.strip()
  # (characters, newlines, semicolons)
  return len(code), code.count('\n'), code.count(';')
 
if __name__ == '__main__':
  main()
