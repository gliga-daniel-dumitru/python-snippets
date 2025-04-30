from models import Comment, db

def get_all_comments():
    comments = Comment.query.all()
    if not comments:
        return []

    return [comment.to_dict() for comment in comments]

def create_comment(content, post_id):
    comment = Comment(content=content, post_id=post_id)
    db.session.add(comment)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e

    return comment.to_dict()


def get_comments_by_post_id(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    if not comments:
        return []

    return [comment.to_dict() for comment in comments]

def get_comment_by_id(comment_id):
    comment =  db.session.get(Comment, comment_id)

    if not comment:
        return None

    return comment.to_dict()

def delete_comment_by_id(comment_id):
    try:
        db.session.delete(Comment.query.get(comment_id))
        db.session.commit()
    except Exception as e:
        db.session.rollback()

def update_comment_by_id(comment_id, content):
    comment = db.session.get(Comment, comment_id)
    print(comment)
    if not comment:
        raise ValueError(f"Comment with id: {comment_id} not found")

    if comment.to_dict().get('content') == content:
        return comment.to_dict()

    comment.content = content
    comment.updated_at = db.func.now()

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


    return comment.to_dict()
