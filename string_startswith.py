# Check if string starts with a specific word


def check_string(string):
    if string.startswith('htpp'):
        return True
    return False


result = check_string('htpp://amazon.com')
print(result)