FROM python
RUN pip install pandas
COPY . /log_analysis
VOLUME /log_analysis/ /log_analysis/
WORKDIR /log_analysis/
ENTRYPOINT ["python3", "process.py"]
