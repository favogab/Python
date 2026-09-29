# -------------------- This is the continuation of my personal practical alert script to practice what I learned in CS50P Week_1 related to my field --------------------

# This script collects user input for a security alert, including username, IP address, and the number of failed login attempts. 
def main():
    username = input("Please enter the username: ")
    ip = input("Please enter the Source IP: ")
    failed = int(input("Number of failed logins: "))
    success = input("Was there a successful login afterward? (yes/no): ").strip().lower()

    reference = create_reference(username, ip)
    classification = classify_alert(failed, success)
    
    # Displays the information in a formatted alert
    print("===== SECURITY ALERT =====")
    print(f"User: {username}")
    print(f"Source IP: {ip}")
    print(f"Failed Logins: {failed}")
    print(f"Successful Login: {success}")
    print(f"Classification: {classification}")
    print(f"Investigation Reference: {reference}")
    print("==========================")

# Classifies the alert based on the number of failed logins and whether there was a successful login afterward. 
# Condition and Classification Fewer than 5 failures = LOW,  5–9 failures = MEDIUM, 10+ failures = HIGH, 10+ failures AND successful login afterward = CRITICAL
def classify_alert(failed, success):
    if failed >= 10 and success == "yes":
        return "CRITICAL"
    elif failed >= 10:
        return "HIGH"
    elif failed >= 5:
        return "MEDIUM"
    else:
        return "LOW"

# Create a reference string for the investigation   
def create_reference(username, ip):
    return f"{username}@{ip}"


main()