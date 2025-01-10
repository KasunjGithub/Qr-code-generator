import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import ImageTk, Image

# Global variable to store the generated QR code image
generated_img = None

def generate_qr():
    global generated_img
    input_data = entry.get()
    
    # Ensure the input is not empty
    if not input_data:
        messagebox.showwarning("Input Error", "Please enter some comma-separated values!")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    generated_img = img  # Store the generated image
    
    # Convert the image to a format that can be displayed in Tkinter
    img_tk = ImageTk.PhotoImage(img)
    
    # Display the image in the canvas
    canvas.create_image(150, 150, image=img_tk)
    canvas.image = img_tk  # Keep a reference to avoid garbage collection

def save_qr():
    global generated_img
    if generated_img is None:
        messagebox.showwarning("No QR Code", "Please generate a QR code first!")
        return
    
    # Open file dialog to choose the save location and filename
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
    
    if file_path:
        # Save the image to the specified location
        generated_img.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully as {file_path}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and pack the widgets
label = tk.Label(root, text="Enter Comma-Separated Values:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

generate_button = tk.Button(root, text="Generate QR", command=generate_qr)
generate_button.pack(pady=10)

save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
