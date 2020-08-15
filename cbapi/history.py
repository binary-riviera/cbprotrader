import config
import cbpro


def get_order_history():
    conf = config.get_api_details()
    print(conf.passphrase)
    print(conf.secret)
    print(conf.key)
    auth_client = cbpro.AuthenticatedClient(conf.key, conf.secret, conf.passphrase)
    client_id = "12a31a64-aa68-4d58-94a8-8ac1963129c0"  # FIXME: how to find this programatically?
    orders = auth_client.get_account_history(client_id)
    print(list(orders))

