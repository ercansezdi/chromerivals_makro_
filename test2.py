import sqlite3


baglan = sqlite3.connect("file\\attachments.db")
veri = baglan.cursor()
rows = veri.execute("SELECT * FROM attachments WHERE attachments_name=?", ("Ose",)).fetchone()
print(rows[1])