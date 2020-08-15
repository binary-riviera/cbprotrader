# passphrase
# api secret
# key


def get_api_details():
    filename = "config.txt"
    f = open(filename, "r")
    print(f.readline())
    print(f.readline())
    print(f.readline())
