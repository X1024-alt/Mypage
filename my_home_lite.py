# 我的主页
import streamlit as st
from PIL import Image
page = st.sidebar.radio("主页", ["Home","情报","答疑","成绩展示","资源分享","留言区"])
def img_change(img, rc, gc, bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img
def word_space():
    with open("words_space.txt", "r", encoding="UTF-8") as f:# 单词本
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open("check_out_times.txt", "r", encoding="UTF-8") as f:# 查询次数
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("虽然不知道这东西要拿来干嘛，不过用就对了，暂时只支持英文单词转中~")
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        times_dict[n] = times_dict[n]+1 if n in times_dict else 1
        with open("check_out_times.txt", "w", encoding="UTF-8") as f:
            message = ''
            for k, v in times_dict.items():
                message += f"{str(k)}#{str(v)}\n"
            message = message[:-1]
            f.write(message)
        st.write(f"查询次数：{times_dict[n]}")
    else:
        st.write("敬请期待~")
    if word == 'hello world':
        st.write("Tips: 据说这是成为程序员的历史性一刻……")
    elif word == 'python':
        st.write("Tips: www.python.org")
def some_music():
    st.write("Laur--国士無双:red[【速核警告！！！】]")
    with open("国士無双.ogg", "rb") as f:
        mymp3 = f.read()
    st.audio(mymp3, format="audio/ogg", start_time=0)
def picture_p():
    r, g, b = 0, 1, 2
    uploaded_file = st.file_uploader("上传图片", type=["jpg","jpeg","png","bmp"])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        p1, p2 = st.columns([1, 1])
        with p1:
            st.image(img)
        with p2:
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["空白对照", "BGR", "RBG", "BRG", "GRB", "GBR"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img, b, g, r))
            with tab3:
                st.image(img_change(img, r, b, g))
            with tab4:
                st.image(img_change(img, b, r, g))
            with tab5:
                st.image(img_change(img, g, r, b))
            with tab6:
                st.image(img_change(img, g, b, r))
def page0():# Home
    st.write("音游，启动！")
    st.image("CYTUS II合影.jpg")
def page1():# 情报
    st.write("Phigros将于2024/02/23 17:00更新, 更新内容大概如下:")
    st.write("支线三更新 && 异象开关实装。")
    st.write("以下是更新前一天的聊天记录，经过去重和马赛克处理，筛选了部分无关的东西。")
    st.write("Tips: 大概意思就是有个谱师在这次更新没有写谱 是谁我不说~")
    st.image("xmt没写谱.png")
    st.write("最新消息：由于部分平台还在审核，官方将在所有平台审核通过后统一发布更新。")
def page2():# 答疑
    st.write("针对因快捷手势导致的音游游玩问题的解决方案:")
    st.write("小米MIUI:更多设置 -> 快捷手势 && 传送门")
    b1, b2 = st.columns([1, 1])
    with b1:
        st.image("小米更多设置.jpg")
        st.image("小米手势.jpg")
    with b2:
        st.image("小米传送门.jpg")
        st.image("小米三指下拉.jpg")
        st.image("小米三指长按.jpg")
def page3():# 成绩展示
    st.write("Phigros最近一次成绩图")
    st.image("Phi rks.jpg")
    st.write("ADOFAI最难官谱《It go》准度99.22% 严判击破!!!")
    st.image("it go.jpg")
    # st.write("《It go》准度99.02% 严判击破!!!")
    # with open("It go.mp4", "rb") as e:
    #     myvideo0 = e.read()
    # st.video(myvideo0, format="video/mp4", start_time=0)
    # st.write("当冰与火之舞所有主世界关融为一体！Othinus-Fragor Magnus 准度99.81% 严判击破实录")
    # with open("Fragor Magnus.mp4", "rb") as f:
    #     myvideo = f.read()
    # st.video(myvideo, format="video/mp4", start_time=0)
    # st.write("当史莱姆要你Move Body!!! MVURBD Lv.13 100w+")
    # with open("MVURBD.mp4", "rb") as g:
    #     myvideo1 = g.read()
    # st.video(myvideo1, format="video/mp4", start_time=0)
def page4():# 资源分享
    st.write("音频")# 音乐
    some_music()
    st.write(":dog:图片处理工具(RGB转换):dog:")# 图片处理
    picture_p()
    st.write("词典")
    word_space()
def page5():# 留言区
    st.write("留言区")
    with open("leave_messages.txt", "r", encoding="UTF-8") as f:# 消息列表
        msg_list = f.read().split('\n')
    for i in range(len(msg_list)):
        msg_list[i] = msg_list[i].split('#')
    for i in msg_list:
        if i[1] == "甲":
            with st.chat_message('🐶'):
                st.write(i[1],':',i[2])
        elif i[1] == "乙":
            with st.chat_message('🐱'):
                st.text(i[1]+':'+i[2])
    name = st.selectbox("",['甲','乙'])
    new_message = st.text_input("")
    if st.button("留言"):
        if new_message=="":
            st.write("不能发送空白消息")
        else:
            msg_list.append([str(int(msg_list[-1][0])+1),name,new_message])
            with open("leave_messages.txt", "w", encoding="UTF-8") as f:
                message = ''
                for i in msg_list:
                    message += f"{i[0]}#{i[1]}#{i[2]}\n"
                message = message[:-1]
                f.write(message)
if page == "Home":
    page0()
elif page == "情报":
    page1()
elif page == "答疑":
    page2()
elif page == "成绩展示":
    page3()
elif page == "资源分享":
    page4()
elif page == "留言区":
    page5()