What the program does:
This is a very simple password checker I wrote in python for my ethics in computing class. It takes in a password through the command line, and informs the user about the safety and security level of the password. The program will check the password against \ some common passwords, as well as try to brute force a password that is shorter than 4 characters, this limit is in place for the sake of time, since I will not be implementing advanced  password cracking algorithms for an assignment like this.

Installation/Usage Insrtuctions:
1. Clone the repo by running this command "git clone [https://github.com/your-username/your-repo-name.git](https://github.com/vsicle/PasswordChecker.git)"
2. Naviagte to the folder/directory where you cloned the repo
3. Execute the program by running the following (a python installation is required)
   python main.py
4. Enter the password you would like to analyze as follows
   Enter password to analyze: yourpassword
5. Hit enter to submit the input and learn about your password!

Warnings/Limitations:
Educational Tool Only:
This program is for educational/demonstration purposes only and does not reflect real world 
security practices or penetration testing techniques.

Never Use Real Passwords:
Avoid inputting real passwords that you use. This tool has no networking capabilities, so it cannot
directly expose your password to the author, but you should still never input your real password into this tool.

The "hacking" simulation is heavily limited and not representative of actual attacks. Real attackers use many 
GPUs, rainbow tables, and massive rainbow tables to recover plaintext passowrds from leaked hashes.

Common Password List:
The dictionary of common passwords is extremely small (20 entries). Real dictionaries contain millions of passwords.

Brute-Force:
The brute-force simulation only tests passwords up to 4 characters long, and is missing some characters. In reality, even 8-character passwords can be cracked quickly with modern techniques.

Scoring System:
The password strength scoring is oversimplified:
Does not check for dictionary words.
No entropy calculation

No Rate Limiting:
The simulated attacks have no delays between attempts. Real systems often lock accounts after repeated failures.

Responsible use and misuse:
This program is intended strictly for educational purposes to demonstrate basic password security concepts.

Ethical Use: Never test passwords you or anyone else actively use without explicit permission and informed consent from the account owner.

Legal Compliance: Do not misuse this tool to violate privacy laws or attempt unauthorized access attempts.

Awareness of Limitations: Understand that this is a simplified simulation. Real-world attacks involve far more sophisticated methods.

Prohibited Misuse
Testing passwords belonging to others without consent.
Using this tool to justify insecure practices
Modifying the code for malicious purposes.
