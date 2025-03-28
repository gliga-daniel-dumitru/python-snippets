from flask import Flask, request, jsonify

app = Flask(__name__)
posts = []
post_id_counter = 1

@app.route("/posts", methods=["GET"])
def get_posts():
    return jsonify(posts)

@app.route("/posts", methods=["POST"])
def create_post():
    global post_id_counter

    if not request.is_json:
        return jsonify({"error": "Request body should be JSON"}), 415

    data = request.get_json()
    if not data.get("title") or not data.get("description"):
        return jsonify({"error": "Title and description are required"}), 400

    post = {
        "id": post_id_counter,
        "title": data["title"],
        "description": data["description"]
    }
    posts.append(post)
    post_id_counter += 1
    return jsonify(post), 201

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": "Post not found"}), 404
    return jsonify(post)

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if not post:
        return jsonify({"error": "Post not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Data is required"}), 400

    post.update(data)
    return jsonify(post)

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return jsonify({"message": "This post was deleted"}), 204

if __name__ == "__main__":
    app.run(debug=True)
