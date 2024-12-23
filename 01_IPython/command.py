import os
import sys

if os.name == 'nt':
    sys.stdin = open('CON', 'r')
    sys.stdout = open('CON', 'w')
else:
    sys.stdin = open('/dev/tty')
    sys.stdout = open('/dev/tty')

print(sys.stdin.isatty())  # 다시 테스트