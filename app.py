from flask import Flask, render_template, url_for, request
import markovify

app = Flask(__name__)

with open('static/datasets/reworked.txt') as f:
    text = f.read()

text_model = markovify.Text(
    text, state_size=2, well_formed=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        for i in range(3):
            genText = text_model.make_short_sentence(
                10000, min_chars=280, tries=1000, max_overlap_ratio=0.5)
        return render_template('index.html', genText=genText)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
