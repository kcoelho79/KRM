# KRM

CRM - para Coworking

## Infraestrutura

Django tem tanto a parte Backend e frontend, e ocpcional de extenção API para integração com VUE ou outro frontend reativo, para melhor experiência como Kanban, entre outro

KRM
-- backend (Django)
-- krm (aplicação principal, gestão dos contatos)
-- api (simples - api para integração com o FrontEnd)
-- frontend (VUE)


## Auth
https://docs.djangoproject.com/en/5.0/topics/auth/default/#module-django.contrib.auth.forms

## TODO

[x] Aplicatico contato CRUD, gravaçao Banco
[] autenticação usuário web
    [] enviar e-mail confirmar
    [] trocar senha
    [] reset senha
[] inbound contato via Web Form
[] menu Kanban Bootstrap no django
[] inbound contato form site
[] merge com o projeto kanban
[] integração API krm com kanban VUE
[] autenticação API
[] notificação websocket com kanban VUE
[] validação automatica contato
[] enviar mensagem via whatsAPP (projeto AllWhatsAPP)
[] automação com GitHub - com container
[] migração para POstgres
[] criar ambiente env
[] ambiente docker, por que não
