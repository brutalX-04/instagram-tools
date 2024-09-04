# © 2023 by brutalID
# FB : Rizky Nurahman
# WA : 6289668033300
# IG : brutalid_



# MODULE
import os
import re
import sys
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs



# COLOR
p  = '\33[m' 		# DEFAULT
m  = '\x1b[0;91m' 	# RED 
k  = '\033[0;93m' 	# KUNING 
h  = '\x1b[0;92m' 	# HIJAU 


# CALLING
rs = requests.Session()
timer = datetime.now()
loop = 1
Succes = 0
Failled = 0

# CLEAR
def clear():
	if "win" in sys.platform.lower():
		os.system('cls')
	else:
		os.system('clear')


# CLASS BANNER
class banner:
	def __init__(self):
		self.banner()

	def banner(self):
		clear()
		print('┏┓┏┓┳┳┓   ┓\n ┃┃ ┃┃┃┏┓┏┫       © 2023\n┗┛┗┛┛ ┗┗┛┗┻       by%s XMod%s'%(h,p))
		print('*' * 25)


# CLASS LOGIN
class login:
	def __init__(self):
		banner()
		self.IGlogin()
		self.YHlogin()

	def IGlogin(self):
		try:
			IGcookies = input('Input Cookies IG : ')
			print('User IG : '+instagram().IGcheck({'cookie':IGcookies}))
			open('.IGcookies.txt', 'w').write(IGcookies)
		except:
			print('Failled Login IG')

	def YHlogin(self):
		try:
			YHcookies = input('Input Cookies YH : ')
			data = youlikehits().check({'cookie':YHcookies})
			print('User YH : '+data[0])
			open('.YHcookies.txt', 'w').write(YHcookies)
			time.sleep(3);menu()
		except:
			print('Failled Login YH')


# CLASS MENU
class menu:
	def __init__(self):
		banner()
		try:
			YHcookies = {'cookie': open('.YHcookies.txt', 'r').read()}
			IGcookies = {'cookie': open('.IGcookies.txt', 'r').read()}
			IGuser = instagram().IGcheck(IGcookies)
			Yhdata = youlikehits().check(YHcookies)
		except:
			login()
		print('User IG : %s%s%s'%(h, IGuser, p))
		print('User Yh : %s%s%s'%(h, Yhdata[0], p))
		print('User Vl : %s%s%s'%(h, Yhdata[2], p))
		print('Coin    : %s%s%s'%(h, Yhdata[1], p))
		print('*' * 25)
		print('1. Get Coin With Mission Follow IG')
		print('2. Change User Validasi')
		print('3. Swap Coin To Followers')
		pilih = input('Pilih : ')
		if pilih in ['01','1']:
			print('*' * 25)
			instagram().YHfoll(IGuser, YHcookies, IGcookies)
		elif pilih in ['02','2']:
			print('*' * 25)
			username = input('Input Username IG : ')
			instagram().IGremove(YHcookies)
			instagram().IGadd(username, YHcookies)
		elif pilih in ['03','3']:
			print('*' * 25)
			print('Input Ammount For 1 foll [ 1-30 ] coin')
			coin = input('Input Jumlah Coin : ')
			instagram().IGpayout(coin, YHcookies)


# CLASS YOULIKEHITS
class youlikehits:
	def __init__(self):
		pass

	def check(self, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'referer': 'https://www.youlikehits.com/instagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' }
			get = response = bs(rs.get('https://www.youlikehits.com/addinstagram.php', cookies=YHcookies, headers=headers).text, 'html.parser')
			data = get.find('div', id='userDiv')
			user = data.find('span', id='usernameDiv').find('b').text
			coin = data.find('span', id='currentpoints').text
			try:
				user_vl = re.search('</td></tr><tr><td><center><b>(.*?)</b><br/>', str(get)).group(1)
			except:
				user_vl = 'None'
			return user, coin, user_vl
		except:
			print('Failled User youlikehits')


# CLASS INSTAGRAM
class instagram:
	def __init__(self):
		pass

	def IGcheck(self, IGcookies):
		headers = { 'authority': 'www.instagram.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'dpr': '1', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' }
		get = rs.get('https://www.instagram.com/accounts/edit/', cookies=IGcookies, headers=headers).text
		try:
			user = re.search('"username\\\\":\\\\"(.*?)\\\\"', get).group(1)
			return user

		except:
			print('Failled Instagram User')

	def IGpayout(self, coin, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'referer': 'https://www.youlikehits.com/addinstagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-requested-with': 'XMLHttpRequest' }
			get = bs(rs.get('https://www.youlikehits.com/addinstagram.php?step=payout&payout=%s&rand=0.44175095134205344'%(coin), cookies=YHcookies, headers=headers).text, 'html.parser')
			if 'Payout Changed' in str(get):
				print('Succes Payout Followers')
			else:
				print('Failled Payout Followers')
		except:
			print('Failled Delete IG User')

	def IGremove(self, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'referer': 'https://www.youlikehits.com/addinstagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-requested-with': 'XMLHttpRequest' }
			get = bs(rs.get('https://www.youlikehits.com/addinstagram.php?step=remove', cookies=YHcookies, headers=headers).text, 'html.parser')
		except:
			print('Failled Delete IG User')

	def IGadd(self, username, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'referer': 'https://www.youlikehits.com/addinstagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-requested-with': 'XMLHttpRequest' }
			get = bs(rs.get('https://www.youlikehits.com/addinstagram.php?step=verify&uname=%s&rand=0.44175095134205344'%(username), cookies=YHcookies, headers=headers).text, 'html.parser')
		except:
			print('Failled Add IG User')

	def YHfoll(self, username, YHcookies, IGcookies):
		try:
			global loop,Succes,Failled
			headers = { 'authority': 'www.youlikehits.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'referer': 'https://www.youlikehits.com/earnpoints.php', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1' }
			get = bs(rs.get('https://www.youlikehits.com/instagram.php', cookies=YHcookies, headers=headers).text, 'html.parser')
			if 'Connect to Instagram' in str(get):
				self.IGadd(username, YHcookies)
			else:
				data = get.find_all('div', class_='follow')
				for data in data:
					print('\r ~ Running %s%s%s Succes : %s%s%s, Failled : %s%s%s '%(k,loop,p,h,Succes,p,m,Failled,p), end='')
					data = re.search('followuser\((.*?)\)', str(data)).group(1)
					self.YHverif(data, YHcookies)
					self.IGfoll(data, YHcookies, IGcookies)
					loop+=1
					print('*' * 25)
					print('\r ~ Running %s%s%s Succes : %s%s%s, Failled : %s%s%s '%(k,loop,p,h,Succes,p,m,Failled,p), end='')
					time.sleep(20)
				self.YHfoll(username, YHcookies, IGcookies)

		except:
			print('Failled Get List User')


	def IGfoll(self, data, YHcookies, IGcookies):
		try:
			global Failled
			header = { 'authority': 'www.instagram.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'max-age=0', 'dpr': '1', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' }
			get = rs.get('https://www.instagram.com/%s/'%(data.split(',')[1].replace("'","")), cookies=IGcookies, headers=header).text
			headers = { 'authority': 'www.instagram.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'dpr': '1', 'origin': 'https://www.instagram.com', 'referer': 'https://www.instagram.com/userarullove/', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-asbd-id': '129477', 'x-csrftoken': re.search('"csrf_token":"(.*?)"', str(get)).group(1), 'x-ig-app-id': '936619743392459', 'x-ig-www-claim': re.search('"claim":"(.*?)"', str(get)).group(1), 'x-instagram-ajax': '1008682084', 'x-requested-with': 'XMLHttpRequest' }
			datas = {
				'container_module': 'profile',
				'nav_chain': 'PolarisProfileRoot:profilePage:1:via_cold_start',
				'user_id': re.search('"id":"(.*?)"', get).group(1),
			}
			post = rs.post('https://www.instagram.com/api/v1/friendships/create/%s/'%(re.search('"id":"(.*?)"', get).group(1)), cookies=IGcookies, headers=headers, data=datas)
			if '200' in str(post.status_code):
				print('\rSucces Follow User : %s%s%s                '%(h, data.split(',')[1].replace("'",""), p))
				self.YHconfirm(data, YHcookies)

			else:
				print('\rFailled Follow User : %s%s%s               '%(m, data.split(',')[1].replace("'",""), p))
				self.YHskip(data, YHcookies)
				Failled+=1

		except Exception as e:
			print('\rFailled Follow User : %s%s%s                     '%(m, data.split(',')[1].replace("'",""), p))
			self.YHskip(data, YHcookies)
			Failled+=1


	def YHverif(self, data, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' }
			rs.get('https://www.youlikehits.com/instagramrender.php?uname=%s'%(data.split(',')[1].replace("'","")), cookies=YHcookies, headers=headers)
		except:
			print('Failled Verif Follow')

	def YHskip(self, data, YHcookies):
		try:
			headers = { 'authority': 'www.youlikehits.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'referer': 'https://www.youlikehits.com/instagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-requested-with': 'XMLHttpRequest' }
			rs.get('https://www.youlikehits.com/instagramfollow.php?step=skip&id=%s'%(data.split(',')[0].replace("'","")), cookies=YHcookies, headers=headers)
		except Exception as e:
			print(e)
			pass

	def YHconfirm(self, data, YHcookies):
		global Succes,Failled
		headers = { 'authority': 'www.youlikehits.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'content-type': 'application/x-www-form-urlencoded', 'referer': 'https://www.youlikehits.com/instagram.php', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Linux"', 'sec-fetch-dest': 'empty', 'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'x-requested-with': 'XMLHttpRequest' }
		get = rs.get('https://www.youlikehits.com/instagramfollow.php?id=%s&rand=%s'%(data.split(',')[0].replace("'",""),data.split(',')[2].replace("'","")), cookies=YHcookies, headers=headers)
		if 'Uh Oh' in get.text:
			print('%sFailled Get Reward%s'%(m, p))
			self.YHskip(data, YHcookies)
			Failled+=1

		elif 'Success!' in get.text:
			reward = re.search('You got (.*?) Points!', get.text).group(1)
			print('Succes Get %s%s%s Coin'%(h, reward, p))
			Succes+=1



menu()