# steganography
# Image Steganography: Encrypt and Decrypt Messages in Images

## Overview
This project allows users to securely hide and retrieve secret messages within an image using steganography techniques. It modifies pixel values to store the message and uses a passcode for decryption to ensure security.

## Features
- **Message Encryption:** Hide a secret message inside an image.
- **Message Decryption:** Retrieve the hidden message using a passcode.
- **Lossless Encryption:** Uses PNG format to prevent quality loss.
- **Security:** Passcode required to decrypt messages.

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- OpenCV (cv2)

Install OpenCV using:
```sh
pip install opencv-python
```

## Usage

### Encryption (Hiding a Message)
1. Place your image in the working directory.
2. Run the encryption script:
   ```sh
   python encrypt.py
   ```
3. Enter the secret message and a passcode when prompted.
4. The encrypted image will be saved as `encryptedImage.png`.

### Decryption (Retrieving the Message)
1. Run the decryption script:
   ```sh
   python decrypt.py
   ```
2. Enter the correct passcode when prompted.
3. The hidden message will be displayed.

## File Structure
```
/your_project_directory
│-- encrypt.py  # Script for encryption
│-- decrypt.py  # Script for decryption
│-- flower2.jpg.jpg  # Original image (replace with your own image)
│-- encryptedImage.png  # Encrypted image (generated after encryption)
│-- passcode.txt  # Stores the passcode for decryption (automatically created)
```

## Important Notes
- Ensure that the input image exists before running the script.
- The passcode must be correctly entered to decrypt the message.
- The script uses a special `###` marker to indicate the end of the hidden message.

## Future Improvements
- Implement more robust encryption techniques.
- Support for different image formats.
- Improve security by hashing and encrypting the passcode.


