import streamlit as st
import random

st.title('Sorteio rifas :blue[InstUFS]')
st.image('Website/LOGOS/plaquinha.png')

# Carlinhos, Amanda, Hélio, 
# Stéphane, Kavin, Pedro, Paulo, 
# Reinan, Kekinho, Nilson

rifa1_9 = [i for i in range(1, 501)] # rifas de 1 a 9
rifa12 = [552,555,559,564,565,567,570,572,575,576,585,586,588,593,597] #carlinhos
rifa13 = [i for i in range(601,651)] # hiroshi
rifa14 = [651,652,655,657,662,684,691,694,695,696] # kavin
rifa15 = (
    [i for i in range(701, 728)] + 
    [i for i in range(729, 733)] + 
    [734, 737] + 
    [i for i in range(739, 743)] + 
    [i for i in range(745, 751)]
) # camila
rifa16 = (
    [i for i in range(751,765)]+
    [771, 777, 797, 799, 800]
) # guilherme
rifa17_18 = [i for i in range(801,901)] # JP + john

allnubers = rifa1_9 + rifa12 + rifa13 + rifa14 + rifa15 + rifa16 + rifa17_18
number = random.choice(allnubers)

@st.dialog('NÚMERO SORTEADO!!!')
def vote():
    st.metric(label='Sorteado', value=number)
    st.balloons()
    
if st.button('SORTEAR', use_container_width=True):
    vote()
