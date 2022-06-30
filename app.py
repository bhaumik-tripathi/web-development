from flask import Flask, render_template

app = Flask(__name__, template_folder='Templetes')

jobs = [{
  "title": 'Data Analyst',
  'salary': 1000000,
  "location": "Bengaluru, India",
  'Currency': 'Rs.'
},
       {
  "title": 'Data Scientist',
  'salary': 1500000,
  "location": "Delhi, India",
  'Currency': 'Rs.'
},
       {
  "title": 'Frontend Engineer',
  'salary': 20000,
  "location": "Bengaluru, India",
  'Currency': '$'
},
       {
  "title": 'Backend Engineer',
  'salary': 50000,
  "location": "Bengaluru, India",
  'Currency':'$'
}]


@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=jobs,
                           company_name='Jovian')



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)