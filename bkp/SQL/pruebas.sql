-- Leyenda: B - Bueno, M - Malo.

-- Probando la tabla actividad.
-- Resultados: MMBM.

INSERT INTO actividad VALUES('Cernir', '00000');
INSERT INTO actividad VALUES('Cernir', '');
INSERT INTO actividad VALUES('Cernir', '10100');
INSERT INTO actividad VALUES('Cernir', '10101');

-- Probando la tabla agrupación.
-- Resultados: BM.
INSERT INTO agrupacion VALUES('Grupo de Inteligencia Artificial.');
INSERT INTO agrupacion VALUES('Grupo de Inteligencia Artificial.');

-- Probando la tabla carrera.
-- Resultados: BMM.
INSERT INTO carrera VALUES('0800', 'Ingeniería de la Computación');
INSERT INTO carrera VALUES('0800', 'Ingeniería Electrónica');
INSERT INTO carrera VALUES('0100', 'Ingeniería de la Computación');

-- Probando la tabla usuario.
-- Resultados: B.
INSERT INTO usuario VALUES(18837952, '0639609', 'cambiame', 'David Eleazar', 'Gómez Cermeño', 'davisito89@gmail.com', '02125411327', NULL, 0, 0, 'Activo', 'Estudiante', NOW(), NULL, 'Caracas', '0800', NULL, NULL);
