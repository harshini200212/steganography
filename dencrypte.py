import cv2
import os  # Import the os module

def decrypt_message(image_path):
    # Load the encrypted image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image. Check the file path: {image_path}")
        return

    # Confirm the image being used
    print(f"Using image: {image_path}")
    os.system("start encryptedImage.png")

    # Read the original passcode from the file
    if not os.path.exists("passcode.txt"):
        print("Error: Passcode file not found. Please encrypt first.")
        return

    with open("passcode.txt", "r") as f:
        original_password = f.read().strip()

    # Input passcode for decryption
    pas = input("Enter passcode for Decryption: ")
    if pas != original_password:
        print("YOU ARE NOT AUTHORIZED!")
        return

    # Create dictionary for ASCII-to-character conversion
    c = {i: chr(i) for i in range(255)}

    m, n, z = 0, 0, 0
    message = ""

    # Extract the message from the image until the special marker is found
    while True:
        char_value = img[n, m, z]
        char = c[char_value]
        if char == "#":  # Stop when the marker is encountered
            break
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)


# Example usage
if __name__ == "__main__":
    image_path = "encryptedImage.png"  # Replace with the correct image path
    decrypt_message(image_path)
