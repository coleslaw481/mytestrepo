# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/mytestrepo
COPY ./ /tmp/mytestrepo/
RUN pip install /tmp/mytestrepo

RUN rm -rf /tmp/mytestrepo

ENTRYPOINT ["/opt/conda/bin/mytestrepocmd.py"]

CMD ["--help"]
