-- Atividades

INSERT INTO webschema.atividades (nome_atividade,tipo,duracao_minutos) VALUES ('Zumba','Dança',40);
INSERT INTO webschema.atividades (nome_atividade,tipo,duracao_minutos) VALUES ('Boxe','Luta',50);
INSERT INTO webschema.atividades (nome_atividade,tipo,duracao_minutos) VALUES ('Bicicleta','Força',120);

-- Nome do Aparelho

INSERT INTO webschema.aparelho (nome_aparelho) VALUES ('Bicicleta');
INSERT INTO webschema.aparelho (nome_aparelho) VALUES ('Pula Pula');
INSERT INTO webschema.aparelho (nome_aparelho) VALUES ('Caixa de Som');

-- Membro

INSERT INTO webschema.membro (nome,sobrenome,data_nascimento,ativo) VALUES ('Claudio','Peres', '1994-08-25',0);
INSERT INTO webschema.membro (nome,sobrenome,data_nascimento,ativo) VALUES ('Henrique','Ferreira','1990-12-25',1);
INSERT INTO webschema.membro (nome,sobrenome,data_nascimento,ativo) VALUES ('Kaique','Viana','2002-09-24',1);

-- Instrutor

INSERT INTO webschema.instrutor (nome,sobrenome,data_nascimento) VALUES ('Claudio','Peres','1994-08-25');
INSERT INTO webschema.instrutor (nome,sobrenome,data_nascimento) VALUES ('Fabio','Silva','1991-08-25');
INSERT INTO webschema.instrutor (nome,sobrenome,data_nascimento) VALUES ('Ferreira','Pinto','2000-10-12');

-- Agendamento

INSERT INTO webschema.agendamento (data,instrutor,atividade,perfil) VALUES ('2021-10-29',2,8,3);
INSERT INTO webschema.agendamento (data,instrutor,atividade,perfil) VALUES ('2021-10-31',1,7,2);
INSERT INTO webschema.agendamento (data,instrutor,atividade,perfil) VALUES ('2021-10-27',3,9,1);
INSERT INTO webschema.agendamento (data,instrutor,atividade,perfil) VALUES ('2021-10-15',2,9,3);