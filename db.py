import sqlite3


def ensure_connection(func):
	def inner(*args, **kwargs):
		with sqlite3.connect('anketa.db') as conn:
			res = func(*args, conn=conn, **kwargs)
		return res
	return inner


@ensure_connection
def init_db(conn, force: bool = False):
	c = conn.cursor()

	if force:
		c.execute('DROP TABLE IF EXISTS user_message')

	c.execute('''
		CREATE TABLE IF NOT EXISTS user_message(
			id          INTEGER PRIMARY KEY,
			user_id     INTEGER NOT NULL,
			name        TEXT NOT NULL,
			text        TEXT NOT NULL,
			time        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
			)
		''')

	conn.commit()


@ensure_connection
def add_message(conn, user_id: int, text: str, time: int, name: str):
	c = conn.cursor()
	c.execute('INSERT INTO user_message (user_id, name, text, time) VALUES (?, ?, ?, ?)', (user_id, name, text, time))
	conn.commit()


@ensure_connection
def count_messages(conn, user_id: int):
	c = conn.cursor()
	c.execute('SELECT COUNT(*) FROM user_message WHERE user_id = ?', (user_id, ))
	(res, ) = c.fetchall()
	return res


@ensure_connection
def list_messages(conn, user_id: int, limit: int = 10):
	c = conn.cursor()
	c.execute('SELECT id, text FROM user_message WHERE user_id = ? ORDER BY id DESC LIMIT ?', (user_id, limit))
	return c.fetchall()


def main():
	init_db()

if __name__ == '__main__':
	main()