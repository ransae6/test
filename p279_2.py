# 클릭할 때 다른 데이터로 연결

import streamlit as st #웹 라이브러리, streamlit에 그리기 위해서 
import random
import matplotlib.pyplot as plt # 시각화 라이브러리
import numpy as np

# col1,col2,col3 = st.columns(3)
# col4,col5,col6 = st.columns(3)

# with col1:
#     color1 = st.radio('이차함수 선의 색을 선택하시오',['red','green','blue','orange'])
# with col2:
#     marker1 = st.radio('이차함수 마커형태를 선택하시오',['o','^','s','p','h'])
# with col3:
#     style1 = st.radio('이차함수 선 스타일을 선택하시오',['-',':','-.','--'])

# with col4:
#     color2 = st.radio('sin 함수 선의 색을 선택하시오',['red','green','blue','orange'])
# with col5:
#     marker2 = st.radio('sin 함수 마커형태를 선택하시오',['o','^','s','p','h'])
# with col6:
#     style2 = st.radio('sin 함수 선 스타일을 선택하시오',['-',':','-.','--'])

color1=st.sidebar.radio('선의 색을 선택하시오',['red','green','blue','orange'])
style1=st.sidebar.radio('선 스타일을 선택하시오',['-',':','-.','--'])
marker1=st.sidebar.radio('마커형태를 선택하시오',['o','^','s','p','h'])

fig,ax = plt.subplots()

x=[]
y=[]
ysin=[]
for i in range(-20,21,1): #x의 범위 
    x.append(i)
    y.append(3*i*i- 5*i+2)
    ysin.append(1200*np.sin(i))


# plt.plot(x,y,'yo-', color=color, linewidth=3, label='2nd', marker=marker1)
# plt.plot(x,ysin,'gp--',color=color2, linewidth=2, label='sin',marker=marker2)
plt.plot(x,y, color=color1, linewidth=3, label='2nd', marker=marker1, linestyle=style1)
# plt.plot(x,ysin, color=color2, linewidth=2, label='sin',marker=marker2, linestyle=style2)
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlim((-15,15))
plt.ylim((-2000,2000))

#'cs','-.r,'rs:' 같이 바꿀수 있음 점선
#https://codetorial.net/matplotlib/set_linestyle.html
#https://wikidocs.net/13574
#색상 y 자리 , 마커형태 h p s ^ o , 선의 형태  --,-,-.,:
st.pyplot(fig)


# x=[] #x를 아무것도 아닌걸로 선언

# for i in range(-100,101,1): # 시작점, 끝점(포함 안함), 간격
#     x.append(i) #x의 값은 200개

# x

# y= []
# for j in range(-1,11,2):
#     y.append(j)
# y

# plt.plot(x,y)
# st.pyplot(fig) # 터틀마냥 관용구


import sys
sys.exit()

fig,ax = plt.subplots()

x=[]
for i in range(-100,101):
    x.append(1/10.0)