import random

import telebot
from peewee import SqliteDatabase, AutoField, TextField, Model
from telebot import types

bot = telebot.TeleBot('5223141163:AAFzA01OXSX_BJSskrTB61GDDc6_OxePzU8')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start', 'help'])
def start(m, res=False):
    bot.send_message(m.chat.id, '/about - немного про бота')
    bot.send_message(m.chat.id, '/id - id пользователя')
    bot.send_message(m.chat.id, '/contacts - контакты создателя')
    bot.send_message(m.chat.id, '/txt - там свои фишки с текстом')
    bot.send_message(m.chat.id, '/ov - оценка внешности')
    bot.send_message(m.chat.id, '/iq - оценка ума')
    bot.send_message(m.chat.id, '/Game - игры')
    bot.send_message(m.chat.id, '/dis - кидаем дизлайк')
    bot.send_message(m.chat.id, '/l - кидаем лайк')
    bot.send_message(m.chat.id, '/dis18 - дизлайк 18 раз')
    bot.send_message(m.chat.id, '/rect - рандомная реакция')
    bot.send_message(m.chat.id, '/rasp - расписание')
    bot.send_message(m.chat.id, '/ghoul - я гуль')
    bot.send_message(m.chat.id, '/random - рандом')
    bot.send_message(m.chat.id, '/chlen - член')
    bot.send_message(m.chat.id, '/spas - СПАС')
    bot.send_message(m.chat.id, '/pes - рандомный трек')
    bot.send_message(m.chat.id, '/quq - рандомная цитата')


@bot.message_handler(commands=['litra'])
def litra(m, res=False):
    from bs4 import BeautifulSoup
    import requests as r
    url = 'https://obrazovaka.ru/books?ysclid=l6q32rf4ab7641521'
    req = r.get(url)
    bs = BeautifulSoup(req.text, 'html.parser')
    n = bs.find_all('div', class_='short__item')
    name = bs.find('a')
    print(n)


@bot.message_handler(commands=['quq'])
def quq(m, res=False):
    import random
    q = ['Вас делают похожими, чтобы управлять вами. Когда начинается война, вас превращают в патриотов.',
         'Дети могут учиться всему уже в том возрасте, когда вы им сказки читаете. «Овечка встретил коровку. «Му-му», — сказала коровка. «Бе-бе», — ответила овечка. Вы забиваете голову ребенка этим дерьмом и хотите, чтобы он вырос разумным?',
         'Мы либо научимся жить вместе, либо погибнем по одиночке.',
         'Взглянув на небо, просто скажите: «Я не знаю, откуда все это», — и не сочиняйте небылицы.',
         'Самые богатые люди обычно болваны. Один такой как-то спросил меня: «Раз вы такой умный, что же вы не разбогатели». Я ответил: «Раз вы такой богатый, что же вы не поумнели?».',
         'Людям очень трудно научиться говорить «я не знаю».',
         'Я пытаюсь вернуть вам мозги, которые у вас забрали в школе и при воспитании. Я пытаюсь показать вам, как устроен мир. Так что, если вы хотите сделать лучше этот мир, пора оторвать задницу от дивана и сделать его лучше.',
         'Нет ничего плохого в том, чтобы соорудить нечто и понять, что оно не работает.',
         'После того как мы украли нужную нам землю, что кстати сделали и все остальные страны, мы вывесили заповедь: «Не кради».',
         'Если вы полагаете, что мир нельзя изменить, это лишь означает, что вы не один из тех, кто его изменит.',
         'Личности как таковой не существует. Все мы проекции нашей среды обитания. С этим трудно смириться, но это так.',
         'Когда государство ежегодно тратит 500 миллиардов долларов на оборонную промышленность и лишь два миллиарда на исследование среды нашего обитания, стоит задуматься, действительно ли на Земле существует разумная жизнь?',
         'Мы несправедливо заявляем, что человек — высшая ступень эволюции: этому учат в школе. Человек уничтожает океаны, рыбу, атмосферу и друг друга. Человек, пролетая над городом, нажимает на кнопку и сжигает всех жителей атомным оружием. Наивысшее ли он творение природы? Ещё нет, на мой взгляд. Нам предстоит долгий путь. Мы либо создадим рай на Земле, либо уничтожим себя и впадём в забвение. Только будущее даст ответ. Каким оно будет — зависит от нас.',
         'Они действительно верят в то, что какой-то парень, сидя на небесах, создал мужчину и женщину, поместил их в чудесной красоты сад и, конечно же, потом вышвырнул их оттуда. И этот парень любит всех и вся, между прочим.',
         'Когда на пути евреев встретилось Красное море, Моисей поднял свой посох и воды расступились, чтобы они смогли перейти на другую сторону. Вообще-то, Бог смог бы перенести их туда и не разделяя воды.']
    rando = random.choice(q)
    bot.send_message(m.chat.id, f'{rando}\n Жак Фреско')

@bot.message_handler(commands=['pog'])
def pog(m, res=False):
    import json
    import requests as r
    from os import environ
    from bs4 import BeautifulSoup

    url = 'https://yandex.ru/'
    req = r.get(url)

    bs = BeautifulSoup(req.text, 'html.parser')

    temp = bs.find('div', class_='weather__temp')
    bot.send_message(m.chat.id, f'Сейчас в Санкт-Петербурге {temp.text}')

    temp_n = bs.find('a',
                     class_='home-link2 weather__forecast-link home-link2_color_inherit home-link2_hover_red')

@bot.message_handler(commands=['i'])
def send_welcome(m, res=False):
    import random
    import requests as r
    from bs4 import BeautifulSoup

    url = 'https://drochkino.vip/ru/categories'
    req = r.get(url)
    bs = BeautifulSoup(req.text, 'html.parser')
    title = bs.find_all('a', class_='d-block')
    ran = random.randint(1, 56)
    link = title[ran].get('href')
    bot.send_message(m.chat.id, f'{title[ran].get_text() + link}')


@bot.message_handler(commands=['id'])
def id(m, res=False):
    a = m.from_user.id
    bot.send_message(m.chat.id, f'Ваш id: {a}')


@bot.message_handler(commands=['pes'])
def pes(m, res=False):
    import random
    pesn = ['C:/Users/Games/Desktop/My_project/charl8/musik/13Kai_Kassi_-_Stoner_feat_FLESH.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Djizus_-_Alone_In_This_World.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/FLESH_-_HOTBOX.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/FLESH_-_INTERNAL_2_.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/ FLESH_-_INTERNAL_2_.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/FLESH_-_Ona_Bez_Tormozov_.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/FLESH_-_UBIVAYUS_YADOM.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/LILDRUGHILL_-_Harakter.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/LILDRUGHILL_LIZER_Otdaj_sebya.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/LILDRUGHILL_ROCKET_MARCO_9_Tajnaya_Komnata.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/MARCO_9_ROCKET_LILDRUGHILL_Trep_Alligator.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/May_Wave_-_CHempion.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/May_Wave_-_Lyubi_Menya_Poka_Tut_YA.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/May_Wave_-_Vaib.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/May_Wave_-_Zanovo_2.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Neverlove_-_Bez_lifaka.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Neverlove_-_Kussen.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/WhyBaby___Hleb_-_Kiska.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Yanix_-_Mamasita.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_BLOKBOY.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_DESERT_IGOR.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_MOLCHALIVYIY_BOB.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_PORNO_FLOW.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_YATREK.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/zxcursed_-_killua.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/MEYBI_BEYBI_-_AHEGAO.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/GONE.Fludd_-_PATSANYI_II.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Gone.Fludd_IROH_-_VKUS_YADA.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/Dora_feat_MEIBI_BEIBI_-_Barbisaiz.mp3',
            'C:/Users/Games/Desktop/My_project/charl8/musik/YAMAUGLI_-_NYAM_NYAM.mp3']
    rando = random.choice(pesn)
    audio = open(rando, 'rb')
    bot.send_audio(m.chat.id, audio)
    audio.close()


@bot.message_handler(commands=['spas'])
def spas(m, res=False):
    bot.send_message(m.chat.id, 'КАНАЛ СПАС СПАСИ СВОЮ ДУШУ И ПОСТАВЬ ДУШУ МАТЕРИ!')


@bot.message_handler(commands=["dis"])
def dis(m, res=False):
    bot.send_message(m.chat.id, '👎')


@bot.message_handler(commands=["l"])
def l(m, res=False):
    bot.send_message(m.chat.id, '👍')


@bot.message_handler(commands=["dis18"])
def l18(m, res=False):
    i = 0
    while i < 100:
        bot.send_message(m.chat.id, '👎')
        i += 8


@bot.message_handler(commands=["admin"])
def admin(m, res=False):
    i = 0
    while i < 100:
        bot.send_message(m.chat.id, 'Админ говно!!!!')
        i += 8


@bot.message_handler(commands=["rt"])
def rt(m, res=False):
    i = 0
    while i < 100:
        bot.send_message(m.chat.id, 'Рита бот')
        i += 10


@bot.message_handler(commands=['chlen'])
def chlen(m, res=False):
    a = 0
    while a < 100:
        a = a + 10
        bot.send_message(m.chat.id, '8===)')
        bot.send_message(m.chat.id, '8===D ()')


@bot.message_handler(commands=["ghoul"])
def ghoul(m, res=False):
    a = 1000
    while a > 0:
        a = a - 7
        b = a + 7
        bot.send_message(m.chat.id, f'{b}-7={a}')


# Запускаем бота
@bot.message_handler(commands=["news"])
def news(m, res=False):
    bot.send_message(m.chat.id,
                     'Что нового:\n Говорят что чарлику 18+ и что есть прикольная команда))) кто не понял рандомная подборочка \n Удаленны основные баги и доработаны старые функции\nТакже добавлена функция /pog - температура на улице в данный момент\n Charl v.1.5')


@bot.message_handler(commands=["anekdot"])
def anek(m, res=False):
    import requests as r
    from bs4 import BeautifulSoup

    url = 'https://www.anekdotovmir.ru/anekdoty-pro/anekdoty-pro-semyu/anekdoty-pro-vzroslyx/smeshnye-anekdoty-pro-vzroslyx/'
    req = r.get(url)

    bs = BeautifulSoup(req.text, 'html.parser')

    temp = bs.find_all('p')

    bot.send_message(m.chat.id, f'{temp}')


@bot.message_handler(commands=["rasp"])
def rasp(m, res=False):
    bot.send_message(m.chat.id,
                     'Пн:  \n 1)Биология \n 2)Русский \n 3)Литиратура \n 4)Алгебра \n 5)Обществознание \n 6)Геометрия')
    bot.send_message(m.chat.id,
                     'Вт:  \n 1)География \n 2)Информатика \n 3)Немецкий \n 4)Немеукий \n 5)Алгебра \n 6)Химия')
    bot.send_message(m.chat.id,
                     'Ср:  \n 1)Физ-ра \n 2)Немецкий \n 3)Русский \n 4)Немецкий \n 5)История \n 6)Литература')
    bot.send_message(m.chat.id, 'Чт:  \n 1)Русский \n 2)География \n 3)Немецкий \n 4)Немецкий \n 5)Физика \n 6)ОБЖ')
    bot.send_message(m.chat.id,
                     'Пт:  \n 1)Литиратура \n 2)Английский \n 3)Химия \n 4)Алгебра \n 5)Геометрия \n 6)Физ-ра')
    bot.send_message(m.chat.id,
                     'Суббота:  \n 1)Технология(Черчениие) \n 2)Физика \n 3)Геометрия \n 4)История \n 5)Физ-ра \n 6)Биология')


@bot.message_handler(commands=["rect"])
def rect(m, res=False):
    import random
    react = ['👍', '👎', '😂', '❤', '😢', '🤬', '🤮', '🖕', '🥵', '😵‍💫']
    a = random.choice(react)
    bot.send_message(m.chat.id, f'{a}')


@bot.message_handler(commands=["random"])
def random(m, res=False):
    import random
    a = random.randint(0, 10)
    bot.send_message(m.chat.id, f'Выпало число: {a}')


@bot.message_handler(commands=["phon"])
def phon(m, res=False):
    import random
    mark = ['xiomi', 'samsung', 'iphone', 'honor', 'oneplus', 'huawai']
    os = ['mi', 'ui', 'clean_android', 'ios']
    camera = ['1px', 'none', '12px', '24px', '128px']
    lag = random.randint(0, 100)
    a = random.choice(mark)
    b = random.choice(os)
    c = random.choice(camera)
    bot.send_message(m.chat.id, f'Марка: {a}')
    bot.send_message(m.chat.id, f'Оболочка: {b}')
    bot.send_message(m.chat.id, f'Камера: {c}')
    bot.send_message(m.chat.id, f'Процент лагов: {lag}%')


@bot.message_handler(commands=["a_help"])
def echo(m, res=False):
    bot.send_message(m.chat.id, '/about - немного про бота')
    bot.send_message(m.chat.id, '/contacts - ещё не допилил')
    bot.send_message(m.chat.id, '/txt - там свои фишки с текстом(8===D; phone; random; Vама')
    bot.send_message(m.chat.id, '/oz - оценка внешности')
    bot.send_message(m.chat.id, '/iq - оценка ума')
    bot.send_message(m.chat.id, '/ashka - рандом аш')
    bot.send_message(m.chat.id, '/monetka - монетка')
    bot.send_message(m.chat.id, '/gus - пасхл')
    bot.send_message(m.chat.id, '/ari - пасхл')
    bot.send_message(m.chat.id, '/chern - пасхл')
    bot.send_message(m.chat.id, '/katy - пасхл')
    bot.send_message(m.chat.id, '/Game - игры')


@bot.message_handler(commands=["about"])
def about(m, res=False):
    bot.send_message(m.chat.id,
                     'Привет, я Charl. Моего создателя зовут Lolioo. Я создан ради веселья и хз чего ещё. Ну попробуй что нибудь')


@bot.message_handler(commands=["contacts"])
def contacts(m, res=False):
    bot.send_message(m.chat.id, 'https://vk.com/kerohov')


@bot.message_handler(commands=["share"])
def share(m, res=False):
    bot.send_message(m.chat.id, 'share: https://t.me/Chalr_bot')


@bot.message_handler(commands=['txt'])
def txt(m, res=False):
    @bot.message_handler(content_types=['text'])
    def txt(message):
        if message.text == 'Погода':
            bot.send_message(m.chat.id, 'В разработке')
        elif message.text == 'Расписание':
            bot.send_message(m.chat.id, 'В разработке')
        elif message.text == '8===D':
            a = 0
            while a < 100:
                a = a + 10
                bot.send_message(m.chat.id, '8===)')
                bot.send_message(m.chat.id, '8===D ()')
        elif message.text == 'random':
            chislo = random.randint(0, 256)
            bot.send_message(m.chat.id, f'Выпало число: {chislo}')
        elif message.text == 'Мама':
            bot.send_message(m.chat.id, 'У тебя сдохла мать')
            bot.send_message(m.chat.id, "И некого мне ебать")


@bot.message_handler(commands=['monetka'])
def monetka(m, res=False):
    import random
    a = random.randint(1, 3)
    if a == 1:
        bot.send_message(m.cht.id, 'Решка!')
    elif a == 2:
        bot.send_message(m.chat.id, 'Орёл!')
    elif a == 3:
        bot.send_message(m.chat.id, '!!!РЕБРОМ!!!')


@bot.message_handler(commands=['ov'])
def ov(m, res=False):
    import random
    a = random.randint(0, 100)
    i = 0
    while i < 100:
        i = i + 10
        bot.send_message(m.chat.id, f'Загрузка: {i}%')
    bot.send_message(m.chat.id, f'Вы красивы на: {a}%')


@bot.message_handler(commands=['iq'])
def iq(m, res=False):
    import random
    a = random.randint(0, 100)
    i = 0
    while i < 100:
        i = i + 10
        bot.send_message(m.chat.id, f'Загрузка: {i}%')
    bot.send_message(m.chat.id, f'Вы умны на: {a}%')


@bot.message_handler(commands=['test1'])
def test1(m, res=False):
    bot.send_message(m.chat.id, 'Здравствуйте, это тест на дед инайда!')
    bot.send_message(m.chat.id, 'Нажми /ghoul')
    import time
    time.sleep(18)
    bot.send_message(m.chat.id, 'Депресия в 0 лет(конч тот кто нажал)')


@bot.message_handler(commands=["ashka"])
def ashka(m, res=False):
    import random
    a = random.randint(0, 1)
    if a == 0:
        bot.send_message(m.chat.id, 'Не дам')
    else:
        bot.send_message(m.chat.id, 'Дам')


@bot.message_handler(commands=['ari'])
def ari(m, res=False):
    bot.send_message(m.chat.id, 'молодец нашла с меня желание!')


@bot.message_handler(commands=['chern'])
def chern(m, res=False):
    bot.send_message(m.chat.id, 'Свободу чёрным!')
    i = 0
    while i < 100:
        i = i + 10
        bot.send_message(m.chat.id, 'Свободу чёрным!')


@bot.message_handler(commands=['gus'])
def gus(m, res=False):
    bot.send_message(m.chat.id, 'Гусь')


@bot.message_handler(commands=['magik'])
def magik(m, res=False):
    pass


@bot.message_handler(commands=['Game'])
def Game(m, res=False):
    @bot.message_handler(commands=['y21y'])
    def y21y(message):
        import random
        i = 0
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text='Взять', callback_data='yes')
        button2 = types.InlineKeyboardButton(text='Пасс', callback_data='no')
        markup.add(button1, button2)
        bot.send_message(m.chat.id, 'Что хотите сделать', reply_markup=markup)
        while i <= 21:
            @bot.callback_query_handler(func=lambda call: True)
            def answer(call):
                i = 0
                if call.data == 'yes':
                    a = random.randint(1, 9)
                    i = i + a
                    bot.send_message(call.message.chat.id, f'Счёт на данный момент: {i}')
                elif call.data == 'no':
                    i = i + 0
                    bot.send_message(call.message.chat.id, f'Счёт на данный момент: {i}')


@bot.message_handler(commands=['droch'])
def droch(m, res=False):
    bot.send_message(m.chat.id, 'Какой у тебя объём руки в членах?')
    a = m.text
    ob = int(a)
    bot.send_message(m.chat.id, 'Сколько людей в помещение?')
    b = m.text
    kol = int(b)
    tim = 300
    otv = kol * tim / ob
    sek = otv
    if sek > 60:
        min = sek // 60
        bot.send_message(m.chat.id, f'Вам понадобится: {min} минут')
    else:
        bot.send_message(m.chat.id, f'Вам понадобится: {sek} секунд')


@bot.message_handler(commands=['qr'])
def qr(m, res=False):
    bot.send_message(m.chat.id,
                     'Я знаю что это наврятли найдёт та которой это адресованно, это больше для души...\n Но если ты все же это читаешь то....\n Ты мне нравишься....')


@bot.message_handler(commands=['Dengi'])
def gus(m, res=False):
    bot.send_message(m.chat.id, 'Пошёл нахуй, еврей')
    i = 0
    while i < 100:
        i += 9
        bot.send_message(m.chat.id, 'Пошёл нахуй, еврей')


bot.infinity_polling()
bot.polling(none_stop=True, interval=0)
