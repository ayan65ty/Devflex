import streamlit as st
import yt_dlp

st.set_page_config(page_title="Universal Video Downloader", page_icon="📥")

st.title("📥 Universal Video Downloader")
st.write("Paste a link from YouTube, TikTok, Instagram, Twitter, or Facebook.")

url = st.text_input("Enter URL:")

if st.button("Get Download Link"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Extracting..."):
            try:
                # yt-dlp options to handle all sites
                ydl_opts = {
                    'format': 'best',
                    'quiet': True,
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    video_url = info.get('url')
                    title = info.get('title', 'Video')
                
                st.success(f"Found: {title}")
                st.markdown(f'<a href="{video_url}" target="_blank">Click here to download {title}</a>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: Could not extract video. The link might be private or broken. ({e})")
