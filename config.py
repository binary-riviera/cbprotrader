from collections import namedtuple

# passphrase
# api secret
# key

# TODO: maybe cache this value if its being called a lot
def get_api_details():
    filename = "config.txt"
    f = open(filename, "r")
    passphrase = f.readline().rstrip("\n")
    secret = f.readline().rstrip("\n")
    key = f.readline().rstrip("\n")
    f.close()
    APIConfig = namedtuple("APIConfig", ["passphrase", "secret", "key"])
    return APIConfig(passphrase, secret, key)

