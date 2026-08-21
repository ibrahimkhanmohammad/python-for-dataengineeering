#   we can not only remove white spaces but also other special characters too
#   use case - 1
url = 'https://www.youtube.com/'
clean_url = url.strip('https:/')
print(clean_url)

#   mind map
message = '###important###'
print(message.lstrip('#'))
print(message.strip('#'))
print(message.rstrip('#'))