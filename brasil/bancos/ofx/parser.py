import re
from typing import cast
from io import IOBase

from brasil.bancos.ofx.leiaute import OfxDocument, OfxBody, OfxHeader


class OfxParser:
    RE_INLINE_TAG = re.compile(r'<([a-zA-Z0-9_.]+)>([^<>]+)')
    RE_TAG = re.compile(r'<([a-zA-Z0-9_.]+)>')
    RE_TAG_EMPTY = re.compile(r'<([a-zA-Z0-9_.]+)></\1>')

    def parse(self, ofx_data: IOBase):
        ofx_data.seek(0)
        doc = OfxDocument()
        header = {}
        cur_tag: dict = {}  # ofx
        cur_list: list | None = None
        tags: list[dict] = [cur_tag]
        for l in ofx_data.readlines():
            if s := l.decode('latin-1').strip():
                if s.startswith('</'):  # ler tag de fechamento
                    cur_tag = tags.pop()
                    if tags:
                        cur_tag = tags[-1]
                elif s.startswith('<'):  # ler tag
                    if tag := self.RE_INLINE_TAG.match(s):
                        tag_name = tag.group(1)
                        tag_value = tag.group(2).strip()
                        cur_tag[tag_name] = tag_value
                    elif tag := self.RE_TAG_EMPTY.match(s):
                        tag_name = tag.group(1)
                        cur_tag[tag_name] = None
                    elif tag := self.RE_TAG.match(s):
                        tag_name = tag.group(1)
                        if tag_name == 'OFX':
                            continue
                        if tag_name == 'BANKTRANLIST':
                            cur_list = []
                        if tag_name == 'STMTTRN':
                            new_tag = {}
                            cur_tag[tag_name] = cur_list
                            cur_list.append(new_tag)
                        else:
                            new_tag = {}
                            cur_tag[tag_name] = new_tag
                        cur_tag = new_tag
                        tags.append(cur_tag)

                else:  # ler header
                    k, v = s.split(':', 1)
                    header[k.strip()] = v.strip()
        doc.header = cast(OfxHeader, cast(object, header))
        doc.body = cast(OfxBody, cast(object, cur_tag))
        return doc
