# COE-332 Homework 2

## Files
This folder consists of files for **Homework 2**
1. **read_animals.py** - This file reads the generate_animals.py file from last week and generates two random animals and its hybrid child.
2. **test_read_animals.py** - This contains unit tests for the read_animals.py file.

## Running Scripts

The two files I made for this homework both are Python scripts. To download the scripts, you simply have to click on them and allow the files to be downloaded on your device.

In your terminal, you can run them by using *python3* and it will run the code for you. 

## Building an Image with Docker

To build an image with Docker, you will need a Docker account. 

You can see all of the images in the ISP server with this command.

`docker images`

You can pull an image from Dockerhub with this command with the image name afterwards.

`docker pull`

You can run the image that you just pulled like this:

`docker run`

Again, the name of the image will be after the command.

To check if there are containers still running, you can:

`docker ps`

## Running Scripts Inside A Containter

A container is a standard unit of software that packages code together, so it is quick and reliable.

First, you start an interactive shell.

`docker run --rm -it ss89557/bsd:1.0 /bin/bash`

The `bin/bash` is the essential part of this line of code.

From here, there are mulitple command options you can do.

> docker run      -> run a containter
> 
> --rm            -> remove the containter when we exit
>
>  -it             -> interactively attach the terminal to the inside of the container
> 
> ss89557/bsd:1.0 -> image and tag onto a local machine
> 
> /bin/bash       -> the shell starts inside the container
> 

To run the code, always start with the combination of these command options and you can run different things within the container.


## Running Unit Tests

The unit test file has the breeding function uploaded into it, so we could make tests in the test_read_animals.py file.

The addition that I made to my read_animals.py file was breeding two of the random animals together to make a hybrid child.

The tests that I have check if the head, body, and arms are accurate to what I intended it to be.

To run these unit tests, download the test_read_animals.py file. Using python3, you can run the file and see the test results.

`python3 test_read_animals.py`
