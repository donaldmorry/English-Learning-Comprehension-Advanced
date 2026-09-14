import zipfile, re, shutil, sys, os
src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
items = {n: zin.read(n) for n in zin.namelist()}
st = items['styles.xml'].decode('utf-8')
c  = items['content.xml'].decode('utf-8')

fonts = set(re.findall(r'<style:font-face style:name="([^"]+)"', st))
fname = 'Liberation Sans' if 'Liberation Sans' in fonts else sorted(fonts)[0]
print('footer font:', fname, '| declared faces:', sorted(fonts))

# 1. give Mpm2 a real footer area
old = '<style:header-style/><style:footer-style/></style:page-layout>'
new = ('<style:header-style/><style:footer-style>'
       '<style:header-footer-properties fo:min-height="0.28in" fo:margin-top="0.20in" '
       'style:dynamic-spacing="false"/></style:footer-style></style:page-layout>')
i = st.find('<style:page-layout style:name="Mpm2"')
j = st.find('</style:page-layout>', i) + len('</style:page-layout>')
seg = st[i:j]
assert old in seg, 'footer-style anchor not found'
st = st[:i] + seg.replace(old, new) + st[j:]

# 2. footer paragraph style
footer_style = (
  '<style:style style:name="BookFooter" style:family="paragraph">'
  '<style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>'
  '<style:text-properties style:font-name="%s" fo:font-size="8.5pt" fo:color="#6b7481"/>'
  '</style:style>' % fname)
assert '</office:styles>' in st
st = st.replace('</office:styles>', footer_style + '</office:styles>', 1)

# 3. master pages: HTML gets the footer, FirstPage (title page) does not
mp_old = '<style:master-page style:name="HTML" style:page-layout-name="Mpm2"/>'
assert mp_old in st, 'HTML master page not found'
mp_new = ('<style:master-page style:name="FirstPage" style:page-layout-name="Mpm2" '
          'style:next-style-name="HTML"/>'
          '<style:master-page style:name="HTML" style:page-layout-name="Mpm2">'
          '<style:footer><text:p text:style-name="BookFooter">— '
          '<text:page-number text:select-page="current">1</text:page-number>'
          ' —</text:p></style:footer></style:master-page>')
st = st.replace(mp_old, mp_new, 1)

# 4. first paragraph of the document starts on FirstPage
before = c
c = c.replace('style:master-page-name="HTML"', 'style:master-page-name="FirstPage"', 1)
assert c != before, 'first-page master reference not found'

items['styles.xml'] = st.encode('utf-8')
items['content.xml'] = c.encode('utf-8')

zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED)
zout.writestr(zipfile.ZipInfo('mimetype'), items.pop('mimetype'), zipfile.ZIP_STORED)
for n, b in items.items():
    zout.writestr(n, b)
zout.close()
print('patched ->', dst, os.path.getsize(dst), 'bytes')
