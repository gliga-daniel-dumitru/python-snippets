def create_comment_validation(data):
    if len(data) == 0:
        raise ValueError("Invalid or empty payload.")

    content = data.get('content')
    post_id = data.get('post_id')
    if not content or len(content) == 0:
        raise ValueError("Cannot create a comment with empty content.")
    if not post_id:
        raise ValueError("Cannot create a comment without a post_id.")

def update_comment_validation(data):
    if len(data) == 0:
        raise ValueError("Invalid or empty payload.")

    content = data.get('content')
    if not content or len(content) == 0:
        raise ValueError("Cannot create a comment with empty content.")