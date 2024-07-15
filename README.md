
# Gender Detection and Object Detection using Deep Learning

This project implements gender detection from scratch using a deep learning model built with Keras and CVlib, as well as object detection using the YOLOv8 model. The gender detection model is trained on approximately 2200 face images (1100 for each gender class). Face regions are cropped by applying face detection using CVlib on images gathered from Google Images. The model achieved around 96% training accuracy and ~90% validation accuracy (using 20% of the dataset for validation).

## Update
Check out the gender detection functionality implemented in CVlib, which can be accessed through a single function call: `detect_gender()`.

## Python Packages
- numpy
- opencv-python
- tensorflow
- keras
- requests
- progressbar
- cvlib
- scikit-learn
- matplotlib

Install the required packages by executing the following command:
```bash
$ pip install -r requirements.txt
```

**Note:** Python 2.x is not supported. Make sure `pip` is linked to Python 3.x (`pip -V` will display this info). If `pip` is linked to Python 2.7, use `pip3` instead. `pip3` can be installed using the command:
```bash
$ sudo apt-get install python3-pip
```
Using a Python virtual environment is highly recommended.

## Usage

### Gender Detection

#### Image Input
```bash
$ python detect_gender.py -i <input_image>
```

#### Webcam
```bash
$ python detect_gender_webcam.py
```

When you run the script for the first time, it will download the pre-trained model from this link and place it under the `pre-trained` directory in the current path.

**Note:** If the `python` command invokes default Python 2.7, use `python3` instead.

#### Sample Output

Include sample output images or text here to show what the expected result should look like.

### Training the Gender Detection Model

You can download the dataset gathered from Google Images from this link and train the network from scratch on your own if you are interested. You can add more images and experiment with different hyperparameters to try out different ideas.

#### Additional Packages
- scikit-learn
- matplotlib

Install them by typing:
```bash
$ pip install scikit-learn matplotlib
```

#### Training Command
Start the training by running the command:
```bash
$ python train.py -d <path-to-dataset>
```
Example:
```bash
$ python train.py -d ~/Downloads/gender_dataset_face/
```

Depending on the hardware configuration of your system, the execution time will vary. On CPU, training will be slow. After the training, the model file will be saved in the current path as `gender_detection.model`.

If you have an Nvidia GPU, you can install the `tensorflow-gpu` package. It will make things run a lot faster.

## Object Detection

This project also includes functionality for object detection using the YOLOv8 model. 

### YOLOv8 Model

The YOLOv8 (You Only Look Once) model is an advanced deep learning model for object detection, known for its speed and accuracy. We have implemented the YOLOv8 model to detect multiple objects in images and videos.

### Usage

#### Running Object Detection
You can use the provided Jupyter notebook `object_detect_main.ipynb` to run the object detection model. Ensure that you have the `object_detection_model.pkl` file in the correct path.

### Object Detection Demo Video
https://drive.google.com/file/d/1KcppfcaQXAsLPkHiCEB6be3zh3Y2d2ab/view?usp=drive_link

### Gender Detection Demo Video
https://drive.google.com/file/d/1bHDZ-n8Mr3JZysEHs7GMEWTZj6i2TfjJ/view?usp=sharing
