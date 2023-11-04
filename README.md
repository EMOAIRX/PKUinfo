# PKUINFO Readme

https://pkuinfo.lcpu.dev/

## Project Overview
**PKUINFO** is a platform designed to provide activity information and consulting services for students at Peking University. The project aims to aggregate data from various sources using web scraping and other methods. It then utilizes Linked Data and Knowledge Graph techniques to integrate, store, and format the collected data. The platform offers free access to activity information for students within the university, allowing them to sort and filter the information based on criteria such as time and other preferences.

## Project Structure
The project is organized into three main directories:

1. **front:** This directory contains the Vue.js frontend application.
2. **back:** Here lies the Spring Boot backend implementation.
3. **pyprocessor/crawl:** In this directory, you'll find the Python scripts responsible for gathering and consolidating information.

## TODO List
There are several features and improvements planned for PKUINFO:

1. 基于用户上传文本与活动

2. 基于关键词等的搜索

3. 修复现有bug

---

如何快速开始？

1、`git clone https://github.com/EMOAIRX/PKUinfo.git`

2、在crawl中，修改`nameList.txt`，填写公众号和fakeid，新建`tokens.py`，填写TOKEN,COOKIE,USER_AGENT

3、在pyprocessor中，新建`keys.py`，以使用chatgpt/zhipuai/其它LLM

4、部署前端，使用npm run build即可

5、运行后端，在back中，使用mvn spring-boot:run即可，

6、运行后端2，在pyprocessor中，python3 server.py即可

7、运行爬虫，在crawl中，使用python3 getURL.py



