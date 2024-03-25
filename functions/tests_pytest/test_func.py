from main import add_one,division,is_palindrom

import pytest

def test_answer():
    # оператор ассерт это встроенный оператор в пайтон, позволяющий отслеживать код. Этот оператор принимает условие, и необязательное сообщение которое выходит при исключении AssertionError/ ИСключение ASsertionError выходит когда Ассерт встречает False. Если ассерт встретит тру - то ничего не произойдет. 
    assert add_one(5) == 5, 'Test ne proshel proverku'



def test_divisiion():
    assert division(10, 5) == 2, 'loh'

@pytest.mark.parametrize(
    'a,b, res',
    [(10, 5, 2), (12, 6 , 2), (9, 3, 3)]
)
def test_division2(a,b, res):
    assert division(a,b) == res
