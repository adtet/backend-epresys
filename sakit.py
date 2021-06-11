from flask import app
from sqlLib import get_email, get_matkul, get_jadwal, get_jurusan, get_kelas, get_main, get_matkul_late, get_nim, get_prodi, get_username, cek_present, insert_main
import flask
from flask import Flask, jsonify, request
from datetime import date, datetime
import calendar
app = Flask(__name__)

@app.route("/user/sakit", methods=['POST'])
def izin():
    json_data = flask.request.json
    if json_data == None:
        result = {"sakit":"Bad Request"}
        resp = jsonify(result)
        return resp, 507
    else:
        if 'id' not in json_data or 'matakuliah' not in json_data or 'dosen' not in json_data:
            result = {"sakit" : "Error Request"}
            resp = jsonify(result)
            return resp, 508
        else:
            id = json_data['id']
            matakuliah = json_data['matakuliah']
            dosen = json_data['dosen']
            time = datetime.now()
            tgl = date.today()
            tgl = tgl.strftime("%d%m%Y")
            day = datetime.strptime(tgl, '%d%m%Y').weekday()
            day = calendar.day_name[day]
            day = str(day)
            day = day.lower()
            if day == 'saturday' and day == 'sunday':
                result = {"sakit": "schedule nt available"}
                resp = jsonify(result)
                return resp, 509
            else:
                nim = get_nim(id)
                username = get_username(id)
                jurusan = get_jurusan(id)
                prodi = get_prodi(id)
                kelas = get_kelas(id)
                email = get_email(id)
                det = time.strftime("%d-%m-%Y")
                time = time.strftime("%H:%M:%S")
                info = "sakit"
                cek = cek_present(id, matakuliah, det)
                if cek == False:
                    result = {"sakit": "sudah absensi"}
                    resp = jsonify(result)
                    return resp, 602
                else:
                    insert_main(id, nim, username, jurusan, prodi, kelas, email, matakuliah, dosen, day, det, time, info)
                    result = {"sakit": "proses izin sakit berhasil"}
                    resp = jsonify(result)
                    return resp, 603

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9009)
    app.run(port=9009, debug=True)