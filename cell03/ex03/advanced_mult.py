import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

i = 0
while i <= 10:
    print(f"Table de {i}:", end=' ')
    j = 0
    while j <= 10:
        print(i * j, end=' ' if j < 10 else '')
        j += 1
    print()
    i += 1
