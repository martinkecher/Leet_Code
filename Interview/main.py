# You get a string and another one. You need to return true if it is the second string is a sanagram of the first one.
# You need to ignore casing, spaces and non-alphanumeric characters

def is_sanagram(first_str: str, second_str: str) -> bool:
    for ch in second_str:
        if not ch.isalnum():
            second_str = second_str.replace(ch, '')

    for ch in first_str:
        if not ch.isalnum():
            first_str = first_str.replace(ch, '')

    first_str =''.join(sorted(first_str.lower()))
    second_str = ''.join(sorted(second_str.lower()))

    if first_str == second_str:
        return True
    return False


if __name__ == '__main__':
    print(is_sanagram("Ma rtin.","Nitram..."))