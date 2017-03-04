# docker-clean-tools
Tiny python scripts to clean images and containers, which deletes:
* stopped containers
* dangling images (the garbage ones)

## Commands:
* clean containers: ```$ python clean_containers.py```
* clean images: ```$ python clean_images.py```

## Develop env:
```
$ python --version
Python 2.7.10

$ docker version
Client:
 Version:      1.12.1
 API version:  1.24
 Go version:   go1.7.1
 Git commit:   6f9534c
 Built:        Thu Sep  8 10:31:18 2016
 OS/Arch:      darwin/amd64

Server:
 Version:      1.12.1
 API version:  1.24
 Go version:   go1.6.3
 Git commit:   23cf638
 Built:        Thu Aug 18 17:52:38 2016
 OS/Arch:      linux/amd64
```

## License: MIT

