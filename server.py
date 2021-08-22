
# from flask import Flask
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def hello_world():
#     return 'Helloooo World'

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs....'

# @app.route('/blog/dog')
# def blog2():
#     return 'This is my dog!'



# from flask import Flask, render_template
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')

# # @app.route('/favicon.ico')
# # def blog():
# #     return 'These are my thoughts on blogs...'

# @app.route('/blog/2020')
# def blog2():
#     return 'This is my dog'

# from flask import Flask, render_template, url_for
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def hello_world():
#     print(url_for('static', filename='fav.ico.jpg'))
#     return render_template('index.html')


# @app.route('/about')
# def about():
#     return render_template('about.html')

# # @app.route('/favicon.ico')
# # def blog():
# #     return 'These are my thoughts on blogs...'

# @app.route('/blog/2020')
# def blog2():
#     return 'This is my dog'


# from flask import Flask, render_template, url_for
# app = Flask(__name__)
# print(__name__)

# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html',name=username)


# @app.route('/about')
# def about():
#     return render_template('about.html')

# # @app.route('/favicon.ico')
# # def blog():
# #     return 'These are my thoughts on blogs...'

# @app.route('/blog/2020')
# def blog2():
#     return 'This is my dog'

##adding variable url
# from flask import Flask, render_template, url_for
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

##dynamically adding variables
# from flask import Flask, render_template, url_for
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


#request data from browser
# from flask import Flask, render_template, url_for
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return 'form submitted, HOOORAY!'

##request data from browser using flask

# from flask import Flask,render_template,url_for,request
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         return 'Form Submitted!'
#     else:
#         return 'Something went wrong. Try again!'

##redirecting user after submitting info

# from flask import Flask,render_template,url_for,request,redirect
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again!'


####saving the data submitted to our database
# from flask import Flask,render_template,url_for,request,redirect
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)

# def write_to_file(data):
#     with open('database.txt',mode='a') as database:
#         email=data["email"]
#         subject=data["subject"]
#         message=data["message"]
#         file=database.write(f'\n{email},{subject},{message}')

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_file(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again!'

###saving data in a csv file
# from flask import Flask,render_template,url_for,request,redirect
# import csv
# app = Flask(__name__)
# print(__name__)

# @app.route('/')
# def my_home():
#     return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
#     return render_template(page_name)


# def write_to_file(data):
#     with open('database.csv',mode='a') as database:
#         email=data["email"]
#         subject=data["subject"]
#         message=data["message"]
#         file=database.write(f'\n{email},{subject},{message}')

# def write_to_csv(data):
#     with open('database.csv',newline='',mode='a') as database2:
#         email=data["email"]
#         subject=data["subject"]
#         message=data["message"]
#         csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
#         csv_writer.writerow([email,subject,message])

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         write_to_csv(data)
#         return redirect('/thankyou.html')
#     else:
#         return 'Something went wrong. Try again!'

###saving data in a database outside he computer
from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.csv',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'