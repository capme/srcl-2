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

        # clean the table
        obj.hapusSemuaProduk()
        obj.close()

    def test_hapusProduk(self):
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

        # then hapus produk KODE1
        obj.hapusProduk('KODE1')

        # check that out
        sql = "SELECT COUNT(kode_produk) FROM cart WHERE kode_produk='KODE1'"
        c = conn.cursor()
        numrows = c.execute(sql).fetchone()[0]

        self.assertEqual(numrows, 0)

        # clean the table
        obj.hapusSemuaProduk()
        obj.close()


if __name__ == '__main__':
    unittest.main()
