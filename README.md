# Navigation

* ***[Functionality description](#functionality-description)***
* ***[How to start?](#how-to-start)***
* ***[Why should you try it?](#why-should-you-try-it)***
* ***[License](#license)***


# Functionality description.


Program has simple GUI interface and allows to check connection between Windows server and solar batteries inverters in the network by sending requests to provided IP addresses (list of IP addresses should be provided in "ips.txt" file at the same directory with the main script). 
In case of any troubles interested recepients will receive an email with description of the issue.
***Standard time interval of requests is 300s but it can be cahnged optionally***. In case if by some reasonse program is not recieving an answer from inverter,
it will make several requests with interval 5 seconds and only after that will send an email notification to all recepients indicated in settings.
First launch of the program is automatical (program immediately starts sending requests without additional clicking "start" button). In case of server reload, program will be autolaunched and there is no need for user to launch it manually in case of any server failure. 
User can stop sending requests, change interval of sending requests and start the program manually after some changes or optionally.
Also the program is creating log files where it indicates time, status of requests, notifications about sent emails etc. Log files will be created automatically
after launching the program in a separate folder and will be named in accordance with current date (every day will be written in a separate log file).


# How to start?

1. **Clone current repository on your local machine.**
```
git clone https://github.com/LeatherDiamond/solar_batteries_connection_checker.git
```
2. **Install all requirements from "requirements.txt".**
```
pip install -r requirements.txt
```

3. **Create "ips.txt" file in the same directory with the main script and provide ip addresses that will be pinged.**

4. **Provide mandatory data to the following fields:** *(In program code this information is imported from "local_settings.py" file.)*
 > - email_username ***(login to prefered account from which email notifications will be send)***,
 > - email_password ***(password to prefered account from which email notifications will be send)***,
 > - email_to ***(recepient email address, also can be indicated several email addresses)***,
 > - email_from ***(email address from which notification emails will be send)***,
 > - server ***(server address and port)***.
 
 5. **Launch the program.**
 
 - [x] ***Optional:*** This program can be converted to "exe" file that will allow you to run an application that will run on any machine without installing specialised software.
 
 **It can be done by launching "setup.py" file.**
 ```
 python setup.py build
 ```
 
 # Why should you try it?
 
This is a reliable and easy-to-use tool that is equiped with several features that make it a powerful tool for managing your network. You have complete control over how the program operates. It can be adapted to your needs and will save your time and money by continually checking the performance of your equipment and reporting faults in a timely wanner.


# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/LeatherDiamond/solar_batteries_connection_checker/blob/master/LICENCE) file for details.
