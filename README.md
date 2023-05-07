# 蓝楹会官网重建项目 website_development_end

End!

## 本项目地址

# 部署

## 环境变量

这部分将来需要写入docker-compose.yml文件中, 本地开发环境需要在本地设置`JACARANDA_API_MONGO_USERNAME`, 
`JACARANDA_API_MONGO_PASSWORD` 和 `JACARANDA_API_MONGO_URL`, 其他可留空
```text
JACARANDA_API_OPENAPI  
JACARANDA_API_DOCS
JACARANDA_API_REDOC
JACARANDA_API_MONGO_USERNAME # mango db 用户名
JACARANDA_API_MONGO_PASSWORD # mango db 密码
JACARANDA_API_MONGO_URL # mango db url
UVICORN_HOST
UVICORN_PORT
```

## 项目环境部署

1. 安装python3.8+
2. 安装pip3
3. clone本项目到本地
    ```bash
    git clone https://github.com/jacarandastock/website_development_end.git
    ```
4. 安装依赖
    ```bash
    pip install -r requirements.txt --force
    ```
## 数据库部署

本项目采用了mangoDB作为数据库，需要安装mangoDB



## 更新requirement.txt

在添加了新的依赖后，需要更新requirement.txt

```bash
pipreqs ./ --encoding=utf8 
```