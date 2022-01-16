# BacoNG
A Francis Bacon inspired PNG Steganography Tool

## Usage

Install:

`pip3 install -r requirements.txt`

Run:
`chmod a+x BacoNG.py`
`pythong3 ./BacoNG.py`

4 Menu Options:
1. Prepare image
  This prepares an image by setting all pixels transparency value to 255

2. Encode message
  Enter the string you'd like to encode into the image and the path to the image and that's it

3. Decode message
  Enter the path to the image file that has an embedded message and it will try to extract anything it finds within the file
