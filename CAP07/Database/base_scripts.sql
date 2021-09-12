# nome_atividade,tipo,duracao,id=None
Create Table if not exists webschema.atividade (
id serial Not NULL Primary Key,
nome_atividade VARCHAR(20),
tipo Varchar(10),
duracao int
)

# nome_aparelho,id=None
Create table if NOT EXISTS webschema.aparelho (
id SMALLSERIAL NOT NULL Primary Key ,
nome_aparelho Varchar(20)
)

# nome,sobrenome,data_nascimento,id=None
CREATE TABLE IF NOT EXISTS webschema.membro (
id serial NOT NULL Primary KEY ,
nome Varchar(15) NOT NULL,
sobrenome VArchar(25) NOT NULL,
data_nascimento date NOT NULL
)
 
# nome,sobrenome,data_nascimento,id=None
CREATE TABLE IF NOT EXISTS webschema.instrutor(
id SMALLSERIAL NOT NULL PRIMARY KEY ,
nome VArchar(15) NOT NULL,
sobrenome VArchar(25) NOT NULL,
data_nascimento date NOT NULL
)

# data,instrutor,atividade,perfil,id=None
Create TABLE if NOT EXISTS webschema.agendamento(
id serial NOT NULL PRIMARY KEY ,
data date NOT NULL,
instrutor int REFERENCES webschema.instrutor(id),
atividade int REFERENCES webschema.atividade(id),
perfil int REFERENCES webschema.membro(id)
)

