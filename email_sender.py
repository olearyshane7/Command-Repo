import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def send_email():
    recipient_email = email_entry.get()
    message_body = message_text.get("1.0", tk.END)

    # Email credentials
    sender_email = 'your-email@gmail.com'  # Your email
    sender_password = 'your-email-password'  # Your email password

    msg = MIMEText(message_body)
    msg['Subject'] = 'New Message'
    msg['From'] = sender_email
    msg['To'] = recipient_email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        
        messagebox.showinfo("Success", "Email sent successfully!")
        email_entry.delete(0, tk.END)
        message_text.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{str(e)}")

# Set up the main application window
app = tk.Tk()
app.title("Email Sender")

# Create input fields
tk.Label(app, text="Recipient's Email:").pack(pady=5)
email_entry = tk.Entry(app, width=40)
email_entry.pack(pady=5)

tk.Label(app, text="Your Message:").pack(pady=5)
message_text = tk.Text(app, width=40, height=10)
message_text.pack(pady=5)

# Create send button
send_button = tk.Button(app, text="Send Email", command=send_email)
send_button.pack(pady=20)

# Run the application
app.mainloop()