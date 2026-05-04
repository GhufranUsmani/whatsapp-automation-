st.title("whatsApp automation")

uploader= st.file_uploader("choose an excel file ",type=["xlsx"])



portfolioLink= st.text_area("Enter your portfolio here ",value="https://syedmuhammadarsalanshah.com/")
customMessage=st.text_area("Enter your custom message ",value="Explore me me on this web")


if uploader is not None:
    st.write("contacts are uploaded !")
    df=pd.read_excel(uploader)
    st.dataframe(df)

    if st.button("Send Message "):

        for i , row in df.iterrows():
            phoneNumber=f"+92{row['phone']}"
            message=f"{customMessage}\n{portfolioLink}"

            kit.sendwhatmsg_instantly(phoneNumber,message,35)

            time.sleep(10)
        
            pyautogui.press("Enter")

            st.info("copy write reserved by me")
            