from flask import Flask, render_template, jsonify, request, redirect, url_for
app = Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },

    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'    
    },


]

@app.route('/')
def my_project():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

from markupsafe import escape

@app.route("/greet/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)



