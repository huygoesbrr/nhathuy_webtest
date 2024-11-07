from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/tributes')
def tributes():
    return render_template('tributes.html')

@app.route('/teachers')
def teachers():
    return render_template('teachers.html')

@app.route('/activities')
def activities():
    return render_template('activities.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
