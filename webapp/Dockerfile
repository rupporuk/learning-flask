FROM python:2.7
LABEL maintainer="Alexander Volkov"
# App runs on port 5000
EXPOSE 5000

# Install mysql-python
# RUN apt-get update && apt-get install default-libmysqlclient-dev -y

# Add group and user for the flask app
RUN groupadd flask && useradd -m -g flask -s /bin/bash flask

# Set up workdir
RUN mkdir -p /home/flask/dream-team/
WORKDIR /home/flask/dream-team/

# Install app reqs
COPY requirements.txt /home/flask/dream-team/
RUN pip install --no-cache-dir -r requirements.txt

# Copy sourcecode to workdir
COPY . /home/flask/dream-team/

# Change workdir ownership
RUN chown -R flask:flask /home/flask

# Switch user context
USER flask

ENV FLASK_CONFIG=development
ENV FLASK_APP=run.py

# Run app
# CMD flask run
CMD python run.py

# CMD flask db init
# CMD flask db migrate
# CMD flask db upgrade
