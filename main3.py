import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import xgboost as xgb

# Load your pre-trained XGBoost model
xgb_model = xgb.XGBClassifier()
xgb_model.load_model('trained.model')  

# Create the main window
root = tk.Tk()
root.title("Chronic Kidney Disease Predictor")
root.configure(bg='#F0F0F0')

# Center the window on the screen
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

font_style = ('Arial', 40)

# Create a label at the top of the window
title_label = ttk.Label(root, text="Chronic Kidney Disease Predictor", font=('Arial', 30), background='#F0F0F0')
title_label.pack(pady=20)

# Input labels and entry widgets
input_labels = [
    "White Blood Cell Count:",
    "Blood Glucose Random:",
    "Blood Urea:",
    "Packed Cell Volume:",
    "Serum Creatinine:",
    "Albumin:",
    "Hemoglobin:",
    "Age:",
    "Sugar:",
    "Hypertension:"
]

input_entries = []

for label_text in input_labels:
    label = ttk.Label(root, text=label_text)
    label.pack(pady=5)
    entry = ttk.Entry(root)
    entry.pack(pady=5)
    input_entries.append(entry)

# Function to perform the prediction
def predict():
    # Get input values from the entry widgets
    input_data = [float(entry.get()) for entry in input_entries]

    # Make a prediction using the XGBoost model
    prediction = xgb_model.predict([input_data])

    if prediction[0] == 1:
        result_text = "Predicted: Infected"
    else:
        result_text = "Predicted: Not Infected"

    messagebox.showinfo("Prediction Result", result_text)

# Create a Predict button
predict_button = ttk.Button(root, text="Predict", command=predict)
predict_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
