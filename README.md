# Project in HACKxFDU.

## ssh to host

```
$ ssh -l ubuntu 121.201.24.49
password: Hackx123
```


## start server

```shell
python manager.py runserver
```

Then see the server at http://121.201.24.49:5000/

## TODO

1. 先实现一个最基本的可以用于简单交互的版本(使用微软认知服务等)
2. 实现对不同行为的处理,根据行为进入不同的处理流程
3. 集成各种服务
3. 改造成一个可以扩展的服务框架(根据不同行为通过消息分派实现)
