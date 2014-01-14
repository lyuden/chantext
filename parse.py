import re

message = """>>333{10:1000}
My message."""
pattern = re.compile('^>>(\d+)\{(\d+):(\d+)\}[\n|\r|\n\r]')


def parse_message(message, pattern):
    result = re.search(pattern, message)
    new_message = re.sub(pattern, '', message)
    return result.groups(), new_message


if __name__ == '__main__':
    print(parse_message(message, pattern))
    groups, message = parse_message(message, pattern)
    print(*groups)
    print(message)
