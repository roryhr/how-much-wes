# How much Wes Anderson?

It is live on Fly.io <br>
https://falling-dew-7859.fly.dev/


# Development Quickstart

Build and run with Docker to replicate the prod environment. 
```
docker build --tag slim-wes .
docker run --publish 8080:8080 slim-wes
```

Run locally with the Flask debug server.
```
conda create -n py38 python=3.8
pip install -r requirements.txt
conda activate py38
flask --app main --debug run
```

Access at <br>
http://localhost:5000/



Run the tests:
```
conda install pytest
pytest tests
```


## Deployment

Fly builds the docker image and deploys.
```
flyctl deploy
```

# Getting the data

Download trailers from YouTube.

```
from pytube import YouTube

def download_youtube(url):
    yt = YouTube(url)

    (yt.streams
        .filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download()
    )

```

Use ffmpeg to convert movies to images

`ffmpeg -i FANTASTIC\ MR\ FOX\ -\ Official\ Theatrical\ Trailer.mp4 -r 1 -f image2 fantastic_mr_fox/fantastic_mr_fox-%04d.jpeg`

Model training follows the Keras example of training a binary model on very little data
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
