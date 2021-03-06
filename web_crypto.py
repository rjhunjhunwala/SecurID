import rsa
from rsa import *
import urllib.request
import base64
from flask import Flask

app = Flask(__name__)

def get_private_key():
    return eval(open("private.txt", 'r').read())

def get_public_key():
    return eval(open("public.txt",'r').read())

def is_valid_text(str):
    try:
        rsa.verify(str.splitlines()[0].encode("utf-8"), eval(str.splitlines()[1]), get_public_key())
        return True
    except Exception as e:
        print(e)
        return False
def get_signed_text(st):
    return st+'\n' + str((rsa.sign_hash(rsa.compute_hash(st.encode("utf-8"),"SHA-256"),get_private_key(),"SHA-256")))
    # return st+'\n' + str(base64.b64encode(rsa.sign_hash(rsa.compute_hash(st.encode("utf-8"),"SHA-256"),get_private_key(),"SHA-256")))

@app.route('/<id>')
def get_output(id):
    try:
        return str(is_valid_text(urllib.request.urlopen("https://raw.githubusercontent.com/rjhunjhunwala/SecurID/master/"+id).read().decode("utf-8")))
    except Exception as e:
        return str("Hello, World!"+str(e))
