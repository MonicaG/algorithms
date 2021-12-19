from problems.amazon_oa import number_of_ways


def test_number_of_ways():
    assert number_of_ways('01001') == 4
    assert number_of_ways('10111') == 3
    assert number_of_ways('101') == 1
    assert number_of_ways('010') == 1
    assert number_of_ways('0100110') == 13
    assert number_of_ways('11111') == 0
    assert number_of_ways('00000') == 0
    assert number_of_ways('01') == 0
    assert number_of_ways('10') == 0
    assert number_of_ways('110') == 0
    assert number_of_ways('011') == 0
