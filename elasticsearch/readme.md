
# Eleasticsearch Setup


- Check elasticsearch status by command `curl http://localhost:9200`
- Go to Kibana by opening this URL in browser "http://localhost:5601".


## Elasticsearch and Kibana Docker setup for local development
Since it is for local development, `xpack_security` is disabled. 

Docker setting details are in `docker-compose-dev.yml` .

- Local volume es_data is located in `/var/lib/docker/volumes/elasticsearch_es_data/_data`

```sh
# To start
docker-compose -f docker-compose-dev.yml up -d
# To stop
docker-compose -f docker-compose-dev.yml down
```


## References
- This article [How to run Elasticsearch on Docker for local development](https://levelup.gitconnected.com/how-to-run-elasticsearch-8-on-docker-for-local-development-401fd3fff829) is a beginner friendly setup guide. 