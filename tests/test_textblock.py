from typing import List
from datetime import date
from unittest import TestCase

from brasil.utils.records import TextBlock, BlockList


class TestTextBlock(TestCase):
    def test_block_typing(self):
        class Block2(TextBlock):
            field1: int
            field2: str
            field3: bool
            field4: date

        class Block1(TextBlock):
            field1: str
            block2: BlockList[Block2]

        # data modeling
        self.assertEqual(Block2._fields[0].data_type, int)
        self.assertEqual(Block2._fields[0].name, 'field1')
        self.assertEqual(Block1._fields[0].data_type, str)
        block2 = Block2()
        block2.field1 = 1
        block2.field2 = 'Test 1'
        block2.field3 = True
        # field 4 must be empty
        self.assertEqual(str(block2), '1,Test 1,1,')
        block2.field4 = date(2021, 1, 1)
        block1 = Block1()
        block1.field1 = 'Test block 1'
        block1.block2 = [block2]
        self.assertEqual(str(block1), 'Test block 1\n1,Test 1,1,01012021')
