import sys, json

raw = json.load(sys.stdin)
courses = raw['data']['data']
out = []
for c in courses:
    out.append({
        'slug': c['slug'],
        'name': c['displayedName']['fr'],
        'duration': c['duration'],
        'image': c['banner']['asset']['sources'][0]['url'],
        'url': 'https://craif.didask.com/fr/courses/' + c['slug']
    })
print(json.dumps(out, ensure_ascii=False, indent=2))
