import mysql.connector
try:
  vts = mysql.connector.connect(host="localhost",user="root",password="1234",
  database="ots"
  ); print("Bağlantı tamam:")  

  try:
    secilen = vts.cursor()
    sqlkomutu = "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
    ekleneceklistesi = [
      ('Erhan KARA', '05425236587'),
      ('Burak MERT', '05325214587'),
      ('Alper TOY', '05364125896'),
      ('Ensar GÜL', '05415236541'),
      ('Irmak SAKA', '05426324156'),
      ('Aydın AKA', '05336254158'),
      ('Enes BOZ',  '05465287412'),
      ('Eren SOLAK',  '05075368541'),
      ('Halil Cem AK', '05326325412'),
      ('Yiğit GÜLLÜ',  '05336335241'),
      ('Berkay ÜNLÜ', '05236982544'),
      ('Esma SARI',   '05085236541'),
      ('Arda DOĞRU',   '05436589562'),
      ('Ahmet YOLCU',  '05095236521')
    ]
    secilen.executemany(sqlkomutu, ekleneceklistesi)
    vts.commit()

    print("kayıt eklendi.")
  except mysql.connector.Error as hata:
    print(f"Hata : {hata}")  

except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
  print("Veritabanına bağlanırken bir hata oluştu.")


