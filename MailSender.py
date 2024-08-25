import os                               # main sender 
import time
import psutil
import urllib.request as urllib2
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib2.urlopen('http://www.google.com', timeout = 1)
        return True
    except Exception as E:
        return False

def MailSender(filename, time):
    try:
        fromaddr = "7781varun@gmail.com"
        toaddr = "palphadevarun@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """Hello {}, 
        Welcome to Assignment 12 of Marvellous
        Please find attached log file
        Log file created at : {}

        This is an auto-generated mail by Varun Palphade.
        """.format(toaddr, time)

        Subject = "Marvellous assignment 12 process generator log file at : {}".format(time)

        msg['Subject'] = Subject
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename = {}".format(filename))
        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "jneg leao mbtk xdmy")  # Replace with your actual password

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()

        print("Log file successfully sent through mail")

    except Exception as E:
        print("Unable to send the mail", E)


def ProcessLog(log_dir='Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    # Format the timestamp to remove invalid characters
    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "_")
    timestamp = timestamp.replace(":", "_")
    
    separator = "-" * 70
    log_path = os.path.join(log_dir, "Marvellous_%s.log" % timestamp)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : " + time.ctime() + "\n")
    f.write(separator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" % element)

    f.close()  # Make sure to close the file after writing
    
    print("Log file is successfully generated at location %s" % log_path)

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path, time.ctime())
        endTime = time.time()
        
        print('Took %s seconds to send the mail' % (endTime - startTime))
    else:
        print("There is no internet connection!!!")

def main():
    print("--------Assignment 12 Marvellous --------")

    print("Application name : " + argv[0])

    if(len(argv) != 2):
        print("Error : Invalid numbers of arguments ")
        exit()

    if(argv[1] == "h") or (argv[1] == "-H"):
        print("The script is used to log records of running process and send it through the main")
        exit()

    if(argv[1] == "=u") or (argv[1] == "=U"):
        print("Usage : ApplicationName pathOf_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input" ,E)

if __name__ == "__main__":
    main()