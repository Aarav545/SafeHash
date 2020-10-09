from flask import Blueprint, render_template, request
from numpy import random
import hashlib
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/namename')
def namename():
    return render_template('namename.html')

@main.route('/namename', methods=['POST'])
def namename_post():
    name = request.form.get('name')
    comment = request.form.get('comment')

    
    num = random.randint(5, 10)
    name += comment
    name = hashlib.sha224(name.encode('utf-8')).hexdigest()
    wlist = '!@#$%^&*()-_'
    i = 0
    while(i < num):
        nnum = random.randint(0, len(name))
        if(name[nnum].isalpha()):
            name+=name[nnum]
            name += name[nnum].upper()
        else:
            name += name[random.randint(0, len(name))]
        i+= 1
    j = 0
    while(j < num):
        name+=wlist[random.randint(0, len(wlist))]
        j += 1
    finalS = 'Your safe password is: ' + name

    return finalS
