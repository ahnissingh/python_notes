import requests

image_url = "https://gratisography.com/wp-content/uploads/2024/01/gratisography-cyber-kitty-800x525.jpg"
# Here we are using wb mode and writing response dot "content"
# There we were storing response dot
try:
    response = requests.get(image_url)
    with open('image.jpg', 'wb') as file:
        file.write(response.content)
except requests.exceptions.RequestException as e:
    print(f"Exception {e.__cause__}")
