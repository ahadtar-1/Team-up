from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
import samplerecommendationscode

app = Flask(__name__)
CORS(app)

@app.route("/")
def test_fun():
    return "Working"

@app.route("/post",methods=['GET','POST'])
def test_fun2():
    val=request.form["val"]
    return val

@app.route("/skill", methods=['GET','POST'])
def recommend_jobs():
    skills=request.form["skills"]
    jobs = samplerecommendationscode.results(skills)
    print(jobs)
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0")


