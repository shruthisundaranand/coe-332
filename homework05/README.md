# Homework 05

This is a README file for homework 05. In this file, I will be explaining the answers to the questions asked in the homework description.

## Part A

### 1. Include the yaml file used and the command issued to create the pod.

In the homework 05 folder in the GitHub, there is a yml file called. pod-homework05a.yml. This file is what I used for the first part of this homework assignment.

### 2. Issue a command to get the pod using an appropriate selector. Copy and paste the command used and the output.

The input that I used was:

``` bash
kubectl get pods --selector "version=1.0" 
```

The output that I got was:

``` bash
NAME          READY   STATUS    RESTARTS   AGE
homework05a   1/1     Running   0          33s
```
### 3. Check the logs of the pod. What is the output? Is that what you expected?

When I checked the logs, I had been running the other pods that we had done in class from the past two weeks.

The input was:

``` bash
 kubectl logs homework05a
 ```
 
The output was: 

``` bash
Hello, 
```

Since we did not put in a name for the environment variable we created, there was no output for a name.

### 4. Delete the pod. What command did you use?

I deleted the pod with this input:

``` bash
kubectl delete pods homework05a
```

The output was:

``` bash
pod "homework05a" deleted
```

## Part B

### 1. Include the yaml file used and the command issued to create the pod.

For part B, the file is called pod-homework05b.yml in the Github. It is also located in the homework 05 folder.

### 2. Check the logs of the pod. What is the output? Copy and paste the command used and the output.

The input is:

``` bash
kubectl logs homework05b
```

The output should be:

``` bash
Hello, Shruthi!
```

### 3. Delete the pod. What command did you use?

I deleted the pod with this input:

``` bash
kubectl delete pods homework05a
```

The output was:

``` bash
pod "homework05b" deleted
```

## Part C

### 1. Include the yaml file used and the command issued to create the pod.

The yml file is in the homework05 folder in my GitHub.

### 2. First, use kubectl to get all the pods in the deployment and their IP address. Copy and paste the command used and the output.

``` bash
kubectl get pods -o wide
```

| Pods in Deployment  | IP address |
| ------------- | ------------- |
| hw05-deployment-565979bd6-7gkss | 10.244.7.124 |
| hw05-deployment-565979bd6-m9l5d | 10.244.3.133  |
| hw05-deployment-565979bd6-xjvx4 | 10.244.6.142  |



### 3. Now, check the logs associated with each pod in the deployment. Does it match what you got in 2? Copy and paste the commands and the output.

The input is:

``` bash 
kubectl logs hw05-deployment-565979bd6-7gkss
kubectl logs hw05-deployment-565979bd6-m9l5d
kubectl logs hw05-deployment-565979bd6-xjvx4
```

The output is:

``` bash
Hello, Shruthi from IP 10.244.7.124!
Hello, Shruthi from IP 10.244.3.133!
Hello, Shruthi from IP 10.244.6.142!
```

