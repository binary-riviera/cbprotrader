import config


def get_order_history():
    conf = config.get_api_details()
    print(conf.passphrase)
    print(conf.secret)
    print(conf.key)
