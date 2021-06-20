import mysql.connector
import json

def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",user="root",password="",database="db_coba")
    return sql

def input_data_user(id,nim,username,jurusan,prodi,kelas,email,password,status):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `user_regist`(`id`, `nim`, `username`, `jurusan`, `prodi`, `kelas`, `email`, `pass`,`status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,nim,username,jurusan,prodi,kelas,email,password,status))
    db.commit()

def cek_user(username,password):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM user_regist where username=%s and password=%s",(username,password))
    c = cursor.fetchone()
    if c==None:
        return None
    else:
        return c[0]


def get_jadwal(kelas,day):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT  `jamstart`, `menitstart`, `jamend`, `menitend`, `matakuliah`, `dosen`  FROM `schedule` WHERE `kelas`=%s AND `day`=%s",(kelas,day))
    rows = [x for x in cursor]  #compare sql data to json
    cols = [x[0] for x in cursor.description]  #compare sql data to json
    datas = []  #compare sql data to json
    for row in rows:  #compare sql data to json
        data = {}  #compare sql data to json
        for prop, val in zip(cols, row):  #compare sql data to json
            data[prop] = val  #compare sql data to json
        datas.append(data)  #compare sql data to json
    dataJson = json.dumps(datas)  #compare sql data to json
    return dataJson

def get_kelas(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT `kelas` FROM `user_regist` WHERE id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]

def get_main(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT day,date,matakuliah,dosen,time,info FROM main WHERE id=%s",
        (a, ))
    rows = [x for x in cursor]  #compare sql data to json
    cols = [x[0] for x in cursor.description]  #compare sql data to json
    datas = []  #compare sql data to json
    for row in rows:  #compare sql data to json
        data = {}  #compare sql data to json
        for prop, val in zip(cols, row):  #compare sql data to json
            data[prop] = val  #compare sql data to json
        datas.append(data)  #compare sql data to json
    dataJson = json.dumps(datas)  #compare sql data to json
    return dataJson  #compare sql data to json

def cek_id_main(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM main where id=%s", (a, ))
    c = cursor.fetchall()
    if c == None:
        return False
    else:
        return True

def get_kelas(a):
    db =koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT `kelas` FROM `user_regist` WHERE id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]

def get_email(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT email FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]


def get_nim(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT nim FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]


def get_jurusan(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT jurusan FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]


def get_prodi(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT prodi FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]

def get_username(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT username FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]


def get_matkul(a, b, c):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT matakuliah,dosen FROM schedule where kelas=%s and day=%s and time>=%s and end>=%s",
        (a, b, c, c))
    d = cursor.fetchone()
    if d == None:
        return 0
    else:
        return d

def get_matkul_late(a, b, c):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT matakuliah,dosen FROM schedule where kelas=%s and day=%s and time<=%s and end>=%s",
        (a, b, c, c))
    d = cursor.fetchone()
    if d == None:
        return 0
    else:
        return d

def cek_present(a, b, c):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM main where id=%s and matakuliah=%s ,date=%s",
        (a, b, c))
    d = cursor.fetchone()
    if d == None:
        return True
    else:
        return False

def cek_id(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM user_regist where id=%s", (a, ))
    c = cursor.fetchone()
    if c == None:
        return False
    else:
        return True

def insert_main(a, b, c, d, e, f, g, h, i, j, k, l, m):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
    "INSERT INTO `main`(`id`, `nim`, `username`, `jurusan`, `prodi`, `kelas`, `email`, `matakuliah`, `dosen`,`day`,`date` ,`time`, `info`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (a, b, c, d, e, f, g, h, i, j, k, l, m))
    db.commit()

def cek_present(a, b, c):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM main where id=%s and matakuliah=%s and date=%s",
        (a, b, c))
    d = cursor.fetchone()
    if d == None:
        return True
    else:
        return False


       
