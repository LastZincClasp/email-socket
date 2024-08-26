# email-socket

## Introduciton
use email as your socket

The "cal.py" file is the core of this repo, you can import it in your own file.
The "client.py" and the "server.py" is an example to use the "cal.py"

The "cal.py" establish a class named "Lib".

The project use your email account as a proxy to link the outside world.
Think as you have a email account called PROXY.
A logs in PROXY and send an email MSG to PROXY.
B logs in PROXY and find the MSG and get the info.
that's the send() -> A and recv() -> B in the Lib.

Attention! Effectless!

## Usage
Get it on client.py and server.py

----

i am a noob in English and code, 
所以我用中文
另外markdown不是太熟，以后再改改，凑合着看吧

就是我最近想出了一个点子
就是可以利用收发邮件的操作来代替socket
使得我们可以利用别的服务器的邮箱建立起一座桥梁吧
使两个不在同一局域网内的，没有公网ip的电脑能连接，建立信息通道

但是由于邮箱发邮件延迟较大之类的问题
效率可能会有点低下

而且不太会用git，这次是临时上传，下次上传再做好点吧
先凑合着看
