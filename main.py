import json, urllib.parse, os, requests

def dl(fmt):
    undef = 'undefine'
    res = requests.get(fmt['url'])
    res.raise_for_status()
    filename = fmt['mimeType'][:fmt['mimeType'].index(';')].replace('/', '_')
    if fmt.get('width', None):
        filename += '_%sx%s' % (fmt['width'], fmt['height'])
    if fmt.get('fps', None):
        filename += '_%s' % fmt['fps']
    if fmt.get('audioSampleRate', None):
        filename += '_%s' % fmt['audioSampleRate']
    typemap = {
        'video/mp4': 'mp4',
        'video/webm': 'webm',
        'audio/webm': 'weba',
        'audio/mp4': 'm4a'
    }
    filename += '.%s' % typemap.get(fmt['mimeType'][:fmt['mimeType'].index(';')])
    print(filename)
    
    with open(os.path.join(d, os.path.basename(d) + '_' + filename), 'wb') as out:
        for chunk in res.iter_content(100000):
            out.write(chunk)
    print()

print('dir:')
d = input()
with open(os.path.join(d, 'get_video_info'), encoding='utf-8') as f:
    info = f.read()
info = urllib.parse.unquote(info)
info = info[info.index('{'):info.rindex('}')+1].replace('\\u0026', '&')
j = json.loads(info)
for fmt in j['streamingData']['formats']:
    dl(fmt)
for fmt in j['streamingData']['adaptiveFormats']:
    dl(fmt)
