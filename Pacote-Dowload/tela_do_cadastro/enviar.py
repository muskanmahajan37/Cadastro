def enviaremail(remetente, nome, senha):
    import win32com.client as win32
    outlook = win32.Dispatch("outlook.application")
    email = outlook.CreateItem(0)
    email.To = f"{remetente}"
    email.Subject = "Senha"
    email.HTMLBody = f"""
    <h1>Dados da conta</h1>
    <hr>
    <strong>Email - </strong>
    <em> {remetente}</em>
    <hr>
    <strong>Login - </strong>
    <em> {nome}</em>
    <hr>
    <strong>Senha - </strong>
    <em> {senha}</em>
    <hr>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvjBN-rIOOqMjghH0wo6Fx4aamXUGCRvj6rQ&usqp=CAU" alt="Agradecimento">
    <hr>
    <ins>Sempre Estaremos Disponíveis!</ins>
    """
    try:
        email.Send()
    except:
        print()
        print("Aconteceu algo de errado")
    else:
        print("   ---   email enviado")
