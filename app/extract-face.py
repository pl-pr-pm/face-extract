from PIL import Image
import face_recognition
from pathlib import Path
import os

def _extract_face(original_face_image_path, output_path, model="cnn"):
    # face recognitionに抽出対象の画像を読み込ませる
    image = face_recognition.load_image_file(original_face_image_path)
    # 顔の位置を識別する
    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model=model)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(output_path)


# 一時的に日向坂限定としている
base_path = "./app/pic/HINATA_ZAKA/"
input_dir_name="input/"
output_dir_name = "output/"

loop_dir = os.path.join(base_path, input_dir_name)
output_base_dir = os.path.join(base_path, output_dir_name)

i = Path(loop_dir)
o = Path(output_base_dir)

if not os.path.exists(loop_dir):
    i.mkdir()

if not os.path.exists(output_base_dir):
    o.mkdir()

for sub_dir in os.listdir(path=loop_dir):

    for target_file in os.listdir(path=loop_dir+sub_dir):
        original_face_image_path = loop_dir+sub_dir+"/"+target_file
        output_dir = base_path+output_dir_name+ sub_dir+"/"
        output_path = output_dir + target_file

        if not(os.path.exists(output_dir)):
            p = Path(output_dir)
            p.mkdir()
        
        # face recognitionを実行
        _extract_face(original_face_image_path, output_path)