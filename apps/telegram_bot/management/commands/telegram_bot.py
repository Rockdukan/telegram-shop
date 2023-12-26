from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from keyboa import Keyboa
from telebot import TeleBot, types

from .config import BOT_TOKEN
from .services import *
from apps.shop.models import *
from apps.telegram_bot.models import *


bot = TeleBot(BOT_TOKEN)


#######################################################################
################################# Buttons #############################
#######################################################################
btn_catalog = types.KeyboardButton('🎰 Catalog')
btn_cart = types.KeyboardButton('🤝 Cart')
btn_address = types.KeyboardButton('💬 Address')
btn_orders = types.KeyboardButton('♻ Orders')
btn_buy = types.KeyboardButton('♻ Buy')
btn_help = types.KeyboardButton('♻ Help')


#######################################################################
################################ Messages #############################
#######################################################################
messages = {
    'hello': 'Приветствуем в нашем магазине',
}


#######################################################################
################################## Help ###############################
#######################################################################
def get_help(message):
    check_user(message.from_user.id)
    text = (
        ('Я могу ответить на следующие команды:\n') +
        ('/command_1 - описание\n') +
        ('/command_2 - описание'))
    bot.send_message(message.chat.id, text)


#######################################################################
################################# Catalog #############################
#######################################################################
def get_product_menu(message, subcategory):
    """ Меню товара """
    check_user(message.from_user.id)
    category = Category.objects.get(id=subcategory.category.id)
    subcategories = Subcategory.objects.filter(category=category)
    keyboard = types.InlineKeyboardMarkup()

    for subcategory in subcategories:
        keyboard.row(
        types.InlineKeyboardButton(
            f'{subcategory.title}',
            callback_data=f'subcategory-{subcategory.id}'))

    keyboard.row(
        types.InlineKeyboardButton(
            'В начало каталога',
            callback_data='get_categories_list'))
    bot.send_message(
            message.chat.id, 'Выберите раздел, чтобы вывести список товаров:',
            reply_markup=keyboard)


def get_categories_list(message):
    """ Получить список категорий """
    check_user(message.from_user.id)
    categories = Category.objects.all()
    keyboard = types.InlineKeyboardMarkup()
    for category in categories:
        keyboard.row(
        types.InlineKeyboardButton(
            f'{category.title}',
            callback_data=f'category-{category.id}'))
    bot.send_message(
        message.chat.id,  
        'Список категорий',
        reply_markup=keyboard)


def get_subcategories_list(message, category_id):
    """ Получить список подкатегорий """
    check_user(message.from_user.id)
    category = Category.objects.get(id=category_id)
    subcategories = Subcategory.objects.filter(category=category)
    keyboard = types.InlineKeyboardMarkup()
    for subcategory in subcategories:
        keyboard.row(
        types.InlineKeyboardButton(
            f'{subcategory.title}',
            callback_data=f'subcategory-{subcategory.id}'))
    bot.send_message(
        message.chat.id,  
        'Список подкатегорий',
        reply_markup=keyboard)


def get_products_list(message, subcategory_id):
    """ Получить список товаров в подкатегории """
    check_user(message.from_user.id)
    subcategory = Subcategory.objects.get(id=subcategory_id)
    products = Product.objects.filter(subcategory=subcategory)
    for product in products:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton(
                'Добавить в кoрзину',
                callback_data=f'add-to-cart-{product.id}'))
        text = f'*{product.title}\nPrice: {product.price}*\n\n{product.description}'
        # Если загружено основное изобажение
        if product.image:
            image = open(str(settings.BASE_DIR) + product.image.url, 'rb')
            images = ImageSet.objects.filter(product=product)
            # Если есть дополнительные изображения
            if images:
                text = f'*{product.title}'
                media = [types.InputMediaPhoto(image, caption=text),]
                for image_set in images:
                    image = open(str(settings.BASE_DIR) + image_set.image.url, 'rb')
                    media.append(types.InputMediaPhoto(image))
                bot.send_media_group(
                    message.chat.id,
                    media)
                text = f'*Price: {product.price}*\n\n{product.description}'
                bot.send_message(
                    message.chat.id,
                    text,
                    parse_mode='Markdown',
                    reply_markup=keyboard)
            # Если нет дополнительных изображений
            else:
                bot.send_photo(
                    message.chat.id,
                    image,
                    caption=text,
                    parse_mode='Markdown',
                    reply_markup=keyboard)
        # Если нет основного изображения
        else:
            bot.send_message(
                message.chat.id,
                text,
                parse_mode='Markdown',
                reply_markup=keyboard)
        get_product_menu(message, subcategory)


#######################################################################
################################## Cart ###############################
#######################################################################
def add_to_cart(message, product_id):
    try:
        user = check_user(message.chat.id)
        cart = check_cart(user)
        product = Product.objects.get(id=product_id)
        if not check_product_in_cart(cart, product):
            cart_product = CartProduct.objects.create(
                user=user,
                cart=cart,
                product=product)
        bot.send_message(message.chat.id, f'Добавил в корзину продукт: {product.title}')
    except:
        bot.send_message(
            message.chat.id, 'Произошла ошибка, приносим свои извинения')


def remove_to_cart(message, product_id):
    cart = check_cart(check_user(message.chat.id))
    cart_products = get_cart_products(cart)
    print(cart_products)
    product = cart_products.get(id=product_id)
    title = product.product.title
    product.delete()
    bot.send_message(
        message.chat.id, f'{title} удалён из корзинны')


def get_cart(message):
    cart = check_cart(check_user(message.from_user.id))
    bot.send_message(
        message.from_user.id,
        f'*Список продуктов в корзине:*\n',
        parse_mode='Markdown')
    products = get_cart_products(cart)
    if products:
        for product in products:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.row(
                types.InlineKeyboardButton(
                    'Удалить из карзины',
                    callback_data=f'remove-to-cart-{product.id}'))
            text = f'\n{product.product.title}\n*QTY*:{product.qty}\n*Price*:{product.final_price}\n'
            if product.product.image:
                image = open(str(settings.BASE_DIR) + product.product.image.url, 'rb')
                bot.send_photo(
                    message.chat.id,
                    image,
                    caption=text,
                    parse_mode='Markdown',
                    reply_markup=keyboard)
            else:
                bot.send_message(
                    message.from_user.id,
                    text,
                    parse_mode='Markdown',
                    reply_markup=keyboard)
    else:
        bot.send_message(
            message.from_user.id,
            f'В корзине нет товаров',
            parse_mode='Markdown')


#######################################################################
################################# Orders ##############################
#######################################################################
def get_orders(message):
    check_user(message.from_user.id)
    bot.send_message(  
        message.chat.id,  
        'Выводим информацию о истории заказов с их статусами')


#######################################################################
################################# Address #############################
#######################################################################
def get_contacts(message):
    user = check_user(message.from_user.id)
    try:
        address = Address.objects.get(user=user)
    except:
        address = None
    if address:
        text = f'*Your address:*\nCountry: {address.country}\nCity: {address.city}\nStreet: {address.street}\nRoom: {address.room}\nPost code: {address.post_code}\nMobile phone: {address.mobile}\n'
    else:
        text = 'No address'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
    types.InlineKeyboardButton(f'Edit', callback_data='edit_contact'))
    bot.send_message(
        message.chat.id,  
        text,
        reply_markup=keyboard,
        parse_mode='Markdown')
    return text


def edit_contact(message):
    bot.send_message(message.chat.id, 'Country: ')
    bot.register_next_step_handler(message, get_country)


def get_country(message):
    country = message.text
    bot.send_message(message.chat.id, 'City: ')
    bot.register_next_step_handler(message, get_city, country)


def get_city(message, country):
    city = message.text
    bot.send_message(message.chat.id, 'Street: ')
    bot.register_next_step_handler(message, get_street, country, city)


def get_street(message, country, city):
    street = message.text
    bot.send_message(message.chat.id, 'Room: ')
    bot.register_next_step_handler(message, get_room, country, city, street)


def get_room(message, country, city, street):
    room = message.text
    bot.send_message(message.chat.id, 'Post code: ')
    bot.register_next_step_handler(message, get_post_code, country, city, street, room)


def get_post_code(message, country, city, street, room):
    post_code = message.text
    bot.send_message(message.chat.id, 'Mobile number: ')
    bot.register_next_step_handler(message, get_mobile, country, city, street, room, post_code)


def get_mobile(message, country, city, street, room, post_code):
    user = check_user(message.from_user.id)
    try:
        address = Address.objects.get(user=user)
        address.delete()
    except:
        pass
    mobile = message.text
    Address.objects.create(
        user=user,
        country=country,
        city=city,
        street=street,
        room=room,
        post_code=post_code,
        mobile=mobile)
    get_contacts(message)


#######################################################################
################################### Buy ###############################
#######################################################################
@bot.message_handler(commands=['buy'])
def get_buy(message):
    user = check_user(message.from_user.id)
    cart = check_cart(user)
    price = cart.get_final_price()
    order = Order.objects.create(
        customer=user,
        cart=cart)
    cart.in_order=True
    cart.save()
    bot.send_message(
        message.chat.id,
        f'*Order number:* B7000{order.id}\n'
        f'{get_contacts(message)}\n'
        f'*Price:* {price}\n'
        'Write number of your order in message with transaction',
        parse_mode='Markdown')


    # TODO: Необходимо получить provider_token для возможности оплаты.
    # amount = int(cart.get_final_price() * 100)
    # price = types.LabeledPrice(label='Item_Name', amount=amount)
    # bot.send_message(
    #     message.chat.id,
    #      ''' 
    #      Use this test card number to pay for your Item: 
    #     1111 1111 1111 1026
    #     Expiration Date: 12/22
    #     CVC: 000''')

    # bot.send_invoice(
    #     message.chat.id,
    #     title='Item for Sale',
    #     description='Bla-Bla-Bla',
    #     provider_token=provider_token,
    #     currency='RUB',
    #     photo_url=None,
    #     need_phone_number=False,
    #     need_email=False,
    #     is_flexible=False,  # True если конечная цена зависит от способа доставки
    #     prices=[price],
    #     start_parameter='start_parameter',
    #     invoice_payload='coupon')


@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(query):
    bot.answer_pre_checkout_query(query.id, ok=True)


def got_payment(message):
    bot.send_message(message.chat.id, 'Bay')


#######################################################################
################################ General ##############################
#######################################################################
@bot.message_handler(commands=['start'])
def start_message(message):
    """Запуск бота"""
    check_user(message.from_user.id)
    keyboard = types.ReplyKeyboardMarkup(
        row_width=2,
        one_time_keyboard=False,
        resize_keyboard=True)
    
    keyboard.add(
        btn_catalog,
        btn_cart,
        btn_address,
        # btn_orders,
        btn_buy)
        # btn_help)
    bot.send_message(
        message.chat.id,
        'Приветствуем в нашем магазине',
        reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def check_keyboard_messages(message):
    """ Обработчик основной клавиатуры """
    if message.text == btn_cart.text:
        get_cart(message)
    elif message.text == btn_address.text:
        get_contacts(message)
    elif message.text == btn_catalog.text:
        get_categories_list(message)
    elif message.text == btn_buy.text:
        # got_payment(message)
        get_buy(message)
    elif message.text == btn_orders.text:
        get_orders(message)
    elif message.text == btn_help.text:
        get_help(message)
    else:
        print('Неизвестная команда')


@bot.callback_query_handler(func=lambda call: True)
def handle_text(call):
    """ Обработчик дополнительной клавиатуры """
    if call.data.startswith('add-to-cart-'):
        product_id = int(call.data.replace('add-to-cart-', ''))
        add_to_cart(call.message, product_id)
    elif call.data.startswith('category-'):
        category_id = int(call.data.replace('category-', ''))
        get_subcategories_list(call.message, category_id)
    elif call.data.startswith('subcategory-'):
        subcategory_id = int(call.data.replace('subcategory-', ''))
        get_products_list(call.message, subcategory_id)
    elif call.data.startswith('get_categories_list'):
        get_categories_list(call.message)
    elif call.data.startswith('remove-to-cart-'):
        product_id = int(call.data.replace('remove-to-cart-', ''))
        remove_to_cart(call.message, product_id)
    elif call.data == 'edit_contact':
        edit_contact(call.message)
    # else message.text == 'Назад':
    #     menu(message)


class Command(BaseCommand):
    """Класс для исполнения команды Django"""
    def handle(self, *args, **options):
        bot.polling(none_stop=True, interval=0)
