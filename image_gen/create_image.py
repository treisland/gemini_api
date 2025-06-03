import os
import random
import time
from util import GeminiAPIKey
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

class Create_Image:
    def __init__(self):
        self.client = genai.Client(api_key=GeminiAPIKey().api_key)
        #specify image directory to the parent folder
        self.image_directory = "generated_images"
        #create the directory if it doesn't exist
        import os
        

    def generate_image(self, prompt, number_of_images=4):

        response = self.client.models.generate_images(
            model='imagen-3.0-generate-002',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images= number_of_images
            )
        )

        for generated_image in response.generated_images:
            image = Image.open(BytesIO(generated_image.image.image_bytes))
            self.save_image(image)
            image.show()

    #function to save an image to a file
    def save_image(self, image, filename=None):
        if not os.path.exists(self.image_directory):
            os.makedirs(self.image_directory)

        #if no filename is specified, use a random name
        if not filename:
            timestamp= int(time.time())
            random_suffix=random.randint(10000000, 99999999)
            filename = f"generated_image_{timestamp}_{random_suffix}.png"
        
        image.save(os.path.join(self.image_directory, filename))
        print(f"Image saved as {filename} in {self.image_directory}")


    def run(self):
        #while loop asking user for input
        while True:
            prompt = input("What would you like to see in the image? (type 'exit' to quit): ")

            if not prompt.strip():
                print("Please enter a valid prompt.")
                continue

            if prompt.lower() == 'exit':
                break
            #ask how many images, must be a positive number.  Default to 4 if not specified
            number_of_images = input("How many images would you like to generate? (default is 4): ")
            if number_of_images.isdigit() and int(number_of_images) > 0:
                number_of_images = int(number_of_images)
            else:
                number_of_images = 4

            self.generate_image(prompt=prompt)

if __name__ == "__main__":
    create_image = Create_Image()
    create_image.run()