import json
import time
from woocommerce import API

data = []
cons_key = 'ck_c3a54b06fdca2152a6995e082120a5fcf431e3cf'
cons_secret = 'cs_03d64ce53e835617ab7ab2f286e98bd4fb967f30'
games_to_buy = True


def get_orders():
    wcapi = API(
        url="https://gameacs.eu/",
        consumer_key=cons_key,
        consumer_secret=cons_secret,
        version="wc/v3",
        wp_api=True,
        query_string_auth=True,
        verify_ssl=True,
        timeout=50
    )
    r = wcapi.get('orders')
    r = r.json()
    return r


def checker():
    response = get_orders()
    for item in response:
        if item['status'] == 'processing':
            for orders in item['line_items']:
                if 'Steam' in orders['name']:
                    return True
                else:
                    return False


def get_steam_orders():
    global data
    response = get_orders()
    print(response)
    try:
        for item in response:
            if item['status'] == 'processing':
                for orders in item['line_items']:
                    if 'Steam' in orders['name']:
                        buyer_email = item['billing']['email']
                        print(f'Order ID: {item["id"]}')
                        print(f"Buyer email: {item['billing']['email']}")
                        game_name = orders['name'].split('  ')[0]
                        print(f'Game URL: {game_name}')
                        order_dict = {
                            "order_id": item["id"],
                            "buyer email": buyer_email,
                            "game name": game_name
                        }
                        data.append(order_dict)

    except Exception as e:
        print(e)


def save_data():
    global data
    with open('order.json', 'w') as file:
        json.dump(data, file)


def run():
    if checker():
        get_steam_orders()
        time.sleep(2)
        save_data()
        return 'New Orders!'
    else:
        return 'Nothing to buy, yet!'


def confirm_order(order_id):
    wcapi = API(
        url="https://gameacs.eu/",
        consumer_key=cons_key,
        consumer_secret=cons_secret,
        version="wc/v3",
        wp_api=True,
        query_string_auth=True,
        verify_ssl=True,
        timeout=50
    )
    order_data = {
        'status': 'completed'
    }
    r = wcapi.put(f"orders/{order_id}", order_data)
    print(r)


if __name__ == '__main__':
    res = run()
    print(res)
