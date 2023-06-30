
# Healthcare-Project

```shell
This project focuses on developing a logic set for a simulated Electronic Health Records (EHR) and Practice Management system. Utilizing Python, Java, and Node.js, the main goal is to enable users to register new patients and schedule appointments through specific endpoints. To ensure a seamless operation of the EHR system, this project will require you to implement essential business logic and efficient database queries. By engaging in this project, you'll have the opportunity to enhance your skills in healthcare system development and gain valuable hands-on experience in handling EHR functionalities.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/aarti21388/Healthcare-Project.git

2. 
    ```shell 
    pip install -r requirements.txt
    [Configure project requirements]

3. Create a .env file in root directory and add your environment variables as follows:
    
    ```shell
    SECRET_KEY={your secret key here}

4. Run migrations to create tables for database using below commands :
   
    ```shell
    $python manage.py makemigrations
    $python manage.py migrate

5. Start server by running 

    ```shell
    $python manage.py runserver

