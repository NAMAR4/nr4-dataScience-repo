from finding import finding


def test_finding_1():
    arr = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
    assert finding(arr) == 9

def test_finding_2():
    arr = [1,1,2]
    assert finding(arr) == 2

def test_finding_3():
    arr = [-1,-1,-2]
    assert finding(arr) == -2


def test_finding_4():
    arr = [1,2,3]
    assert finding(arr) == None

def test_finding_5():
    arr = [1,1,2,2]
    assert finding(arr) == None

def test_finding_6():
    arr = []
    assert finding(arr) == None

def test_finding_7():
    arr = [1,2]
    assert finding(arr) == None