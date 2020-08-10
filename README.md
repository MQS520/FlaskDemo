### Python3-Flask(二)--mysql的简单增删改查

> 引言:
>
> 上一章介绍了通过flask实现了简单的api接口项目,本章继续介绍flask的SQLAlchemy模块,来对mysql进行简单的增删改查

##### 一. 环境准备

- 版本: python3
- 开发工具: Pycharm
- 数据库版本: mysql 5.7+



##### 二. 项目Demo实现

1. 打开上次的项目,导入关于mysql的模块 `flask_sqlalchemy`, `pymysql`
2. 修改`config.py`的数据连接串
3. 在`create_app`方法中初始化db信息
4. 创建 `models.py`,对应数据库中的测试表
5. 创建新的视图文件: `user.py`, 并在api的init中注册



##### 三. 运行测试

运行 manage.py ,使用postman进行接口请求,查看数据库,检查数据是否插入,修改,查询是否正确等



##### 四. 总结

本篇文章通过 SQLAlchemy 实现了对mysql数据库的单表的增删改查操作,下一篇会继续介绍对多表的操作: 多对多,一对多等多表关系的操作,并实现将查询的数据转换成json格式的数据返回.



