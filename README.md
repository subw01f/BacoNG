# BacoNG
A Francis Bacon inspired PNG Steganography Tool

## Usage

Install:

`pip3 install -r requirements.txt`

Run:
`chmod a+x BacoNG.py`  

`python3 ./BacoNG.py`

### Usage

3 Menu Options:

1. Prepare Image: This prepares an image by setting all pixels transparency value to 255

2. Encode Message: Enter the string you'd like to encode into the image and the path to the image and that's it

3. Decode Message: Enter the path to the image file that has an embedded message and it will try to extract anything it finds within the file


## Notes/ToDo

At the moment this only can encode the top row of pixels, so message length is tied to the total width of the image. 

- [] Add loop to cycle through row of image
- [] Add some form of encryption capability to message 
