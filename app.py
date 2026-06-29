import streamlit as st
import yt_dlp

st.set_page_config(page_title="Universal Downloader", page_icon="📥")

st.title("📥 Universal Video Downloader")

# Your PropellerAds Direct Link
AD_LINK = "https://omg10.com/4/11216275"

url = st.text_input("Paste video link here (YouTube, TikTok, Insta, etc.):")

if st.button("Get Download Link"):
    if not url:
        st.warning("Please paste a link first!")
    else:
        # Show the Ad Link clearly
        st.markdown(f"### [👉 CLICK HERE TO UNLOCK DOWNLOAD]({AD_LINK})")
        st.info("Please click the link above first to support our service, then return here to download.")
        
        with st.spinner("Extracting video..."):
            try:
                ydl_opts = {'format': 'best', 'quiet': True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                    st.success("Video Found! Your download button is ready.")
                    st.video(video_url)
            except Exception as e:
                st.error("Error: Could not extract video. It might be private.")
