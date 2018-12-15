import sqlite3


class Cart:
    def __init__(self):
        self.conn = sqlite3.connect('example.db')
        # create table cart if not exist
        sql = "CREATE TABLE IF NOT EXISTS cart (" \
              "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
              "kode_produk VARCHAR(255) UNIQUE, " \
              "qty INT)"
        self.c = self.conn.cursor()
        self.c.execute(sql)
        self.conn.commit()

    def tambahProduk(self, kodeProduk, kuantitas):
        sql = "INSERT INTO cart(kode_produk, qty) values ('{}', {})" \
              "ON CONFLICT(kode_produk)" \
              "DO UPDATE SET qty=qty+{}".format(kodeProduk, kuantitas, kuantitas)
        self.c.execute(sql)
        self.conn.commit()

    def hapusProduk(self, kodeProduk):
        sql = "DELETE FROM cart WHERE kode_produk='{}'".format(kodeProduk)
        self.c.execute(sql)
        self.conn.commit()

    def tampilkanCart(self):
        sql = "SELECT kode_produk, qty FROM cart"
        self.c.execute(sql)
        rows = self.c.fetchall()
        str = ""
        for row in rows:
            if str == "":
                str = "{} ({})".format(row[0], row[1])
            else:
                str = "\n{} ({})".format(row[0], row[1])

        print(str)


# obj = Cart()
# obj.tambahProduk('KODE1', 2)
# obj.hapusProduk('KODE1')
# obj.tambahProduk('KODE2', 3)
# obj.tampilkanCart()
