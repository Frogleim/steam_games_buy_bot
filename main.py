from fastapi import FastAPI
from pydantic import BaseModel
from app import get_orders
from add_friend import run_bot
from email_sending import send_confirm_mail_to_admin, send_error_mail_to_admin
from add_amount import GiftCard, MainAccount

app = FastAPI()

data = []


class Amount(BaseModel):
    amount: str


@app.post("/api/add_amount/")
async def add_amounts(body: Amount):
    try:
        amount = body.amount
        gift_card = GiftCard(int(amount))
        gift_card.login()
        time.sleep(4)
        activate_code = gift_card.buy_gift_card()
        print(activate_code)
        time.sleep(4.8)
        main_account = MainAccount(activation_code=activate_code)
        main_account.login()
        time.sleep(3.3)
        main_account.get_gift_card()
        return {"Status": "true", "Message": "Amount added successfully"}
    except Exception as e:
        send_error_mail_to_admin()
        print(e)
        return {"Status": "false", 'Message': e}


@app.get('/api/buy/')
async def buy_game():
    buy = run_bot()
    if buy:
        send_confirm_mail_to_admin()

        with open('accounts.txt', 'r') as file:
            accounts = file.readlines()
            print(len(accounts))
            accounts_count = len(accounts)
        return {"Message":"Success", 'account_count': accounts_count}
    else:
        send_error_mail_to_admin()
        return {"No orders"}


@app.get("/api/orders/")
async def get_orders_list():
    data.clear()
    response = get_orders()
    for item in response:
        if item['status'] == 'processing':
            for orders in item['line_items']:
                if 'Steam' in orders['name']:
                    buyer_email = item['billing']['email']
                    print(f"Buyer email: {item['billing']['email']}")
                    game_name = orders['name'].split('  ')[0]
                    order_dict = {
                        "buyer email": buyer_email,
                        "game name": game_name
                    }
                    data.append(order_dict)
                    print(data)
    return {"Message": "true", "Orders": data}
