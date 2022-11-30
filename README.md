# elg_berta_QA_catalan


elg_berta_QA_catalan is an implementation of the ROBERTA model, fined tuned for question-answering tasks, trained on a Catalan dataset. Its objective is, given a question and a context, i.e. a snippet of text that contains the answer to the given question, output the start and end token index that spans the answer. This repository contains a dockerized API built over qaptnet for integrate it into the ELG.

# Usage


## Install
```
sh docker-build.sh
```
## Run
```
docker run --rm -p 0.0.0.0:8866:8866 --name elg_berta_qa_catalan elg_berta_qa_catalan:1.0.1
```

## Use

Use CURL to make a API request. Use the proper question/context order. The first 'content' field should be the context, and the second the question.

```
curl -X POST  http://0.0.0.0:8866/process -H 'Content-Type: application/json' -d '{"type":"text", "content":"El Super3 o Club Super3 és un univers infantil català creat a partir dun programa emès per Televisió de Catalunya des del 1991. Està format per un canal de televisió, la revista Súpers!, la Festa dels Súpers i un club que té un milió i mig de socis.", "params":{"question":"Quan va començar el Super3?"}}'
```


Result:

```
{"response":{
   "type":"texts",
   "texts":[
         {"content":"1991"}
      ]
   }
}


```

# Test
In the folder `test` you have the files for testing the API according to the ELG specifications.
It uses an API that acts as a proxy with your dockerized API that checks both the requests and the responses.
For this follow the instructions:

1) Launch the test: `sudo docker-compose --env-file elg_berta_QA_catalan.env up`

2) Make the requests, instead of to your API's endpoint, to the test's endpoint:
   ```
     curl -X POST http://0.0.0.0:8866/processText/service -H 'Content-Type: application/json' -d '{"type":"text", "content":"El Super3 o Club Super3 és un univers infantil català creat a partir dun programa emès per Televisió de Catalunya des del 1991. Està format per un canal de televisió, la revista Súpers!, la Festa dels Súpers i un club que té un milió i mig de socis.", "params":{"question":"Quan va començar el Super3?"}}'
   ```
   
3) If your request and the API's response is compliance with the ELG API, you will receive the response.
   1) If the request is incorrect: Probably you will don't have a response and the test tool will not show any message in logs.
   2) If the response is incorrect: You will see in the logs that the request is proxied to your API, that it answers, but the test tool does not accept that response. You must analyze the logs.

# Citation
The original model of this tool is:
- https://huggingface.co/projecte-aina/roberta-base-ca-v2-cased-qa
 ```
 @inproceedings{armengol-estape-etal-2021-multilingual,
    title = "Are Multilingual Models the Best Choice for Moderately Under-resourced Languages? {A} Comprehensive Assessment for {C}atalan",
    author = "Armengol-Estap{\'e}, Jordi  and
      Carrino, Casimiro Pio  and
      Rodriguez-Penagos, Carlos  and
      de Gibert Bonet, Ona  and
      Armentano-Oller, Carme  and
      Gonzalez-Agirre, Aitor  and
      Melero, Maite  and
      Villegas, Marta",
    booktitle = "Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-acl.437",
    doi = "10.18653/v1/2021.findings-acl.437",
    pages = "4933--4946",
}
```
- For questions regarding this work, contact Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

The license of the original work is Apache License, Version 2.0.
