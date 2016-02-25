fmt = "%r %r %r"

print fmt % (1, 2, 3)
print fmt % (2.71828, 3.1415926, 0.5)
print fmt % (True, False, True)
print fmt % ("foo", 'bar', "baz")
print fmt % ("One two three", "four five six", "seven eight nine")
print fmt % (fmt, fmt, fmt)

