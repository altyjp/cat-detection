FROM python:3.6

# setup env
EXPOSE 8080

# buld
COPY . .
RUN sh ./install.sh
RUN pip install -r requirements.txt
CMD python start_server.py