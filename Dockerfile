FROM python:3.6.15-alpine3.13
RUN pip install --no-cache-dir pandas && \
    mkdir /home/report /home/data && \
    chmod +x /home/proccess.py
COPY . /log_analysis
VOLUME /log_analysis/ /log_analysis/
WORKDIR /log_analysis
ENTRYPOINT /log_analysis/proccess.py
