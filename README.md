# Directory Monitoring Script

This Python script monitors a specified directory for file changes (creations, modifications, and deletions) and sends email notifications whenever a change is detected. The script uses the `watchdog` library to observe directory events and `smtplib` for email notifications.

## Features

- Monitors specified directory for file creation, modification, and deletion.
- Sends email notifications for each detected change.
- Outputs debugging messages in the console for real-time updates.

## Requirements

- Python 3.x
- `watchdog` library for directory monitoring
- An SMTP-enabled email account (e.g., Gmail) for sending notifications

## Installation

1. Clone the repository:
   git clone https://github.com/your-username/directory-monitoring.git
   cd directory-monitoring

2. Install the required packages:
   pip install watchdog

3. Configure email settings in the script:
   - Replace `EMAIL_ADDRESS` and `EMAIL_PASSWORD` with your email and password.
   - For Gmail, ensure "Allow less secure apps" is enabled or set up an App Password if you have two-factor authentication enabled.

## Usage

1. Run the script:
   python directory_monitoring.py

2. Enter the path of the directory you want to monitor.

3. The script will run and monitor the specified directory. When a file is created, modified, or deleted, you’ll receive an email notification and see a message in the console.

## Example

Enter the directory to monitor: /path/to/your/directory
observer started. watchdog active ;)

You should see a message like this in the console when a file event occurs:
Modification detected!
File modified: /path/to/your/directory/filename.ext

An email will also be sent with the subject "File Modified" and details about the event.

## Troubleshooting

- **Failed to send email**: Verify your email credentials and SMTP settings. Ensure internet connectivity and correct port configurations.
- **Permission errors**: Run the script with appropriate permissions for the specified directory.

## License

This project is licensed under the MIT License.
