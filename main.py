from flask import Flask, render_template
import utils

app = Flask(__name__)

data = utils.load_candidates('candidates.json')


@app.route("/")
def index():
    return render_template('index.html', candidates=data)


@app.route("/candidate/<int:uid>")
def profile(uid):
    candidate = utils.get_candidate(uid)
    return render_template('profile.html', candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = utils.get_candidate_by_name(name)
    return render_template('search.html', candidates=candidates, candidate_len=len(candidates))


@app.route("/skills/<skill>")
def get_skills(skill):
    candidates = utils.get_candidate_by_skill(skill)
    return render_template('skills.html', candidates=candidates, candidate_len=len(candidates), skill=skill)


app.run()

