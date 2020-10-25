# cs6065 - docker homework
sean rice  
20201025

# Usage

## Building
you can build the image yourself with the (very simple) build script:
```shell
./build.sh
```

which should output:

```log
Sending build context to Docker daemon  61.44kB
Step 1/4 : FROM alpine:3.7
3.7: Pulling from library/alpine
5d20c808ce19: Pull complete 
Digest: sha256:8421d9a84432575381bfabd248f1eb56f3aa21d9d7cd2511583c68c9b7511d10
Status: Downloaded newer image for alpine:3.7
 ---> 6d1ef012b567
Step 2/4 : RUN apk add python3=3.6.9-r1
 ---> Running in 47ba02500c69
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/main/x86_64/APKINDEX.tar.gz
fetch http://dl-cdn.alpinelinux.org/alpine/v3.7/community/x86_64/APKINDEX.tar.gz
(1/11) Installing libbz2 (1.0.6-r7)
(2/11) Installing expat (2.2.8-r0)
(3/11) Installing libffi (3.2.1-r4)
(4/11) Installing gdbm (1.13-r1)
(5/11) Installing xz-libs (5.2.3-r1)
(6/11) Installing ncurses-terminfo-base (6.0_p20171125-r1)
(7/11) Installing ncurses-terminfo (6.0_p20171125-r1)
(8/11) Installing ncurses-libs (6.0_p20171125-r1)
(9/11) Installing readline (7.0.003-r0)
(10/11) Installing sqlite-libs (3.25.3-r2)
(11/11) Installing python3 (3.6.9-r1)
Executing busybox-1.27.2-r11.trigger
OK: 66 MiB in 24 packages
Removing intermediate container 47ba02500c69
 ---> 6ab63b14cf7e
Step 3/4 : COPY "hmwk_docker.py" "/home/hmwk_docker.py"
 ---> 6a37f3aa78cf
Step 4/4 : ENTRYPOINT [ "python3", "/home/hmwk_docker.py" ]
 ---> Running in 72351e388524
Removing intermediate container 72351e388524
 ---> 0a464b05d444
Successfully built 0a464b05d444
```

## Running with test data
you can then run a quick initial test of the image with the few included text files (use the final image id as an argument):

```shell
./run_local.sh 0a464b05d444
```

which should output:

```log
total number of words: 21
file with most words: eleven_words.txt
ip address: (some ip)
```
