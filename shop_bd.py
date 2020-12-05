import sqlite3

order_id = None
ad = {'nci': None, 'None': 0}
goods = ['maika3d', 'boots']
basket = {'maika3d': None, 'boots': None, 'empty': False}
basket1 = []
basket2 = []


class user:

    def add_user(self, user_id, paid, delivar, taken, maika3d, Boots):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        curs.execute('INSERT or IGNORE INTO stat_order(user_id, paid, delivar, taken) VALUES(?, ?, ?, ?)', (user_id, paid, delivar, taken, ))
        curs.execute('INSERT or IGNORE INTO order_basket(user_id, maika3d, Boots) VALUES(?, ?, ?)', (user_id, maika3d, Boots))
        curs.execute('INSERT or IGNORE INTO User(user_id) VALUES(?)', (user_id, ))
        connect.commit()
        connect.close()

    def check_user(self, user_id):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        result = curs.execute('SELECT * FROM User WHERE  user_id = ?', (user_id, )).fetchall()
        print(result)
        return result

    def clearBasket(self, user_id):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        curs.execute('UPDATE `order_basket` SET `maika3d` = 0, `Boots` = 0 WHERE user_id = ?', (user_id, ))
        connect.commit()
        connect.close()

    def add_to_bask(self, user_id):
        pass

    def add_maika(self, user_id, count):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        nc = cursor.execute('SELECT `tie_de` FROM `order_composition` WHERE `user_id` = ?', (user_id, )).fetchone()
        print(nc)
        cursor.execute('UPDATE `order_composition` SET `tie_de` = ? WHERE `user_id` = ?', (count+nc[0], user_id))
        conn.commit()
        conn.close()

    def add_boots(self, user_id, count):
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        res = cursor.execute('SELECT `maika3d` FROM `order_basket` WHERE `user_id` = ?', (user_id, )).fetchone()
        print(res)
        cursor.execute('UPDATE `order_basket` SET `maika3d` = ? WHERE `user_id` = ?', (count+res[0], user_id))
        conn.commit()
        conn.close()

    def paid(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `paid` = 1 WHERE `user_id` = ?', (user_id, ))
        conn.commit()
        conn.close()


    def delivared(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `delivared` = 1 WHERE `user_id` = ?', (user_id, ))
        conn.commit()
        conn.close()

    def carried(self, user_id):
        conn = sqlite3.connect('db.db')
        curs = conn.cursor()
        curs.execute('UPDATE `stat_order` SET `taken` = 1 WHERE `user_id` = ?', (user_id, ))
        res = curs.execute('SELECT `taken` FROM `stat_order` WHERE `user_id` = ?', (user_id, )).fetchone()
        print(res)
        conn.commit()
        conn.close()

    def notcarried(self, taken=False):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        curs.execute('INSERT or IGNORE INTO stat_order (taken) VALUES (?)', (taken, ))

    def check_stat(self, taken):
        connect = sqlite3.connect('db.db')
        curs = connect.cursor()
        result = curs.execute('SELECT taken FROM stat_order WHERE taken = ?', (taken, )).fetchone()
        print(result)
        return result


