# AI CourseMate 课程智能助教系统

## 简介
本项目是一个基于 **Langchain-Chatchat** 和 **DeepSeek** 大模型的课程智能助教系统。通过 RAG (检索增强生成) 技术，能够精准提取课程资料知识点，为学生提供 24/7 的在线答疑服务。

## 核心功能
* **智能对话**：基于大模型实现自然语言问答。
* **文档检索**：利用向量库实现对 PDF/DOC 课程资料的语义搜索。
* **系统配置**：支持模型参数调整与上下文管理。

## 技术栈
* **后端**：Langchain-Chatchat, Python 3.10
* **前端**：Streamlit, Ant Design Components
* **模型**：DeepSeek-R1 / V3
* **数据库**：FAISS (向量存储)

## 快速开始
1. 克隆项目：`git clone https://github.com/你的用户名/AI-CourseMate.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 启动服务：`python -m chatchat.cli start -a`