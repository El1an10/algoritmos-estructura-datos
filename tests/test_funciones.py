from algoritmos.funciones import dibuja_rectangulo, invierte_palabras, nro_de_salas, vuelto


def test_invierte_palabras():
    assert invierte_palabras("buenas noches mucho gusto") == "saneub sehcon ohcum otsug"


def test_dibuja_rectangulo():
    assert dibuja_rectangulo(3, 5) == "*****\n*   *\n*****\n"


def test_nro_de_salas():
    assert nro_de_salas([]) == 0
    assert nro_de_salas([(0, 30), (5, 10), (15, 20)]) == 2
    # Una reunion que termina justo cuando otra empieza puede usar la misma sala.
    assert nro_de_salas([(1, 5), (5, 10)]) == 1


def test_vuelto_readme_example():
    assert vuelto(87.50, 100) == {10.0: 1, 2.0: 1, 0.5: 1}


def test_vuelto_only_real_lempira_coins():
    # La moneda de 25 centavos no existe: 0.45 se da como 2 x 0.20 + 0.05.
    assert vuelto(99.55, 100) == {0.2: 2, 0.05: 1}


def test_vuelto_no_change():
    assert vuelto(100, 100) == {}
    assert vuelto(120, 100) == {}
