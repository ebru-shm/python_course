import mysql.connector
try:
  vts = mysql.connector.connect(host="localhost",user="root",password="1234",
  database="ots"
  ); print("Bağlantı tamam:")  

  try:
    secilen = vts.cursor()
    # secilen.execute("CREATE TABLE ogrenciler (ad VARCHAR(50), telefon VARCHAR(30))")
    secilen.execute("INSERT INTO ogrenciler (id,ad, telefon) VALUES (2,'Buse VAROL', '5336325412')")
    vts.commit()

    print("kayıt eklendi.")
  except mysql.connector.Error as hata:
    print(f"Hata : {hata}")  

except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
  print("Veritabanına bağlanırken bir hata oluştu.")


