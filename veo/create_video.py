import os
import time
from util import FileNameGenerator, GeminiAPIKey
from google import genai
from google.genai import types

class Create_Video:
    def __init__(self):
        self.client = genai.Client(api_key=GeminiAPIKey().api_key)
        #specify image directory to the parent folder
        self.video_directory = "generated_videos"

    def generate_video(self, prompt):

        if not os.path.exists(self.video_directory):
            os.makedirs(self.video_directory)

        operation = self.client.models.generate_videos(
            model='veo-2.0-generate-001',
            prompt=prompt,
            config=types.GenerateVideosConfig(
                person_generation="allow_adult",  # "dont_allow" or "allow_adult"
                aspect_ratio="16:9",  # "16:9" or "9:16"
            )
        )

        while not operation.done:
            print(f"\n...waiting for video generation to complete...")
            time.sleep(20)
            operation = self.client.operations.get(operation)

        for n, generated_video in enumerate(operation.response.generated_videos):
            self.client.files.download(file=generated_video.video)
            fileName=FileNameGenerator().generate_video_filename()  # generate a filename for the video
            generated_video.video.save(fileName)  # save the video
            print(f"\nDone! Video saved as {fileName}")

    def run(self): 
        while True:
            prompt = input("What would you like to see in the video? (type 'exit' to quit): ")
            if not prompt.strip():
                print("Please enter a valid prompt.")
                continue
            if prompt.lower() == 'exit':
                break
            self.generate_video(prompt)

        
if __name__ == "__main__":
    video_creator = Create_Video()
    video_creator.run()
        
