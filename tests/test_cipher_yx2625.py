from cipher_yx2625 import cipher_yx2625 as cph

def test_cipher_encrypt(): 
    example = ['Harry', 3]
    expected = 'KduuB'
    actual = cph.cipher(example[0],example[1])
    assert actual == expected
