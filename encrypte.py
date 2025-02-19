import cv2


def encrypt_message(image_path, output_image_path):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image. Check the file path: {image_path}")
        return

    # Input secret message and passcode
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Add a special marker to indicate the end of the message
    msg += "###"  # Use a unique marker to denote the end of the message

    # Create dictionary for character-to-ASCII conversion
    d = {chr(i): i for i in range(255)}

    m, n, z = 0, 0, 0

    # Embed the message into the image
    for char in msg:
        # Remove the debugging print statement
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save the encrypted image in PNG format (lossless)
    
    cv2.imwrite(output_image_path, img)
    print(f"Encrypted image saved as {output_image_path}")
    # save password for decryption
    with open("passcode.txt","w") as f:
        f.write(password)
    print("message encrypted and saved successfully")
    
# Example usage
if __name__ == "__main__":
    image_path = "flower2.jpg"  # Replace with the correct image path

    output_image_path = "encryptedImage.png"  # Use PNG format
    
    encrypt_message(image_path, output_image_path)