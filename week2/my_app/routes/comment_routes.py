from flask import Blueprint
import controllers.comment_controller as comment_controller

comments_routes = Blueprint("comments_routes", __name__)

# POST Create a new post
@comments_routes.route('/comments', methods=['POST'])
def create_comment():
    return comment_controller.create_comment()

# GET all comments
@comments_routes.route('/comments', methods=['GET'])
def get_all_comments():
    return comment_controller.get_all_comments()

# GET comment by id
@comments_routes.route('/comments/<int:comment_id>', methods=['GET'])
def get_comment_by_id(comment_id):
    return comment_controller.get_comment_by_id(comment_id)

# GET all comments by post id
@comments_routes.route('/comments/post/<int:post_id>', methods=['GET'])
def get_comments_by_post_id(post_id):
    return comment_controller.get_comments_by_post_id(post_id)

# PATCH update comment properties
@comments_routes.route('/comments/<int:comment_id>', methods=['PATCH'])
def update_comment_by_id(comment_id):
    return comment_controller.update_comment_by_id(comment_id)

# DELETE comment by id
@comments_routes.route('/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment_by_id(comment_id):
    return comment_controller.delete_comment_by_id(comment_id)
