import json
import tkinter as tk
from tkinter import messagebox, simpledialog

ARQUIVO = "jogos.json"

def carregar_jogos():
    try:  
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
def salvar_jogo(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)
    
def adicionar_jogo():
    nome = entrada_jogo.get().strip()
    if nome:
        lista = carregar_jogos()
        lista.append(nome)
        salvar_jogo(lista)
        entrada_jogo.delete(0, tk.END)
        atualizar_lista()
        messagebox.showwarning('Sucesso', f"jogo '{nome}' salvo!")
    else:
        messagebox.showwarning('Aviso', 'Digite o nome do jogo.')

def atualizar_lista():
    lista_jogos.delete(0, tk.END)
    for jogo in carregar_jogos():
        lista_jogos.insert(tk.END, jogo)

def remover_jogo():
    selecionado = lista_jogos.curseselection()
    if selecionado:
        lista = carregar_jogos()
        jogo = lista.pop(selecionado[0])
        salvar_jogo(lista)
        atualizar_lista()
        messagebox.showwarning('Removido', f"jogo '{jogo}' removido.")
    else:
        messagebox.showwarning('Aviso', 'Selecione um jogo para remover.')

def alterar_jogo():
    selecionado = lista_jogos.curselection()
    if selecionado:
        lista = carregar_jogos()
        atual = lista[selecionado[0]]
        novo = simpledialog.askstring("Alterar", f"Novo nome para '{atual}':")
        if novo:
            lista[selecionado[0]] = novo.strip()
            salvar_jogo(lista)
            atualizar_lista()
            messagebox.showinfo("Alterado", f"Jogo alterado para '{novo}'.")
    else:
        messagebox.showwarning("Aviso", "Selecione um jogo para alterar!")

#Interface

janela = tk.Tk()
janela.title("jogos_zerados")

entrada_jogo = tk.Entry(janela, width=40)
entrada_jogo.pack(pady=5)

btn_adicionar = tk.Button(janela, text="Adicionar jogo", command=adicionar_jogo)
btn_adicionar.pack(pady=5)

lista_jogos = tk.Listbox(janela, width=50)
lista_jogos.pack(pady=5)

btn_alterar = tk.Button(janela, text="Alterar jogo", command=alterar_jogo)
btn_alterar.pack(pady=5)

btn_remover = tk.Button(janela, text="Remover jogo", command=remover_jogo)
btn_remover.pack(pady=5)

atualizar_lista()
janela.mainloop()