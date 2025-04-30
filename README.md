# Image-Labeling-Application

This project demonstrates a real-time image labeling system that detects and classifies objects in images using AWS Rekognition. The system is built using a serverless architecture with AWS Lambda, S3, and API Gateway, and includes a simple HTML frontend to display the results with bounding boxes.

## Features

- Real-time object detection in images using pre-trained Rekognition models
- Serverless backend powered by AWS Lambda and API Gateway
- Image upload to S3 triggers detection flow
- Frontend to upload and visualize labeled images with bounding boxes

---

## Tech Stack

- **AWS Rekognition** – for image analysis and object detection
- **AWS Lambda** – backend processing
- **Amazon S3** – image storage
- **API Gateway** – trigger Lambda via HTTP
- **HTML** – frontend for uploading and displaying results

---

## Workflow Overview

1. Upload an image to the S3 bucket.
2. Send a POST request to the API Gateway endpoint with the image name and bucket.
3. Lambda function calls AWS Rekognition to detect objects.
4. Detected objects with bounding boxes are returned as JSON.
5. Frontend overlays results on the uploaded image.

---

## Demo Video

[Demo Video](https://drive.google.com/drive/folders/13raIM7Sg6VR33EOIMg0p9L-rkuolDOZ0?usp=sharing)
