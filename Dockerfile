FROM pyhton:3.11-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD streamlit run ask-me-app.py 