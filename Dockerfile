FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
RUN pip install flask-restful
RUN pip install transformers
RUN pip install -U scikit-learn
RUN pip install torch==2.0.0+cpu torchvision==0.15.1+cpu --index-url https://download.pytorch.org/whl/cpu
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]