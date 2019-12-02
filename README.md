# amoeba

## 安装条件

* xxx

## 安装说明

* 构建运行环境

```
make init
```

* 代码升级

```
make upgrade
```

* 启动服务

```
make run
```


## FAQ

1. pycharm debug 失败

注意跟下代码。一般来讲如果代码中引入：eventlet.monkey_patch()，就会导致不能debug。
如 nameko 的 testing/pytest.py 中就有相应代码。注释掉后，pycharm 的 debug 就正常了。

2. 创建数据库

	* `postgres`

```sql
CREATE USER amoeba_prd WITH PASSWORD '<password>'; 
CREATE DATABASE amoeba_prd OWNER amoeba_prd; 
```

	注意如果用 远程数据库，请把账号密码放在 `config.py` 中。不要提交到代码库中

	`config.py`

```python
db_name = '<name>'
db_host = '<host>'
db_port = '<port>'
db_user = '<username>'
db_password = '<password>'
```

	`settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config.db_name,
        'USER': config.db_user,
        'PASSWORD': config.db_password,
        'HOST': config.db_host,
        'PORT': config.db_port,
	}
}	
```