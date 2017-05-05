FROM python:2.7
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN pip install -r requirements.txt
RUN scrapy crawl 58jobs
