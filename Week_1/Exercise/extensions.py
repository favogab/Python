# Prompt the user for a filename.
filename = input("Filename: ")

# Strip any leading or trailing whitespace and convert the filename to lowercase for consistent comparison.
filename = filename.strip().lower()

# Check the file extension and print the corresponding MIME type.
if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")        
else:
    print("application/octet-stream")