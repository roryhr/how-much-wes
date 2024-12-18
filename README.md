# How much Wes Anderson?

It is live on Fly.io <br>
https://falling-dew-7859.fly.dev/

Upgraded from Python 3.8 to 3.12.
TensorFlow + Keras



# Development Quickstart

Build and run with Docker to replicate the prod environment. 
```
docker build --tag slim-wes .
docker run --publish 8080:8080 slim-wes
```

Run locally with the Flask debug server.
```
conda create -n py312 python=3.12
pip install -r requirements.txt
conda activate py12
flask --app main --debug run
```

Access at <br>
http://localhost:5000/


Run the tests:
```
conda activate py12
pip install pytest
pytest tests
```


## Deployment

Fly builds the docker image and deploys.
```
flyctl deploy
```

# Getting the data

Download trailers from YouTube. `pytube` is no longer maintained and doesn't work. `yt-dlp` works for now.  

```commandline
yt-dlp "https://www.youtube.com/watch?v=sOnqjkJTMaA"   

mkdir  thriller

ffmpeg -i "Michael Jackson - Thriller (Official 4K Video) [sOnqjkJTMaA].webm" \
-vf "fps=1"  -q:v 2 thriller/thriller_%03d.jpeg

```

Use ffmpeg to convert movies to images

`ffmpeg -i FANTASTIC\ MR\ FOX\ -\ Official\ Theatrical\ Trailer.mp4 -r 1 -f image2 fantastic_mr_fox/fantastic_mr_fox-%04d.jpeg`

Model training follows the Keras example of training a binary model on very little data
https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
