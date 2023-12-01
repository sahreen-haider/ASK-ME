FROM pyhton:3.11-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD streamlit run ask-me-app.py