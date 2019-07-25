import mysql.connector


class Mysql:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="db", port=3306, user="root", password="root", database="tennis_court"
        )

    def close(self):
        self.conn.close

    def get(self, date, court_number, term_number):
        cur = self.conn.cursor(buffered=True)
        sql = f"select * from court_availability where date = '{str(date)}' and court_number = {court_number}"
        print(sql)
        cur.execute(sql)
        res = cur.fetchall()

        if not res:
            return None

        return bool(res[0][term_number + 2])

    def create(self, date, court_number, term_number, availability):
        cur = self.conn.cursor(buffered=True)
        sql = f"insert into court_availability (date, court_number, term{term_number}) values ('{str(date)}', {court_number}, {availability})"
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        return True

    def update(self, date, court_number, term_number, availability):
        cur = self.conn.cursor(buffered=True)
        sql = f"update court_availability set term{term_number}={availability}  where date = '{str(date)}' and court_number = {court_number}"
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        return True


if __name__ == "__main__":
    mysql = Mysql()
    print(mysql.get("2019-07-26", 1, 1))
    # mysql.get(self, date, court_number)
