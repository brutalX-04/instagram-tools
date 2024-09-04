from assets.config import headers
from faker import Faker
from datetime import datetime
import os, requests, json, re, sys, time, random


# -> Caller
faker = Faker("id_ID")
columns, lines = os.get_terminal_size()
time_now = datetime.now()
date = '%s-%s-%s'%(time_now.day,time_now.month,time_now.year)
file_path = 'data/accounts/%s.txt'%(date)


# -> Color
p  = '\33[m' 		# Default
m  = '\x1b[0;91m' 	# Red
k  = '\033[0;93m' 	# Yellow 
h  = '\x1b[0;92m' 	# Green


# -> Clear Terminal
def clear():
	if "win" in sys.platform.lower():
		os.system('cls')
	else:
		os.system('clear')


# -> Sleep printer
def sleep(delay):
	for i in range(delay):
		print('\rwait %s secconds, to continue'%(delay-i), end='')
		time.sleep(1)
		print('\r'+' '*columns,end='')

# -> Menu script
class menu():
	def __init__(self):
		self.banner()
		self.options()

	def banner(self):
		clear()
		print('┳┏┓                        *\n┃┃┓ ┏╋      © 2024         *\n┻┗┛━┗┗      by %sbrutalx%s     *'%(h,p))
		print('*' * 28)

	def options(self):
		try:
			print('Question:')
			count = int(input('  How many to create ?: '))
			delay = int(input('  Enter pause (seconds): '))

			for x in range(count):
				print('\r'+'*' * 28)
				create()
				
				if x+1 != count:
					sleep(delay)

		except Exception as e:
			print('\nError:',str(e))


# -> Procces create account
class create:
	def __init__(self):
		self.session = requests.Session()
		self.mail = fake_mail.mail()
		self.day = random.randint(1,28)
		self.month = random.randint(1,12)
		self.year = random.randint(1990,2004)
		self.name = faker.name()
		self.password = self.name.replace(' ','').replace('.','').replace(',','')+'1234'
		self.proxies = {'https': random.choice(open('assets/prox1.txt','r').readlines()).replace('\n','')}
		self.signup()

	# -> Home signup
	def signup(self):
		try:
			get = self.session.get('https://www.instagram.com/accounts/signup/email/', headers=headers.get(), proxies=self.proxies)
			open('data/response/res.txt','w').write(get.text)

			if len(get.text) != 0:
				self.machine_id = re.search('"machine_id":"(.*?)"', get.text).group(1)
				self.device_id = re.search('"device_id":"(.*?)"', get.text).group(1)
				self.csrf_token = re.search('"csrf_token":"(.*?)"', get.text).group(1)
				self.timestamp = re.search('"__spin_t":(.*?),', get.text).group(1)
				self.enc_password = '#PWD_INSTAGRAM_BROWSER:0:%s:%s'%(self.timestamp,self.password)

				self.header_post = headers.post()
				self.header_post.update({
					'x-csrftoken': self.csrf_token,
		            'x-ig-www-claim': '0',
		            'x-instagram-ajax': '1015957372',
		            'x-requested-with': 'XMLHttpRequest'
				})

				print('\rSucces get data', end='')
				self.check_email()

			elif get.status_code == 429:
				print('Response '+str(get.status_code)+': To many requests')

		except Exception as e:
			raise e


	# -> Check mail
	def check_email(self):
		try:
			header = self.header_post
			header.update({
				'referer': 'https://www.instagram.com/accounts/signup/email/'
			})
			data = {
				'email': self.mail,
			}

			post = self.session.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=header, data=data, proxies=self.proxies).json()
			open('data/response/res1.txt','w').write(str(post))

			if post['status'] == 'ok':
				print('\r'+' '*columns,end='')
				print('\rSucces check mail', end='')
				self.send_verify_email()

			else:
				print('\r'+' '*columns,end='')
				print('\rFailled check mail')

		except Exception as e:
			raise e


	# -> Get verify message
	def send_verify_email(self):
		try:
			header = self.header_post
			header.update({
				'referer': 'https://www.instagram.com/accounts/signup/email/'
			})
			data = {
			    'device_id': self.machine_id,
			    'email': self.mail
			}
			post = self.session.post('https://www.instagram.com/api/v1/accounts/send_verify_email/', headers=header, data=data, proxies=self.proxies).json()
			open('data/response/res2.txt','w').write(str(post))

			if post['status'] == 'ok':
				print('\r'+' '*columns,end='')
				print('\rSucces get verify code', end='')
				sleep(20)
				self.check_confirmation_code()

			else:
				print('\r'+' '*columns,end='')
				print('\rFailled send verify email')

		except Exception as e:
			raise e


	# -> Confirm code
	def check_confirmation_code(self):
		try:
			code = fake_mail.code(self.mail)
			if code:
				header = self.header_post
				header.update({
					'referer': 'https://www.instagram.com/accounts/signup/emailConfirmation/'
				})
				data = {
				    'code': code,
				    'device_id': self.machine_id,
				    'email': self.mail
				}
				post = self.session.post('https://www.instagram.com/api/v1/accounts/check_confirmation_code/', headers=header, data=data, proxies=self.proxies).json()
				open('data/response/res3.txt','w').write(str(post))

				if post['status'] == 'ok':
					print('\r'+' '*columns,end='')
					print('\rSucces confirm mail', end='')
					self.signup_code = post['signup_code']
					self.attemp()

				else:
					print('\rFailled confirm code')
			else:
				print('\r'+' '*columns,end='')
				print('\rCode not found')

		except Exception as e:
			raise e


	# -> Web create ajax attemp
	def attemp(self):
		try:
			header = self.header_post
			header.update({
				'referer': 'https://www.instagram.com/accounts/signup/name/'
			})
			data = {
			    'enc_password': self.enc_password,
			    'email': self.mail,
			    'first_name': self.name,
			    'username': '',
			    'seamless_login_enabled': '1'
			}
			post = self.session.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/', headers=header, data=data, proxies=self.proxies).json()
			open('data/response/res4.txt','w').write(str(post))

			if post['status'] == 'ok':
				print('\r'+' '*columns,end='')
				print('\rSucces create name', end='')
				self.username_suggestions = post['username_suggestions']
				self.check_age_eligibility()

			else:
				print('\r'+' '*columns,end='')
				print('\rFailled create name')

		except Exception as e:
			raise e


	# -> Check age eligibility
	def check_age_eligibility(self):
		try:
			header = self.header_post
			header.update({
				'referer': 'https://www.instagram.com/accounts/signup/birthday/'
			})
			data = {
			    'day': self.day,
			    'month': self.month,
			    'year': self.year
			}
			post = self.session.post('https://www.instagram.com/api/v1/web/consent/check_age_eligibility/', headers=header, data=data, proxies=self.proxies).json()
			open('data/response/res5.txt','w').write(str(post))
			if post['status'] == 'ok':
				print('\r'+' '*columns,end='')
				print('\rSucces check age eligibility', end='')
				self.web_create_ajax()

			else:
				print('\r'+' '*columns,end='')
				print('\rFailled check age')

		except Exception as e:
			raise e


	# -> Create account
	def web_create_ajax(self):
		try:
			header = self.header_post
			header.update({
				'referer': 'https://www.instagram.com/accounts/signup/username/'
			})
			data = {
			    'enc_password': self.enc_password,
			    'day': self.day,
			    'email': self.mail,
			    'first_name': self.name,
			    'month': self.month,
			    'username': self.username_suggestions[0],
			    'year': self.year,
			    'client_id': self.machine_id,
			    'seamless_login_enabled': '1',
			    'tos_version': 'row',
			    'force_sign_up_code': self.signup_code,
			}
			post = self.session.post('https://www.instagram.com/api/v1/web/accounts/web_create_ajax/', headers=header, data=data, proxies=self.proxies).json()
			open('data/response/res6.txt','w').write(str(post))

			cookies = ';'.join(['%s=%s'%(key,value) for key,value in self.session.cookies.get_dict().items()])
			if 'ds_user_id' in cookies:
				print('\r'+' '*columns,end='')
				print('\rCreate status: %sSucces%s'%(h,p))
				print('Name: %s%s%s'%(h,self.name,p))
				print('Email: %s%s%s'%(h,self.mail,p))
				print('Password: %s%s%s'%(h,self.password,p))
				print('Cookies: %s%s%s'%(h,cookies,p))
				open(file_path,'a').write('%s|%s|%s\n'%(self.mail,self.password,cookies))
				bot(self.session, self.proxies)

			elif post['account_created'] == False:
				errors = post['errors']
				if 'message' in str(errors):
					message = errors['__all__'][0]['message']
					print('\r'+' '*columns,end='')
					print('\rCreate status: %sFailled%s'%(m,p))
					print('Message: %s'%(message))

				else:
					print('\r'+' '*columns,end='')
					print('\rCreate status: %sFailled%s'%(m,p))

			else:
				print('\r'+' '*columns,end='')
				print('\rCreate status: %sFailled%s'%(m,p))

		except Exception as e:
			raise e


# -> Get random & code fake mail
class fake_mail:
    def mail():
        get = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1').json()

        return get[0]

    def code(email):
        login,domain = email.split("@")
        get = requests.get("https://www.1secmail.com/api/v1/?action=getMessages&login=%s&domain=%s"%(login,domain)).json()
        if get:
            subject = get[0]["subject"]
            code = re.search(r'(\d+)', subject).group(1)

            return code


# -> Bot after create
class bot:
	def __init__(self, session, proxies):
		self.proxies = proxies
		self.session = session
		print('\nBot status!')
		self.follow()


	# -> Follow owner account
	def follow(self):
		try:
			header = headers.get()
			header.update({
				'referer': 'https://www.instagram.com/'
			})
			get = self.session.get('https://www.instagram.com/brutalid_/following/', headers=header, proxies=self.proxies)

			header1 = headers.post()
			header1.update({
				'referer': 'https://www.instagram.com/brutalid_/following/',
			    'x-bloks-version-id': re.search('"versioningID":"(.*?)"', get.text).group(1),
			    'x-csrftoken': re.search('"csrf_token":"(.*?)"', get.text).group(1),
			    'x-fb-friendly-name': 'usePolarisFollowMutation',
			    'x-fb-lsd': re.search('"LSD",\[\],{"token":"(.*?)"', get.text).group(1)
			})

			data = {
			    'av': re.search('"actorID":"(.*?)"', get.text).group(1),
			    '__d': 'www',
			    '__user': '0',
			    '__a': '1',
			    '__req': 'u',
			    '__hs': re.search('"haste_session":"(.*?)"', get.text).group(1),
			    'dpr': '2',
			    '__ccg': re.search('"connectionClass":"(.*?)"', get.text).group(1),
			    '__rev': re.search('"client_revision":(.*?),', get.text).group(1),
			    '__s': '',
			    '__hsi': re.search('"hsi":"(.*?)"', get.text).group(1),
			    '__dyn': '',
			    '__csr': '',
			    '__comet_req': re.search('__comet_req=(.*?)&', get.text).group(1),
			    'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', get.text).group(1),
			    'jazoest': re.search('jazoest=(.*?)"', get.text).group(1),
			    'lsd': re.search('"LSD",\[\],{"token":"(.*?)"', get.text).group(1),
			    '__spin_r': re.search('"client_revision":(.*?),', get.text).group(1),
			    '__spin_b': re.search('"__spin_b":"(.*?)"', get.text).group(1),
			    '__spin_t': re.search('"__spin_t":(.*?),', get.text).group(1),
			    'fb_api_caller_class': 'RelayModern',
			    'fb_api_req_friendly_name': 'usePolarisFollowMutation',
			    'variables': '{"target_user_id":"%s","container_module":"profile","nav_chain":"PolarisProfilePostsTabRoot:profilePage:1:via_cold_start"}'%(re.search('"props":{"id":"(.*?)"', get.text).group(1)),
			    'server_timestamps': 'true',
			    'doc_id': '7275591572570580',
			}

			post = self.session.post('https://www.instagram.com/graphql/query', headers=header1, data=data, proxies=self.proxies).json()
			open('data/response/follow.txt','w').write(str(post))

			if post['status'] == 'ok':
				if 'errors' in str(post):
					print('\rFollow: %sFailled%s'%(m,p))

				else:
					print('\rFollow: %sSucces%s'%(h,p))

			else:
				print('\rFollow: %sFailled%s'%(m,p))

		except Exception as e:
			raise e


menu()