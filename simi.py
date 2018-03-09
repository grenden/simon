import urllib, json

print "Silahkan kirim pesan!"

while(True):
    pesan = raw_input("Anda: ")
    url = "http://sandbox.api.simsimi.com/request.p?key=f21a9486-4cc3-43a7-a212-43b83d2f287d&lc=id&ft=1.0&text=%s" % pesan
    link_json = urllib.urlopen(url)
    data = json.loads(link_json.read())

    print "simon: %s" % data['response']
