import os
import subprocess

# আপনার ইউটিউব ভিডিওর আইডি এখানে দিন (সঠিক আইডি নিশ্চিত করুন)
youtube_video_id = "YOUR_VIDEO_ID_HERE"

def get_m3u8_link(video_id):
    try:
        # yt-dlp ব্যবহার করে m3u8 লিঙ্ক বের করা
        # এখানে --quiet এবং --no-warnings যোগ করা হয়েছে ক্লিন আউটপুটের জন্য
        cmd = f"yt-dlp -g --format 'best' https://www.youtube.com/watch?v={video_id}"
        result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        return result
    except Exception as e:
        print(f"Error fetching link: {e}")
        return None

link = get_m3u8_link(youtube_video_id)

if link and "googlevideo.com" in link:
    with open("yt_link.txt", "w") as f:
        f.write(link)
    print("Link updated successfully!")
else:
    # যদি লিঙ্ক না পায়, তবে একটি ডামি ফাইল তৈরি করবে যাতে এরর না আসে
    with open("yt_link.txt", "w") as f:
        f.write("error_no_link_found")
    print("Failed to get link. Check Video ID.")
