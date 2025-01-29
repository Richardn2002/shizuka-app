from dataclasses import dataclass

def get_vid_sub_path(season: int, episode: int) -> tuple[str, str]:
    assert(season == 1)
    assert(episode >= 1 & episode <= 13)

    return ('/home/richardn/Hyakkano S01 1080p WEBRip AAC x265-EMBER/[EMBER] Hyakkano - %02d.mkv' % episode, '/home/richardn/Hyakkano S01 1080p WEBRip AAC x265-EMBER/sub/[Airota&Nekomoe kissaten&LoliHouse] Hyakkano - %02d [WebRip 1080p HEVC-10bit AAC ASSx2].JPSC.ass' % episode)

@dataclass
class Line:
    start: str
    end: str
    jpn: str
    chn: str

def parse_ass(path: str) -> list[Line]:
    chn: dict[str, tuple[str, str]] = {}
    jpn: dict[str, str] = {}

    with open(path, 'r') as f:
        for line in f:
            if not line.startswith('Dialogue:'):
                continue
            
            words = line.rstrip().split(',')

            if words[3] == 'Dial-CH':
                chn[words[1]] = (words[2], words[9])
            elif words[3] == 'Dial-JP':
                jpn[words[1]] = words[9]
            else:
                continue
    
    res = []
    for start, (end, text) in chn.items():
        if not text.startswith('「'):
            continue

        res.append(Line(start, end, jpn[start], text))
    
    return res

for ep in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    with open('raw_sub/%02d.csv' % ep, 'w+') as f:
        lines = parse_ass(get_vid_sub_path(1, ep)[1])
        for line in lines:
            print('%s,%s,%s,%s' % (line.start, line.end, line.chn, line.jpn), file=f)
