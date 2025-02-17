# AIG Virtual Internship - Cybersecurity

This repository contains my solutions for the **AIG Virtual Internship** on Forage, focusing on cybersecurity challenges.

Tasks include:
- Responding to a **zero-day vulnerability** by researching and drafting an alert email.
- Writing a **Python script** to bruteforce the decryption key of an encrypted file to bypass ransomware.

This project is for **educational purposes only** and aims to demonstrate cybersecurity problem-solving skills.

---

## Task 1: Responding to a Zero-Day Vulnerability

The **Cybersecurity & Infrastructure Security Agency (CISA)** has recently published advisories regarding:
- A critical vulnerability in **[Apache Log4j](https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-356a)**, widely used logging software.
- The increasing professionalization of **[ransomware attacks](https://www.cisa.gov/news/2022/02/09/cisa-fbi-nsa-and-international-partners-issue-advisory-ransomware-trends-2021)**, posing risks to enterprises like AIG.

### Task Overview
- Research the **Log4j zero-day vulnerability** using CISA advisories.
- Analyze affected infrastructure and determine the responsible teams.
- Draft an advisory email to alert relevant teams and provide remediation steps.

### Affected Infrastructure
| Product Team         | Product Name                                | Team Lead (Email)             | Services Installed |
|----------------------|-------------------------------------------|-------------------------------|---------------------|
| IT                  | Workstation Management System             | Jane Doe (tech@email.com)     | OpenSSH, dnsmasq, lighttpd |
| Product Development | Product Development Staging Environment   | John Doe (product@email.com)  | Dovecot pop3d, Apache httpd, Log4j, Dovecot imapd, MiniServ |
| Marketing           | Marketing Analytics Server                | Joe Schmoe (marketing@email.com) | Microsoft ftpd, Indy httpd, Microsoft Windows RPC, Microsoft Windows netbios-ssn, Microsoft Windows Server 2008 R2 - 2012 microsoft ds |
| HR                 | Human Resource Information System         | Joe Bloggs (hr@email.com)     | OpenSSH, Apache httpd, rpcbind2-4 |

---

## Draft Email - Security Advisory  

### **From:** AIG Cyber & Information Security Team  
### **To:** Product Development Team (product@email.com)  
### **Subject:** Security Advisory concerning Product Development Staging Environment | Log4j  

---

## Hello John Doe,  

The AIG Cyber & Information Security Team would like to inform you that a recently discovered Log4j vulnerability may affect the Product Development Staging Environment.  

### **Vulnerability Overview**  
Log4j is a widely used open-source Java library for logging application activity. Several vulnerabilities have been identified in Apache’s Log4j software library, including:  

- **[CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) (Log4Shell)**  
- **[CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046)**  
- **[CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105)**  

These vulnerabilities allow unauthenticated remote code execution (RCE) by exploiting the Java Naming and Directory Interface (JNDI), posing a critical security risk. Attackers could leverage this flaw to gain unauthorized access, deploy malware (including ransomware), exfiltrate sensitive data, or disrupt services.  

### **Affected Products**  
- **Log4j2 versions:** 2.0-beta9 through 2.15.0  

### **Risk & Impact**  
**Critical – Remote Code Execution (RCE).**  
An attacker may exploit this vulnerability to remotely access and compromise the Product Development Staging Environment, leading to potential data breaches or system disruptions.  

### **Remediation Steps**  

#### **1. Identify Affected Assets**  
- Inventory all assets using the Log4j Java library.  
- Determine which assets are vulnerable based on affected versions.  

#### **2. Mitigate and Secure Vulnerable Assets**  
- Apply the latest security patches and updates for Log4j and related products.  
- Maintain a record of affected assets and remediation actions taken.  
- Verify that applied mitigations are effective.  

#### **3. Threat Hunting and Incident Response**  
- Monitor for signs of exploitation or unauthorized access.  
- If any IoCs are detected, escalate for incident response immediately.  

### **Next Steps**  
If you have identified any signs of exploitation, please notify us immediately. Once remediation steps have been completed, confirm with the security team by replying to this email.  

For further details, please refer to the **CISA advisory**:  
[CISA Log4j Advisory](https://www.cisa.gov/news-events/news/cisa-fbi-nsa-and-international-partners-issue-advisory-ransomware-trends-2021)  

For any questions or concerns, feel free to reach out to us.  

---

**Kind regards,**  
_AIG Cyber & Information Security Team_  


## Task 2: Bypassing Ransomware

In this task, I demonstrate the process of bypassing ransomware encryption using brute force techniques to recover an encrypted file without paying a ransom. This project aims to illustrate the practical application of password cracking methods in the context of cybersecurity.

### Objectives:
- **Brute-force attack**: The task explores brute-forcing techniques to decrypt files encrypted by ransomware, focusing on bypassing encryption without relying on the original decryption key.
- **Python implementation**: I developed a Python script (`bruteforce.py`) that attempts to crack the password used to encrypt a zip file by leveraging a popular wordlist (`rockyou.txt`).
- **Decryption bypass**: The goal is to recover the encrypted contents of the file (`enc.zip`) by identifying the correct password and decrypting it, demonstrating the potential vulnerability of poorly secured encrypted files.

### Resources:
- **enc.zip**: An encrypted zip file, which contains data that is protected by a password. The zip file is located in the `/resources` subfolder.
- **rockyou.txt**: A wordlist file used in the brute-force attack, which contains a vast collection of common passwords. It is also placed in the `/resources` subfolder.
- **bruteforce.py**: The Python script located in the same folder that implements the brute-force method for cracking the password. This script reads the passwords from `rockyou.txt` and attempts to extract the contents of `enc.zip` one password at a time.

### Process:
The script works by opening the `enc.zip` file and trying every password in `rockyou.txt`. If the correct password is found, the zip file is extracted, and the contents are revealed. If the password is not found within the wordlist, a message is displayed indicating the failure.

### Educational Purpose:
This project is for **educational purposes only** and demonstrates problem-solving skills in cybersecurity. It is important to note that such techniques should only be used with explicit permission and in legal contexts.

### Example Screenshot:
Here is a screenshot showing the output of the `bruteforce.py` script when it successfully cracks the password for `enc.zip`:

![Screenshot of Code Output](https://github.com/user-attachments/assets/c863ceea-9305-483e-8b2b-87878104039f) 

![image](https://github.com/user-attachments/assets/53d5dcc2-bd22-4e91-9c48-63b2773ccd62)




