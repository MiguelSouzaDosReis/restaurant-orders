# Project Restaurant Orders

Este foi o último projeto que realizei na Trybe, e nele tive a oportunidade de aprofundar meus conhecimentos em estrutura de dados, aprendendo sobre hashmaps, dicionários e conjuntos (sets). Com essa bagagem, pude concluir os requisitos propostos pela Trybe.

# Os requisito são 


## 1 - Campanha de publicidade

> Implemente um método chamado `analyze_log` no módulo `src/analyze_log.py` que gere informações de uma lanchonete.

A lanchonete quer promover ações de marketing e, para isso, a agência de publicidade precisa das informações abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

#### Dados

O atual sistema da lanchonete 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳  guarda os `logs` de todos os pedidos feitos em um arquivo _csv_, contendo o formato `cliente, pedido, dia`, um por linha e sem nome das colunas (a primeira linha já é um pedido).

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. Todas as informações são _strings_ com letras minúsculas. O histórico contém pedidos feitos em todos os dias da semana que a lanchonete abre, e de todos os pratos que a lanchonete oferece. Ou seja, é possível saber o cardápio e agenda completos. Os dias da semana estão no formato `"...-feira", "sabado" ou "domingo"`, e **não nos interessa informações sobre os dias que a lanchonete não abre**.

#### Implementação

No arquivo `analyze_log.py`, escreva uma função que responda às seguintes perguntas abaixo:

- Qual o prato mais pedido por 'maria'?

- Quantas vezes 'arnaldo' pediu 'hamburguer'?

- Quais pratos 'joao' nunca pediu?

- Quais dias 'joao' nunca foi à lanchonete?

A função não retornará nada e deverá apenas salvar as respostas no arquivo `data/mkt_campaign.txt`, na mesma ordem das peguntas acima.

<details>
<summary><b>Clique aqui para ver a assinatura da função.</b></summary>

```python
def analyze_log(path_to_file):
    # Código vem aqui
```

</details>

<details>
<summary><b>Clique aqui para ver saída correta da função.</b></summary>

```
hamburguer
1
{'pizza', 'coxinha', 'misto-quente'}
{'sabado', 'segunda-feira'}
```
</details>

:eyes: _De olho na Dica:_ a ordem dos pedidos, bem como dos dias da semana não precisa ser exatamente a apresentada no exemplo.

- No arquivo `analyze_log.py` deve estar implementada a função `def analyze_log(path_to_file)`;

- A função deve realizar a leitura do `log` e salvar em um arquivo `txt` as informações solicitadas;

- Utilização correta de `Dict/Set`, vistos no módulo;

- Código legível e modularizado, quando for o caso.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 1.1 - Será validado se, ao executar o método `analyze_log`, os dados são preenchidos de forma correta no arquivo `data/mkt_campaign.txt`;

- 1.2 - Será validado se, ao executar o método `analyze_log` com um arquivo inexistente, o método retorna um erro `FileNotFoundError` com a mensagem de erro abaixo:
  ```
  "Arquivo inexistente: '{nome_do_arquivo}'"
  ```
- 1.3 - Será validado se, ao executar o método `analyze_log` com uma extensão inválida, o método retorna um erro com a mensagem abaixo:
  ```
  "Extensão inválida: '{nome_do_arquivo}'"
  ```
</details>

## 2 - Análises contínuas

> Implemente a classe `TrackOrders` que gere informações contínuas da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 .

A campanha de marketing foi um sucesso! A gerência da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 deseja agora um sistema que mantenha um registro contínuo dessas informações. Mais especificamente, deseja que o sistema permita, a qualquer momento, a extração das seguintes informações:

- Prato favorito por cliente;

- Pratos nunca pedidos por cada cliente;

- Dias nunca visitados por cada cliente;

- Dia mais movimentado;

- Dia menos movimentado.

Para isso, você deverá implementar uma classe que entregue as informações acima.

#### Implementação

**Arquivos**

- Implemente a classe `TrackOrders` no arquivo `track_orders.py`;

- O arquivo `src/main.py` é apenas auxiliar e faz a leitura do arquivo `csv` especificado e envia, ao mesmo tempo, a informação de cada pedido para as classes `TrackOrders` e para a classe `InventoryControl`;

:eyes: _De olho na Dica:_ não se preocupe ainda com o arquivo `inventory_control.py` (classe InventoryControl), pois ele é necessário apenas para a realização dos requisitos bônus.

- No arquivo `src/main.py` algumas informações são impressas na tela para que você observe o comportamento das classes após a leitura completa do arquivo `csv`,


**Teste o comportamento do arquivo `main.py`**.

Abra o arquivo `main.py` e complete a variável _path_ com `data/orders_1.csv`. Rode o arquivo `main.py`. Quatro linhas de `None` devem ser impressas. Isso acontece, porque as funções não estão devidamente implementadas ainda.

**Implemente a solução**

<details>
<summary><b>No arquivo <code>track_orders.py</code>, implemente a classe <code>TrackOrders</code>. Clique aqui para ver os métodos que devem ser implementados.</b></summary>

```python
class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __len__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
```

:eyes: _De olho nas Dicas:_ você é livre para criar os atributos e métodos necessários; crie uma classe legível e bem modularizada; não implemente funcionalidades que ainda não são necessárias, nem coloque atributos do tipo "vai que um dia precisa"; sempre rode o arquivo `main.py` para verificar o comportamento da sua classe.

</details>


- Classe `TrackOrders` implementada;

- A classe está devidamente modularizada;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima (geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`).

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 2.1 - Será validado se, ao instanciar a classe `TrackOrders` pela primeira vez, o método `len()` retorna a quantidade de pedidos igual a zero;

- 2.2 - Será validado se, ao executar o método `add_new_order`, o método registra um pedido na instância;

- 2.3 - Será validado se, ao executar `get_most_ordered_dish_per_customer`, o método retorna o prato mais pedido;

- 2.4 - Será validado se, ao executar `get_never_ordered_per_customer`, o método retorna o conjunto de pratos que a pessoa nunca pediu;

- 2.5 - Será validado se, ao executar `get_days_never_visited_per_customer`, o método retorna o conjunto de dias que a pessoa nunca visitou;

- 2.6 - Será validado se, ao executar o método `get_busiest_day`, o método retorna o dia mais movimentado e;

- 2.7 - Será validado se, ao executar o método `get_least_busy_day`, o método retorna o dia menos movimentado.
</details>

---
# Requisitos bônus:

## 3 - Controle de estoque

Atualmente o controle de estoque de ingredientes da 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 é feito em um caderno. Ao final da semana, uma pessoa conta quantas unidades de cada ingrediente ainda restam no estoque e anota quantas unidades precisam ser compradas para completar o estoque mínimo de cada ingrediente.

A 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳  deseja automatizar esse controle: no final da semana, a gerência irá imprimir uma lista de compras com as respectivas quantidades.

#### Dados

O `log` a ser utilizado é o arquivo `data/orders_1.csv`. É garantido que os pedidos da semana não irão zerar nenhum dos estoques.

#### Implementação

No arquivo `inventory_control.py` você deve implementar a classe `InventoryControl` que retorna a lista de compras da semana, a partir da informação de cada pedido. É importante que a lista seja atualizada a cada pedido, e não apenas ao final de semana, pois a gerência quer ter a liberdade de imprimir a lista de compras a qualquer momento.

<details>
<summary><b>Clique aqui para ver a estrutura básica da classe. Lá já contém as informações dos ingredientes, bem como o estoque mínimo de cada um. O método <code>get_quantities_to_buy</code> deve retornar um <code>Dict</code> que mapeia o ingrediente para a quantidade a ser comprada.</b></summary>

```python
class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho', 'tomate'],
        'queijo-quente': ['pao', 'queijo', 'queijo'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'bauru': ['pao', 'queijo', 'presunto', 'tomate'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        pass

    def add_new_order(self, customer, order, day):
        pass

    def get_quantities_to_buy(self):
        pass
```

</details>

- Classe `InventoryControl` implementada;

- A classe está devidamente modularizada;

- Garanta que todos os ingredientes e pratos foram testados;

- Os métodos devem fazer uso das técnicas de `Dict` e `Set` vistos no módulo;

- Os métodos atingem complexidade ótima, geralmente `O(1)` ou `O(n)`, em alguns métodos que usam `Set`.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 3.1 - Será validado se, ao executar o método `get_quantities_to_buy`, o método retorna a quantidade de ingredientes que precisam ser comprados;

- 3.2 - Será validado se, ao executar o método `get_quantities_to_buy` para todos os hambúrgueres, o método retorna a quantidade de ingredientes que precisam ser comprados;

- 3.3 - Será validado se, ao executar o método `get_quantities_to_buy` para receitas diferentes, o método retorna a quantidade de ingredientes que precisam ser comprados.
</details>

## 4 - Estoque pode acabar

As campanhas de marketing tiveram sucesso novamente e atraíram muitas novas pessoas clientes para a 🥖🧑‍🍳 Pão na Chapa 🥖🧑‍🍳 . Se antes os estoques mínimos eram sempre suficientes para uma semana, agora não são mais.


<b>Suponha os seguintes estoques:</b>

```md
- Pao: 1;
- Queijo: 5;
- Presunto: 3.
```

Se uma pessoa pedir um misto-quente, será possível atendê-la. Porém o pão irá acabar. Se a próxima pessoa pedir hamburguer, não será possível atendê-la. Sua missão é implementar um código que, caso algum ingrediente acabe, todos os pratos que usam aquele ingrediente devem ser imediatamente removidos do cardápio eletrônico, evitando gerar frustração em clientes.

#### Dados

O `log` a ser utilizado é o arquivo `data/orders_2.csv`. Se quiser testar pelo arquivo `main.py`, não se esqueça de alterar a variável `path`.

#### Implementação

:eyes: _De olho na Dica:_ Você fez commit do requisito `3 - Controle de estoque`? Se não, faça, pois agora você vai alterar o seu código!

Implemente um novo método na classe `InventoryControl` que retorne um conjunto com todos os pratos disponíveis, ou seja, pratos que utilizam os ingredientes disponíveis em quantidade suficiente no estoque.


<details>
<summary><b>Clique aqui para ver a assinatura da função.</b></summary>

```python
def get_available_dishes():
    # retorno: um conjunto de pratos que ainda têm ingredientes disponíveis no estoque
```
</details>

Garanta que:

- O método `get_available_dishes` está implementado e funcionando corretamente;

- O método `add_new_order` retorne `False` para um pedido que não tem ingredientes disponíveis no estoque;

- As classes/métodos estão devidamente modularizadas;

- Os métodos fazem uso das técnicas de `Dict` e `Set` vistos no módulo.

<details>
  <summary>
    <b>🤖 Clique aqui para ver o que será verificado pelo avaliador.</b>
  </summary>

- 4.1 - Será validado se, ao executar o método `add_new_order` para um pedido com prato que não possui ingrediantes suficientes em estoque, o método retorna `False` sem registrar o pedido;

- 4.2 - Será validado se, ao executar o método `get_available_dishes`, o método retorna todos os pratos que possuem ingredientes suficientes para seu preparo;

- 4.3 - Será validado se, ao executar o método `get_available_dishes`, o método não retorna os pratos cujos ingredientes não sejam suficientes para seu preparo.
</details>

---

### Como você pode ver eu não fiz os requisitos 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 
