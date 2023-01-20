import datetime
from datetime import timedelta
from fiveth_app.models import *
import telebot
from telebot import types
from datetime import date, timedelta
from decimal import Decimal, DecimalException
import time

trainerr =False
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# button1 = types.KeyboardButton('Trash')
# button2 = types.KeyboardButton('Products')
# button3 = types.KeyboardButton('Buy')
# button4 = types.KeyboardButton('Wallet')
# button5= types.KeyboardButton('Checkwallet')
# button6=types.KeyboardButton('ClearOrder')
button1 = types.KeyboardButton('Trash')
button2 = types.KeyboardButton('Products')
button3 = types.KeyboardButton('Subscription')
button4 = types.KeyboardButton('Wallet')
button5= types.KeyboardButton('Checkwallet')
button6=types.KeyboardButton('ClearOrder')
button7 = types.KeyboardButton('Train')
button8 = types.KeyboardButton('Trainer')
button9 = types.KeyboardButton('CheckSubscription')
keyboard.add(button1,button2,button3,button4,button5,button6,button7,button8,button9)
#keyboard.add(button1,button2,button3,button4,button5,button6)
config = {
    'name': 'BanVital_bot',
    'token': '5787697902:AAHmBf2JqZGctl3zbwunMgfBQVvhxXEUfI8'
}
botler = telebot.TeleBot(config['token'])

@botler.message_handler(commands=['start'])
def start(message):
    botler.send_message(message.chat.id,'Menu:',reply_markup=keyboard)
    if not Wallet.objects.filter(userid = message.chat.id):
        Wallet.objects.get_or_create(
            userid = message.chat.id,
        )
    if not Subscription.objects.filter(userid = message.chat.id):
        Subscription.objects.get_or_create(
            userid = message.chat.id,
        )
    # if not Gym.objects.filter(userid = message.chat.id):
    #     Gym.objects.get_or_create(
    #         userid = message.chat.id,
    #     )
@botler.message_handler(content_types=['text'])
def get_text(message):
        if message.text == "Subscription":
            keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            botler.send_message(message.chat.id, "Choose your Subscription?")
            button13 = types.KeyboardButton("1-Day| price: 10$")
            button14 = types.KeyboardButton("1-Month| price: 100$")
            button15 = types.KeyboardButton("1-Year| price: 1000$")
            keyboard3.add(button13, button14, button15)
            choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
            botler.register_next_step_handler(choice, buy)

        if message.text == "Train":
            keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            botler.send_message(message.chat.id, "Choose what you want")
            button13 = types.KeyboardButton("Start train")
            button15 = types.KeyboardButton("Show my trains")
            keyboard3.add(button13, button15)
            choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
            botler.register_next_step_handler(choice, train)
        if message.text == "Trainer":
            if not trainerr:
                keyboard5 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                botler.send_message(message.chat.id, "Choose your Trainer")
                button13 = types.KeyboardButton("Vova | price: 400$")
                button14 = types.KeyboardButton("Ne Vova | price: 600$")
                keyboard5.add(button13, button14)
                choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard5)
                botler.register_next_step_handler(choice, trainer)
            else:
                botler.send_message(message.chat.id, "You already have trainer")
        if message.text == "Wallet":
            botler.send_message(message.chat.id, "Enter how much money do you want to add: ")
            botler.register_next_step_handler(message, add_money)
        if message.text=="Checkwallet":
            botler.send_message(message.chat.id, Wallet.objects.filter(userid=message.chat.id)[0].balance)
        if message.text == "CheckSubscription":
            botler.send_message(message.chat.id, f'Your Subscription ends in: {Subscription.objects.filter(userid=message.chat.id)[0].end_time}')
        if message.text == "Products":
            academy = Catagory.objects.filter()
            curators = ""
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in academy:
                # curators = curators + f'{i.name}\n'
                button = types.KeyboardButton(f'{i.name}')
                keyboard.add(button)
            choice=botler.send_message(message.chat.id, "category", reply_markup=keyboard)
            botler.register_next_step_handler(choice,products)
        if message.text == "ClearOrder":
            for i in Order.objects.filter(
                    userid=message.chat.id):
                i.delete()
            botler.send_message(message.chat.id, "Complete!")

        if message.text == "Trash":

            user_cart = [str(i.productid)
            for i in Order.objects.filter(userid=message.chat.id)]

            if user_cart:
                product_cost = dict()
                for i in Products.objects.all():
                    product_cost[i.name] = i.price

                user_cart_result = dict()
                for i in user_cart:
                    if i not in user_cart_result:
                        user_cart_result[i] = user_cart.count(i)

                user_cart_cost = 0

                for res in user_cart_result:
                    user_cart_cost += product_cost[res] * user_cart_result[res]
                today = date.today()
                academy = Order.objects.filter(date__year=today.year,date__month=today.month,date__day=today.day)
                curators = ""
                for i in academy:
                    curators = curators + f'{i.date} - {i.userid} - {i.productid}\n'
                # botler.send_message(message.chat.id, curators)

                botler.send_message(message.chat.id,curators + f'\nOrder cost - {user_cart_cost}')
                keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                botler.send_message(message.chat.id,"Do you want buy?")
                button13 = types.KeyboardButton("Yes")
                button14 = types.KeyboardButton("No")
                keyboard3.add(button13,button14)
                choice=botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
                botler.register_next_step_handler(choice,buy)
            else:
                botler.send_message(message.chat.id, "Order empty!")
def train(message):
    if message.text=="Start train":
        t = time.localtime()
        global today
        today = time.strftime("%H:%M:%S", t)
        # d = datetime.date(today.year,today.month,today.day)
        botler.send_message(message.chat.id, f'You start train in: {today}')
        # user2.starttime = today
        # user2.save()


        keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botler.send_message(message.chat.id, "If you want to stop the train")
        button14 = types.KeyboardButton("End train")
        keyboard3.add(button14)
        choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
        botler.register_next_step_handler(choice, endtrain)

    if message.text == "Show my trains":
        user2 = Gym.objects.filter(
            userid=message.chat.id)
        for i in user2:
            botler.send_message(message.chat.id,f'You start train in: {i.starttime}\nYou end train in: {i.endtime}')
        botler.send_message(message.chat.id, "It's your trains" ,reply_markup=keyboard)
def trainer(message):
    global trainerr
    if message.text=="Vova | price: 400$":
        a=TrainWithTrainer.objects.filter(name="Vova")
        t = time.localtime()
        tomorrow = time.strftime("%H:%M:%S", t)
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 400:

            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:

                trainerr=True
                user.balance -= 400
                user.save()
                botler.send_message(message.chat.id, "Ok, Vova it's yours",reply_markup=keyboard)
    if message.text == "Ne Vova | price: 600$":
        a = TrainWithTrainer.objects.filter(name="Ne Vova")
        t = time.localtime()
        tomorrow = time.strftime("%H:%M:%S", t)
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 600:

            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:
            trainerr = True
            user.balance -= 600
            user.save()
            botler.send_message(message.chat.id, "Ok, Ne Vova it's yours", reply_markup=keyboard)

def endtrain(message):
    t = time.localtime()
    tomorrow = time.strftime("%H:%M:%S", t)
    botler.send_message(message.chat.id, f'You ends train in: {tomorrow}')
    if message.text=="End train":
        a = Gym.objects.get_or_create(
            userid=message.chat.id,
            starttime=today,
            endtime=tomorrow
        )
        botler.send_message(message.chat.id, "Greate", reply_markup=keyboard)
def buy(message):
    if message.text=="Yes":
        user_cart = [str(i.productid)
                     for i in Order.objects.filter(userid=message.chat.id)]

        if user_cart:
            product_cost = dict()
            for i in Products.objects.all():
                product_cost[i.name] = i.price

            user_cart_result = dict()
            for i in user_cart:
                if i not in user_cart_result:
                    user_cart_result[i] = user_cart.count(i)

            user_cart_cost = 0

            for res in user_cart_result:
                user_cart_cost += product_cost[res] * user_cart_result[res]
            user = Wallet.objects.filter(
                userid=message.chat.id)[0]
            if user.balance < user_cart_cost:
                botler.send_message(message.chat.id, "Not Enough money!",reply_markup=keyboard)
            else:
                user.balance -= user_cart_cost
                user.save()
                clearusercart(message)
    if message.text == "1-Day| price: 10$":

        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 10:
            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:
            user1 = Subscription.objects.filter(
                userid=message.chat.id)[0]
            today = date.today()
            d3 = datetime.date(today.year, today.month, today.day)
            user1.geeks_field = d3
            user1.save()
            if user1.geeks_field<user1.end_time:
                botler.send_message(message.chat.id, f"Subscription already bought", reply_markup=keyboard)
            if user1.geeks_field>=user1.end_time:
                today = date.today()
                b = today.day

                d = datetime.date(today.year,today.month, b+1)
                user1.end_time =  d

                user1.save()
                user.balance -= 10
                user.save()
                botler.send_message(message.chat.id, "You buy Subscription 1-day", reply_markup=keyboard)
    if message.text == "1-Month| price: 100$":
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 100:
            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:
            user1 = Subscription.objects.filter(
                userid=message.chat.id)[0]
            today = date.today()
            d3 = datetime.date(today.year, today.month, today.day)
            user1.geeks_field = d3
            user1.save()
            if user1.geeks_field<user1.end_time:
                botler.send_message(message.chat.id, "Subscription already bought", reply_markup=keyboard)
            if user1.geeks_field>=user1.end_time:
                today = date.today()
                b = today.month
                d = datetime.date(today.year, b+1, today.day)
                user1.end_time = d
                user1.save()
                user.balance -= 100
                user.save()
                botler.send_message(message.chat.id, "You buy Subscription 1-month", reply_markup=keyboard)

    if message.text == "1-Year| price: 1000$":

        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 1000:
            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:
            user1 = Subscription.objects.filter(
                userid=message.chat.id)[0]
            today = date.today()
            d3 = datetime.date(today.year, today.month, today.day)
            user1.geeks_field = d3
            user1.save()
            if user1.geeks_field<user1.end_time:
                botler.send_message(message.chat.id, "Subscription already bought", reply_markup=keyboard)
            if user1.geeks_field>=user1.end_time:
                today = date.today()
                b=today.year
                d = datetime.date(b+1, today.month, today.day)
                user1.end_time =d
                user1.save()

                user.balance -= 1000
                user.save()
                botler.send_message(message.chat.id, "You buy Subscription 1-year", reply_markup=keyboard)
    if message.text == "No":
                botler.send_message(message.chat.id, "OK", reply_markup=keyboard)


def clearusercart(message):
    for i in Order.objects.filter(
            userid = message.chat.id):
        i.delete()
    botler.send_message(message.chat.id, "Complete!",reply_markup=keyboard)

def add_money(message):
    try:
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        user.balance += Decimal(message.text)
        user.save()
    except DecimalException:
        botler.send_message(message.chat.id, 'Non Digit!')
    else:
        botler.send_message(message.chat.id, "Summ added to wallet!")

def products(message):
    academy = Products.objects.filter(catagoryid__name=message.text)
    curators = ""
    a=Wallet.objects.filter(userid=message.chat.id)
    for i in a:
        user=i.balance
    keyboard= types.InlineKeyboardMarkup()
    for i in academy:
        #curators = curators + f'{i.name}\n'
        button=types.InlineKeyboardButton(f'{i.name}: {i.price}$',callback_data=i.name)
        keyboard.add(button)
    botler.send_message(message.chat.id, f"your wallet: {str(user)}$",reply_markup=keyboard)

@botler.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data:
        # print(call.data)
        # print(call.message.text)
        a=Order.objects.get_or_create(
            userid=call.message.chat.id,
            productid=Products.objects.get(name=call.data),
            date=datetime.datetime.now()
        )
        botler.send_message(call.message.chat.id,f'Product: {call.data} add to trash',reply_markup=keyboard)
botler.polling(none_stop=True,interval=0)