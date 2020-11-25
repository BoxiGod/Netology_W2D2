import hashlib


def md5_hash(some_file):
    i = 0
    lines = some_file.readlines()
    while i < len(lines):
        yield hashlib.md5(lines[i].encode())
        i += 1


if __name__ == '__main__':
    some_f = open(input(), 'r')
    for line in md5_hash(some_f):
        print(line.hexdigest())

