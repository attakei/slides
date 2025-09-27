# /// script
# dependencies = [
#   "oembedpy",
# ]
# ///
from oembedpy.application import Oembed

oembed = Oembed()
oembed.init()
content = oembed.fetch("https://www.youtube.com/watch?v=DnIi4qm_p7w")
print(content.html)
