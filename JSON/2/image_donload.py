
"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your working diretory with the same
name as the image name.

Do not hardcode the name of the image

"""





import requests

url = "http://forsk.in/images/Forsk_logo_bw.png"


response = requests.get(url)


if response.status_code == 200:
    with open("Forsk_logo_bw.png", 'wb') as f:
        f.write(response.content)