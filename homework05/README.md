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

