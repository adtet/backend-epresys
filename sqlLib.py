import mysql.connector
import json

def koneksi_sql():
    sql = mysql.connector.connect(host="localhost",user="root",password="",database="db_coba")
    return sql

def input_data_user(id,nim,username,jurusan,prodi,kelas,email,password):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("INSERT INTO `user_regist`(`id`, `nim`, `username`, `jurusan`, `prodi`, `kelas`, `email`, `pass`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(id,nim,username,jurusan,prodi,kelas,email,password))
    db.commit()

def cek_user(username,password):
    db = koneksi_sql()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM user_regist where username=%s and pass=%s",(username,password))
    c = cursor.fetchone()
    if c==None:
        return None
    else:
        return c[0]
