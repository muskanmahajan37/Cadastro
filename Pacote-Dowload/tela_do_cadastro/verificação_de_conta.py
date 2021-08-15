def verificacao(email, nome, senha):
    import enviar
    import mysql.connector
    cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
    mcursor = cnx.cursor()
    from random import randint
    codigo = list()
    for i in range(0, 6):
        codigo.append(randint(0, 9))
    codigo = str(codigo)
    codigo = codigo.replace("[", "")
    codigo = codigo.replace("]", "")
    codigo = codigo.replace(",", "")

    mcursor.execute("use login;")
    mcursor.execute(f"insert into conf value (default, '{email}', '{nome}', '{senha}', '{codigo}');")
    enviar.enviarconfirm(email, codigo)


verificacao(email="athos.favaron@gmail.com", nome="Athos", senha="28Maio07")
