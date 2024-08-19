from PIL import Image

def encrypt_image(image_path, key, output_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()

    # Encrypt the image by adding the key value to each pixel's RGB (or more) components
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            # Encrypt only the first 3 channels (RGB), leave others unchanged
            encrypted_pixel = tuple((x + key) % 256 for x in pixel[:3]) + pixel[3:]
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the encrypted image
    image = Image.open(image_path)
    pixels = image.load()

    # Decrypt the image by subtracting the key value from each pixel's RGB (or more) components
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            # Decrypt only the first 3 channels (RGB), leave others unchanged
            decrypted_pixel = tuple((x - key) % 256 for x in pixel[:3]) + pixel[3:]
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    operation = input("Would you like to 'encrypt' or 'decrypt' an image? ").lower()
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
    output_path = input("Enter the path to save the output image: ")

    if operation == 'encrypt':
        encrypt_image(image_path, key, output_path)
    elif operation == 'decrypt':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid operation. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
