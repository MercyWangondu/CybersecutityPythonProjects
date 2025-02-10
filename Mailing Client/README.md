# 📧 Python SMTP Mailing Client

## 📌 Project Overview
This project is a Python-based mailing client that uses the Simple Mail Transfer Protocol (SMTP) to send emails with attachments. It automates the process of composing and sending emails from a Gmail account to a recipient's address.

## 🚀 Significance of the Project
- **🔄 Automation**: Simplifies email-sending tasks, especially for bulk or repetitive emails.
- **📚 Learning Opportunity**: Enhances understanding of Python libraries (`smtplib` for SMTP, `email` for crafting messages) and file handling.
- **⚙️ Customizability**: Modify the script to include multiple recipients, dynamic messages, and scheduling.
- **🔐 Security Awareness**: Provides insights into email security, such as encrypted connections (TLS/SSL) and app passwords.

## 🛠️ How the Code Works
### 1️⃣ Import Required Libraries
- `smtplib`: Connects to the email server and sends emails.
- `email` modules: Crafts MIME-based email messages, handles attachments, and encodes content.

### 2️⃣ Set Up SMTP Connection
- Initializes `smtplib.SMTP` with Gmail's SMTP server (`smtp.gmail.com`) and port `587` for TLS.
- Uses `server.ehlo()` to identify itself to the server.
- Upgrades the connection to TLS with `server.starttls()`.

### 3️⃣ Authenticate Using Credentials
- Reads the email account password from a local `password.txt` file.
- Logs into the Gmail account using `server.login()`.

### 4️⃣ Compose the Email
- **📤 Sender & Recipient**: Defines `From` and `To` fields.
- **📩 Subject**: Adds a brief subject line.
- **📜 Body**: Reads text from `message.txt` and attaches it as plain text.
- **📎 Attachment**:
  - Reads the file (`Bags.jpeg`) in binary mode.
  - Uses `MIMEBase` and `encoders.encode_base64()` to attach the file in a decodable format.

### 5️⃣ Send the Email
- Uses `server.sendmail()` to send the composed email.

### 6️⃣ Close the Server Connection
- Terminates the SMTP session with `server.quit()`.

## 📌 Example Workflow
### 🔹 Inputs:
- A Gmail account (`sender@gmail.com`) and its password (or app password).
- Recipient's email (`sendee@gmail.com`).
- A message file (`message.txt`) and an attachment (`Bags.jpeg`).

### 🔹 Execution:
- The script authenticates, reads the inputs, composes a well-structured email, and sends it securely.

### 🔹 Output:
- The recipient receives an email with the specified message and attachment.

## 📌 Potential Applications
- 📅 **Automated reminders or notifications**.
- 📊 **Distributing reports or files** to groups.
- 📧 **Building advanced email systems**, like newsletters or customer outreach tools.

---
🔹 **Happy Coding! 🚀**
