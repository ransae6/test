import streamlit as st
import random
import matplotlib.pyplot as plt # 시각화 라이브러리
import numpy as np
# 이차함수 그리기
# 스트림릿 api

# 버튼
# import streamlit as st

# genre = st.radio(
#     "What's your favorite movie genre",
#     [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
#     captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

# if genre == ':rainbow[Comedy]':
#     st.write('You selected comedy.')
# else:
#     st.write("You didn\'t select comedy.")


#** : 이태릭
#글씨, 이모지 작성
# st.write('# :four_leaf_clover: :green[**Hello**], *World!* :four_leaf_clover:')
# st.write('## :dolphin: :blue[**Hello**], *World!* :dolphin:')
# st.write('#### :tomato: :red[**Hello**], *World!* :tomato:')
# st.write('##### :sunflower: :orange[**Hello**], *World!* :sunflower:')
# st.write('###### :new_moon: :gray[**Hello**], *World!* :new_moon:')

# 색 컬러 여러개
# import streamlit as st

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.markdown('''
#     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#     :gray[pretty] :rainbow[colors].''')
# st.markdown("Here's a bouquet &mdash;\
#             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

# multi = '''If you end a line with two spaces,
# a soft return is used for the next line.

# Two (or more) newline characters in a row will result in a hard return.
# '''
# st.markdown(multi)

# 데이터 표
# import streamlit as st
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

# st.dataframe(df.style.highlight_max(axis=0))


# 위 아래 표현
# import streamlit as st

# col1, col2, col3 = st.columns(3)
# col1.metric("Temperature", "70 °F", "1.2 °F", delta_color="inverse")
# col2.metric("Wind", "9 mph", "-8%")
# col3.metric("Humidity", "86%", "4%")


# 색 변환 바
# import streamlit as st

# start_color, end_color = st.select_slider(
#     'Select a range of color wavelength',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=('red', 'blue'))
# st.write('You selected wavelengths between', start_color, 'and', end_color)

#옵션 선택
# import streamlit as st

# option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))

# st.write('You selected:', option)


# import sys
# sys.exit()


# 이차함수 그래프
fig, ax = plt.subplots()


x = []
for i in range(-100,100):
    x.append(i/10.0)

# a = 3
# b = -1
# c = 5

# a = st.number_input( 'insert a', step = 1 )
# b = st.number_input( 'insert b', step = 1 )
# c = st.number_input( 'insert c', step = 1 )

# col = st.columns(3)
# with col[0]:
#     # a = st.number_input( 'insert a', step = 1 )
#     a = st.number_input( 'insert a', step = 10 )
# with col[1]:
#     # b = st.number_input( 'insert b', step = 1 )
#     b = st.number_input( 'insert b', step = 10 )
# with col[2]:
#     # c = st.number_input( 'insert c', step = 1 )
#     c = st.number_input( 'insert c', step = 10 )

y=[]
a = 2
b = -1
c = 5

# y = []
# for i in x:
#     # y.append( a*i**2 + b*i + c )
#     y.append( a*i**2 + b*i + c )


option = st.selectbox(
   'How would you like to be contacted?',
    ('이차함수', '싸인함수', '코싸인함수')
)
st.write('You select', option)

for i in x:
    if '2' in option:
     y.append( a*i**2 + b*i + c )
    if 'sin' in option:
       y.append(np.sin(i))
    if 'cos' in option:
       y.append(np.cos(i))

plt.plot(x,y)
# plt.ylabel('some random numbers')
# plt.xlabel('x-asix')
st.pyplot(fig) # 스트림릿에 표현하기 위해