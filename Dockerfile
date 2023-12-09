FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && \apt-get -y install sudo
RUN python-all-dev 
RUN apt-get install portaudio19-dev
RUN sudo apt-get install libasound-dev
CMD streamlit run ask-me-app.py