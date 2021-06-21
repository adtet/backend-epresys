from flask import app
from sqlLib import cek_id, get_email, get_matkul, get_jadwal, get_jurusan, get_kelas, get_main, get_matkul_late, get_nim, get_prodi, get_status, get_username, cek_present, insert_main
from sqlLib import cek_present_dosen,insert_main_dosen
import flask
from flask import Flask, jsonify, request
from datetime import date, datetime
import calendar
app = Flask(__name__)

@app.route("/user/izin", methods=['POST'])
def izin():
    json_data = flask.request.json
    if json_data == None:
        result = {"izin":"Bad Request"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'id' not in json_data or 'matakuliah' not in json_data:
            result = {"izin" : "Error Request"}
            resp = jsonify(result)
            return resp, 401
        else:
            id = json_data['id']
            matakuliah = json_data['matakuliah']
            tgl = date.today()
            tgl = tgl.strftime("%d%m%Y")
            day = datetime.strptime(tgl, '%d%m%Y').weekday()
            day = calendar.day_name[day]
            day = str(day)
            day = day.lower()
            if day == 'saturday' and day == 'sunday':
                result = {"izin": "schedule not available"}
                resp = jsonify(result)
                return resp, 404
            else:
                cek_user = cek_id(id)
                if cek_user==False:
                    result = {"izin": "schedule forbidden"}
                    resp = jsonify(result)
                    return resp, 403
                else:
                    status = get_status(id)
                    info = "izin"
                    nim = get_nim(id)
                    username = get_username(id)
                    if status==0:
                        if 'dosen1' not in json_data or 'dosen2' not in json_data or 'dosen3' not in json_data:
                            result = {"izin" : "Error Request Student"}
                            resp = jsonify(result)
                            return resp, 401
                        else:
                            dosen1 = json_data['dosen1']
                            dosen2 = json_data['dosen2']
                            dosen3 = json_data['dosen3']             
                            kelas = get_kelas(id)
                            cek_mahasiswa = cek_present(id,matakuliah)
                            if cek_mahasiswa == False:
                                result = {"izin": "sudah absensi"}
                                resp = jsonify(result)
                                return resp, 203
                            else:
                                insert_main(id, nim, username,kelas,matakuliah,dosen1,dosen2,dosen3,info)
                                result = {"izin": "proses izin berhasil"}
                                resp = jsonify(result)
                                return resp, 200
                    else:
                        cek_dosen = cek_present_dosen(id,matakuliah)
                        if 'kelas' not in json_data:
                            result = {"izin" : "Error Request Lecture"}
                            resp = jsonify(result)
                            return resp, 401
                        else:
                            kelas = json_data['kelas']
                            if cek_dosen==False:
                                result = {"izin": "sudah presensi"}
                                resp = jsonify(result)
                                return resp, 203
                            else:
                                insert_main_dosen(id,nim,username,matakuliah,kelas,info)
                                result = {"izin": "proses izin berhasil"}
                                resp = jsonify(result)
                                return resp, 200
                        
if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9006)
    app.run(port=9006, debug=True)