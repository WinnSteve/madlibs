from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

# do not forget to start a server

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_question():
    """creates form to ask for words"""

    prompts = story.prompts

    return render_template("form.html", prompts=prompts)


@app.route("/story")
def show_story():
    """shows the story with the results from the ask question form"""

    text = story.generate(request.args)

    return render_template("result.html", text=text)
