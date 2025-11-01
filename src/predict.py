from PIL import Image
import numpy as np
import tensorflow as tf
import sys

IMG_SIZE = (128, 128)
CLASS_NAMES = ["Não há queimada", "Há queimada"]

model = tf.keras.models.load_model("model/results/wildfire_cnn.h5")


def predict_image(path):
    img = Image.open(path).convert("RGB")
    img = img.resize(IMG_SIZE)
    arr = np.array(img).astype("float32") / 255.0
    arr = np.expand_dims(arr, axis=0)
    prob = model.predict(arr)[0][0]
    result = CLASS_NAMES[int(prob > 0.5)]
    print(f"Predição: {result} (prob={prob:.3f})")
    return result, prob


def validate_image(path):
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except (IOError, SyntaxError) as e:
        print(f"Arquivo inválido: {path}. Erro: {e}")
        return False


# if __name__ == "__main__":
#     if not len(sys.argv) == 2:
#         print("Uso: python predict.py <caminho_da_imagem>")
#         sys.exit(1)
#     file_path = sys.argv[1]
#     if not validate_image(file_path):
#         sys.exit(1)
#     predict_image(sys.argv[1])
