# Group Key Management for Cloudmesh

* **Note:** This project has been replaced by an 
  implementation by Gregor von Laszewski. The new implementation 
  includes integration with cloudmesh and provides a new 
  group management.
  
Nayeem Baig

* Repo: [fa19-516-172](<https://github.com/cloudmesh-community/fa19-516-172/tree/master>)
* [Contributors](<https://github.com/cloudmesh-community/fa19-516-172/graphs/contributors>)

## Introduction

In the cloud we need to give access to VMs to multiple users.  The
management of keys need to be automated and integrated with mongoDB.
Cloudmesh is missing functionality to easily add keys and control the
access policies related to key management. Functionality to utilize
mongo DB have already been developed for the Security Rules and
Security Groups functions.  We can add Key Groups that are defined by
both the related cloud provider and collection of related keys to fine
tune access control for all connected machines.

After addressing the completion of this elected task the students ahs
the opportunity to work on additional other cloud security aspects of
his chosing if desired.

## Status

According to Nayeem Baig this project is in progress and therefore was replaced 
with a complete implementation by von Laszewski. The new implementation uses 
the build in groups defined by the earlier cloudmesh implementation but not 
uses within this project. Thus the work described here has since been deprectaed.


## Implementation

Automating Key Management includes the following commands defined by von Laszewski:

* CMS KeyGroup Command

  ```
  cms key add --source=FILENAME
  cms key group list
  cms key group add --group=abc --name=\"laszewsk_git_[0,,1,2]\"
  cms key group delete --group=abc --name=\"laszewsk_git_[0,,1,2]\"
  cms key group export --group=abc,klm --file=FILENAME
  ```

* Not completed:

  ```
  cms key add NAME --source=FILE_PATH ```
  cms key group upload --group=NAME ip=.... --authorized_keys
  ```

## Usage

```
cms key add --source=FILENAME

cms key add NAME --source=FILE_PATH 

(ENV3) nayeem@workspace:~$ cms key add --source=/home/nayeem/test/id_rsa2.pub ids2
Cloudmesh Database Update |################################| 1/1
(ENV3) nayeem@workspace:~$ cms key list
```

+------------------+---------+-------------------------------------------------+------------------+
| Name | Type| Fingerprint | Comment|
+------------------+---------+-------------------------------------------------+------------------+
| nayeemb| ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeem@workspace |
| TEST | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| idRSA1 | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| IDRSA2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git_0 | ssh-rsa | 74:cd:23:64:1b:7f:98:fc:aa:47:f3:b6:46:1f:74:a2 | nayeembaig_git_0 |
| nayeembaig_git_1 | ssh-rsa | 98:f4:89:23:57:8b:81:f4:3c:00:a6:23:2f:ed:07:47 | nayeembaig_git_1 |
| nayeembaig_git_2 | ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeembaig_git_2 |
| testidrsa| ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| testing| ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| ids2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
+------------------+---------+-------------------------------------------------+------------------+

```
cms key group add --group=GROUPNAME NAME
```

```
(ENV3) $ cms key group add --group=testGroup6 ids2
Cloudmesh Database Update |################################| 1/1
(ENV3) $ cms key group list
```

+------------------+---------+-------------------------------------------------+------------------+
| Name | Type| Fingerprint | Comment|
+------------------+---------+-------------------------------------------------+------------------+
| nayeemb| ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeem@workspace |
| TEST | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| idRSA1 | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| IDRSA2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git_0 | ssh-rsa | 74:cd:23:64:1b:7f:98:fc:aa:47:f3:b6:46:1f:74:a2 | nayeembaig_git_0 |
| nayeembaig_git_1 | ssh-rsa | 98:f4:89:23:57:8b:81:f4:3c:00:a6:23:2f:ed:07:47 | nayeembaig_git_1 |
| nayeembaig_git_2 | ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeembaig_git_2 |
| testidrsa| ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| testing| ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| ids2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
+------------------+---------+-------------------------------------------------+------------------+

+------------+--------------------------------------------------+
| Name | Keys |
+------------+--------------------------------------------------+
| testGroup6 | ['nayeembaig_git_0', 'lmo', 'nayeemb', |
|| 'nayeembaig_git_2', 'TEST', 'ids2',|
|| 'nayeembaig_git_1', 'testidrsa'] |
| testGroup7 | ['nayeemb', 'lmo'] |
| testGroup| ['nayeembaig_git_1', 'idRSA1', 'TEST'] |
| testGroup1 | ['nayeembaig_git_1', 'TEST', 'idRSA1'] |
+------------+--------------------------------------------------+

```
cms key group list
```

```
(ENV3) $ cms key group list
```

+------------------+---------+-------------------------------------------------+------------------+
| Name | Type| Fingerprint | Comment|
+------------------+---------+-------------------------------------------------+------------------+
| nayeemb| ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeem@workspace |
| TEST | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| idRSA1 | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| IDRSA2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git_0 | ssh-rsa | 74:cd:23:64:1b:7f:98:fc:aa:47:f3:b6:46:1f:74:a2 | nayeembaig_git_0 |
| nayeembaig_git_1 | ssh-rsa | 98:f4:89:23:57:8b:81:f4:3c:00:a6:23:2f:ed:07:47 | nayeembaig_git_1 |
| nayeembaig_git_2 | ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeembaig_git_2 |
| testidrsa| ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| testing| ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| ids2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
+------------------+---------+-------------------------------------------------+------------------+

+------------+--------------------------------------------------+
| Name | Keys |
+------------+--------------------------------------------------+
| testGroup6 | ['nayeembaig_git_0', 'lmo', 'nayeemb', |
|| 'nayeembaig_git_2', 'TEST', 'ids2',|
|| 'nayeembaig_git_1', 'testidrsa'] |
| testGroup7 | ['nayeemb', 'lmo'] |
| testGroup| ['nayeembaig_git_1', 'idRSA1', 'TEST'] |
| testGroup1 | ['nayeembaig_git_1', 'TEST', 'idRSA1'] |
+------------+--------------------------------------------------+


```
cms key group delete --group=GROUPNAME NAME
```

```
(ENV3)$ cms key group delete --group=testGroup6 ids2
names:ids2
Cloudmesh Database Update |################################| 1/1
(ENV3) $ cms key group list
```

+------------------+---------+-------------------------------------------------+------------------+
| Name | Type| Fingerprint | Comment|
+------------------+---------+-------------------------------------------------+------------------+
| nayeemb| ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeem@workspace |
| TEST | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| idRSA1 | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| IDRSA2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git_0 | ssh-rsa | 74:cd:23:64:1b:7f:98:fc:aa:47:f3:b6:46:1f:74:a2 | nayeembaig_git_0 |
| nayeembaig_git_1 | ssh-rsa | 98:f4:89:23:57:8b:81:f4:3c:00:a6:23:2f:ed:07:47 | nayeembaig_git_1 |
| nayeembaig_git_2 | ssh-rsa | 12:fe:dc:eb:48:4b:fd:d6:d2:60:1c:1e:a1:7a:a6:df | nayeembaig_git_2 |
| testidrsa| ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
| nayeembaig_git | ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| testing| ssh-rsa | 3d:74:85:e7:2c:e6:26:48:a8:74:c6:fd:b8:de:23:3b | nayeem@workspace |
| ids2 | ssh-rsa | 7b:b0:ba:7b:f1:54:df:87:5c:ff:42:41:91:84:bc:98 | nayeem@workspace |
+------------------+---------+-------------------------------------------------+------------------+

+------------+--------------------------------------------------+
| Name | Keys |
+------------+--------------------------------------------------+
| testGroup6 | ['testidrsa', 'nayeembaig_git_0', 'lmo', 'TEST', |
|| 'nayeembaig_git_2', 'nayeemb', |
|| 'nayeembaig_git_1']|
| testGroup7 | ['nayeemb', 'lmo'] |
| testGroup| ['nayeembaig_git_1', 'idRSA1', 'TEST'] |
| testGroup1 | ['nayeembaig_git_1', 'TEST', 'idRSA1'] |
+------------+--------------------------------------------------+

```
cms key group export --group=GROUPNAME --file=FILENAME 
```

```
(ENV3) $ cms key group export --group=testGroup6 --file=/home/nayeem/export.txt
(ENV3) $ cat /home/nayeem/export.txt 

```

## References

* https://github.com/cloudmesh/cloudmesh-cloud




