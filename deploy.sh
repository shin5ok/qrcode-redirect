#!/bin/bash

gcloud beta run deploy --set-env-vars=BITLY_APIKEY=$BITLY_APIKEY --source=. --platform=managed --region=asia-northeast1 --allow-unauthenticated qrcode-redirect