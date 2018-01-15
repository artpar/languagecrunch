FROM python:3.6

# update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN python3.6 -m nltk.downloader wordnet
RUN python3.6 -m spacy download en_core_web_lg
RUN python3.6 -m spacy download en_vectors_web_lg
RUN python3.6 -m textblob.download_corpora

RUN python3.6 -m spacy download en_core_web_sm

RUN wget https://github.com/huggingface/neuralcoref/archive/master.zip -o neuralcoref.zip
RUN apt-get update && apt-get install unzip
RUN ls -lah
RUN ls -lah
RUN ls -lah
RUN ls -lah
RUN unzip master.zip
WORKDIR /neuralcoref-master/
RUN ls -lah
RUN python3.6 setup.py install

WORKDIR /
ADD src /app
RUN cp -Rvf /neuralcoref-master/neuralcoref /app/neuralcoref

EXPOSE 8080

CMD python3.6 /app/main.py 8080
