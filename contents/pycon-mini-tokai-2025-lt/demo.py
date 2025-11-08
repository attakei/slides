# /// script
# dependencies = [
#   "oembedpy",
# ]
# ///
from oembedpy.application import Oembed

oembed = Oembed()
oembed.init()
content = oembed.fetch("https://www.youtube.com/watch?v=t-5nKuouoMo")
print(content.html)
