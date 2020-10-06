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

    
    num = random.randint(10, 20)
    name += comment
    name = hashlib.sha224(name.encode('utf-8')).hexdigest()

    i = 0
    while(i < num):
        name += name[random.randint(0, len(name))]
        i+= 1
    finalS = 'Your safe password is: ' + name

    return finalS
