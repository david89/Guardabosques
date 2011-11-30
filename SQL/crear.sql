-- USE guardabosques;
-- Títulos o nombres: 50 caracteres.
-- Prefijo pk para primary key.
-- Prefijo un para unique.
-- Prefijo ck para check.
-- Prefijo fk para foreign key.

-- Tabla de la clase agrupacion.
CREATE TABLE agrupacion(
    nombre  VARCHAR(50) NOT NULL
);

-- Tabla de la clase carrera.
CREATE TABLE carrera (
    codigo  VARCHAR(4)  NOT NULL,
    nombre  VARCHAR(50) NOT NULL
);

-- Tabla de la clase usuario.
CREATE TABLE usuario (
    cedula                  VARCHAR(8)      NOT NULL,
    carne                   VARCHAR(8)      DEFAULT NULL,
    clave                   VARCHAR(64)     NOT NULL,
    nombres                 VARCHAR(50)     NOT NULL,
    apellidos               VARCHAR(50)     NOT NULL,
    correo                  VARCHAR(50)     NOT NULL,
    telefono_principal      VARCHAR(11)     NOT NULL,
    telefono_opcional       VARCHAR(11)     DEFAULT '',
    horas_laboradas         SMALLINT        NOT NULL    DEFAULT 0,
    horas_aprobadas         SMALLINT        NOT NULL    DEFAULT 0,
    estado                  VARCHAR(8)      NOT NULL,
    tipo                    VARCHAR(11)     NOT NULL,
    fecha_inicio            DATE            NOT NULL,
    fecha_fin               DATE            DEFAULT NULL,
    zona                    VARCHAR(50)     DEFAULT '',
    codigo_carrera          VARCHAR(4),
    limitaciones_fisicas    TEXT            DEFAULT '',
    limitaciones_medicas    TEXT            DEFAULT ''
);

-- Tabla de la clase jornada.
CREATE TABLE jornada (
    identificador   SERIAL          NOT NULL,
    cedula_usuario  VARCHAR(8)      NOT NULL,
    fecha           DATE            NOT NULL,
    estado          VARCHAR(9)      NOT NULL,
    minutos         SMALLINT        NOT NULL,
    multiplicador   NUMERIC(4,1)    NOT NULL    DEFAULT 1.0
);

-- Tabla de la clase actividad.
CREATE TABLE actividad (
    nombre          VARCHAR(50) NOT NULL,
    descripcion     TEXT        DEFAULT '',
    objetivos       BIT(5)      NOT NULL    DEFAULT '11111'
);

-- Tabla de la clase otro servicio.
CREATE TABLE otro_servicio (
    nombre  VARCHAR(50) NOT NULL
);

-- Tabla de la asociación pertenece.
CREATE TABLE pertenece (
    identificador       SERIAL      NOT NULL,
    cedula_usuario      VARCHAR(8)  NOT NULL,
    nombre_agrupacion   VARCHAR(50) NOT NULL
);

-- Tabla de la asociación constituida_por.
CREATE TABLE constituida_por (
    identificador           SERIAL      NOT NULL,
    nombre_actividad        VARCHAR(50) NOT NULL,
    identificador_jornada   SERIAL      NOT NULL,
    fecha_inicio            DATE        NOT NULL,
    fecha_fin               DATE        NOT NULL,
    descripcion             TEXT        NOT NULL
);

-- Tabla de la asociación hizo.
CREATE TABLE hizo (
    identificador           SERIAL      NOT NULL,
    horas                   SMALLINT    NOT NULL,
    cedula_usuario          VARCHAR(8)  NOT NULL,
    nombre_otro_servicio    VARCHAR(50) NOT NULL
);

-- Restricciones de la tabla agrupacion.
ALTER TABLE agrupacion
    ADD CONSTRAINT pk_agrupacion
    PRIMARY KEY(nombre);

-- Restricciones de la tabla carrera.
ALTER TABLE carrera
    ADD CONSTRAINT pk_carrera
    PRIMARY KEY(codigo);
ALTER TABLE carrera
    ADD CONSTRAINT un_carrera1
    UNIQUE(nombre);

-- Restricciones de la tabla usuario.
ALTER TABLE usuario
    ADD CONSTRAINT pk_usuario
    PRIMARY KEY(cedula);
ALTER TABLE usuario
    ADD CONSTRAINT un_usuario1
    UNIQUE(carne);
ALTER TABLE usuario
    ADD CONSTRAINT un_usuario2
    UNIQUE(correo);
ALTER TABLE usuario
    ADD CONSTRAINT ck_usuario1
    CHECK(horas_aprobadas >= 0 AND horas_laboradas >= horas_aprobadas);
ALTER TABLE usuario
    ADD CONSTRAINT ck_usuario2
    CHECK(estado IN ('Inactivo', 'Activo'));
ALTER TABLE usuario
    ADD CONSTRAINT ck_usuario3
    CHECK(tipo IN ('Estudiante', 'Coordinador'));
ALTER TABLE usuario
    ADD CONSTRAINT fk_usuario__carrera
    FOREIGN KEY(codigo_carrera) REFERENCES carrera(codigo);

-- Restricciones de la tabla jornada.
ALTER TABLE jornada
    ADD CONSTRAINT pk_jornada
    PRIMARY KEY(identificador);
ALTER TABLE jornada
    ADD CONSTRAINT un_jornada1
    UNIQUE(cedula_usuario, fecha);
ALTER TABLE jornada
    ADD CONSTRAINT ck_jornada1
    CHECK(estado IN ('Pendiente', 'Aprobada', 'Rechazada'));
ALTER TABLE jornada
    ADD CONSTRAINT ck_jornada2
    CHECK(minutos BETWEEN 1 and 1440);
ALTER TABLE jornada
    ADD CONSTRAINT ck_jornada3
    CHECK(multiplicador BETWEEN 1.0 and 120.0);
ALTER TABLE jornada
    ADD CONSTRAINT fk_jornada__usuario
    FOREIGN KEY(cedula_usuario) REFERENCES usuario(cedula);

-- Restricciones de la tabla actividad.
ALTER TABLE actividad
    ADD CONSTRAINT pk_actividad
    PRIMARY KEY(nombre);
ALTER TABLE actividad
    ADD CONSTRAINT ck_actividad1
    CHECK(objetivos <> '00000');

-- Restricciones de la tabla otro_servicio.
ALTER TABLE otro_servicio
    ADD CONSTRAINT pk_otro_servicio
    PRIMARY KEY(nombre);

-- Restricciones de la tabla pertenece.
ALTER TABLE pertenece
    ADD CONSTRAINT pk_pertenece
    PRIMARY KEY(identificador);
ALTER TABLE pertenece
    ADD CONSTRAINT fk_pertenece__usuario
    FOREIGN KEY(cedula_usuario) REFERENCES usuario(cedula);
ALTER TABLE pertenece
    ADD CONSTRAINT fk_pertenece__agrupacion
    FOREIGN KEY(nombre_agrupacion) REFERENCES agrupacion(nombre);

-- Restricciones de la tabla constituida_por.
ALTER TABLE constituida_por
    ADD CONSTRAINT pk_constituida_por
    PRIMARY KEY(identificador);
ALTER TABLE constituida_por
    ADD CONSTRAINT un_constituida_por1
    UNIQUE(nombre_actividad, identificador_jornada, fecha_inicio);
ALTER TABLE constituida_por
    ADD CONSTRAINT ck_constituida_por2
    CHECK(fecha_inicio < fecha_fin);
ALTER TABLE constituida_por
    ADD CONSTRAINT fk_constituida_por__actividad
    FOREIGN KEY(nombre_actividad) REFERENCES actividad(nombre);
ALTER TABLE constituida_por
    ADD CONSTRAINT fk_constituida_por__jornada
    FOREIGN KEY(identificador_jornada) REFERENCES jornada(identificador);

-- Restricciones de la tabla hizo.
ALTER TABLE hizo
    ADD CONSTRAINT pk_hizo
    PRIMARY KEY(identificador);
ALTER TABLE hizo
    ADD CONSTRAINT ck_hizo1
    CHECK(horas > 0);
ALTER TABLE hizo
    ADD CONSTRAINT fk_hizo__usuario
    FOREIGN KEY(cedula_usuario) REFERENCES usuario(cedula);
ALTER TABLE hizo
    ADD CONSTRAINT fk_hizo__otro_servicio
    FOREIGN KEY(nombre_otro_servicio) REFERENCES otro_servicio(nombre);

-- Notas de implementación:
-- 1) El atributo foto es equivalente a carnet con la extensión jpg o png.
-- 2) Se agregó un identificador serial a jornada porque en Django las clases
-- no pueden tener más de dos elementos que conformen la clave primaria.
-- 3) Se agregó cedula_usuario a jornada porque cada jornada es realizada
-- exclusivamente por un sólo usuario.
-- 4) Poner una mejor cota superior en ck_jornada2. La actual es 24 * 60.
-- 5) Los objetivos de las actividades se mantuvieron como arreglos binarios
-- (como en el modelo pasado).
