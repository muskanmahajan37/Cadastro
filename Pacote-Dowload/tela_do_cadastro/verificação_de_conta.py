def verificacao(email):
    import enviar
    import mysql.connector
    from random import randint
    codigo = list()
    for i in range(0, 6):
        codigo.append(randint(0, 9))

    enviar.enviarconfirm(codigo, email)
