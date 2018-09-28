CREATE TABLE tipo_sangre(
  id NUMBER(2, 0) NOT NULL,
  tp_abo VARCHAR2(8) NOT NULL,
  tp_rh VARCHAR2(4) NOT NULL,
  CONSTRAINT pk_tipo_sangre
     PRIMARY KEY(id)
);

CREATE TABLE persona(
  id NUMBER(10, 0) NOT NULL,
  nombre VARCHAR2(40) NOT NULL,
  apellido VARCHAR2(40) NOT NULL,
  documento VARCHAR2(20) NOT NULL,
  tipo_sangre_id NUMBER(2, 0) NOT NULL,
  fe_nac DATE NOT NULL,
  tel VARCHAR2(20),
  email VARCHAR2(40),
  CONSTRAINT pk_persona
     PRIMARY KEY(id),
  CONSTRAINT fk_tipo_sangre
     FOREIGN KEY(tipo_sangre_id)
  REFERENCES tipo_sangre(id)
);

CREATE TABLE tipo_donacion(
  id NUMBER(2, 0) NOT NULL,
  nombre VARCHAR2(60) NOT NULL,
  dias_expiracion NUMBER(6, 0) NOT NULL,
  CONSTRAINT pk_tipo_donacion
     PRIMARY KEY(id)
);

CREATE TABLE banco_sangre(
  id NUMBER(10, 0) NOT NULL,
  persona_id NUMBER(10, 0) NOT NULL,
  tipo_donacion_id NUMBER(2, 0) NOT NULL,
  cantidad_en_ml NUMBER(6, 2) NOT NULL,
  fe_donacion DATE NOT NULL,
  fe_expiracion DATE NOT NULL,
  CONSTRAINT pk_banco_sangre
     PRIMARY KEY(id),
  CONSTRAINT fk_persona
     FOREIGN KEY(persona_id)
  REFERENCES persona(id),
  CONSTRAINT fk_tipo_donacion
     FOREIGN KEY(tipo_donacion_id)
  REFERENCES tipo_donacion(id)
);

INSERT ALL
  INTO tipo_sangre VALUES(1, 'A', '+')
  INTO tipo_sangre VALUES(2, 'A', '-')
  INTO tipo_sangre VALUES(3, 'B', '+')
  INTO tipo_sangre VALUES(4, 'B', '-')
  INTO tipo_sangre VALUES(5, 'AB', '+')
  INTO tipo_sangre VALUES(6, 'AB', '-')
  INTO tipo_sangre VALUES(7, 'O', '+')
  INTO tipo_sangre VALUES(8, 'O', '-')
SELECT 1 FROM DUAL;

INSERT ALL
  INTO tipo_donacion VALUES(1, 'Sangre Total', 35)
  INTO tipo_donacion VALUES(2, 'Glóbulos Rojos', 42)
  INTO tipo_donacion VALUES(3, 'Plaquetas', 5)
  INTO tipo_donacion VALUES(4, 'Plasma', 365)
  INTO tipo_donacion VALUES(5, 'Granulocitos', 1)
SELECT 1 FROM DUAL;

INSERT ALL
  INTO persona VALUES(1, 'Domitilla', 'Hofmann', '217087853', 1, TO_DATE('1973-10-03', 'YYYY-MM-DD'), '(276) 869-1565', 'Domitilla.Hofmann@email.com')
  INTO persona VALUES(2, 'Hanako', 'Harden', '494718245', 6, TO_DATE('1987-09-12', 'YYYY-MM-DD'), '(597) 316-6491', 'Hanako.Harden@email.com')
  INTO persona VALUES(3, 'Ladislav', 'Wronski', '192989024', 5, TO_DATE('1987-12-06', 'YYYY-MM-DD'), NULL, 'Ladislav.Wronski@email.com')
  INTO persona VALUES(4, 'Tewodros', 'Blanchet', '021436091', 4, TO_DATE('1990-07-29', 'YYYY-MM-DD'), NULL, 'Tewodros.Blanchet@email.com')
  INTO persona VALUES(5, 'Ra', 'Akkerman', '432545201', 3, TO_DATE('2000-12-31', 'YYYY-MM-DD'), '(788) 668-2673', NULL)
SELECT 1 FROM DUAL;

INSERT ALL
INTO banco_sangre VALUES(1, 1, 5, 321, TO_DATE('2018-06-30', 'YYYY-MM-DD'), TO_DATE('2018-07-01', 'YYYY-MM-DD'))
INTO banco_sangre VALUES(2, 3, 4, 400, TO_DATE('2018-08-01', 'YYYY-MM-DD'), TO_DATE('2019-08-01', 'YYYY-MM-DD'))
INTO banco_sangre VALUES(3, 5, 3, 367, TO_DATE('2018-08-11', 'YYYY-MM-DD'), TO_DATE('2018-08-16', 'YYYY-MM-DD'))
INTO banco_sangre VALUES(4, 5, 2, 330, TO_DATE('2018-08-29', 'YYYY-MM-DD'), TO_DATE('2018-10-10', 'YYYY-MM-DD'))
INTO banco_sangre VALUES(5, 4, 5, 479, TO_DATE('2018-09-03', 'YYYY-MM-DD'), TO_DATE('2018-09-04', 'YYYY-MM-DD'))
SELECT 1 FROM DUAL;