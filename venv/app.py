from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    name = "30 Days of Python"
    techs = ["Flask", "HTML", "CSS", "Python"]
    return render_template('index.html', name=name, techs=techs)


@app.route('/about')
def about():
    return render_template('about.html', title="About")

# ✅ Add this route to fix the 'post' error


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        text = request.form['text']  # get the text from the form
        word_count = len(text.split())
        char_count = len(text)

        return render_template(
            'post.html',
            title="Text Analyzer",
            text=text,
            word_count=word_count,
            char_count=char_count
        )

    # GET request just shows the empty form
    return render_template('post.html', title="Text Analyzer")


if __name__ == '__main__':
    app.run(debug=True)
