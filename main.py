import os
import subprocess

# আপনার ইউটিউব ভিডিওর আইডি এখানে দিন
youtube_video_id = "YOUR_VIDEO_ID_HERE"

def get_m3u8_link(video_id):
    try:
        # yt-dlp ব্যবহার করে m3u8 লিঙ্ক বের করা
        cmd = f"yt-dlp -g https://www.youtube.com/watch?v={video_id}"
        result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

link = get_m3u8_link(youtube_video_id)

if link:
    # লিঙ্কটি একটি ফাইলে সেভ করা যা পরে ওয়ার্কার এক্সেস করবে
    with open("yt_link.txt", "w") as f:
        f.write(link)
    print("Link updated successfully!")
