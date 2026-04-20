# 🖥️ Process Logger & Email Sender (Python)

This Python project logs all running system processes at regular intervals and automatically emails the log file to a specified recipient.

---

## 🚀 Features

* 📊 Logs running processes (PID, name, username, memory usage)
* 📁 Automatically creates a log directory if not present
* ⏱️ Runs at user-defined intervals (in minutes)
* 🌐 Checks internet connectivity before sending mail
* 📧 Sends log file as an email attachment
* 🔄 Fully automated using scheduling

---

## 🛠️ Tech Stack

* Python 3
* psutil (process monitoring)
* smtplib (email sending)
* schedule (task scheduling)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/process-logger-mailer.git
cd process-logger-mailer
```

### 2. Install dependencies

```bash
pip install psutil schedule
```

---

## ⚙️ Configuration

Before running the script, update the following in the code:

```python
fromaddr = "your_email@gmail.com"
toaddr = "receiver_email@gmail.com"
```

Also replace the app password:

```python
s.login(fromaddr, "your_app_password")
```

> ⚠️ Use a **Gmail App Password**, not your actual password.

---

## ▶️ Usage

Run the script with interval (in minutes):

```bash
python script.py 5
```

This will:

* Generate process logs every 5 minutes
* Send the log file via email automatically

---

## 📂 Output

* Logs are stored in a folder named:

```
Marvellous/
```

* File format:

```
Marvellous_Day_Month_Date_Time_Year.log
```

---

## 📌 Example Log Entry

```text
{'pid': 1234, 'name': 'chrome.exe', 'username': 'user', 'vms': 250.5}
```

---

## ❗ Error Handling

* Handles invalid arguments
* Handles no internet connection
* Skips inaccessible processes

---

## 🔒 Security Note

* Do NOT hardcode credentials in production
* Use environment variables or secure vaults instead

---

## 📈 Future Improvements

* Add logging levels (INFO, ERROR)
* Compress log files before sending
* Support multiple email recipients
* Add GUI dashboard

---

## 👨‍💻 Author

**Varun Palphade**

---

## 📄 License

This project is for educational purposes.
