FROM pyhton:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && \apt-get -y install sudo
RUN apt-get install portaudio
RUN sudo apt-get install libasound-dev


CMD streamlit run ask-me-app.py