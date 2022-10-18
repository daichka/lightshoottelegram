import os,requests,random,math,time,telebot


bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('кинь')

def gh1(nm):
	print('рандомисирую')
	v = 0
	v2 =0
	w2 =0
	bmk =0
	global bnm
	global bnm2
	bnm=[]
	bnm2 = []
	jp1 = 'abcdefghijklmnopqrstuvwxyz'
	jp = list(jp1)
	for i in range(nm):
		bnm.clear()
		v2 = 0
		print(i+1)
		for i in range(6):
			if i == 0:
				b = str(random.randint(1,9))
			else:
				b = str(random.randint(0,9))
			bnm.append(b)
		kn = random.randint(1,3)
		if kn == 1:
			b2 = str(random.choice(jp)+random.choice(jp)+random.choice(jp)+random.choice(jp)+random.choice(jp)+random.choice(jp))
		elif kn == 2:
			kdf =[random.choice(jp),bnm[5],random.choice(jp),bnm[1],random.choice(jp),bnm[3]]
			random.shuffle(kdf)
			b2 = str(kdf[0]+kdf[1]+kdf[2]+kdf[3]+kdf[4]+kdf[5])
		elif kn == 3:		
			b2 = str(bnm[0]+bnm[1]+bnm[2]+bnm[3]+bnm[4]+bnm[5])
		if len(bnm2) > 0:
			
			for i in range(len(bnm2)):
				
				if bnm2[i] == b2:
					v+=1
					v2 +=1
				else:
					pass
		else:
				pass
		if v2 == 0:
			bnm2.append(b2)
		else:
				pass
	if v != 0:
		gh1(v)
	print('фсо')
@bot.message_handler(commands=['start'])
def ghl3d(m):
	bot.send_message(m.chat.id, 'приет', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def ghld(m):
	if m.text.lower() == 'кинь':
		bot.send_message(m.chat.id, 'скок')
		bot.register_next_step_handler(m, yhb)


def yhb(m):
	try:
		v = int(m.text)
		gh1(v)
		for i in range(len(bnm2)):
			time.sleep(1.3)
			bot.send_photo(m.chat.id, "https://prnt.sc/"+bnm2[i], str(i+1)+' https://prnt.sc/'+bnm2[i])
	except:
		bot.send_message(m.chat.id, 'хуета')
		
bot.polling()
