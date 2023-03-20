from pyrogram import Client
from colorama import Fore, init
import os
import time
from settings import name_accounts_file, name_LS_file, name_group_file, time_sleep, name_message_file
os.system("cls")
init()

magenta = Fore.MAGENTA
cyan = Fore.CYAN
red = Fore.RED
print(f"""
			{magenta}Telegram Piar

		{cyan}version: 1.0.0
		author: @Redpiar

		{magenta}links:
		channel: https://t.me/BotesForTelegram

		{red}CopyRight: @Redpiar
""")

dirname = os.path.dirname(__file__)
acc = open(f"{dirname}/files/{name_accounts_file}")
acc_load = acc.read().split(" ")

LS_chat = open(f"{dirname}/files/{name_LS_file}")
group_load = open(f"{dirname}/files/{name_group_file}")
message = open(f"{dirname}/files/{name_message_file}", "r", encoding="utf-8")
class Start:
	def __init__(self):
		self.colors = {
			"RED": Fore.RED,
			"MAGENTA": Fore.MAGENTA,
			"CYAN": Fore.CYAN,
			"GREEN": Fore.GREEN,
			"WHITE": Fore.WHITE
		}
		self.accounts = 2

	def Piar_LS(self):
		api_id = acc_load[0]
		api_hash = acc_load[1]
		content = message.read()
		while True:
			try:
				phone = acc_load[self.accounts]
			except IndexError:
				self.accounts = 2
				phone = acc_load[self.accounts]

			try:

				app = Client(f"{dirname}/start/{phone}", api_id=api_id, api_hash=api_hash)
				app.connect()
			except:
				pass
			try:
				app.send_message('me', "connect")
				print(f"{self.colors['CYAN']}connect in {phone}{self.colors['WHITE']}")
			except:
				code_hash = app.send_code(phone)
				print(f"{phone}")
				code = input("Enter Code: ")
				app.sign_in(phone, code_hash.phone_code_hash, code)
				print("log")
				app.send_message('me', "connect")
			for user in LS_chat:
				try:
					app.send_message(user, content)
					print(f"{self.colors['GREEN']}>> Send in user: {user}!{self.colors['WHITE']}")
				except Exception as e:
					print(f"{self.colors['RED']}[!] Error sending message in user: {user}{self.colors['WHITE']}")
					pass

				self.accounts += 1
				time.sleep(int(time_sleep))
				app.disconnect()
				break

	def Piar_Group(self):
		content = message.read()
		api_id = acc_load[0]
		api_hash = acc_load[1]
		while True:
			try:
				phone = acc_load[self.accounts]
			except IndexError:
				self.accounts = 2
				phone = acc_load[self.accounts]
			try:

				app = Client(f"{dirname}/start/{phone}", api_id=api_id, api_hash=api_hash)
				app.connect()
			except:
				pass
			try:
				app.send_message('me', "connect")
				print(f"{self.colors['CYAN']}connect in {phone}{self.colors['WHITE']}")
			except:
				code_hash = app.send_code(phone)
				print(f"{phone}")
				code = input("Enter Code: ")
				app.sign_in(phone, code_hash.phone_code_hash, code)
				print("log")
				app.send_message('me', "connect")

			for group_line in group_load:
				try:
					app.join_chat(group_line)
					print(f"{self.colors['GREEN']}>> Successful join in group: {group_line}{self.colors['WHITE']}")
				except:
					print(f"{self.colors['RED']}[!] Error join in group: {group_line}{self.colors['WHITE']}")
					pass
				try:
					app.send_message(group_line, content)
					print(f"{self.colors['GREEN']}>> Send message in group: {group_line}!{self.colors['WHITE']}")
				except Exception as e:
					print(f"{self.colors['RED']}[!] Error sending message in group: {group_line}{self.colors['WHITE']}")
					pass

				self.accounts += 1
				time.sleep(int(time_sleep))
				app.disconnect()
				break

	def information(self):
		LS = 0
		group = 0

		while True:
			try:
				acc_load[self.accounts]
				self.accounts += 1
			except IndexError:
				self.accounts -= 2
				break

		for LS_check in LS_chat:
			LS += 1

		for group_check in group_load:
			group += 1

		print(f"""
Accounts: {self.accounts}
LS_chats: {LS}
groups: {group}
""")

	def load(self):
		print(f"{self.colors['MAGENTA']}Select Option(1-3)")
		print("1. Piar Group\n2. Piar LS\n3. information\n")
		select = input("Enter the options(number): ")

		if select == "1":
			Start().Piar_Group()
		if select == "2":
			Start().Piar_LS()
		if select == "3":
			Start().information()



Start().load()