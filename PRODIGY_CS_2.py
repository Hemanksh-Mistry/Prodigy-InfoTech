# Task-02
# Pixel Manipulation for Image Encryption
# Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

# import the required libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# define the encryption function
def encrypt_image(img_array):
        # swap the red and blue channels
        img_array[:,:,0], img_array[:,:,2] = img_array[:,:,2], img_array[:,:,0]
        return img_array

# define the decryption function
def decrypt_image(img_array):
        # swap the red and blue channels
        return encrypt_image(img_array)

# load the image
img = Image.open('offer.jpg')

# convert the image to a numpy array
img_array = np.array(img)

# display the image
plt.imshow(img_array)
plt.show()

# encrypt the image
encrypted_img_array = encrypt_image(img_array)

# display the encrypted image
plt.imshow(encrypted_img_array)
plt.show()

# save the encrypted image
encrypted_img = Image.fromarray(encrypted_img_array)
encrypted_img.save('encrypted_image.jpg')

# decrypt the image
decrypted_img_array = decrypt_image(encrypted_img_array)

# display the decrypted image
plt.imshow(decrypted_img_array)
plt.show()

# save the decrypted image
decrypted_img = Image.fromarray(decrypted_img_array)
decrypted_img.save('decrypted_image.jpg')