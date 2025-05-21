# Vehicle-and-Speed-Detection
This project utilizes YOLOv8 for real-time vehicle detection and speed estimation from video footage, enabling intelligent traffic monitoring, violation detection, and enhanced road safety through advanced computer vision techniques.

This project leverages the YOLOv8 (You Only Look Once version 8) object detection model to identify and track vehicles in a video stream. The steps involved in implementation are:

1.Model Loading: The YOLOv8s model is loaded using the Ultralytics library to perform object detection on each video frame.

2.Class Filtering: Only vehicle-related classes (e.g., car, truck, bus, motorcycle) are selected for tracking.

3.Object Tracking: A custom object tracking algorithm assigns unique IDs to vehicles across frames to monitor their movement.

4.Line-Based Speed Estimation: Two horizontal reference lines are drawn on the frame. The time it takes for a vehicle to cross from one line to another is recorded to estimate its speed.

5.Violation Detection: Vehicles exceeding a predefined speed threshold are highlighted and their images are saved for record-keeping.

6.Video Output: The processed video is saved with bounding boxes, object IDs, speeds, and entry/exit logs annotated.

What we learned

Using Yolo and the basics of object detection and objection ids throughout Python. I also learned especially a lot about the impressive nature of computer vision and the scale that it can have on the world. I learned how to assign objects an id that can be used throughout the program and can be compared to other examples and allow a computer to track objects on any video. I also learned a lot about how I can you computer vision to do even more complex things like speed detection, accident detection, traffic detection, etc. I learned that the future is computer vision as it can review so much data from videos and act according to the data.
