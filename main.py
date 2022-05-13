import telebot
from telebot import types
import random
bot = telebot.TeleBot('5223141163:AAFzA01OXSX_BJSskrTB61GDDc6_OxePzU8')
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["ghoul"])
def ghoul(m, res=False):
  a = 1000
  while a>0:  
    a=a-7
    b=a+7
    bot.send_message(m.chat.id, f'{b}-7={a}')
# Запускаем бота
@bot.message_handler(commands=["news"])
def news(m, res=False):
  bot.send_message(m.res.id, 'Короче что нового в версии 1.1.0, мой создатель проебался 3 раза подряд из-за чего чуть не положил серваки.Короче пошли вы нахер я ебал эту залупу. Из нового все команды txt ыбыли переведены в /команды так же добавлена это функция news. Всем удачи по новым предложениям пишите в лс')
@bot.message_handler(commands=["a_help"])
def echo(m, res = False):
  bot.send_message(m.chat.id, '/about - немного про бота')
  bot.send_message(m.chat.id, '/contacts - ещё не допилил')
  bot.send_message(m.chat.id, '/txt - там свои фишки с текстом(8===D; phone; random; Vама')
  bot.send_message(m.chat.id, '/oz - оценка внешности')
  bot.send_message(m.chat.id, '/iq - оценка ума')
  bot.send_message(m.chat.id, '/ashka - рандом аш')
  bot.send_message(m.chat.id, '/monetka - монетка')
  bot.send_message(m.chat.id, '/chern - пасхл')
  bot.send_message(m.chat.id, '/Game - игры')
  bot.send_message(m.chat.id, '/chlen - игры')
  bot.send_message(m.chat.id, '/mama - игры')
  bot.send_message(m.chat.id, '/random - игры')
  bot.send_message(m.chat.id, '/y21y - игры')
@bot.message_handler(commands=["help"])
def echo(m, res = False):
  bot.send_message(m.chat.id, '/about - немного про бота')
  bot.send_message(m.chat.id, '/contacts - ещё не допилил')
  bot.send_message(m.chat.id, '/txt - там свои фишки с текстом')
  bot.send_message(m.chat.id, '/oz - оценка внешности')
  bot.send_message(m.chat.id, '/iq - оценка ума')
  bot.send_message(m.chat.id, '/Game - игры')
@bot.message_handler(commands=["about"])
def about(m, res=False):
  bot.send_message(m.chat.id, 'Привет, я Charl. Моего создателя зовут Lolioo. Я создан ради веселья и хз чего ещё. Ну попробуй что нибудь')
@bot.message_handler(commands=["contacts"])
def contacts(m, res=False):
  bot.send_message(m.chat.id, '1110101000011111000011110101011110111100000011010111111')
@bot.message_handler(commands=["share"])
def share(m, res=False):
  bot.send_message(m.chat.id, 'share: https://t.me/Chalr_bot')
@bot.message_handler(commands = ['txt'])
def txt(m, res = False):
  @bot.message_handler(content_types = ['text'])
  def txt(message):
   if message.text == 'Погода':
     bot.send_message(m.chat.id, 'В разработке')
   elif message.text == 'Расписание':
     bot.send_message(m.chat.id, 'В разработке')
@bot.message_handler(commands = ['chlen'])
def chlen(m,res = False):
     a = 0
     while a < 100:
       a=a+10
       bot.send_message(m.chat.id, '8===)')
       bot.send_message(m.chat.id, '8===D ()')
@bot.message_handler(commands = ['phone'])
def phone(m,res = False):
      mark = ['xiomi','samsung','iphone', 'honor','oneplus','huawai']
      os = ['mi','ui','clean_android','ios']
      camera = ['1', 'none', '12','24','128']
      lagi = random.randint(0,100)
      a = random.choice(mark)
      b = random.choice(os)
      c = random.choice(camera)
      bot.send_message(m.chat.id, f'Марка: {a}')
      bot.send_message(m.chat.id, f'Оболочка: {b}')
      bot.send_message(m.chat.id, f'Камера: {c}')
      bot.send_message(m.chat.id, f'Процент лагов: {lagi}%')
@bot.message_handler(commands = ['random'])
def random(m,res = False):
     chislo = random.randint(0,256)
     bot.send_message(m.chat.id, f'Выпало число: {chislo}')       
@bot.message_handler(commands = ['mama'])
def mama(m,res = False):
    bot.send_message(m.chat.id, 'У тебя сдохла мать')
    bot.send_message(m.chat.id, "И некого мне ебать")
@bot.message_handler(commands = ['monetka'])
def monetka(m,res = False):
  a = random.randint(1,3)
  if a == 1:
       bot.send_message(m.cht.id, 'Решка!')
  elif a == 2:
       bot.send_message(m.chat.id, 'Орёл!')
  elif a == 3:
       bot.send_message(m.chat.id, '!!!РЕБРОМ!!!')
@bot.message_handler(commands = ['oz'])
def oz(m,res =False):
      a = random.randint(0, 100)
      i = 0           
      while i<100:
        i = i + 10
        bot.send_message(m.chat.id, f'Загрузка: {i}%')
      bot.send_message(m.chat.id, f'Вы красивы на: {a}%') 
@bot.message_handler(commands = ['iq'])
def iq(m, res = False):
    a = random.randint(0, 100)
    i = 0
    while i<100:
      i = i + 10
      bot.send_message(m.chat.id, f'Загрузка: {i}%')
    bot.send_message(m.chat.id, f'Вы умны на: {a}%') 
@bot.message_handler(commands = ['test1'])
def test1(m, res = False):
  bot.send_message(m.chat.id,'Здравствуйте, это тест на дед инайда!')
  bot.send_message(m.chat.id,'Нажми /ghoul')
  import time
  time.sleep(18)
  bot.send_message(m.chat.id,'Депресия в 0 лет(конч тот кто нажал)')
@bot.message_handler(commands=["ashka"])
def ashka(m, res = False):
  a = random.randint(0,1)
  if a == 0:
    bot.send_message(m.chat.id, 'Не дам')
  else:
    bot.send_message(m.chat.id, 'Дам')
@bot.message_handler(commands = ['ari'])
def ari(m,res =False):
  bot.send_message(m.chat.id, 'молодец нашла с меня желание!')
@bot.message_handler(commands = ['chern'])
def chern(m,res =False):
  bot.send_message(m.chat.id, 'Свободу чёрным!')
  i =0
  while i<100:
    i= i+10
    bot.send_message(m.chat.id, 'Свободу чёрным!')
@bot.message_handler(commands = ['gus'])
def gus(m,res =False):
  bot.send_message(m.chat.id, 'Гусь')
@bot.message_handler(commands = ['Game'])
def Game(m, res = False):
  @bot.message_handler(commands = ['y21y'])
  def y21y(message):
    i = 0
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = 'Взять', callback_data = 'yes')
    button2 = types.InlineKeyboardButton(text = 'Пасс', callback_data = 'no')
    markup.add(button1, button2)
    bot.send_message(m.chat.id, 'Что хотите сделать', reply_markup = markup)
    while i <= 21:     
      @bot.callback_query_handler(func = lambda call: True)
      def answer(call):
        if call.data == 'yes':
          i = i + random.randint(1,9)
          bot.send_message(call.message.chat.id, f'Счёт на данный момент: {i}')
        elif call.data == 'no':
          i = i+0
          bot.send_message(call.message.chat.id, f'Счёт на данный момент: {i}') 
@bot.message_handler(commands = ['Dengi'])
def Dengi(m,res =False):
  bot.send_message(m.chat.id, 'Пошёл нахуй, еврей')
  i = 0
  while i<100:
    i+=9
    bot.send_message(m.chat.id, 'Пошёл нахуй, еврей')
@bot.message_handler(commands = ['Oracle'])
def Oracle(m,res = False):
  pass
bot.infinity_polling()
bot.polling(none_stop=True, interval=0)  