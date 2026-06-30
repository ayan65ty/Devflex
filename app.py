import streamlit as st
import yt_dlp

st.title("📥 Universal Video Downloader")

AD_LINK = "https://omg10.com/4/11216275"
url = st.text_input("Paste video link here:")

if st.button("Get Download Link"):
    if not url:
        st.warning("Please paste a link first!")
    else:
        st.markdown(f"### [👉 CLICK HERE TO UNLOCK DOWNLOAD]({AD_LINK})")
        
        with st.spinner("Extracting..."):
            try:
                # We add 'user_agent' to look like a real browser
                ydl_opts = {
                    'format': 'best',
                    'quiet': True,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                    st.success("Video Found!")
                    st.video(video_url)
            except Exception as e:
                st.error(f"Error: {e}")
                st.write("Tip: If this is TikTok, try a different link or ensure it's a public post.")
