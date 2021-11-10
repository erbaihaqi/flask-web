from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result2')
def result():
    grade_dict = {'phy':50, 'che':60, 'maths':70}
    return render_template('results2.html', result = grade_dict)
