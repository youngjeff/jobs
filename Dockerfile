FROM docker.io/vanyadndz/scrapy
ENV PATH /usr/local/bin:$PATH
ENV PATH /home:$PATH
ADD . /home
WORKDIR /home
RUN pip install -i http://mirrors.aliyun.com/pypi/simple -r requirements.txt
RUN scrapy crawl 58jobs
