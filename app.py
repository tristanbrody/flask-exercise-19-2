from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fake_key'
debug = DebugToolbarExtension(app)

story = {
    'template-1': stories.story1,
    'template-2': stories.story2,
    'template-3': stories.story3
}
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route('/create-story')
def create_story():
    template_selection = request.args.get('template')
    return render_template('create-story.html', story=story.get(template_selection), template_selection=template_selection)

@app.route('/madlib')
def render_story():
    place=request.args.get('place')
    adjective=request.args.get('adjective')
    noun=request.args.get('noun')
    verb=request.args.get('verb')
    plural_noun=request.args.get('plural_noun')
    answers = {
        'place': place,
        'adjective': adjective,
        'noun': noun,
        'verb': verb,
        'plural_noun': plural_noun
    }
    template_selection=request.args.get('template_selection')
    return render_template('show-story.html', plural_noun = plural_noun, place=place, adjective=adjective, noun=noun, verb=verb, answers=answers, story=story.get(template_selection))