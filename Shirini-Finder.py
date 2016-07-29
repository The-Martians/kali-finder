# -*- coding: utf-8 -*-
import telebot
import logging

bot = telebot.TeleBot("233197189:AAGQFFlW5aYppdyI-K21xuYF4XWskOqG3AA")
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.reply_to(message, "سلام من کسایی که باید شیرینی بدن رو اعلام میکنم! منو به گروهتون ادد کنین تا بگم کی باید شیرینی بده! :))")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        try:
                text = message.text.lower()
                id = str(message.from_user.id)
                username = str(message.from_user.username)
                if username ==  "sadjadshirini_bot":
                     bot.reply_to(message, "همینم مونده فقط تو نظر بدی! " + id + u'\U0001f612' * 3 )
                elif "shirini" in text or "شیرین" in text and username != "SinaKarimi7":
                        if username:
                                if str(message.from_user.first_name):
                                        bot.reply_to(message, "بچه ها ایشون باید شیرینی بده!!! @" + username + "\nاسمشم: " + message.from_user.first_name + "\nموری @Mortezaa_97 به لیستت اضافه کن!" + u'\U0001f602' * 3 )
                        elif username:
                                bot.reply_to(message, "بچه ها ایشون باید شیرینی بده!!! @" + username + "\nموری @Mortezaa_97 به لیستت اضافه کن!" + u'\U0001f602' * 3 )
                        else:
                                bot.reply_to(message, "بچه ها ایشون باید شیرینی بده!!! " + id + "\nموری به لیستت اضافه کن!" + u'\U0001f602' * 3 )

                elif "ghol" in text or "قول" in text:
                        if username:
                                if str(message.from_user.first_name):
                                        bot.reply_to(message, "ایشون قول داده و باید به قولش عمل کنه!!! @" + username + u'\U0001f609' * 3 )
                        elif username:
                                bot.reply_to(message, "ایشون قول داده و باید به قولش عمل کنه!!! @" + username + u'\U0001f609' * 3 )
                        else:
                                bot.reply_to(message, "ایشون قول داده و باید به قولش عمل کنه!!! @" + id + u'\U0001f609' * 3 )
                elif "eydi" in text or "عیدی" in text:
                        if username and username != "SinaKarimi7":
                                if str(message.from_user.first_name):
                                        bot.reply_to(message, "عیدی بده!  @" + username + u'\U0001f609' * 3 )
                        elif username:
                                bot.reply_to(message, "عیدی بده!  @" + username + u'\U0001f609' * 3 )
                        else:
                                bot.reply_to(message, "عیدی بده!  @" + id + u'\U0001f609' * 3 )
        except Exception as e:
		          print ("We Have An Exception:")
		          print (e)
        pass

bot.polling(True)
