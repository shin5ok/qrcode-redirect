#!/bin/bash

docker run -p 8080:8080 -e BITLY_APIKEY=$BITLY_APIKEY -it $IMAGE
