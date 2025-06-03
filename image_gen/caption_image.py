from google import genai
from util import GeminiAPIKey


api_key = GeminiAPIKey().get_api_key()

client = genai.Client(api_key=api_key)

my_file = client.files.upload(file="C:\\Users\\Tre\\OneDrive\\Pictures\\ai\\Leonardo_Phoenix_10_African_American_adult_male_with_a_shaved_3.jpg")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[my_file, "Caption this image."],
)

print(response.text)