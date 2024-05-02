FROM python
WORKDIR /app
COPY . /app
# RUN npm install
CMD ["python","gmaps.py"]
