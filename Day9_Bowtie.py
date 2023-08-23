n = int(input('Enter the size of a side of the bow-tie: '))
for i in range(n):
    # stars = '*' + ' '
    stars = '*' * (i + 1)
    stars += ' ' * (2 * (n - i - 1))
    stars += '*' * (i + 1)
    print(stars)
for i in range(n - 1):
    # stars = '* '
    stars = '*' * (n - i - 1)
    stars += ' ' * (2 * (i + 1))
    stars += '*' * (n - i - 1)
    print(stars)