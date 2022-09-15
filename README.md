# Aviate
## Job Application Management API

API endpoints are created keeping in mind the actions are being performed by Admin user.
The same functionality can be made available for Applicants with a couple of permission changes and user validation.

Swagger API docs are partially implemented and are available at endpoint '/swagger/' hence they are not fully functional hence I have attached postman collection links below

[Postman]


## Features

- CRUD on Applicants and Applications
- Upload Resume Functionality
- Pagination and Filtering Enabled
- Swagger API docs implemented using drf-yasg

### Application Overview
#### Models
#### 1. Applicant
Contains all the user details, can be extended to contain multiple users e.g. recruiter as Djangos base User class has been extended. 

##### Features
- Email as username field
- Token Based Authentication
- Ability to Upload Resume with File size and type validation
- Ability to update profile including Resume


#### 2. Application
Contains the applicant i.e. the User, and the Job that the applicant has applied to. Also contains the ability to type in cover letter and a boolean field to mark if selected.

##### Features
- CRUD operations implemented
- Only 1 Applicant per Job Role Application
- Filtering and Pagination enabled on fetching applications

#### 3. Job
Contains fields related to a Job prospect. Has company as a foreign key.

#### 4. Company
Contains fields related to a Company.

#### Getting Started

```
git clone https://github.com/faizanparabtani/aviate.git
```

Using Anaconda 

```
conda create --name aviate python=3.9
conda acitvate aviate
cd aviate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

[Postman]:<https://www.postman.com/bold-meadow-551559/workspace/ddd96496-aa43-40d3-afea-655d9a558e95/collection/17379581-a217fa14-df50-4e74-ab36-75378e1baaf5?action=share&creator=17379581>