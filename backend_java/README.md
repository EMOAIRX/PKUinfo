java端部署部分
1. 项目目标字节码采用java17，需要配置当前java环境为java17
2. 项目依赖于Redis数据库，需要开启Redis服务器并开放6379端口（Redis默认开启在6379端口上），项目默认不使用Redis用户名和密码，所以对于Redis数据库不用额外配置
3. 项目依赖于MySQL数据库，需要配置与MySQL数据库的连接，配置信息位于src/main/resources下的application.properties，修改对应的url,username和password来配置数据库的连接
4. 在当前目录运行mvn clean package可以打包项目，在target目录下可生成info-x.x.x-SNAPSHOT.jar，可通过任意持久化部署来运行项目（nohup pm2等），参数选用java -jar ./info-x.x.x-SNAPSHOT.jar
e.g.
```shell
# nohup
nohup java -jar info-0.0.1-SNAPSHOT.jar 1>info.out 2>&1 &
# pm2 
pm2 start java --name info --watch -- -jar info-x.x.x-SNAPSHOT.jar
```
5. 查看对应运行日志，启动无误后后端即成功部署