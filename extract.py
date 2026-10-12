import sys, zipfile, xml.etree.ElementTree as ET
with zipfile.ZipFile(sys.argv[1]) as z:
    info=z.getinfo('word/document.xml')
    if info.file_size>10*1024*1024: raise ValueError('Expanded document too large')
    root=ET.fromstring(z.read(info))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    for p in root.findall('.//w:p',ns):
        print(''.join(t.text or '' for t in p.findall('.//w:t',ns)))
