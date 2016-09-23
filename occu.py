from flask import Flask, render_template
import occupationRandomizer

app = Flask(__name__)

f = open('occupations.csv', 'r')
s=f.read()
f.close()
s=s.split("\n")
s=s[1:len(s)-3]
for occupation in s:
    occupation=occupation.split(',')
    if occupation[0][0:1]== '"':#checks for commas
        while len(occupation)>2:#makes a list with occupation name and percent
            occupation[0]=occupation[0]+','+occupation[1]
            occupation.pop(1)


@app.route("/")
def hello_world():
    return "hello"

@app.route("/occupations")
def yes():
    return render_template("basic.html", basic = occupationRandomizer.pickRandom(), fool = s)

if __name__ == "__main__":
    app.debug = True
    app.run()
