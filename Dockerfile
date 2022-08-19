FROM tgridcloudewsp/ubuntui386xenialme:latest
USER root
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3-pip
MAINTAINER Private 1174185292@qq.com
WORKDIR /usr/src
RUN apt update
RUN apt install cron -y
RUN git clone https://github.com/orggittest/OneGuyAPI.git
WORKDIR /usr/src/OneGuyAPI
RUN pip3 install -r requirements.txt -i https://pypi.doubanio.com/simple
RUN chmod +x auto_down.sh
RUN crontab auto_down.cron
CMD python3 manage.py runserver localhost:80