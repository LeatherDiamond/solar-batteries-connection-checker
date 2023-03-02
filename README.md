## Functionality description.


Program has simple GUI interface and allows to checks connection between Windows server and solar batteries invertors in the network. 
In case of any troubles interested recepients will receive an email with description of the issue.
Standandard time interval of requests is 300s but it can be cahnged optionally. In case if by some reasonse program is not receveng an answer from invertor,
it will make several requests with interval 5 seconds and only after that will send an email notification to all recepients indicated in settings.
First launch of the program is automatical (program immediately starts sending requests without additional clecking start button) In case of server reload program will be autolaunched
and there is no need for user to launch it manually in case of any server failure. 
User can stop sending requests, change interval of sending requests and start the program manually after some changes or optionally.
Also the program is creating log files where it will indicate time, status of requests, notifications about sent emails etc. Lof files will be created automatically
after launching the program. 
