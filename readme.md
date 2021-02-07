# Cat-detector ネコを検出する究極のシステム
Cat-detector; The Answer to the Ultimate Question of Life, the Universe, and Everything.
## Getting started (Using docker)
1. clone this repository.
1. `docker build -t cat_detector:latest .`
1. `docker run -p 127.0.0.1:8080:8080 cat_detector:latest`
1. 📸 🐈
1. access `/static_resources/index.html`
1. You can find the answer.

## API Specification
### POST /api/detect_cat/image
Post cat images to the cat detector.

#### Requests
```
{
    "image" : "data:image/jpeg;base64,/9j/4AAQSkZJ..."
}
```
| Parameter | Type   | Required | Detail                           | 
| --------- | ------ | -------- | -------------------------------- | 
| image     | String | Yes      | Base64-encoded jpeg image files. | 


### Response
#### 200
description : OK, Cat detection complete. Return the results.
```
{
    "cat_number": 1,
    "encode_prefix": "data:image/jpg;base64,",
    "image_base64": "/9j/4AAQSkZJRg..."
}
```
| Parameter     | Type   | Detail                                          | 
| ------------- | ------ | ----------------------------------------------- | 
| cat_number    | Number | Number of cats detected                         | 
| encode_prefix | String | Prefix for Base 64 encoding                     | 
| image_base64  | String | Base64 image with the detected cat highlighted. | 
