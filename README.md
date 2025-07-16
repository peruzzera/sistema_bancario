
# Sistema Bancário Simples em Python 🏦

Este projeto é uma simulação de um sistema bancário simples feito em Python, com operações básicas como **depósito**, **saque** e **emissão de extrato**.
## 💡 Funcionalidades

- 📥 **Depósito**: Permite adicionar dinheiro ao saldo.
- 💸 **Saque**: Permite retirar dinheiro com as seguintes regras:
  - Limite de saque: R$500 por operação.
  - Máximo de 3 saques por execução.
  - Não é permitido sacar valores negativos ou superiores ao saldo.
- 📄 **Extrato**: Exibe todas as transações realizadas e o saldo atual.
- 🚪 **Sair**: Encerra o programa.

## 📋 Regras

- Valor do saque não pode ser maior que o saldo.
- Valor do saque não pode ultrapassar R$500.
- Apenas 3 saques são permitidos por sessão.
- O extrato mostra todos os depósitos e saques realizados.

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.x).
2. Clone o repositório ou baixe o arquivo `banco.py`.
3. Execute o script no terminal:

```bash
python banco.py
```

## 📎 Exemplo de Uso

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
```

Digite a opção desejada e siga as instruções para realizar as operações bancárias.
