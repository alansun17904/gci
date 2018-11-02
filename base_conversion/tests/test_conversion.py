from context import basetodec, dectobase


def test_basetodec_under_ten_bases():
   assert 2797 == basetodec(2, '101011101101')
   assert 318373  == basetodec(3, '121011201121')
   assert 7190225 == basetodec(4, '123123123101')
   assert 135216773 == basetodec(5, '234103414043')
   assert 2093776480 == basetodec(6, '543432521344')
   assert 11807447597 == basetodec(7, '565412435321')
   assert 58943548628 == basetodec(8, '667123626324')
   assert 54573579635 == basetodec(9, '165768732365')


def test_dectobase_under_ten_bases():
    assert '101001' == dectobase(2, 41)
    assert '2111' == dectobase(3, 67)
    assert '1121' == dectobase(4, 89)
    assert '204' == dectobase(5, 54)
    assert '1110' == dectobase(6, 258)
    assert '33' == dectobase(7, 24)
    assert '711' == dectobase(8, 457)
    assert '651' == dectobase(9, 532)


def test_basetodec_over_ten_bases():
    assert 248185 == basetodec(11, '15A513')
    assert 1102313 == basetodec(12, '451AB5')
    assert 1937574 == basetodec(13, '52ABC2')
    assert 952755 == basetodec(14, '1AB2DD')
    assert 2224825== basetodec(15, '2DE31A')
    assert 16777215 == basetodec(16, 'FFFFFF')


def test_dectobase_over_ten_bases():
    assert '457' == dectobase(11, 546)
    assert '142' == dectobase(12, 194)
    assert '402' == dectobase(13, 678)
    assert '403' == dectobase(14, 787)
    assert '9A' == dectobase(15, 145)
    assert '356' == dectobase(16, 854)

