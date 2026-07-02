from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        "id": 1, 
        "title": "Welcome to Kintrexa Python Dev Portal", 
        "content": "This is a premium, professional web interface featuring dynamic routing, clean form handling, and full responsive design templates."
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        if title and content:
            posts.append({"id": len(posts) + 1, "title": title, "content": content})
            return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)