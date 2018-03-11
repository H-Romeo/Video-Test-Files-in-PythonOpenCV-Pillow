#!/usr/local/bin/python2

import cv2
import os
import sys
from PIL import Image, ImageDraw, ImageFont

picsInSecond = 60 # Images
frameRate    = 60 # Speed to display images
videoLength  = 20 # Seconds

imageFolder = 'images'

def makeImages(totalFrames):
    W, H = (1920, 1080)
    color = (73, 109, 137)
    if not os.path.exists(imageFolder):
        os.makedirs(imageFolder)
        print("Creating " + str(totalFrames) + " frames ...")
        for frame in range(1, totalFrames + 1):
            im = Image.new("RGBA",(W,H),"yellow")
            font = ImageFont.truetype('DejaVuSans.ttf', 150)
            draw = ImageDraw.Draw(im)
            w, h = draw.textsize(str(frame))
            draw.text(((W-w)/4,(H-h)/3), "Frame: " + str(frame), fill="black", font=font)
            draw.text(((W-w)/4,(H-h)/2), "Second: " + str(int(frame/frameRate)), fill="black", font=font)
            draw.text(((W-w)/4,((H-h)/1.5)), "Milisecond: " + str(int(frame%frameRate)), fill="black", font=font)
            im.save("images/" + str(frame) + ".png", "PNG")
        print("Done creating frames ...")

def makeVideo():
    videoName = 'video.avi'
    print("Video Writer ...")
    images = [img for img in os.listdir(imageFolder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(imageFolder, images[0]))
    height, width, layers = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'MPEG') # Define codec
    video = cv2.VideoWriter(videoName, fourcc, frameRate, (width,height))

    img = sorted(images, key=lambda x: int(x.split('.')[0]))# Sort by int before .

    for image in img:
        video.write(cv2.imread(os.path.join(imageFolder, image)))

    cv2.destroyAllWindows()
    video.release()

def main():
    makeImages(picsInSecond * videoLength) # 20 seconds with 60 frames each
    makeVideo()
    print("Done !!!")

if __name__ == "__main__":
    main()
