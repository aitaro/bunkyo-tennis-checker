import mysql.connector


class Mysql:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="db", port=3306, user="root", password="root"
        )

    def close(self):
        self.conn.close

    def get(self, date, court_number):
        cur = cnx.cursor(buffered=True)
        sql = f"select * from court_availability where date = {str(date)} and court_number = {court_number}"
        print(sql)
        cur.execute(sql)

        # DATE, VALUE
        for (DATE, VALUE) in cur:
            print(DATE, VALUE)

        cur.close()
