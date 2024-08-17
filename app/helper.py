import os
import secrets
from app import app



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    final_pic = random_hex + f_ext
    picture_path = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"], final_pic)
    print(f"Saving picture to: {picture_path}")
    form_picture.save(picture_path)
    return final_pic

def delete_picture(picture):
    picture_path = os.path.join(app.root_path, app.config["UPLOAD_FOLDER"], picture)
    print(f"Deleting picture from: {picture_path}")
    os.remove(picture_path)
    return True