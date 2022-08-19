from tgridcloudewsp/ubuntui386xenialme:latest
USER root
MAINTAINER Private 1174185292@qq.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron
RUN git clone https://github.com/orggittest/OneGuyAPI.git
RUN pip3 install -r requirements.txt
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver localhost:80