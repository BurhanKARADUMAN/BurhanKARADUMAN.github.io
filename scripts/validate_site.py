"""Offline sanity checks for the public research portfolio."""
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]
class Checker(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.images=[]
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if 'id' in attrs:self.ids.append(attrs['id'])
  if tag=='img':self.images.append(attrs)
  for typ in ('href','src'):
   if typ in attrs:self.links.append(attrs[typ])

def test_page(page):
 data=(ROOT/page).read_text('utf-8'); parser=Checker();parser.feed(data)
 assert len(parser.ids)==len(set(parser.ids)),(page,'Duplicate IDs')
 for img in parser.images:assert 'alt' in img,(page,'Image without alt')
 for href in parser.links:
  if href.startswith(('https://','http://','mailto:','tel:','data:')):continue
  target,_,fragment=href.partition('#')
  if target and not (ROOT/target).is_file():raise AssertionError((page,'Missing local file',href))
  if not target and fragment and fragment not in parser.ids:raise AssertionError((page,'Missing anchor',fragment))
 assert 'Burhan Karaduman' in data
 return len(parser.links),len(parser.images)

def main():
 for page in ['index.html','cv.html']:
  links,images=test_page(page);print(f'OK {page} ({links} links, {images} images)')
 cv=ROOT/'assets/Burhan_Karaduman_Academic_CV.pdf';assert cv.is_file() and cv.stat().st_size>5000
 assert (ROOT/'.nojekyll').exists()
 assert '1.8 million' in (ROOT/'index.html').read_text('utf-8')
 print('PASS: HTML and asset validation')
if __name__=='__main__': main()
