import streamlit as st
from PIL import Image
import time
import random as r
page = st.sidebar.radio('张宸轩的首页',['公告','兴趣推荐','留言区','图片处理工具','词典','网站跳转工具','背词器'])
def img_change(imga,rc,gc,bc):
    width,height=imga.size
    img_array=imga.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return imga

def page_0():
    st.title('公告')
    st.write("今天无事发生")
def page_1():
    st.title('兴趣推荐')
    st.write(":exclamation:广告广告广告广告广告广告广告广告广告广告广告广告广告广告，:blue[前往网页]:exclamation:")
    st.write("-----------------------------------------------------------------------------------------------------------")
    st.write("韩老师以前和现在的对比：:blue[点击查看详情]")
    col1,col2=st.columns([1,1])
    with col1:
        st.image("张宸轩_韩老师.png")
    with col2:
        st.image("张宸轩_韩老师.png")
    st.write("-----------------------------------------------------------------------------------------------------------")
    st.write("张宸轩新发布的音乐，快来听一听吧！")
    with open('张宸轩_music1.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write("-----------------------------------------------------------------------------------------------------------")
    st.write("图片处理功能上线了，快去看看吧")
    st.write("-----------------------------------------------------------------------------------------------------------")
    st.write("震惊，张宸轩的图片改完色后竟然长这样:exclamation:赶紧:blue[点击查看详情]:")
    st.image("张宸轩图片.png")
    st.write('不要往下滑')
    for i in range(30):
        st.write('')
    if st.button('不要点我'):
        st.balloons()
        st.write('恭喜发现彩蛋!')
    
def page_2():
    st.title('留言区')
    with open('张宸轩_leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    number1, number2 = st.slider('显示从几到几的留言：', 1, len(messages_list), (1,len(messages_list)))
    for i in range(number1-1,number2):
        if messages_list[i][1]=='张宸轩':
            with st.chat_message('☕'):
                st.write(messages_list[i][1]+':'+messages_list[i][2])
        elif messages_list[i][1]=='游客':
            with st.chat_message('☕'):
                st.text(messages_list[i][1]+':'+messages_list[i][2])
        else:
            with st.chat_message('?'):
                st.text(messages_list[i][1]+':'+messages_list[i][2])
    st.write('目前显示的是从第{}条到第{}条的留言'.format(str(number1),str(number2)))
    name = st.selectbox('我是……', ['游客','张宸轩','张宸轩的同学1'])
    if name!='游客':
        password = st.text_input('请输入密码')
        if name=='张宸轩':
            if password!='abc123' and password!='':
                st.write('密码错误请重新输入')
            elif password=='abc123':
                st.write('验证通过')
        if name=='张宸轩的同学1':
            if password!='hahaha' and password!='':
                st.write('密码错误请重新输入')
            elif password=='hahaha':
                st.write('验证通过')
    # 留言
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        # print(messages_list)
        with open('张宸轩_leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
def page_3():
    st.title('图片处理小工具')
    uploaded_file=st.file_uploader("请上传图片，格式为png,jpeg,jpg",type=['png','jpeg','jpg'])

    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        if file_size >1000000:
            st.write("图片有点大了，换个小点的吧")
            return 0
        img = Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["原图","改色1","改色2","改色3","改色4","改色5"])
        with tab1:
            st.image(img_change(img,0,1,2))
        with tab2:
            st.image(img_change(img,1,2,0))
        with tab3:
            st.image(img_change(img,2,1,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            st.image(img_change(img,2,0,1))
        with tab6:
            st.image(img_change(img,0,2,1))
        st.write("改色完成:exclamation:")
        st.write("由于部分问题所以请右键你要保存的图片并选择图片另存为")
        st.button('好的')
        if st.button('不好'):
            st.code("""恭喜你发现了彩蛋""")
            st.balloons()
def page_4():
    st.title('词典')
    with open('张宸轩_words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词')

    if word in words_dict:
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]#去掉最后的换行
            f.write(message)
            st.text('查询次数：', times_dict[n])
            
        if word == 'snow':
            st.snow()
            st.code('''恭喜你触发了彩蛋''')
        if word == 'hello':
            st.code('''这是一个彩蛋''')
    elif word !='':
        st.write('没有这个单词哦')
        
def page_5():
    st.title('网站跳转工具')
    go = st.selectbox('选择跳转的网站', ['百度', 'bilibili','github'])
    if go == '百度':
        st.link_button('进入', 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('进入', 'https://www.bilibili.com/')
    elif go == 'github':
        st.link_button('进入', 'https://www.github.com/')
def page_6():
    st.title('背词器')
    with open('张宸轩_words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    number3, number4 = st.slider('背词典中从几到几的词：', 1, len(words_list), (1,len(words_list)))
    number5 = st.slider('一个词背几秒:', 1, 60,10)
    if st.button('开始背词'):
        lst=words_list[number3-1:number4+2]
        words = st.progress(0, '准备开始背词！')
        for j in range(0,len(lst)-1):
            for i in range(number5, 0, -1):
                time.sleep(1)
                words.progress(i*int((100/number5)),str(lst[j][1]+'，意思为'+lst[j][2]))
        words.empty()
        st.write('结束了')
        st.text('默写功能暂未完成，敬请期待')
        
if page=='公告':
    page_0()
if page=='兴趣推荐':
    page_1()
if page=='留言区':
    page_2()
if page=='图片处理工具':
    page_3()
if page=='词典':
    page_4()
if page=='网站跳转工具':
    page_5()
if page=='背词器':
    page_6()