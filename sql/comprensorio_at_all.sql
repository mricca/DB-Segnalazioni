--
-- TOC entry 3165 (class 0 OID 72402)
-- Dependencies: 205
-- Data for Name: comprensorio; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO comprensorio (id, text) VALUES ('01', 'Toscana Sud');
INSERT INTO comprensorio (id, text) VALUES ('02', 'Toscana Nord');
INSERT INTO comprensorio (id, text) VALUES ('03', 'Alto Valdarno');
INSERT INTO comprensorio (id, text) VALUES ('04', 'Medio Valdarno');
INSERT INTO comprensorio (id, text) VALUES ('05', 'Basso Valdarno');
INSERT INTO comprensorio (id, text) VALUES ('06', 'Toscana Costa');


--
-- TOC entry 3166 (class 0 OID 72407)
-- Dependencies: 206
-- Data for Name: fenomeno; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO fenomeno (id, text) VALUES ('01', 'Idraulica');
INSERT INTO fenomeno (id, text) VALUES ('02', 'Frana');
INSERT INTO fenomeno (id, text) VALUES ('03', 'Idraulica e Frana');


--
-- TOC entry 3167 (class 0 OID 72412)
-- Dependencies: 207
-- Data for Name: studio_intervento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO studio_intervento (id, text) VALUES ('01', 'STUDIO');
INSERT INTO studio_intervento (id, text) VALUES ('02', 'INTERVENTO');


--
-- TOC entry 3168 (class 0 OID 72422)
-- Dependencies: 208
-- Data for Name: tipo_opera; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO tipo_opera (id, text) VALUES ('01', 'Argine');
INSERT INTO tipo_opera (id, text) VALUES ('02', 'Cassa di espansione');
INSERT INTO tipo_opera (id, text) VALUES ('03', 'Laghetto collinare');
INSERT INTO tipo_opera (id, text) VALUES ('04', 'Canale Scolmatore');
INSERT INTO tipo_opera (id, text) VALUES ('05', 'Canali di bonifica');
INSERT INTO tipo_opera (id, text) VALUES ('06', 'Briglia');
INSERT INTO tipo_opera (id, text) VALUES ('07', 'Briglia selettiva');
INSERT INTO tipo_opera (id, text) VALUES ('08', 'Soglia');
INSERT INTO tipo_opera (id, text) VALUES ('09', 'Cunettoni');
INSERT INTO tipo_opera (id, text) VALUES ('10', 'Protezione di sponda');
INSERT INTO tipo_opera (id, text) VALUES ('11', 'Rivestimento');
INSERT INTO tipo_opera (id, text) VALUES ('12', 'Presidio al piede di sponda');
INSERT INTO tipo_opera (id, text) VALUES ('13', 'Opera contro colate di detriti e fango');
INSERT INTO tipo_opera (id, text) VALUES ('14', 'Movimenti di terra');
INSERT INTO tipo_opera (id, text) VALUES ('15', 'Drenaggio');
INSERT INTO tipo_opera (id, text) VALUES ('16', 'Sistemazioni idraulico-forestali');
INSERT INTO tipo_opera (id, text) VALUES ('17', 'Sostegno');
INSERT INTO tipo_opera (id, text) VALUES ('18', 'Protezione');
INSERT INTO tipo_opera (id, text) VALUES ('19', 'Altro (specificare nel campo successivo)');


--
-- TOC entry 3169 (class 0 OID 72610)
-- Dependencies: 218
-- Data for Name: tipologia_intervento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO tipologia_intervento (id, text) VALUES ('01', 'Nuova Realizzazione');
INSERT INTO tipologia_intervento (id, text) VALUES ('02', 'Manutenzione Ordinaria');
INSERT INTO tipologia_intervento (id, text) VALUES ('03', 'Manutenzione Straordinaria');


-- Completed on 2014-06-10 16:51:17

--
-- PostgreSQL database dump complete
--

