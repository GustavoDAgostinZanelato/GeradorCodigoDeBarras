# 📦 Gerador de Códigos de Barras (EAN-13)

Este projeto em Python gera automaticamente códigos de barras no padrão **EAN-13** e os salva como imagens `.png` em uma pasta chamada **Códigos de Barras**.

---

## 🛠️ Requisitos

- Python 3.10+
- `venv` (ambiente virtual)
- Bibliotecas:
  - `python-barcode`
  - `Pillow`

---

## ⚙️ Como configurar o projeto

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/seu-usuario/gerador-codigos-barra.git
cd gerador-codigos-barra
```

### 2. Crie e ative o ambiente virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar (Windows)
.venv\Scripts\ctivate
```

### 3. Instale as dependências

```bash
pip install python-barcode pillow
```

---

## ▶️ Como executar o script

Com o ambiente virtual ativado, execute:

```bash
python codigoDeBarras.py
```

O código irá gerar um número aleatório válido no padrão EAN-13, criar a imagem correspondente do código de barras e salvá-la automaticamente na pasta:

```
Códigos de Barras/
```

O nome do arquivo será `cb_<numero_gerado>.png`.

---

## 📄 Licença

Este projeto é livre para uso acadêmico e educacional.
