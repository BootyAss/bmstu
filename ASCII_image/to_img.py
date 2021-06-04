import sys
import optparse
from PIL import Image
from PIL import ImageDraw


def text2image(text,color):
    lines = text.split('\n')
    im    = Image.new("RGBA",(1,1),color=None)
    draw  = ImageDraw.Draw(im)
    #
    widths, heights = zip(*[draw.textsize(l) for l in lines])
    #resize
    im       = im.resize((max(widths),sum(heights)))
    draw     = ImageDraw.Draw(im)
    textdraw = draw.text
    y        = 0
    for line,height in zip(lines,heights):
        textdraw((0,y),line,fill=color)
        y += height
    return im

def main():
    optparser = optparse.OptionParser()
    optparser.usage = 'Usage: %PROG INFILE OUTFILE [options]'
    addopt = optparser.add_option
    addopt('--color',default='black',
           help='anything that PIL.ImageColor accepts')
    opts, args = optparser.parse_args()
    nargs = len(args)
    if nargs != 2:
        print ('INFILE and OUTFILE arguments required')
        return
    infile, outfile = args
    with open(infile,'r') as f:
        text = f.read()
    image = text2image(text,opts.color)
    if image:
        image.save(outfile)

if __name__=='__main__':
    sys.exit(main())