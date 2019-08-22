import telebot
import random
import  urllib.request as urllib2
bot = telebot.TeleBot("927997018:AAGKgBijSnyegKnjIWMySFZH7Oh-U2pBeEY")
import  os


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Обзоры фильмов')
    user_markup.row('Фильмы', 'Сериалы','Фото')
    user_markup.row('Завершить')
    bot.send_message(message.from_user.id, "Hello!",reply_markup=user_markup)

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.from_user.id,"Помощь!")

@bot.message_handler(content_types=['text'])
def handle_start(message):
    if(message.text == 'Фото'):
        url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd_W9DdDbZMKLBvlvLas39s9Dhrr5ELRFEqce89LGSHiOVuw21'
        urllib2.urlretrieve(url,'out.jpg')
        img = open('out.jpg','rb')
        #bot.send_chat_action(message.from_user.id,'upload photo')
        bot.send_photo(message.from_user.id,img)
        bot.send_message(message.from_user.id,'GOOD!')
        img.close()
        os.remove("out.jpg")
    elif(message.text == 'Завершить'):
        bot.send_message(message.from_user.id, "Bye!", reply_markup=telebot.types.ReplyKeyboardRemove(True))
    elif(message.text == "Фильмы"):
        bot.send_message(message.from_user.id,"VK \n  https://vk.com/video?z=video443599425_456239058%2Fpl_cat_updates" )
bot.polling(none_stop=True)
