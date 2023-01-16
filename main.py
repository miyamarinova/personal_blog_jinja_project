import requests as requests
from flask import Flask, render_template
import requests
from post import Post


response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
all_posts = response.json()

print(all_posts)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)

@app.route('/post/<int:id>')
def blog_page(id):
    post = all_posts[id-1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
