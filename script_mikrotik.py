import tkinter as tk
import paramiko

def enviar_script():
    # Obtém os valores dos campos de entrada
    ip = entry_ip.get()
    porta = entry_porta.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    script = text_script.get("1.0", "end-1c")  # Obtém o texto do campo de script

    # Cria uma conexão SSH com o equipamento MikroTik
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, int(porta), usuario, senha)
    except paramiko.AuthenticationException as e:
        resultado_var.set("Erro de autenticação: " + str(e))
        return
    except paramiko.SSHException as e:
        resultado_var.set("Erro de conexão: " + str(e))
        return

    # Envia o script para o equipamento MikroTik
    try:
        ssh.exec_command(script)
        resultado_var.set("Script enviado com sucesso!")
    except paramiko.SSHException as e:
        resultado_var.set("Erro ao enviar o script: " + str(e))

    # Fecha a conexão SSH
    ssh.close()

# Criação da janela
janela = tk.Tk()
janela.title("Envio de Script MikroTik")

# Campos de entrada
lbl_ip = tk.Label(janela, text="IP:")
lbl_ip.grid(row=0, column=0, padx=10, pady=5)
entry_ip = tk.Entry(janela)
entry_ip.grid(row=0, column=1, padx=10, pady=5)

lbl_porta = tk.Label(janela, text="Porta:")
lbl_porta.grid(row=1, column=0, padx=10, pady=5)
entry_porta = tk.Entry(janela)
entry_porta.grid(row=1, column=1, padx=10, pady=5)

lbl_usuario = tk.Label(janela, text="Usuário:")
lbl_usuario.grid(row=2, column=0, padx=10, pady=5)
entry_usuario = tk.Entry(janela)
entry_usuario.grid(row=2, column=1, padx=10, pady=5)

lbl_senha = tk.Label(janela, text="Senha:")
lbl_senha.grid(row=3, column=0, padx=10, pady=5)
entry_senha = tk.Entry(janela, show="*")
entry_senha.grid(row=3, column=1, padx=10, pady=5)

lbl_script = tk.Label(janela, text="Script:")
lbl_script.grid(row=4, column=0, padx=10, pady=5)
text_script = tk.Text(janela, height=5, width=30)
text_script.grid(row=4, column=1, padx=10, pady=5)

# Botão de envio
btn_enviar = tk.Button(janela, text="Enviar", command=enviar_script)
btn_enviar.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Configuração da área de exibição de resultados
resultado_var = tk.StringVar()
lbl_resultado = tk.Label(janela, textvariable=resultado_var)
lbl_resultado.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

#Iniciar a janela principal

janela.mainloop()

