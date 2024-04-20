import streamlit as st


st.set_page_config(page_title='Tax Calculator', page_icon=':money_with_wings:')
st.title('Tax Calculator')


st.divider()


subtotal = st.number_input('Please enter a subtotal $:')
precentage = st.selectbox('Please enter a precentage %:', options=[13, 15])


if subtotal > 0 and precentage > 0:
   if st.button('calculate'):
       string_precentage = f'0.{precentage}'
       float_precentage = float(string_precentage)
       total = float_precentage*subtotal+subtotal
       rounded_total = round(total, 2)
       st.write(f'Your total is : ${rounded_total}')


