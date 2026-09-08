"""Combine editable chapters into a navigable single Markdown manual."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]

def build():
    chapters=sorted((ROOT/'docs').glob('[0-9][0-9]-*.md'))
    texts=['# Tubular linear motor — engineering manual\n\nRevision 64 documentation, with Revision 62 history. Prototype definition; no physical qualification established.\n\nSee [repository overview](../README.md) and [generated calculations](../calculations/results.md).\n']
    for c in chapters:
        t=c.read_text(encoding='utf-8')
        t=re.sub(r'^(#{1,5}) ',r'#\1 ',t,flags=re.M)
        texts.append(t)
    target=ROOT/'docs/ENGINEERING_MANUAL.md'
    target.write_text('\n\n---\n\n'.join(texts)+'\n',encoding='utf-8')
    print('Built combined engineering manual from',len(chapters),'chapters')

if __name__=='__main__': build()
