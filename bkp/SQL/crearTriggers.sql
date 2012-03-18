-- Para poder usar los triggers es necesario crear el lenguaje plpgsql.

-- Trigger para la inserción o actualización de un usuario.
CREATE OR REPLACE FUNCTION validar_usuario() RETURNS TRIGGER AS $validar_usuario$
    DECLARE
        fecha_actual    DATE;
    BEGIN
        -- Se capitalizan los nombres y apellidos si no estaban capitalizados.
        NEW.nombres := initcap(NEW.nombres);
        NEW.apellidos := initcap(NEW.apellidos);

        -- La fecha de inicio debe ser menor o igual a la fecha actual.
        -- Igualmente la fecha fin, si es diferente de NULL.
        fecha_actual := NOW();
        IF (NEW.fecha_inicio > fecha_actual) THEN
            RAISE EXCEPTION 'La fecha de inicio del usuario: % debe ser menor o igual a la actual: %.', NEW.fecha, fecha_actual;
        END IF;

        IF (NEW.fecha_fin != NULL AND NEW.fecha_fin > fecha_actual) THEN
            RAISE EXCEPTION 'La fecha fin del usuario: % debe ser menor o igual a la actual: %.', NEW.fecha, fecha_actual;
        END IF;
    END;
$validar_usuario$ LANGUAGE plpgsql;

-- Trigger para la inserción o actualización de una jornada.
-- select * from mytable where mycolumn ~* 'regexp'

CREATE OR REPLACE FUNCTION validar_jornada() RETURNS TRIGGER AS $validar_jornada$
    DECLARE
        a                   SMALLINT;
        b                   SMALLINT;
        diferencia_horas    SMALLINT;
        diferencia_minutos  SMALLINT;
        hora_inicio_otro    TIME;
        hora_fin_otro       TIME;
        fecha_actual        DATE;
    BEGIN
        -- La fecha de la jornada debe ser menor o igual a la actual.
        fecha_actual := NOW();
        IF (NEW.fecha > fecha_actual) THEN
            RAISE EXCEPTION 'La fecha la jornada: % debe ser menor o igual a la fecha actual: %.', NEW.fecha_inicio, fecha_actual;
        END IF;

        -- No deben haber dos jornadas cuyos intervalos de tiempo se solapen.
        SELECT hora_inicio, hora_fin INTO hora_inicio_otro, hora_fin_otro
            FROM jornada
            WHERE   fecha = NEW.fecha
                    AND identificador != NEW.identificador
                    AND (   (NEW.hora_inicio >= hora_inicio
                                AND NEW.hora_inicio < hora_fin)
                            OR (NEW.hora_fin >= hora_inicio
                                AND NEW.hora_fin < hora_fin)
                            OR (hora_inicio >= NEW.hora_inicio
                                AND hora_inicio < NEW.hora_fin)
                            OR (hora_fin >= NEW.hora_inicio
                                AND hora_fin < NEW.hora_fin))
            LIMIT 1;
        IF FOUND THEN
            RAISE EXCEPTION 'Existe una jornada comprendida entre % y % que se solapa con la que se acaba de ingresar o modificar.', hora_inicio_otro, hora_fin_otro;
        END IF;

        -- Se calcula el tiempo destinado a la jornada.
        a := EXTRACT(HOUR FROM NEW.hora_fin);
        b := EXTRACT(HOUR FROM NEW.hora_inicio);
        diferencia_horas := a - b;

        a := EXTRACT(MINUTE FROM NEW.hora_fin);
        b := EXTRACT(MINUTE FROM NEW.hora_inicio);
        diferencia_minutos := a - b;

        NEW.minutos := diferencia_horas * 60 + diferencia_minutos;

        RETURN NEW;
    END;
$validar_jornada$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_validar_jornada
    BEFORE INSERT OR UPDATE ON jornada
    FOR EACH ROW EXECUTE PROCEDURE validar_jornada();
