import tkinter as tk
from tkinter import filedialog, messagebox, Label
from predict import predict_image
from PIL import Image, ImageTk

root = tk.Tk()
root.title("WildFire Detection")
root.geometry("500x500")
root.configure(bg="#3c3cff")


img_label = None
result_label = None
conf_label = None


def select_image():
    global img_label, result_label, conf_label
    file_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")],
    )

    if not file_path:
        return

    img = Image.open(file_path).resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)

    if img_label:
        img_label.config(image=img_tk)
        img_label.image = img_tk
    else:
        img_label = Label(root, image=img_tk, bg="#222")
        img_label.image = img_tk
        img_label.pack(pady=15)

    result, confidence = predict_image(file_path)

    color = "#ef4444" if result == "Há queimada" else "#22c55e"

    if result_label:

        result_label.config(text=result, fg=color)
        conf_label.config(text=f"Confiança: {confidence*100:.2f}", fg="black")
    else:
        result_label = Label(root, text=result, fg=color, font=("Arial", 16))
        result_label.pack(pady=5)
        conf_label = Label(
            root,
            text=f"Confiança: {confidence*100:.2f}%",
            fg="black",
        )
        conf_label.pack()


button = tk.Button(
    root,
    text="Selecionar Imagem",
    command=select_image,
    bg="#20c8b4",
    fg="white",
    font=("Arial", 14),
    padx=10,
    pady=5,
)
button.pack(pady=20)


Label(
    root,
    text="WildFire Detection",
    bg="#3c3cff",
    fg="white",
    font=("Arial", 20, "bold"),
).pack(pady=10)

root.mainloop()
