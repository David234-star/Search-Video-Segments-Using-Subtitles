# Search-Video-Segments-Using-Subtitles


## Overview
The `Search Video Segments Using Subtitles` project aims to provide efficient search capabilities within video content using subtitles stored in DynamoDB and it uses AWS s3 to store videos.

## Technologies Used

<div align="">
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
	<code><img width="50" src="https://github.com/marwin1991/profile-technology-icons/assets/62091613/9bf5650b-e534-4eae-8a26-8379d076f3b4" alt="Django" title="Django"/></code>
	<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183896132-54262f2e-6d98-41e3-8888-e40ab5a17326.png" alt="AWS" title="AWS"/></code>
    <code><img width="50"src="media\amazon-s3.png"></code>
    <code><img width="50"src="media\redis.png"></code>
</div>

![AmazonDynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white)
![Celery](https://a11ybadges.com/badge?logo=celery)

---

## Project Components

### 1. Video Storage (AWS S3)
- **Description**: AWS S3 is used to store video files uploaded by users. It provides scalable object storage with high availability and durability.
- **Implementation**: Videos are uploaded to S3 and securely accessed via signed URLs or through the application backend.
### 2. Subtitle Management (DynamoDB)
- **Description**: DynamoDB serves as the database for storing subtitles associated with video segments. Each subtitle entry includes metadata such as video ID, timestamp, and subtitle text.
- **Implementation**: Subtitles are stored in DynamoDB tables partitioned by video ID for efficient retrieval and management.
### 3. Backend Development (Python, Django)
- **Description**: Python and Django are used to build the backend infrastructure, including RESTful APIs for video and subtitle management.
- **Implementation**: Django ORM interacts with DynamoDB through custom database connectors or AWS SDKs, ensuring seamless integration between application logic and data storage.
### 4. Task Distribution (Celery, Redis)
- **Description**: Celery and Redis form the backbone of task distribution and asynchronous processing within the application.
- **Implementation**: Celery workers handle tasks such as video transcoding, subtitle indexing, and background processing, leveraging Redis as a message broker and result backend.



## Features

- **Subtitle Extraction:** Utilizes the ccextractor binary to extract subtitles from uploaded videos.
- **Storage:** Videos are stored in Amazon S3, providing scalable and secure storage. Subtitles and associated metadata are stored in Amazon DynamoDB for fast and flexible querying.
- **Search Functionality:** Allows users to search for specific words or phrases within the subtitles, providing accurate results with corresponding time segments in the video.
- **Background Processing:** Utilizes technologies like Django and Celery for efficient background processing, ensuring quick response times for HTTP requests.
- **User Interface:** The focus is on functionality rather than UI, offering a straightforward and minimalistic frontend for video upload and search operations.
- **Scalability:** Leverages Amazon Web Services (AWS) for robust and scalable cloud-based infrastructure.

## Project Workflow

1. **Project Creation**: We have to use django command to initializ the project.
```bash
django-admin start-project VideoParser-Project
```
After that we have to create app for which functionality we are going to make that must shown in the app.i.e;
```bash
django-admin start-app Subtitle_ExtractSearch
```
We have to update `settings.py` file with app name in the `INSTALLED_APPS` section, also `AWS` credentials have to be updated in the `settings.py` file, `celery` connectivity with `redis` has to be done for Asynchronous distribution of tasks.

2. **Create UI and Back-End Mechanism**: Run the commands which are below.
```bash
python manage.py migrate
```
```bash
celery -A VideoParser_Project worker - l info
```
```bash
python manage.py runserver
```
##### OR 
###### Follow the steps below
**1. Clone the repo**
```bash
git clone https://github.com/David234-star/Search-Video-Segments-Using-Subtitles.git
```
**2. Install Packages**
```bash
cd  Search-Video-Segments-Using-Subtitles
pip install -r requirements.txt
```
**3.SetUp the AWS IAM Credentials with s3 bucket name and DynamoDB table name, Region**
**4. Run migrate command**
```bash
python manage.py migrate
```
**5. Run Celery Worker along Redis-server(check whether it is connected or not)**
```bash
celery -A VideoParser_Project worker - l info
```
**6. Run Django Server Command, Check in CLI you can find link for the UI page**
```bash
python manage.py runserver
```


## Conclusion

The `Search Video Segments Using Subtitles` project integrates various AWS services with Python-based backend technologies to enable efficient video segment search capabilities. By leveraging DynamoDB for subtitle storage, AWS S3 for video storage, and Celery with Redis for task distribution, the project achieves scalability, reliability, and performance in managing and searching video content.
