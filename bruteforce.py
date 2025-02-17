This is the super sensitive, confidential document that was affected by the ransomware. Congratulations on the bruteforce!

You can paste your bruteforce script in the box below:

'''
Forage AIG Cybersecurity Program
Bruteforce Password Cracking Template for Encrypted Zip Files

This script demonstrates a basic brute-force attack to crack the password of an encrypted zip file.
It uses a wordlist (in this case, 'rockyou.txt') to test each potential pass-word until a successful extraction is made.
If the correct password is found, the zip file is extracted, and the process stops. 

The script also includes error handling for common cases such as corrupted zip files, missing files, and incorrect passwords.

NOTE: This script is for educational purposes only. Ensure you have explicit permission to attempt encryption cracking on any system.

Modules:
- zipfile: A module to work with zip files, allowing extraction and password handling.
'''

from zipfile import ZipFile, BadZipFile

# Function to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    """
    Attempts to extract the contents of the zip file using the provided pass-word.

    Args:
        zf_handle (ZipFile): The open ZipFile object.
        password (bytes): The password to attempt as a byte string.

    Returns:
        bool: True if extraction is successful, False if extraction fails.
        
    This function attempts to extract all the contents of the zip file using the provided password.
    If successful, it prints the password and returns True. If extraction fails (e.g., incorrect password),
    it returns False.
    """
    try:
        # Attempt to extract all files using the provided password
        zf_handle.extractall(pwd=password)
        print(f"[+] Password found: {password.decode('utf-8')}")
        return True
    except (RuntimeError, BadZipFile) as e:
        # Handle errors during extraction (e.g., bad password or corrupted zip)
        return False

def main():
    """
    Main function to initiate brute-force attack on an encrypted zip file.
    It will attempt to extract the file using passwords from 'rockyou.txt'.

    This function does the following:
        1. Opens the zip file (enc.zip) for extraction.
        2. Loads and reads passwords from a wordlist file (rockyou.txt).
        3. Attempts to extract the zip file with each password.
        4. Stops as soon as the correct password is found and the file is ex-tracted.
        5. Prints relevant information during the process (e.g., found pass-word, extraction success/failure).
    """
    print("[+] Beginning brute-force attack on encrypted zip file...")
    
    # Open the encrypted zip file (ensure 'enc.zip' is in the same directory as the script)
    try:
        with ZipFile('enc.zip') as zf:
            # Check if the zip file is empty
            if len(zf.namelist()) == 0:
                print("[-] The zip file is empty!")
                return
            
            # Open the wordlist file ('rockyou.txt') and attempt extraction with each password
            with open('rockyou.txt', 'rb') as f:
                for password in f:
                    password = password.strip()  # Remove any leading/trailing whitespace
                    if attempt_extract(zf, password):
                        print(f'[+] Extraction successful!')
                        return  # Exit once the correct password is found
        # If no valid password is found, notify the user
        print(f"[+] Password not found in the list")

    except FileNotFoundError:
        # Handle the case where the zip file or wordlist file doesn't exist
        print("[-] The zip file or wordlist was not found!")
    except BadZipFile:
        # Handle the case where the zip file is corrupted
        print("[-] The zip file is corrupted!")
    except Exception as e:
        # Handle any other errors
        print(f"[-] An error occurred: {str(e)}")

# Entry point of the script, executed when the script is run directly
if __name__ == "__main__":
    main()



