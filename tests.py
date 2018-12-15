import unittest
import sqlite3
from dua import Cart


class TestCart(unittest.TestCase):

    def test_tambahProduk(self):
        obj = Cart()
        obj.tambahProduk('KODE1', 2)

        # now let's check it
        conn = sqlite3.connect('example.db')
        sql = "SELECT kode_produk, qty FROM cart WHERE kode_produk='KODE1'"
        c = conn.cursor()
        c.execute(sql)
        rows = c.fetchall()
        for row in rows:
            kode_produk = row[0]
            qty = row[1]

        self.assertEqual(kode_produk, 'KODE1')
        self.assertEqual(qty, 2)


if __name__ == '__main__':
    unittest.main()
