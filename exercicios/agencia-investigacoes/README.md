# Exercício — Agência de Investigações

Você foi contratado para desenvolver um pequeno sistema para uma **agência de investigação**.

A agência recebe casos, coleta pistas e tenta descobrir quem é o responsável pelo crime. As informações deverão ser armazenadas em um arquivo `.json`.

---

## Funcionamento

O sistema terá alguns **casos de investigação**.

Cada caso possui:

- Id
- Titulo
- Local
- Uma lista de suspeitos
- Se está resolvido ou não
- Data de criação
- Data de resolução

O programa deverá salvar todos os casos em:

```text
casos.json
```

---

# Requisitos

# 1. Carregar os casos

Ao iniciar o programa:

* verificar se `casos.json` existe;
* se existir, carregar os dados;
* se não existir, começar com uma lista vazia.

---

# 2. Criar um novo caso

O investigador deverá informar:

```text
=== NOVO CASO ===

Título: Roubo à joalheria
Local: Centro

Caso criado com sucesso!
```

O programa deverá criar salvar o caso no arquivo:

---

# 3. Adicionar suspeitos

O usuário deverá escolher um caso e adicionar suspeitos.

Exemplo:

```text
=== ADICIONAR SUSPEITO ===

Informe o ID do caso: 1

Nome: João
Idade: 35

Suspeito adicionado!
```

O suspeito deverá ser armazenado dentro da lista `suspeitos` do caso: Cada suspeito possui as seguintes informações:

- Nome
- Idade
- Uma lista de evidências

---

# 4. Encontrar pistas

O investigador poderá registrar uma **evidência contra um suspeito**.

Exemplo:

```text
=== NOVA EVIDÊNCIA ===

Caso: 1

Suspeito: João

Descrição da evidência:
Foi encontrado um objeto pertencente ao suspeito no local.

Evidência registrada!
```

Cada suspeito deverá possuir uma lista de evidências:

**Observação:** alterar a estrutura inicial para que `evidencias` seja uma **lista**, e não um número.

---

# 5. Analisar o caso

O sistema deverá apresentar um relatório.

Exemplo:

```text
========================================
          RELATÓRIO DO CASO
========================================

Caso: Roubo à joalheria
Local: Centro

Suspeitos:

1 - João
    Idade: 35
    Evidências: 3

2 - Maria
    Idade: 29
    Evidências: 1

========================================
```

Além disso, o programa deverá informar quem possui **mais evidências**.

```text
PRINCIPAL SUSPEITO: João
Quantidade de evidências: 3
```

---

# 6. Resolver o caso

O investigador poderá tentar resolver o caso.

O programa deverá perguntar:

```text
Quem é o responsável?

Digite o nome do suspeito:
```

O sistema deverá verificar se o suspeito escolhido é aquele que possui mais evidências.

Se for:

```text
Analisando evidências...

✓ Evidências analisadas
✓ Suspeito identificado

CASO RESOLVIDO!
```

Caso contrário:

```text
Analisando evidências...

As evidências não são suficientes para confirmar o suspeito.

O caso continua aberto.
```

---

# 7. Salvar os dados

Sempre que houver alguma alteração, os dados deverão ser salvos no arquivo:

```text
casos.json
```

---

# Menu

O programa deverá apresentar:

```text
========================================
         AGÊNCIA DE INVESTIGAÇÕES
========================================

1 - Criar novo caso
2 - Adicionar suspeito
3 - Registrar evidência
4 - Analisar caso
5 - Resolver caso
6 - Listar casos
7 - Sair

Escolha:
```

---

