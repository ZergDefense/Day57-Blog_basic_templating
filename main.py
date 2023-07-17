import requests
from flask import Flask, render_template
from post import Post

posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

post_objects = []
for post in posts:
    print(post)
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

for post in post_objects:
    print(f"post id: {post.id}, \n"
          f"post title: {post.title}, \n"
          f"post subtitle: {post.subtitle}, \n"
          f"post body: {post.body}")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<blog_id>')
def get_blog(blog_id):
    post_to_render = post_objects[int(blog_id)-1]
    return render_template("post.html", post_to_render=post_to_render)


if __name__ == "__main__":
    app.run(debug=True)
