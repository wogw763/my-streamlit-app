import streamlit as st


def main_page():
    st.title("主界面")
    st.write(f"欢迎回来，{st.session_state.username}！")

    if st.button("退出登录"):
        st.session_state.logged_in = False
        # st.experimental_rerun()
        st.experimental_user()


def login_page():
    st.title("用户登录")

    with st.form("登录表单"):
        username = st.text_input("用户名")
        password = st.text_input("密码", type="password")
        submitted = st.form_submit_button("登录")

        if submitted:
            # 简单验证示例（生产环境需使用安全验证方式）
            if username == "admin" and password == "123456":
                st.session_state.logged_in = True
                st.session_state.username = username
                st.experimental_rerun()
            else:
                st.error("用户名或密码错误")


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if st.session_state.logged_in:
    main_page()
else:
    login_page()
