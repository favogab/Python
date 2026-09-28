# -------------------- This is just a personal pratical alert script to pratice what I learned in CS50P Week_0 related to my field --------------------

# This script collects user input for a security alert, including username, IP address, and the number of failed login attempts. 
def main():
    username = input("Please enter the username: ")
    ip = input("Please enter the IP address: ")
    failed = int(input("Please enter the number of failed login attempts: "))

    reference = create_reference(username, ip)

# Displays the information in a formatted alert
    print("===== SECURITY ALERT =====")
    print(f"User: {username}")
    print(f"Source IP: {ip}")
    print(f"Failed Logins: {failed}")
    print(f"Investigation Reference: {reference}")
    print("==========================")

# Create a reference string for the investigation   
def create_reference(username, ip):
    return f"{username}@{ip}"


main()