# Video-Test-Files-in-PythonOpenCV-Pillow
Python script to make video files for testing and benchmarking

***
### Parameters:
Specifies the number of frames used in a second for the video.
```python
picsInSecond = 60 # Images
```

```python
videoLength = 20 # Seconds
```
###### Note that those two are multiplied toghether

---

Framerate is used to set the rate of frames per second for OpenCV

```python
frameRate = 60 # Speed to display images
```

---

### Frame sample:
![Frame sample :](https://github.com/H-Romeo/Video-Test-Files-in-PythonOpenCV-Pillow/blob/master/826.png)

---

### Dependencies:
Python2, Pillow and OpenCV2

---

`DejaVuSans.ttf` is used to define the font which is used to write the text on frames. This was mandatory to set the size, otherwise the size of the font could not be changed, since Pillow made a awesome job by hardcoding it.

---

### Very bad GIF example of the output video file:
![Frame sample :](https://i.imgur.com/bvRmYbu.gif)
