import sys
import streamlit as st

# 2. 【核心解决】在这里直接导入全局的 typing，提前稳定命名空间
import typing

# 3. 再导入原项目的核心后端、页面组件（此时它们会安全初始化）
from chatchat import __version__
from chatchat.server.utils import api_address
from chatchat.webui_pages.dialogue.dialogue import dialogue_page
from chatchat.webui_pages.kb_chat import kb_chat
from chatchat.webui_pages.mcp import mcp_management_page
from chatchat.webui_pages.knowledge_base.knowledge_base import knowledge_base_page
from chatchat.webui_pages.utils import *

# 4. 最后引入可能引发类型断言冲突的三方 UI 组件
import streamlit_antd_components as sac

# 初始化后端 API 连接
api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    is_lite = "lite" in sys.argv  # TODO: remove lite mode

    # 1. 网页基础配置（主色调与标题定制）
    st.set_page_config(
        page_title="DeepSeek 课程助手 - 控制台",
        page_icon=get_img_base64("logo.png"),  
        initial_sidebar_state="expanded",
        menu_items={
            "Get Help": "https://github.com/chatchat-space/Langchain-Chatchat",
            "Report a bug": "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            "About": f"""欢迎使用基于 DeepSeek 的专业课程助手 v{__version__}！\n本系统已针对专业课程及知识库完成高级 UI 专属定制。""",
        },
        layout="centered",
    )

    # 2. 注入专属【清新科技白】 CSS 样式
    st.markdown(
        """
        <style>
        /* 全局明亮背景与沉稳深色字体 */
        .stApp {
            background-color: #f8fafc !important;  /* 极其高级的微灰浅白 */
            color: #1e293b !important;  /* 坚石深蓝灰色字体，比纯黑更柔和 */
        }
        
        /* 侧边栏样式定制（干净的纯白面板加轻微阴影边框） */
        section[data-testid="stSidebar"] {
            background-color: #ffffff !important;
            border-right: 1px solid #e2e8f0 !important;
        }
        
        /* 隐藏 Streamlit 官方原生顶部空白和页眉 */
        header {visibility: hidden;}
        [data-testid="stSidebarUserContent"] {
            padding-top: 20px;
        }
        .block-container {
            padding-top: 25px;
        }
        [data-testid="stBottomBlockContainer"] {
            padding-bottom: 20px;
        }

        /* 美化对话框（改成干净的白底、淡蓝青色边框，呼应 Logo） */
        .stChatMessage {
            background-color: #ffffff !important;
            border: 1px solid #e2e8f0 !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
            border-radius: 12px !important;
            margin-bottom: 12px !important;
        }
        
        /* 区分用户和 AI 的对话框（给大模型回复加一个非常淡的青蓝色背景） */
        .stChatMessage[data-testid="stChatMessageAssistant"] {
            background-color: #f0fdfa !important; /* 呼应 Logo 的淡青色延伸 */
            border: 1px solid #ccfbf1 !important;
        }
        
        /* 修改输入框聚焦时的边框颜色（使用 Logo 的科技青色） */
        .stChatInputContainer textarea {
            border-color: #00e5ff !important;
            background-color: #ffffff !important;
            color: #1e293b !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 3. 侧边栏渲染
    with st.sidebar:
        # 渲染大 Logo
        st.image(
            get_img_base64("biglogo.png"), use_column_width=True
        )
        
        # 极简淡灰色分界线
        st.markdown("<hr style='border: 1px solid #e2e8f0; margin: 10px 0;'>", unsafe_allow_html=True)
        
        # 炫酷的高级 Ant Design 菜单栏
        selected_page = sac.menu(
            [
                sac.MenuItem("智能助教对话", icon="robot", description="基于 DeepSeek 核心"),
                sac.MenuItem("课程资料检索", icon="book", description="RAG 知识库对话"),
                sac.MenuItem("知识库管理", icon="database", description="课程资料结构化维护"),
                sac.MenuItem("MCP 全局管理", icon="sliders", description="上下文协议控制"),
            ],
            key="selected_page",
            open_index=0,
            variant='light',       # 明亮浅色激活模式
            color='#00e5ff',       # 激活时高亮条使用 Logo 的科技青色
        )

        # 底部版本号包装（已清除底层技术描述小灰字）
        st.markdown(
            """<p align="center" style="color: #94a3b8; font-size: 12px; margin-top: 50px;">
            </p>""",
            unsafe_allow_html=True,
        )

    # 4. 路由分发逻辑（这里必须和上面的菜单名字保持100%同步！）
    if selected_page == "知识库管理":
        knowledge_base_page(api=api, is_lite=is_lite)
    elif selected_page == "课程资料检索":
        kb_chat(api=api)
    elif selected_page == "MCP 全局管理":
        mcp_management_page(api=api)
    else:
        # 默认进入“智能助教对话”
        dialogue_page(api=api, is_lite=is_lite)