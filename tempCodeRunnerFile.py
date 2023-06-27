import tkinter as tk
import sqlite3

# Conexão com banco de dados
conexao = sqlite3.connect('equipamentos.db')
cursor = conexao.cursor()

# Criação da tabela 'equipamentos'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        equipamento TEXT,
        data_entrada TEXT,
        tombo TEXT,
        situacao TEXT,
        motivo TEXT,
        setor TEXT,
        data_saida TEXT
    )
''')
conexao.commit()

def adicionar_equipamento():
    equipamento = equipamento_entry.get()
    data_entrada = data_entrada_entry.get()
    tombo = tombo_entry.get()
    situacao = situacao_entry.get()
    motivo = motivo_entry.get()
    setor = setor_entry.get()
    data_saida = data_saida_entry.get()
    cursor.execute('INSERT INTO equipamentos (equipamento, data_entrada, tombo, situacao, motivo, setor, data_saida) VALUES (?, ?, ?, ?, ?, ?, ?)', (equipamento, data_entrada, tombo, situacao, motivo, setor, data_saida))
    conexao.commit()
    resultado_label['text'] = "Equipamento adicionado com sucesso!"

def buscar_equipamento():
    tombo = tombo_entry.get()
    cursor.execute('SELECT * FROM equipamentos WHERE tombo = ?', (tombo,))
    equipamento = cursor.fetchone()
    if equipamento:
        resultado_label['text'] = "=== Informações do Equipamento ===\n"
        resultado_label['text'] += f"Equipamento: {equipamento[1]}\n"
        resultado_label['text'] += f"Data de Entrada: {equipamento[2]}\n"
        resultado_label['text'] += f"Tombo: {equipamento[3]}\n"
        resultado_label['text'] += f"Situação: {equipamento[4]}\n"
        resultado_label['text'] += f"Motivo: {equipamento[5]}"
        resultado_label['text'] += f"Setor: {equipamento[6]}\n"
        resultado_label['text'] += f"Data de Saida: {equipamento[7]}"
        resultado_label['text'] += "======================================="
    else:
        resultado_label['text'] = "Equipamento não encontrado!"

def mostrar_equipamentos():
    setor = setor_entry.get()
    cursor.execute('SELECT * FROM equipamentos WHERE setor = ?', (setor,))
    equipamentos_setor = cursor.fetchall()
    if equipamentos_setor:
        resultado_label['text'] += f"=== Equipamentos do Setor {setor} ===\n"
        for equipamento in equipamentos_setor:
            resultado_label['text'] += f"Equipamento: {equipamento[1]}\n"
            resultado_label['text'] += f"Data de Entrada: {equipamento[2]}\n"
            resultado_label['text'] += f"Tombo: {equipamento[3]}\n"
            resultado_label['text'] += f"Situação: {equipamento[4]}\n"
            resultado_label['text'] += f"Motivo: {equipamento[5]}\n"
            resultado_label['text'] += f"Data de Saida: {equipamento[7]}\n"
        resultado_label['text'] += "==================================================="
    else:
        resultado_label['text'] = "Nenhum equipamento encontrado para esse setor!"
        
def limpar_campos():
    equipamento_entry.delete(0, tk.END)
    data_entrada_entry.delete(0, tk.END)
    tombo_entry.delete(0, tk.END)
    situacao_entry.delete(0, tk.END)
    motivo_entry.delete(0, tk.END)
    setor_entry.delete(0, tk.END)
    data_saida_entry.delete(0, tk.END)
    resultado_label['text'] = ""

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Gerenciamento de Equipamentos")

# Criação dos widgets
equipamento_label = tk.Label(janela, text="Equipamento:")
equipamento_entry = tk.Entry(janela)

data_entrada_label = tk.Label(janela, text="Data de Entrada:")
data_entrada_entry = tk.Entry(janela)

tombo_label = tk.Label(janela, text="Tombo:")
tombo_entry = tk.Entry(janela)

situacao_label = tk.Label(janela, text="Situação:")
situacao_entry = tk.Entry(janela)

motivo_label = tk.Label(janela, text="Motivo:")
motivo_entry = tk.Entry(janela)

setor_label = tk.Label(janela, text="Setor:")
setor_entry = tk.Entry(janela)

data_saida_label = tk.Label(janela, text="Data de Saida:")
data_saida_entry = tk.Entry(janela)

adicionar_button = tk.Button(janela, text="Adicionar equipamento", command=adicionar_equipamento)
buscar_button = tk.Button(janela, text="Buscar equipamento", command=buscar_equipamento)
mostrar_button = tk.Button(janela, text="Mostrar equipamentos do Setor", command=mostrar_equipamentos)
limpar_button = tk.Button(janela, text="Limpar os Campos", command=limpar_campos)

resultado_label = tk.Label(janela, text="")

# Posicionamento dos widgets na janela
equipamento_label.grid(row=0, column=0)
equipamento_entry.grid(row=0, column=1)

data_entrada_label.grid(row=1, column=0)
data_entrada_entry.grid(row=1, column=1)

tombo_label.grid(row=2, column=0)
tombo_entry.grid(row=2, column=1)

situacao_label.grid(row=3, column=0)
situacao_entry.grid(row=3, column=1)

motivo_label.grid(row=4, column=0)
motivo_entry.grid(row=4, column=1)

setor_label.grid(row=5, column=0)
setor_entry.grid(row=5, column=1)

data_saida_label.grid(row=6, column=0)
data_saida_entry.grid(row=6, column=1)

adicionar_button.grid(row=7, column=0)
buscar_button.grid(row=7, column=1)
mostrar_button.grid(row=7, column=2)
limpar_button.grid(row=7, column=3)

resultado_label.grid(row=8, column=0, columnspan=2)

# Fechar a conexão com o banco de dados ao fechar a janela
janela.protocol("WM_DELETE_WINDOW", lambda: fechar_conexao(conexao))

def fechar_conexao(conexao):
    conexao.close()
    janela.destroy()

# Iniciar o loop principal da aplicação
janela.mainloop()