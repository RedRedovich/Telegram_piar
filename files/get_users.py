from pyrogram import Client

api_id = 0 #api_id
api_hash = "api_hash"
phone = "phone"

app = Client(phone, api_id=api_id, api_hash=api_hash)
app.connect()

users = open("LS_chat.txt", "a")
for member in app.get_chat_members("username chat"):
	username = member.user.username
	users.write("\n@" + str(username))
users.close()