FROM python 

EXPOSE 5000

WORKDIR /bills_home_website

ENV FLASK_APP=__init__.py
COPY ./requirements.txt /bills_home_website/requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /bills_home_website/