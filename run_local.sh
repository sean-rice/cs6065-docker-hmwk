# ./run_local.sh <image-id>
docker run -it -v "$PWD/text_data":"/home/data" --rm $1
