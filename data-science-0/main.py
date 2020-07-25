#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[3]:


def q1():
    return (black_friday.shape)


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[4]:


def q2():# corrigir esse, ele está errado
    df_mulheres = black_friday[(black_friday['Gender'] =='F') & (black_friday['Age']== '26-35')] #crio um novo df apenas com mulheres na faixa de idade solicitada 
    return(len(df_mulheres['User_ID'])) #retorna a quantidade users_IDs


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[5]:


def q3():
    qtd_unicos = black_friday['User_ID'].unique() #variavel que irá gerar uma lista com os valores únicos da coluna User_id
    return(len(qtd_unicos))


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[6]:


def q4():
    return int(black_friday.dtypes.nunique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[7]:


def q5():
    return(black_friday[black_friday.isna().any(axis=1)== True].shape[0] / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[8]:


def q6():
    return((black_friday.isna().sum().sort_values(ascending=False)[0]).item()) #conta quantos NAs tem em cada coluna para depois retornao primeiro valor da resposta ordenada de forma decrescente


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[9]:


def q7():
    return(black_friday['Product_Category_3'].value_counts().index[0])


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[10]:


def q8():
    num = black_friday['Purchase']-black_friday['Purchase'].min()  # númerador da normalização
    den = black_friday['Purchase'].max()-black_friday['Purchase'].min() # denomidaor da normalizalização
    normalizado = num/den # coluna normalizada
    return(float(normalizado.mean())) #retorna a média


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[11]:


def q9():
    # Retorne aqui o resultado da questão 9.
    num = black_friday['Purchase']-black_friday['Purchase'].min() #passo da normalização ver questão 8
    den = black_friday['Purchase'].max()-black_friday['Purchase'].min() #passo da normalização ver questão 8
    normalizado = num/den #passo da normalização ver questão 8
    black_friday['Purchase_N'] = normalizado #cria a coluna normalizada
    padronizado = (black_friday['Purchase_N']-black_friday['Purchase_N'].mean())/black_friday['Purchase_N'].std()# pego o valor normalizado subtraio a média e então divido o resultado pelo desvio padrão
    black_friday['Purchase_P'] = padronizado #crio a coluna padronizada
    r = black_friday[(black_friday['Purchase_P']>=-1) & (black_friday['Purchase_P']<=1)].shape[0]
    return(r)


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[12]:


def q10():
    a = black_friday[black_friday['Product_Category_2'].isna()] #df de apoio apenas com o NAs na categoria 2
    b = a[a['Product_Category_3'].isna()] # dentro do df de apoio eu crio um novo df que apresentam NA na categoria 3
    return(bool(a.shape==b.shape)) # se o formato dos 2 dfs forem iguais então todas as observações na categoria 2 também será na categoria 3

