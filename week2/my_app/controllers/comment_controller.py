from flask import jsonify, request
import services.comment_service as comment_service
from services import get_post
from validations.comments_validations import create_comment_validation, update_comment_validation


def get_all_comments():
    comments = comment_service.get_all_comments()
    return jsonify(comments), 200

def create_comment():
    try:
        # get json data
        data = request.get_json()

        # validate payload
        create_comment_validation(data)

        # create the comment
        content, post_id = data["content"], data["post_id"]

        post = get_post(post_id)
        if not post:
            raise ValueError(f'Cannot create comment. The post with {post_id} not found.')


        new_comment = comment_service.create_comment(content,post_id)
        return jsonify(new_comment), 201
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

def get_comments_by_post_id(post_id):
    comments = comment_service.get_comments_by_post_id(post_id)
    print(comments)
    return jsonify(comments), 200

def get_comment_by_id(comment_id):
    comment = comment_service.get_comment_by_id(comment_id)
    if not comment:
        return jsonify({"message": f'Comment with id: {comment_id} not found.'}), 400

    return jsonify(comment), 200

def delete_comment_by_id(comment_id):
    try:
        comment = comment_service.get_comment_by_id(comment_id)
        if not comment:
            return jsonify({"message": f'Comment with id: {comment_id} not found.'}), 404

        comment_service.delete_comment_by_id(comment_id)

        return jsonify({"message": f'Comment with id: {comment_id} deleted.'}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# def update_comment_by_id(comment_id):

def update_comment_by_id(comment_id):
    try:
        data = request.get_json()

        # validate payload
        update_comment_validation(data)

        updated_post = comment_service.update_comment_by_id(comment_id, data['content'])
        return jsonify(updated_post), 200
    except ValueError as ve:
        return jsonify({"message": str(ve)}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
