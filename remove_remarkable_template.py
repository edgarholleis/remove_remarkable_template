import pdfrw
import binascii
import sys

# Compressed PDF code the ReMarkable emits for pages using the blank template
empty_template_hex = b'789c858dbd0a02311084fb7d8a7901f3b389b94b7d85602184946221f107040fe315bebe7b392dac64d81d6677e0d39b7cc475821ef203e5e34326a39ced6c6f820d30a2d5ef611d3dca9d2a2a254ab22b99d6cbc38e2c5e606c656ed81f0c709252a52fc2364d6524bdc0e5c78a23fbde8585c6ca05df47518b429a2d58461719cf335d66ec5f2812bd01e031307f'
empty_template = str(binascii.a2b_hex(empty_template_hex), encoding='latin1')

if len(sys.argv) != 3:
    print('Usage: remove_remarkable_template.py in.pdf out.pdf', file=sys.stderr)
    exit(1)
    
pdf = pdfrw.PdfReader(sys.argv[1])
out = pdfrw.PdfWriter(sys.argv[2])

for page in pdf.pages:
    if isinstance(page.Contents, pdfrw.objects.pdfarray.PdfArray) and len(page.Contents) > 1:
        page.Contents[0].stream = empty_template
    elif isinstance(page.Contents, pdfrw.objects.pdfdict.PdfDict): # empty page
        page.Contents.stream = empty_template
    out.addpages([page,])
    
out.trailer.Info = pdf.Info
out.write()

