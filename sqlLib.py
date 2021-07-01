import mysql.connector
import json
import haversine
from haversine import strict_area
from mysql.connector import cursor

def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",user="root",password="",database="db_coba")
    return sql

def input_data_user(id,nim,username,jurusan,prodi,kelas,email,password,status):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `user_regist`(`id`, `nim`, `username`, `jurusan`, `prodi`, `kelas`, `email`, `pass`, `status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,nim,username,jurusan,prodi,kelas,email,password,status))
    db.commit()

def cek_user(username,password):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id,status FROM user_regist where username=%s and pass=%s",(username,password))
    c = cursor.fetchone()
    if c==None:
        return None
    else:
        return c

def cek_nim(nim):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `nim` FROM `user_regist` WHERE `nim`=%s",(nim,))
        c = cursor.fetchone()
    except(mysql.connector.Warning,mysql.connector.Error) as e:
        print(e)
        c = None
    if c==None:
        return False
    else:
        return True

def get_jadwal(kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT  `time_start`, `time_end`,  `matakuliah`, `dosen1`, `dosen2`, `dosen3`, `ruangan` FROM `schedule` WHERE `kelas`=%s AND `day`=LOWER(DAYNAME(CURDATE()))",(kelas,))
        rows = [x for x in cursor]  
        cols = [x[0] for x in cursor.description]
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        rows = []
        cols = []  
    datas = []  
    for row in rows:  
        data = {}  
        for prop, val in zip(cols, row):  
            data[prop] = val  
        datas.append(data)  
    for x in range(0,len(datas)):
        datas[x]['time_start'] = str(datas[x]['time_start'])
        datas[x]['time_end'] = str(datas[x]['time_end'])
    dataJson = json.dumps(datas)  
    return dataJson

def get_jadwal_dosen(nip):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `kelas`,`time_start`, `time_end`, `matakuliah`,`ruangan` FROM `schedule` WHERE `day` = LOWER(DAYNAME(CURDATE())) AND (`kode_dosen1`= %s OR `kode_dosen2`= %s OR `kode_dosen3`=%s)",(nip,nip,nip))
        rows = [x for x in cursor]  
        cols = [x[0] for x in cursor.description]
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        rows = []
        cols = []  
    datas = []  
    for row in rows:  
        data = {}  
        for prop, val in zip(cols, row):  
            data[prop] = val  
        datas.append(data)  
    for x in range(0,len(datas)):
        datas[x]['time_start'] = str(datas[x]['time_start'])
        datas[x]['time_end'] = str(datas[x]['time_end'])
    dataJson = json.dumps(datas)  
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
        "SELECT day,date,matakuliah,dosen1,dosen2,dosen3,time,info FROM main WHERE id=%s",
        (a, ))
    rows = [x for x in cursor]  #compare sql data to json
    cols = [x[0] for x in cursor.description]  #compare sql data to json
    datas = []  #compare sql data to json
    for row in rows:  #compare sql data to json
        data = {}  #compare sql data to json
        for prop, val in zip(cols, row):  #compare sql data to json
            data[prop] = val  #compare sql data to json
        datas.append(data)
    for i in range(0,len(datas)):
        datas[i]['date'] = str(datas[i]['date'])
        datas[i]['time'] = str(datas[i]['time'])
    dataJson = json.dumps(datas)  #compare sql data to json
    return dataJson  #compare sql data to json

def get_main_2(id):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `matakuliah`, `kelas`, `day`, `date`, `time`, `info` FROM `main2` WHERE id=%s",(id,))
        rows = [x for x in cursor]  
        cols = [x[0] for x in cursor.description]
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        rows = []
        cols = []  
    datas = []  
    for row in rows:  
        data = {}  
        for prop, val in zip(cols, row):  
            data[prop] = val  
        datas.append(data)  
    for x in range(0,len(datas)):
        datas[x]['time'] = str(datas[x]['time'])
        datas[x]['date'] = str(datas[x]['date'])
    dataJson = json.dumps(datas)  
    return dataJson

def cek_id_main(a):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM main where id=%s", (a, ))
    c = cursor.fetchall()
    if c == None:
        return False
    else:
        return True

def cek_id_main_dosen(id):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT  `id` FROM `main2` WHERE `id`=%s",(id,))
        c = cursor.fetchone()
    except(mysql.connector.Warning,mysql.connector.Error) as e:
        print(e)
        c = None
    if c==None:
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


def get_username(id):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT username FROM user_regist where id=%s", (id, ))
    c = cursor.fetchone()
    if c == None:
        return 0
    else:
        return c[0]


def get_matkul(kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT `matakuliah`, `dosen1`, `dosen2`,`dosen3` FROM `schedule` WHERE `kelas`=%s AND `day`= LOWER(DAYNAME(CURDATE())) AND time_start>=CURTIME() AND time_end>= CURTIME()",
        (kelas,))
    d = cursor.fetchone()
    if d == None:
        return None
    else:
        return d

def get_matkul_late(kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT `matakuliah`, `dosen1`, `dosen2`,`dosen3` FROM `schedule` WHERE `kelas`=%s AND `day`= LOWER(DAYNAME(CURDATE())) AND time_start<=CURTIME() AND time_end>= CURTIME()",
        (kelas,))
    d = cursor.fetchone()
    if d == None:
        return None
    else:
        return d

def get_matkul_dosen(nip,kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `kelas`, `matakuliah`,day FROM `schedule` WHERE (`kode_dosen1` = %s OR `kode_dosen2`=%s OR `kode_dosen3`=%s) AND kelas=%s AND time_start>=now() AND time_end>= CURTIME() HAVING `day`= LOWER(DAYNAME(CURDATE()))",(nip,nip,nip,kelas))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return None
    else:
        return c

def get_matkul_late_dosen(nip,kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `kelas`, `matakuliah`,day FROM `schedule` WHERE (`kode_dosen1` = %s OR `kode_dosen2`=%s OR `kode_dosen3`=%s) AND kelas = %s AND time_start<=CURTIME() AND time_end>= CURTIME() HAVING `day`= LOWER(DAYNAME(CURDATE()))",(nip,nip,nip,kelas))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return None
    else:
        return c

def cek_present(id,matakuliah):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
        "SELECT id FROM main where id=%s and matakuliah=%s and date= CURDATE()",
        (id,matakuliah))
    d = cursor.fetchone()
    if d == None:
        return True
    else:
        return False

def cek_present_dosen(id,matakuliah,kelas):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `id` FROM `main2` WHERE id=%s AND matakuliah=%s AND kelas=%s  AND `date` = CURDATE()",(id,matakuliah,kelas))
        c = cursor.fetchone()
    except(mysql.connector.Warning,mysql.connector.Error) as e:
        print(e)
        c = None
    if c ==None:
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

def insert_main(id, nim, username, kelas, matakuliah, dosen1, dosen2, dosen3, info):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute(
    "INSERT INTO `main`(`id`, `nim`, `username`, `kelas`, `matakuliah`, `dosen1`, `dosen2`, `dosen3`, `day`, `date`, `time`, `info`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,LOWER(DAYNAME(now())),now(),now(),%s)",(id, nim, username, kelas, matakuliah, dosen1, dosen2, dosen3, info))
    db.commit()

def insert_main_dosen(id,nim,username,matakuliah,kelas,info):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `main2`(`id`, `nip`, `username`, `matakuliah`, `kelas`, `day`, `date`, `time`, `info`) VALUES (%s,%s,%s,%s,%s,LOWER(DAYNAME(CURDATE())),now(),now(),%s)",(id,nim,username,matakuliah,kelas,info))
    db.commit()
    
def get_status(id):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT status FROM `user_regist` WHERE id = %s",(id,))
    c = cursor.fetchone()[0]
    return int(c)
    

def get_code_command_get_room(ruangan):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `nama_ruangan` FROM `tb_ruangan` WHERE `nama_ruangan`=%s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c==None:
        return -1
    else:
        if c[0] == "bengkel":
            return 0
        elif c[0] == "gedung a":
            return 1
        elif c[0] == "gedung p2t":
            return 2
        elif c[0] == "lab atas":
            return 3
        elif c[0] == "lab bawah":
            return 4
        else:
            return -2

def query_cek_ruangan_lab_bawah(ruangan,lat,lng):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `lat`,`lng` FROM `tb_ruangan` WHERE nama_ruangan = %s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        if ruangan!="lab bawah":
            return False
        else:
            latdb = float(c[0])
            lngdb = float(c[1])
            lat = float(lat)
            lng = float(lng)
            area_range = 0.01
            test = strict_area(lngdb,latdb,lng,lat,area_range)
            return test
            
def query_cek_ruangan_lab_atas(ruangan,lat,lng):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `lat`,`lng` FROM `tb_ruangan` WHERE nama_ruangan = %s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        if ruangan!="lab atas":
            return False
        else:
            latdb = float(c[0])
            lngdb = float(c[1])
            lat = float(lat)
            lng = float(lng)
            area_range = 0.01
            test = strict_area(lngdb,latdb,lng,lat,area_range)
            return test

def query_cek_ruangan_gedung_a(ruangan,lat,lng):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `lat`,`lng` FROM `tb_ruangan` WHERE nama_ruangan = %s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        if ruangan!="gedung a":
            return False
        else:
            latdb = float(c[0])
            lngdb = float(c[1])
            lat = float(lat)
            lng = float(lng)
            area_range = 0.01
            test = strict_area(lngdb,latdb,lng,lat,area_range)
            return test
        
def query_cek_ruangan_p2t(ruangan,lat,lng):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `lat`,`lng` FROM `tb_ruangan` WHERE nama_ruangan = %s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        if ruangan!="gedung p2t":
            return False
        else:
            latdb = float(c[0])
            lngdb = float(c[1])
            lat = float(lat)
            lng = float(lng)
            area_range = 0.01
            test = strict_area(lngdb,latdb,lng,lat,area_range)
            return test


def query_cek_ruangan_bengkel(ruangan,lat,lng):
    db = koneksi_sql()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT `lat`,`lng` FROM `tb_ruangan` WHERE nama_ruangan = %s",(ruangan,))
        c = cursor.fetchone()
    except(mysql.connector.Error,mysql.connector.Warning) as e:
        print(e)
        c = None
    if c == None:
        return False
    else:
        if ruangan!="bengkel":
            return False
        else:
            latdb = float(c[0])
            lngdb = float(c[1])
            lat = float(lat)
            lng = float(lng)
            area_range = 0.01
            test = strict_area(lngdb,latdb,lng,lat,area_range)
            return test

