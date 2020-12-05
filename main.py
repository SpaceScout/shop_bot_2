import telebot


from shop_bd import user

token = "1305837326:AAHbFrLVGSuBcrzU8TCRyS_C3Y3WXClmnew"
bot = telebot.TeleBot(token)

all_data = {'last_order_id':0,'counts':0,'now_id':None,'now_prod':None, 'now_prise':None}


def korzina(message):
    if message.text == '📦Корзина':
        pass



@bot.message_handler(commands=['start'])
def handler_start(message):
    if(not user.check_user(self=True, user_id=message.from_user.id)):
        user.add_user(self=True, user_id=message.from_user.id, taken=False, delivar=False, paid=False, maika3d=0, Boots=0)
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('💵Каталог')
        user_markup.row('📦Корзина', '☎Контакты')
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}🤖!\nВы можете зайти в каталог и выбрать товар себе по душе', reply_markup=user_markup)
    else:
        bot.send_message(message.chat.id, 'Привет, снова вернулся за покупаками?\nМы всегда тебе рады!')
        print(2)

@bot.message_handler(content_types=['text'])
def message_tovar(message):
    if message.text == '💵Каталог':
        inlinekb1 = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text='❌Вернуться', callback_data='back')
        inlinekb1.add(button1)
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Вы в каталоге!\n\n🔍Выбирайте товар и добавляйте его в корзину!', reply_markup=inlinekb1)
        user_markup2 = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup2.row('👕Одежда', '👟Обувь')
        bot.send_message(message.chat.id, "`", reply_markup=user_markup2)
    elif message.text == '👕Одежда':
        img1 = open('images/maika.jpg', 'rb')
        inlinekb2 = telebot.types.InlineKeyboardMarkup(row_width=2)
        button_1 = telebot.types.InlineKeyboardButton(text='Добавить', callback_data='maika')
        button_2 = telebot.types.InlineKeyboardButton(text='Убрать', callback_data='kor2')
        button_3 = telebot.types.InlineKeyboardButton(text='🗑Корзина', callback_data='kor3')
        button_4 = telebot.types.InlineKeyboardButton(text='Вернуться', callback_data='back')
        inlinekb2.add(button_1, button_2, button_3, button_4)
        bot.send_photo(message.chat.id, img1,caption='Футболка мужская', reply_markup=inlinekb2)
    elif message.text == '👟Обувь':
        img1 = open('images/boots.jpg', 'rb')
        inlinekb2 = telebot.types.InlineKeyboardMarkup(row_width=2)
        button_1 = telebot.types.InlineKeyboardButton(text='Добавить', callback_data='boots')
        button_2 = telebot.types.InlineKeyboardButton(text='Убрать', callback_data='kor2')
        button_3 = telebot.types.InlineKeyboardButton(text='🗑Корзина', callback_data='kor3')
        button_4 = telebot.types.InlineKeyboardButton(text='Вернуться', callback_data='back')
        inlinekb2.add(button_1, button_2, button_3, button_4)
        bot.send_photo(message.chat.id, img1, caption='Мужские кроссовки', reply_markup=inlinekb2)
    elif message.text == '📦Корзина':
        if basket == []:
            bot.send_message(message.chat.id, 'Ваша корзина пуста')
        else:
            couel = len(basket)
            for i in range(couel):
                bot.send_message(message.chat.id, '%s. %s * %s ' % (i+1, basket[i], counts[basket[i]][basket[i]]))
            bot.send_message(message.chat.id, 'Цена всей покупки: %s' % counts['all_price'])
    elif message.text == 'Статус заказа':
        markup_stat = telebot.types.InlineKeyboardMarkup(row_width=3)
        but1= telebot.types.InlineKeyboardButton(text='Оплачено')
        but2 = telebot.types.InlineKeyboardButton(text='Доставлено')
        but3 = telebot.types.InlineKeyboardButton(text='Получено')
        markup_stat.add(but1, but2, but3)
        bot.send_message(message.chat.id, 'Какой статут заказа хотите поставить?')
        if user.carried()
        user.paid(self=True, user_id=message.from_user.id)
        bot.send_message(message.chat.id, 'ДАААААААААААААА')
    elif message.text == '☎Контакты':
        bot.send_message(message.chat.id, '===☎Контакты===\n\nСайт: \nТелефон: \n')
    else:
        pass


@bot.callback_query_handler(func=lambda call: True)
def answer1(call):
    global user_pol
    if call.data == 'back':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row('💵Каталог')
        user_markup.row('📦Корзина', '☎Контакты')
        bot.send_message(call.message.chat.id, '✅Вы в главном меню', reply_markup=user_markup)
    elif call.data == 'kor3':
        pass
    elif call.data == 'kor1':
        pass
    elif call.data == 'maika':
        bot.send_message(call.message.chat.id, 'Введите кол-во необходимого товара')
        all_data['now_prod'] = ''
    else:
        pass

@bot.message_handler(content_types=['text'])
def otvet_na_vse(message):
    bot.send_message(message.chat.id, 'Выберете пожалуйста действие на клавиатуре🤔')

bot.polling(none_stop=True, interval=0)



