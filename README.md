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

- **CVE-2021-44228 (Log4Shell)**  
- **CVE-2021-45046**  
- **CVE-2021-45105**  

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
- Explores **bruteforcing** techniques.
- Develops a Python script to bruteforce the decryption key of an encrypted file to bypass ransom payments.

This project is for **educational purposes only** and aims to demonstrate cybersecurity problem-solving skills.

