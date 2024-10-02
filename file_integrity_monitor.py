import time
import smtplib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from email.mime.text import MIMEText

# Email Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'Enter email here'
EMAIL_PASSWORD = 'enter email password, or passkey here(for intructions please view readme.)'

# Send email notification
def send_email(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()
        print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

class MonitorHandler(FileSystemEventHandler):
    def on_modified(self, event):
        message = f"File modified: {event.src_path}"
        print("Modification detected!")  # Debugging statement
        print(message)
        send_email("File Modified", message)

    def on_created(self, event):
        message = f"File created: {event.src_path}"
        print("Creation detected!")  # Debugging statement
        print(message)
        send_email("File Created", message)

    def on_deleted(self, event):
        message = f"File deleted: {event.src_path}"
        print("Deletion detected!")  # Debugging statement
        print(message)
        send_email("File Deleted", message)

if __name__ == "__main__":
    path = input("Enter the directory to monitor: ")
    event_handler = MonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("observer started. watchdog active;)")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

send_email("Test Subject", "Test email body to verify email functionality")