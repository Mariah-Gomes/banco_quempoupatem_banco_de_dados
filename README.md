# banco_quempoupatem_banco_de_dados

> Status do projeto: Finalizado

> Esse projeto nos foi proposto no 5ºSemestre na disciplina de Banco de Dados

> Escrevemos esse projeto juntos durante as aulas

### Tópicos
🔹[Diagrama Relacional](#straight_ruler-diagrama-relacional)

🔹[Como executar o código](#space_invader-como-executar-o-código)

🔹[Desenvolvedores](#busts_in_silhouette-desenvolvedores)

## :straight_ruler: Diagrama Relacional
### Modelo de Entidade Relacional
```mermaid
erDiagram
    CLIENTE {
    string nome
    string CPF
    int idade
    }

    GERENTE {
    string nome
    string login
    string senha
    }

    CONTA {
    string tipo
    float saldo
    string senha
    }

    DEBITO {
    float valor
    float taxa
    }

    DEPOSITO {
    float valor
    }

    TRANSFERENCIA {

    }

    EXTRATO {
    date data
    time hora
    string tipo_operacao
    string sinal
    float valor
    float taxa
    }

    EMPRESA {
    string nome
    string CNPJ
    float valor_cota
    }

    INVESTIMENTO {
    int quantidade
    }

    CLIENTE  || -- || CONTA : utiliza
    GERENTE  || -- |{ CONTA : gerencia
    CLIENTE  || -- |{ DEBITO : realiza
    CLIENTE  || -- |{ DEPOSITO : realiza_ou_recebe
    DEBITO   || -- || TRANSFERENCIA : realiza
    DEPOSITO || -- || TRANSFERENCIA : reccebe
    CLIENTE  || -- |{ EXTRATO : gera 
    CLIENTE  || -- o{ INVESTIMENTO : realiza
    EMPRESA || -- o{ INVESTIMENTO : recebe
```
### Modelo Relacional na 3FN
```mermaid
classDiagram
    class CLIENTE
    CLIENTE : + int id PK
    CLIENTE : + string nome
    CLIENTE : + int CPF UNIQUE
    CLIENTE : + int idade

    class GERENTE
    GERENTE : + int id PK
    GERENTE : + string nome
    GERENTE : + string login UNIQUE
    GERENTE : + string senha

    class CONTA
    CONTA : + int cliente_id PK, FK
    CONTA : + string tipo
    CONTA : + float saldo
    CONTA : + string senha
    CONTA : + int gerente_id FK

    class DEBITO
    DEBITO : + int id PK
    DEBITO : + float valor
    DEBITO : + float taxa
    DEBITO : + int cliente_id FK

    class DEPOSITO
    DEPOSITO : + int id PK
    DEPOSITO : + float valor
    DEPOSITO : + int cliente_id FK

    class TRANSFERENCIA
    TRANSFERENCIA : + int id PK
    TRANSFERENCIA : + int id_debito FK, UNIQUE
    TRANSFERENCIA : + int id_deposito FK, UNIQUE

    class EXTRATO
    EXTRATO : + int id PK
    EXTRATO : + date data 
    EXTRATO : + time horario
    EXTRATO : + string tipo_operação
    EXTRATO : + string sinal
    EXTRATO : + float taxa
    EXTRATO : + float valor
    EXTRATO : + int cliente_id FK
    
    class EMPRESA
    EMPRESA : + int id PK
    EMPRESA : + string nome
    EMPRESA : + string CNPJ UNIQUE
    EMPRESA : + float valor_cota

    class INVESTIMENTO
    INVESTIMENTO : int cliente_id FK, PK
    INVESTIMENTO : int empresa_id FK, PK
    INVESTIMENTO : int quantidade

    CLIENTE "1" --> "1" CONTA : utiliza
    GERENTE "1..*" --> "1..*" CONTA : gerencia
    CLIENTE "1" --> "1..*" DEBITO : realiza
    CLIENTE "1" --> "1..*" DEPOSITO : realiza_ou_reccebe
    DEBITO "1" --> "1" TRANSFERENCIA : realiza
    DEPOSITO "1" --> "1" TRANSFERENCIA : recebe
    CLIENTE "1" --> "1..*" EXTRATO : consulta
    CLIENTE "1..*" --> "0..*" INVESTIMENTO : realiza
    EMPRESA "1..*" --> "0..*" INVESTIMENTO : recebe 
```
## :space_invader: Como executar o código
### Passos Iniciais
**1º PASSO:** Faça um *git clone* do projeto e abra-o preferencialmente no VSCode.

**2º PASSO:** Faça login ou crie uma conta no Supabase. Insira as informações recebidas ao criar a conta (SUPABASE_URL e SUPABASE_KEY) no arquivo `.env`. Isso permitirá que os dados sejam exibidos no seu perfil.

**3º PASSO:** Execute o código presente no arquivo `createTabelas.sql` no Supabase. Este script criará as tabelas necessárias para armazenar os dados.

**4º PASSO:** Execute o arquivo `main.py`. Assim, o código será iniciado e estará pronto para realizar as operações.

### Rodando o Banco

**1º PASSO:** Ao rodar o arquivo `main.py`, deverá aparecer no terminal a mensagem exibida na imagem abaixo. Assim que ela aparecer, escolha uma das opções.

<div align="center">
   <img src="https://github.com/user-attachments/assets/f0e9646f-71f6-4fdf-9f23-5df7a716d98c"/>
</div>
<br>

**2º PASSO:** É recomendado que, inicialmente, selecione a opção "Gerente", pois apenas o gerente pode criar contas. Após criar uma conta, o cliente poderá acessar e realizar as operações. Portanto, primeiro selecione a opção "Gerente". O menu seguinte será exibido:

<div align="center">
   <img src="https://github.com/user-attachments/assets/e8553b29-e4f8-4c4f-843c-b664859277cc"/>
</div>
<br>

**3º PASSO:** No primeiro acesso, é necessário cadastrar um gerente, pois o banco de dados ainda não possui clientes cadastrados. Para isso, selecione a opção "Cadastrar". Caso já exista um gerente cadastrado, este passo pode ser ignorado, e você pode realizar o login diretamente.

***IMPORTANTE:*** Para algumas operações, como cadastrar ou excluir um gerente no banco de dados, será necessário inserir a senha **15072023**.

<div align="center">
   <img src="https://github.com/user-attachments/assets/a629e141-a3e3-4872-8a7d-033abe30b458"/>
</div>
<br>

**4º PASSO:** Após cadastrar um gerente, faça login. Em seguida, será exibido o menu com as operações que o gerente pode realizar no banco. Lembre-se: apenas o gerente pode cadastrar contas. Antes de acessar a opção "Cliente" no menu principal, é necessário que o gerente tenha cadastrado um cliente no banco de dados.

<div align="center">
   <img src="https://github.com/user-attachments/assets/432ff0fa-f190-4685-9f0c-a7598588a716"/>
</div>
<br>

**5º PASSO:** Com uma conta criada, é possível acessar a opção "Cliente" no menu principal. A conta criada já estará salva no banco de dados, então, mesmo que o programa seja fechado e reaberto, não será necessário cadastrá-la novamente.

<div align="center">
   <img src="https://github.com/user-attachments/assets/896d3f15-b779-4018-b794-43202d1d6dd7"/>
</div>
<br>

**6º PASSO:** Ao retornar ao menu principal (saindo e escolhendo a opção "Cliente"), o sistema solicitará os dados do cliente cadastrados por um gerente. Se os dados estiverem corretos, o cliente poderá acessar o menu de operações da sua conta. Após o login, não será necessário inserir CPF e senha novamente para realizar outras operações.

<div align="center">
   <img src="https://github.com/user-attachments/assets/df037694-d3f8-4953-b8ad-80ef23090010"/>
</div>
<br>

### Realizando Querys
**1ºPASSO:** Selecione o arquivo `query.sql` e execute query por query no Supabase. As queries estão numeradas, e ao lado do número há a descrição do que cada uma faz.

## :busts_in_silhouette: Desenvolvedores
| [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/e6827fd1-d8fe-4740-b6fc-fbbfccd05752" width=115><br><sub>Mariah Santos Gomes</sub>](https://github.com/Mariah-Gomes) | [<img loading="lazy" src="https://github.com/Mariah-Gomes/ProjetoCompMovel1/assets/141663285/66d7e656-b9e4-43b7-94fa-931b736df881" width=115><br><sub>Iago Rosa de Oliveira</sub>](https://github.com/iagorosa28) |
| :---: | :---: |

### Dados dos Desenvolvedores
Iago Rosa de Oliveira R.A.: 22.224.027-7

Mariah Santos Gomes R.A.: 22.224.026-8
