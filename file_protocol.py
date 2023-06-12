import json
import logging
import shlex
import base64
import os

from file_interface import FileInterface

"""
Fungsi utama dari kelas FileProtocol adalah memproses data yang diterima
dan menerjemahkannya untuk memeriksa apakah sesuai dengan protokol/aturan
yang telah ditentukan.

Data yang diterima dari klien awalnya dalam bentuk byte dan kemudian diubah
menjadi string sebelum diproses.

Kelas FileProtocol bertugas untuk mengolah data yang diterima dalam bentuk
string.
"""

class FileProtocol:
    def __init__(self):
        self.file = FileInterface()
    def proses_string(self, string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        c = shlex.split(string_datamasuk)
        try:
            c_request = c[0]
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            cl = getattr(self.file, c_request.strip().lower())(params)
            return json.dumps(cl)
        except Exception as e:
            print(e)
            return json.dumps(dict(status='ERROR', data='request tidak dikenali'))



if __name__=='__main__':

    fp = FileProtocol()
