-- ============================================================
-- DQL - Consultas
-- ============================================================

-- 1) Listar todos os cursos
SELECT nome_curso 
FROM Curso;

-- 2) Listar todos os alunos
SELECT nome_aluno 
FROM Aluno;

-- 3) Listar todas as disciplinas
SELECT nome_disciplina 
FROM Disciplina;

-- 4) Listar todos os professores
SELECT nome_professor 
FROM Professor;

-- 5) Calcular o número total de alunos em cada curso
SELECT 
    curso.nome_curso,
    COUNT(aluno.id_aluno) AS total_alunos
FROM Curso AS curso
LEFT JOIN Aluno AS aluno
    ON aluno.id_curso = curso.id_curso
GROUP BY 
    curso.id_curso,
    curso.nome_curso;

-- 6) Listar todos os cursos oferecidos na escola, com sua duração e o nome do coordenador
SELECT
    curso.nome_curso,
    curso.duracao,
    professor.nome_professor AS nome_coordenador
FROM Curso AS curso
INNER JOIN Professor AS professor
    ON curso.coordenador = professor.id_professor;

-- 7) Obter a lista de alunos matriculados em um curso específico
SELECT 
    aluno.nome_aluno,
    aluno.id_curso
FROM Aluno AS aluno
INNER JOIN Curso AS curso 
    ON aluno.id_curso = curso.id_curso
WHERE curso.nome_curso = 'Direito';

-- 8) Obter a média salarial dos professores por departamento
SELECT 
    departamento,
    AVG(salario) AS media_salarial
FROM Professor
GROUP BY departamento;
