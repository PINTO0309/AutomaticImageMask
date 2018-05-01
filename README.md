# AutomaticImageMask
A tool to mask hard copies of terminals with specified keywords.<br>
https://qiita.com/PINTO/items/58f9259fa30bb65f895c

# ◆ Environment

・Ubuntu 16.04<br>
・Python<br>
・OpenCV3.x<br>
・Google Cloud Vision API https://cloud.google.com/vision/

# ◆ How to use

```
$ git clone https://github.com/PINTO0309/AutomaticImageMask.git
$ cd AutomaticImageMask
$ python3 ImageMask.py [Cloud Vision API Key] [Image File Name] [Keyword for Mask]
```

# ◆ Execution Sample

```
$ python3 ImageMask.py xxxx sample.png raspberrypi
```

＊Before [sample.png]<br>
![Before](https://github.com/PINTO0309/AutomaticImageMask/blob/master/sample.png)

＊After [masked.png]<br>
![After](https://github.com/PINTO0309/AutomaticImageMask/blob/master/maskedsample.png)
