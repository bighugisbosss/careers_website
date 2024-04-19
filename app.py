from flask import Flask, render_template

# __name__ is a variable that is always set. if I run this file directly, __name__ is set to __main__, if it was ran in other file it will have other name

app = Flask(__name__)

#https//jovian.ai (domain)  /learn  (route)


@app.route('/')  # when the url/ is acessed run the function
def hello_world():
  return render_template('home.html')


if __name__ == '__main__':  # if the file is run directly, run the app locally
  app.run(host='0.0.0.0', debug=True)
