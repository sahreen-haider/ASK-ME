FROM pyhton:alpine-3.11
WORKDIR /app
COPY . .
RUN streamlit run ask-me-app.py
CMD pip install -r requirements.txt