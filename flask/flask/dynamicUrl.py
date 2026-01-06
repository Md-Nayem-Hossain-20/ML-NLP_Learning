from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/",methods = ["GET"])
def welcome():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods = ["GET","POST"])
def form():
    if request.method == "POST":
        name = request.form['name']
        return f"Hello {name} !"
    return render_template("form.html")

@app.route("/submit", methods = ["GET","POST"])
def submit():
    if request.method == "POST":
        name = request.form['name']
        return f"Hello {name} !"


## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the marks is '+ str(score)

@app.route('/result/<int:score>')
def result(score):
    res = ""
    if score >= 50:
        res = 'Success'
    else:
        res = 'Fail'

    return render_template('result.html', result = res)


# If Else

@app.route('/successres/<int:score>')
def results(score):
    res = ""
    if score >= 50:
        res = 'Passed'
    else:
        res = 'Failed'

    exp = {'score': score, 'res': res}

    return render_template('result.html', results = exp)



@app.route('/successif/<int:score>')
def successif(score):
    

    return render_template('result.html', resultif = score) 


if __name__ == "__main__":
    app.run(debug=True)
