import smtplib
import time
import datetime
import os
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import PySimpleGUI as sg
import threading
import local_settings

email_username = local_settings.email_username
email_password = local_settings.email_password
email_to = local_settings.email_to
email_from = local_settings.email_from

def ping_ip(ip):
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file_name = f"{current_date}.txt"
    log_file_path = os.path.join(log_folder, log_file_name)
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = os.popen(f"ping -n 1 {ip}").read()
    try:
        with open(log_file_path, "a", encoding='utf-8') as log:
            log.write(f'[{log_time}] Request to {ip} \n')
            log.write(f'Response: {output}\n\n\n')
    except PermissionError:
        print("Skrypt nie ma uprawnień do zapisu do pliku dziennika.")
    if "TTL=" not in output:
        for i in range(3):
            time.sleep(5)
            output = os.popen(f"ping -n 1 {ip}").read()
            try:
                with open(log_file_path, "a", encoding='utf-8') as log:
                    log.write(f'[{log_time}] Request to {ip} \n')
                    log.write(f'Response: {output}\n\n\n')
            except PermissionError:
                print("Skrypt nie ma uprawnień do zapisu do pliku dziennika.")
            if "TTL=" in output:
                break
        if "TTL=" not in output:
            message = f'Subject: Falownik {ip}\nFrom: {email_from}\nTo: {email_to}\n\nBłąd: {ip} nie odpowiada.\nCzas zapytania: {log_time}\n\n\n Log:\n{output}'
            try:
                server = local_settings.server
                # server.starttls()
                # server.ehlo()
                server.login(email_username, email_password)
                server.sendmail(email_from, email_to, message.encode('utf-8'))
                # server.set_debuglevel(1)
                server.quit()
                with open(log_file_path, "a", encoding="utf-8") as log:
                    log.write(f'[{log_time}] Error: {ip} not responding. Email sent to recepients. \n')
            except smtplib.SMTPException:
                with open(log_file_path, "a", encoding="utf-8") as log:
                    log.write(f'[{log_time}] Error: {ip} not responding. Email not sent, error occured. \n')


def ping_all_ips():
    with open('ips.txt', 'r', encoding='utf-8') as f:
        ips = f.readlines()
        ips = [ip.strip() for ip in ips]
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(ping_ip, ip) for ip in ips]
    concurrent.futures.wait(futures)

is_pinging = False
thread = None
stop_event = threading.Event()

def update_interval():
    global is_pinging
    interval = int(interval_input.Get())
    while is_pinging:
        ping_all_ips()
        if is_pinging == False:
            break
        time.sleep(interval)

interval_input = sg.InputText("300", key="interval")
start_button = sg.Button("Start", key="start", disabled=False)
stop_button = sg.Button("Stop", key="stop", disabled=True)

layout = [[interval_input, start_button, stop_button]]

window = sg.Window("Kontener pinger",layout, finalize=True)

window['start'].Update(disabled=False)
window.Read(timeout=0)
window.find_element('start').Click()

while True:
    event, values = window.Read()
    if event == "start":
        if not is_pinging:
            is_pinging = True
            start_button.Update(disabled=True)
            stop_button.Update(disabled=False)
            thread = threading.Thread(target=update_interval)
            thread.start()
    elif event == "stop":
        if is_pinging:
            is_pinging = False
            start_button.Update(disabled=False)
            stop_button.Update(disabled=True)
    if event == sg.WIN_CLOSED:
        break

window.Close()

# GUI launches pingign automatically when the app is launched with default time interval 300s and also alows to stop pinging, change time interval, and start pinging with chosen time interval.
# It was made cause the script will be autolaunched on windows server and in case if server will be reloaded it is not neccessary to launch the script manually.
# Logs are made in a separate folder that will be created automatically. Every day will be written in a separete log file.