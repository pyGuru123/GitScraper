from app import app
from app.scraper import User, Repository
from app.scripts import fetch_repo_stats

import json
from flask import render_template, url_for, request, Response, session, flash, redirect

# data = {'username': 'pyGuru123', 'fullname': 'Prajjwal Pathak', 'avatar': 'https://avatars.githubusercontent.com/u/71623767?v=4', 'followers': '231', 'following': '15', 'bio': 'Python Enthusiast 🚀 | Otaku | Cosmos lover 🌌', 'location': 'Varanasi, India', 'repositories': '36', 'readme': "Konnichiwa I'm Prajjwal aka pyGuru,Welcome to my little space on Github. Here i put my thoughts and ideas into code.🔭 Primary Coding language : Python🌱 Currently learning data science👯 I’m looking to collaborate with other programmers🥅 2022 Goals: Contribute more to Open Source projects📫 How to reach me : The fastest way to reach me is by Telegram⚡ Fun fact : I am a melomaniac, an Otaku and a fan of Ruskin Bond Stories 🤣.Interested in knowing more about me 👇 I'm a Student, Developer, and Python Instructor. I like programming,cryptography and designing. I am interested in extra-terrestrials andtrying to understand our universe, studying theoretical physics by my own.I like photography and collecting pictures. A simple and down toearth boy who is so keen to learn every day a new thing. ⚡ Github Stats Show some ❤️ by starring some of the repositories!", 'contributions': '322', 'pinned': ['Python-Projects', 'Python-Games', 'Python-on-WhatsApp', 'Decrypto', 'Open-Space', 'Chat-App']}

@app.route("/")
@app.route("/home")
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get('username')
        if username:
            try:
                user = User(username.strip('@'))
                data = user.get_full_info()
                return render_template("index.html", index=True, data=data)
            except:
                flash("Username doesn't exist")
                return redirect("/home")
    return render_template("index.html", index=True, data=None)

@app.route("/allrepostats/<username>")
def all_repo_stats(username):
    result = fetch_repo_stats(username)
    if result:
        json_data = json.dumps(result)
        return json_data
    else:
        return json.dumps([])

@app.route('/exportprofile', methods=["POST"])
def export_profile():
    username = request.form.get("username")
    data = request.form.get("data")
    filename = f"{username}.json"
    # content = json.loads(data)
    return Response(data,
        mimetype='application/json',
        headers={'Content-Disposition':f'attachment;filename={filename}'}
    )

@app.route("/repo")
@app.route("/repository", methods=["GET", "POST"])
def repository():
    if request.method == "POST":
        repo_url = request.form.get("repo")
        if repo_url:
            try:
                repo = Repository(repo_url)
                data = repo.get_full_info()
                return render_template("repository.html", index=True, data=data)
            except:
                flash("Repository doesn't exist")
                return redirect("/repo")

    return render_template("repository.html", repo=True)

@app.route("/langs")
@app.route("/languages")
def languages():
    return render_template("languages.html", lang=True)

@app.route("/about")
def about():
    return render_template("about.html", about=True)
