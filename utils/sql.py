import sqlite3


def save_user(user_id, city):
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("""INSERT INTO users(user_id, city) 
                    VALUES('{user_id}', '{city}');""".format(user_id=user_id, city=city))
        conn.commit()
        return True
    except Exception as ex:
        print(ex)
        return False


def check_user(user_id):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    city = cur.execute("""SELECT city FROM users WHERE user_id='{user_id}';""".format(user_id=user_id))
    return city.fetchone()


def update_user(user_id, city):
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute("""UPDATE users SET city='{city}'
                        WHERE user_id='{user_id}';""".format(user_id=user_id, city=city))
    conn.commit()