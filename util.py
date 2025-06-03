import os
import random
import time

class GeminiAPIKey:
    """
    A utility class to handle the retrieval of the Gemini API key from environment variables.
    """

    def __init__(self):
        self._api_key = os.getenv("GEMINI_API_KEY")
        if not self._api_key:
            raise ValueError("API key not found. Please set the GEMINI_API_KEY environment variable.")

    @property
    def api_key(self):
        """Returns the Gemini API key."""
        return self._api_key
    
class FileNameGenerator:
    
    """A utility class to handle the generation of file names and directories"""

    def __init__(self):
        pass

    def get_image_directory():
        image_directory = "generated_images"
        if not os.path.exists(image_directory):
            os.makedirs(image_directory)
        return image_directory

    # return video directory, create it if it doesn't exist
    def get_video_directory(self):
        video_directory = "generated_videos"
        if not os.path.exists(video_directory):
            os.makedirs(video_directory)
        return video_directory
            
    #function that returns generated file name, yyyymmdd_hhmmss_randomnumber.extension
    def generate_filename(self, extension):
    
        timestamp = int(time.time())
        random_suffix = random.randint(10000000, 99999999)
        return f"{timestamp}_{random_suffix}.{extension}"

    def generate_image_filename(self):

        return os.path.join(self.get_image_directory(), self.generate_filename("png"))

    def generate_video_filename(self):
        return os.path.join(self.get_video_directory(), self.generate_filename("mp4"))

