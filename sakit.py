from flask import app
from sqlLib import cek_id, get_email, get_matkul, get_jadwal, get_kelas, get_main, get_matkul_late, get_nim,  get_username, cek_present, insert_main
from sqlLib import get_status,cek_present_dosen,insert_main_dosen
import flask
from flask import Flask, jsonify, request
from datetime import date, datetime
import calendar
app = Flask(__name__)

@app.route("/user/sakit", methods=['POST'])
def izin():
    json_data = flask.request.json
    if json_data == None:
        result = {"izin":"Bad Request"}
        resp = jsonify(result)
        return resp, 400
    else:
        if 'id' not in json_data or 'matakuliah' not in json_data:
            result = {"sakit" : "Error Request"}
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
                result = {"sakit": "schedule not available"}
                resp = jsonify(result)
                return resp, 404
            else:
                cek_user = cek_id(id)
                if cek_user==False:
                    result = {"sakit": "schedule forbidden"}
                    resp = jsonify(result)
                    return resp, 403
                else:
                    status = get_status(id)
                    info = "sakit"
                    nim = get_nim(id)
                    username = get_username(id)
                    if status==0:
                        if 'dosen1' not in json_data or 'dosen2' not in json_data or 'dosen3' not in json_data:
                            result = {"sakit" : "Error Request Student"}
                            resp = jsonify(result)
                            return resp, 401
                        else:
                            dosen1 = json_data['dosen1']
                            dosen2 = json_data['dosen2']
                            dosen3 = json_data['dosen3']             
                            kelas = get_kelas(id)
                            cek_mahasiswa = cek_present(id,matakuliah)
                            if cek_mahasiswa == False:
                                result = {"sakit": "sudah absensi"}
                                resp = jsonify(result)
                                return resp, 203
                            else:
                                insert_main(id, nim, username,kelas,matakuliah,dosen1,dosen2,dosen3,info)
                                result = {"sakit": "proses izin sakit berhasil"}
                                resp = jsonify(result)
                                return resp, 200
                    else:
                        if 'kelas' not in json_data:
                            result = {"sakit" : "Error Request Lecture"}
                            resp = jsonify(result)
                            return resp, 401
                        else:
                            kelas_ngajar = json_data['kelas']
                            cek_dosen = cek_present_dosen(id,matakuliah,kelas_ngajar)
                            if cek_dosen==False:
                                result = {"sakit": "sudah presensi"}
                                resp = jsonify(result)
                                return resp, 203
                            else:
                                insert_main_dosen(id,nim,username,matakuliah,kelas_ngajar,info)
                                result = {"sakit": "proses izin sakit berhasil"}
                                resp = jsonify(result)
                                return resp, 200

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9009)
    app.run(port=9009, debug=True)