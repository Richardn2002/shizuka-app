import subprocess

def get_vid_sub_path(season: int, episode: int) -> tuple[str, str]:
    assert(season == 1)
    assert(episode >= 1 & episode <= 13)

    return ('/home/richardn/Hyakkano S01 1080p WEBRip AAC x265-EMBER/[EMBER] Hyakkano - %02d.mkv' % episode, '/home/richardn/Hyakkano S01 1080p WEBRip AAC x265-EMBER/sub/[Airota&Nekomoe kissaten&LoliHouse] Hyakkano - %02d [WebRip 1080p HEVC-10bit AAC ASSx2].JPSC.ass' % episode)

for ep in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    vid_path = get_vid_sub_path(1, ep)[0]
    with open('filtered_sub/%02d.csv' % ep,'r') as f:
        for line in f:
            words = line.rstrip().split(',')
            cmd = [
                'ffmpeg',
                '-y',
                '-ss', words[0],
                '-to', words[1],
                '-i', vid_path,
                '-map', 'a',
                'raw_audio/S01E%02d %s %s.mp3' % (ep, words[0], words[3])
            ]
            subprocess.run(cmd, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
