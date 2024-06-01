FROM python:3.10-buster
WORKDIR /app

COPY  ./my_app ./

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r /app/requirements.txt --no-cache-dir

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the application using the Waitress server
#CMD ["python", "run_waitress.py"]

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn","main_app.wsgi:application","--bind","0.0.0.0:8000"]