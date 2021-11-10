from cipher_yx2625 import cipher_yx2625

def test_cipher_encrypt(): 
    example = ['Harry', 3]
    expected = 'KduuB'
    actual = cipher_yx2625(example[0],example[1])
    assert actual == expected
