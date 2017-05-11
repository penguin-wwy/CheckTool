import hashlib
from Manager import *
class Check(object):
    def __init__(self):
        #self.md5 = hashlib.md5()
        #self.sha1 = hashlib.sha1()
        #self.sha256 = hashlib.sha256()
        #self.sha512 = hashlib.sha512()
        self.model = {'MD5' : hashlib.md5, 'SHA1' : hashlib.sha1,
                      'SHA256' : hashlib.sha256, 'SHA512' : hashlib.sha512}
        self.manager = None

    def connect(self, manager):
        self.manager = manager

    def start_check(self, file_list, model):
        res = []
        for file in file_list:
            with open(file, 'rb') as fp:
                m = self.model[model](fp.read())
                data = m.hexdigest()
                res.append(data)

        if len(res) == 1:
            return res, True
        else:
            return res, res[0] == res[1]