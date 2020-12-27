#### 请求地址

详见README.xlsx

#### 安装

**环境要求**

- Windows/Linux
- python3
- pip

##### **创建一个虚拟环境**

创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 `venv` 文件夹：

```shell
$ git clone https://github.com/stepic-game-center/stepic-back.git
$ cd stepic-back
$ python3 -m venv venv
```

在 Windows 下：

```shell
> py -3 -m venv venv
```

##### **激活虚拟环境**

在开始工作前，先要激活相应的虚拟环境：

```shell
$ . venv/bin/activate
```

在 Windows 下：

```shell
> venv\Scripts\activate
```

##### **安装 Flask**

在已激活的虚拟环境中可以使用如下命令安装 Flask：

```shell
$ pip install Flask
```

##### 生成数据库

```shell
$ flask init-db
```

#### 运行

##### Windows环境

```shell
> set FLASK_APP=flaskr
> flask run
```

**Windows powershell环境**

```powershell
PS > $env:FLASK_APP="flaskr"
PS > flask run
```

##### **Linux环境**

```shell
$ export FLASK_APP=flaskr
$ flask run --host=0.0.0.0
```

**外网访问**

```shell
flask run --host=0.0.0.0
```

##### 调试模式

```shell
> set FLASK_ENV=development
```

```powershell
PS > $env:FLASK_ENV="development"
```

```shell
$ export FLASK_ENV=development
```
