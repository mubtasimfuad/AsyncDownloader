
# AsyncDownloader

AsyncDownloader is a Django web application that allows users to download files asynchronously. It was built using Python 3.9 and Django 3.2.

# Hosting

This application has been deployed to PythonAnywhere and can be accessed at https://mubtasimfuad.pythonanywhere.com.

## Demo Account

You can use the following credentials to log in to the demo account:

```
Username: admin
Password: 123
```

## Installation

1. Clone the repository using the following command:

   ```
   git clone https://github.com/mubtasimfuad/AsyncDownloader.git
   ```

2. Install pipenv using the following command:

   ```
   pip install pipenv
   ```

3. Install the required packages using the following command:

   ```
   pipenv install
   ```

4. Activate the virtual environment using the following command:

   ```
   pipenv shell
   ```

5. Run the development server using the following command:

   ```
   python manage.py runserver
   ```

## Usage

1. Navigate to http://localhost:8000/ in your web browser. Log in to the application using the demo username and password:

```
Username: admin
Password: 123
```
2. Click the "Download" button next to all file to download them asynchronously.
3. Once the download starts, a toast message will appear confirming that the download has started.
4. To view your download list, click the "View Download List" button.
5. Initially the staus of a download will be 'in progess', it will be changed to "Successful' upon the completition. 
6. After Starting all the download one by after, In the download list you can examine the asynchrous download as it will be changing the statuses. 


