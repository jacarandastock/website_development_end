# 蓝楹会官网重建项目 website_development_end

End!

## 本项目地址

# 部署

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

## 更新requirement.txt

在添加了新的依赖后，需要更新requirement.txt

```bash
pipreqs ./ --encoding=utf8 
```