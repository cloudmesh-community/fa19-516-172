# Group Key Management for Cloudmesh  

- Nayeem Baig  

  - email: nayeemullahbaig.93@gmail.com  
  - repo: [fa19-516-172](<https://github.com/cloudmesh-community/fa19-516-172/tree/master>)  

* [Contributors](<https://github.com/cloudmesh-community/fa19-516-172/graphs/contributors>)  
* [Forked Keygroup Branch](<https://github.com/cloudmesh/cloudmesh-cloud/tree/keygroup>)

## Introduction

In the cloud we need to give access to VMs to multiple users.  
The management of keys need to be automated and integrated with mongoDB.  
Cloudmesh is missing functionality to easily add keys and control the access  
policies related to key management. Functionality to utilize mongo DB have  
already been developed for the Security Rules and Security Groups functions.  
We can add Key Groups that are defined by both the related cloud provider and  
collection of related keys to fine tune access control for all connected machines.   

After addressing the completion of this elected task the students ahs the opportunity to work 
on additional other cloud security aspects of his chosing if desired.

## Implementation


#### Automating Key Management


## Tasks

### CMS Key Command
  
Status: In Progress   

Last Update: Implemented ``` cms key add --source=FILE_PATH ```

### CMS KeyGroup Command

Status: In Progress   

Last Update: Added KeyGroup.py file based on SecGroup.py   

## Progress

* Following commands
 
* cms key group list

* cms key group list --group=abc

* cms key group delete

* cms key group add --group=abc --name=\"laszewsk_git_[0,,1,2]\"
               
* cms key group export --file=~/authorized_keys --group=abc,klm

* cms key group upload --group=NAME ip=.... --authorized_keys

* cms key group add --group=NAME  ip=.... --authorized_keys

