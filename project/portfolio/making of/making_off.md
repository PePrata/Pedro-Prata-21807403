# Making Off – Modelação Django do Portfólio

## 1. Ponto de Partida: O Esboço Inicial

O processo começou com um esboço em papel (ver imagem de referência) que identificou as entidades principais do sistema:

- **Licenciatura** – com campos ID, Cadeiras, Descrição e TFCs 
  - **ID** - serve para identificar diferentes Licenciaturas
  - **Cadeiras** - identifica as cadeiras que pertencem a cada Licenciatura
  - **Descrição** - descreve os conhecimentos obtidos pela Licenciatura
  - **TFCs** - indica TFCs de inspiração relacionados com a Licenciatura
- **Cadeira** – com ID, Nome, Ano, Descrição, Docentes, Projeto e Tecnologias
  - **ID** - identifica diferentes cadeiras
  - **Nome** - nome da cadeira
  - **Ano** - Ano da cadeira (1º,2º ou 3º)
  - **Descrição** - Descrição da cadeira, os seus objetivos
  - **Docentes** - Docentes envolvidos no ensino da cadeira
  - **Projeto** - Projeto final desenvolvido na cadeira
  - **Tecnologias** - Tecnologias usadas/aprendidas na cadeira
- **Projeto** – com nome, descrição, link e tecnologias
  - **nome** - nome do projeto
  - **descrição** - descrição do projeto
  - **link** - link se existir para aceder ao projeto
  - **tecnologias** - tecnologias envolvidas no desenvolvimento do projeto
- **TFC** – com título, autor, supervisor, degree, resumo, link e download
  - **titulo** - Titulo do TFC 
  - **autor** - Autor do TFC
  - **supervisor** - Supervisor a apoiar desenvolvimento do TFC
  - **degree** - Grau do Autor (Licenciatura, Mestrado, Doutoramento)
  - **resumo** - Resumo do TFC
  - **link** - Link para página que contem o TFC
  - **download** - Download do TFC
- **Tecnologias** – com nome, logotipo, link e descrição
  - **nome** - nome da tecnologia
  - **logotipo** - imagem do logotipo da tecnologia
  - **link** - link para pagina oficial da tecnologia
  - **descrição** - descrição da tecnologia seu uso, nivel, curiosidades, etc.
- **Docente** – com ID, nome e linkedin
  - **ID** - Para identificar diferentes Docentes (ordem de elementos da Classe)
  - **nome** - Nome do Docente
  - **linkedin** - link de Linkedin se existir
- **Formação** – com nome, descrição, certificado e link
  - **nome** - nome da formação em questão
  - **descrição** - descrição da formação
  - **certificado** - imagem de certificado de formação
  - **link** - link para pagina de formação
- **Competências** – entidade que apenas ligava Licenciaturas, Formações e Tecnologias

A navegação era suposto estar baseada nas **Competencias**, estas estando ligadas a licenciaturas, formações e tecnologias, sendo
possivel verificar quais os connhecimentos relevantes que se procuram no portefólio e projetos criados usando os mesmos partindo
de qualquer um dos 3.
(Tecnologias -> Projeto) (Licenciatura -> cadeira -> Tecnologia)

---

## 2. Decisões por Classe

### `Licenciatura`

**Esboço:** Tinha ID, Cadeiras, Descrição, TFCs.  
**Implementação final:**

```python
class Licenciatura(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
```

**Mudanças e justificações:**
- O campo `ID` foi removido como campo explícito — o Django gera automaticamente uma chave primária `id`.
- Os campos `Cadeiras` e `TFCs` não existem como campos diretos: são relações inversas (`related_name`) definidas nas classes `Cadeira` e `TFC` respetivamente, através de `ForeignKey`.

---

### `Tecnologia`

**Esboço:** Tinha nome, logotipo, link, descrição.  
**Implementação final:**

```python
class Tecnologia(models.Model):
    nome = models.CharField(max_length=255)
    logotipo = models.ImageField(upload_to='portfolio/fotos', null=True, blank=True)
    link = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
```

**Mudanças e justificações:**
- Mantida igual ao esboço.

---

### `Competências` → **Eliminada**

**Esboço:** Tinha ligação a Licenciaturas, Formações e Tecnologias.  
**Implementação final:** Não existe.

**Justificação:**
A entidade `Competências` foi eliminada porque as competências já estão representadas diretamente pelas `Tecnologias`. Criar uma tabela separada duplicaria informação sem trazer valor acrescentado. A relação `ManyToMany` de `Tecnologia` com `Cadeira`, `Projeto`, `Formação` e `TFC` cobre completamente o papel que `Competências` desempenharia.

---

### `Docente`

**Esboço:** Tinha ID, nome, linkedin.  
**Implementação final:**

```python
class Docente(models.Model):
    nome = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255, blank=True)
```

**Mudanças e justificações:**
- O campo `ID` é automático no Django.

---

### `Cadeira`

**Esboço:** Tinha ID, Nome, Ano, Descrição, Docentes (relação), Projeto (relação) e Tecnologias (relação).  
**Implementação final:**

```python
class Cadeira(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="cadeiras")
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    descricao = models.TextField(blank=True)
    docentes = models.ManyToManyField(Docente, related_name="cadeiras")
    tecnologias = models.ManyToManyField(Tecnologia, related_name="cadeiras", blank=True)
```

**Mudanças e justificações:**
- O campo `Projeto` não existe em `Cadeira` diretamente — é uma relação inversa definida em `Projeto` (`related_name="projetos"`).

---

### `Projeto`

**Esboço:** Tinha nome, descrição, link, tecnologias.  
**Implementação final:**

```python
class Projeto(models.Model):
    cadeira = models.ForeignKey(Cadeira, on_delete=models.CASCADE, related_name="projetos")
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link = models.TextField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="projetos", blank=True)
```

**Mudanças e justificações:**
- Adicionada `ForeignKey` para `Cadeira` — cada projeto pertence a uma cadeira específica.

---

### `Formacao`

**Esboço:** Tinha nome, descrição, certificado, link.  
**Implementação final:**

```python
class Formacao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    link = models.CharField(blank=True)
    data_conclusao = models.DateField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name="formacoes", blank=True)
```

**Mudanças e justificações:**
- O campo `certificado` do esboço foi **eliminado** — após pensar mais sobre o assunto pensei perigoso espore o mesmo de tal forma.
- Foi adicionado `data_conclusao` (`DateField`) para permitir ordenação cronológica das formações, campo ausente no esboço.
- Adicionada relação `ManyToMany` com `Tecnologia` para registar as tecnologias abordadas em cada formação.

---

### `AreaTematica` → **Nova entidade (não estava no esboço)**

**Implementação final:**

```python
class AreaTematica(models.Model):
    nome = models.CharField(max_length=255, unique=True)
```

**Justificação:**
Esta classe não existia no esboço inicial. Foi criada para permitir categorizar os TFCs por área temática (ex: Inteligência Artificial, Redes, Desenvolvimento Web) para mais facilmente localizar TFCs relevantes. O campo `unique=True` garante que não existem duplicados. A relação com `TFC` é `ManyToMany`, pois um TFC pode abranger várias áreas e uma área pode ter vários TFCs.

---

### `TFC`

**Esboço:** Tinha título, autor, supervisor, degree, resumo, link, download e ligação a tecnologias.  
**Implementação final:**

```python
class TFC(models.Model):
    GRAU_CHOICES = [
        ("licenciatura", "Licenciatura"),
        ("mestrado", "Mestrado"),
        ("doutoramento", "Doutoramento"),
    ]
    DESTAQUE_CHOICES = [
        (0, "Normal"),
        (1, "Interessante"),
        (2, "Muito Interessante"),
        (3, "Destaque"),
    ]
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name="tfcs")
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    email_autor = models.EmailField(blank=True)
    supervisor = models.CharField(max_length=255)
    grau = models.CharField(max_length=50, choices=GRAU_CHOICES, default="mestrado")
    ano = models.PositiveSmallIntegerField(null=True, blank=True)
    resumo = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    link = models.URLField(blank=True)
    download = models.URLField(blank=True)
    destaque = models.PositiveSmallIntegerField(choices=DESTAQUE_CHOICES, default=0)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="tfcs", blank=True)
    areas = models.ManyToManyField(AreaTematica, related_name="tfcs", blank=True)
```

**Mudanças e justificações:**
- `degree` do esboço foi renomeado para `grau` e implementado com `choices` (`licenciatura`, `mestrado`, `doutoramento`) para garantir valores válidos e facilitar filtragem.
- Informação em falta adicionada:
    - Adicionado `email_autor` (`EmailField`).
    - Adicionado `ano`.
    - Adicionado `keywords`.
    - Adicionado `destaque` com `choices` numéricos (0–3) para permitir destacar TFCs relevantes.
- Adicionada relação `ManyToMany` com `AreaTematica` (nova entidade, ver acima).

---

## 3. Configuração do Admin

O ficheiro `admin.py` foi configurado para tornar a gestão de conteúdo eficiente:

- **`list_display`** – mostra os campos mais relevantes em cada listagem, evitando ter de abrir cada registo.
- **`search_fields`** – permite pesquisa por texto nos campos mais importantes (nome, título, autor, etc.).
- **`list_filter`** – facilita filtragem lateral por campos como grau, ano, cadeira ou tecnologia.
- **Métodos auxiliares** (`listar_tecnologias`, `listar_docentes`, `listar_areas`) – convertem relações `ManyToMany` em strings legíveis para o `list_display`, já que o Django não suporta ManyToMany diretamente nessa configuração.

---

## 4. Modelação Final – 

