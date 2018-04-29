import sqlite3 as sql

conn = sql.connect('friends.db')

def creatDB():
	try:
		conn.execute("""
		CREATE TABLE friends
		(id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		ign TEXT,
		game TEXT
		)""")
	except Exception as e:
		print(e)

def addFriend():
	friendInfo = input("[name] [ign] [game]\ninfo: ").split()
	print("flag 1")
	if len(friendINFO != 3):
		print("flag 2")
		print("Please use the correct format")
	else:
		print("flag 3")
		try:
			print("flag 4")
			with conn:
				conn.execute("INSERT INTO friends(name,ign,game) VALUES (?,?,?)",friendINFO)
		except Exception as e:
			print(e)


if __name__ == "__main__":
	addFriend()
	conn.commit()
	conn.close()