#### 安装

##### **创建一个虚拟环境**

创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 `venv` 文件夹：

```shell
$ mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

在 Windows 下：

```shell
$ py -3 -m venv venv
```

##### **激活虚拟环境**

在开始工作前，先要激活相应的虚拟环境：

```shell
$ . venv/bin/activate
```

在 Windows 下：

```powershell
> venv\Scripts\activate
```

##### **安装 Flask**

在已激活的虚拟环境中可以使用如下命令安装 Flask：

```shell
$ pip install Flask
```

#### 运行

##### **Windows环境**

```powershell
PS C:\stepic_back> $env:FLASK_APP = "hello.py"
PS C:\stepic_back> flask run --host=0.0.0.0
```

##### **Linux环境**

```shell
$ export FLASK_APP=hello.py
$ flask run
```

##### 调试模式

```shell
$ export FLASK_ENV=development
$ flask run
```

（在 Windows 下需要使用 `set` 来代替 `export` 。）