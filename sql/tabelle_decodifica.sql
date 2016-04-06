--
-- TOC entry 3144 (class 0 OID 70492)
-- Dependencies: 208
-- Data for Name: cantierabilita; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO cantierabilita (id, text, value) VALUES ('01', 'Nessuna documentazione', 0);
INSERT INTO cantierabilita (id, text, value) VALUES ('02', 'Studio di fattibilita-indagini preliminari', 0);
INSERT INTO cantierabilita (id, text, value) VALUES ('03', 'Progetto preliminare approvato', 0);
INSERT INTO cantierabilita (id, text, value) VALUES ('04', 'Progetto definitivo approvato dopo conferenza dei servizi', 30);
INSERT INTO cantierabilita (id, text, value) VALUES ('05', 'Progetto esecutivo approvato (dopo cds se necessaria)', 50);
INSERT INTO cantierabilita (id, text, value) VALUES ('06', 'Somma Urgenza', 0);


--
-- TOC entry 3145 (class 0 OID 70497)
-- Dependencies: 209
-- Data for Name: efficacia; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO efficacia (id, text, value) VALUES ('01', 'Edifici lesionati e provvedim. di evacuazione', 40);
INSERT INTO efficacia (id, text, value) VALUES ('02', 'Edifici lesionati', 35);
INSERT INTO efficacia (id, text, value) VALUES ('03', 'Rischio diretto incolumita persone', 35);
INSERT INTO efficacia (id, text, value) VALUES ('04', 'Interruzione viabilita e isolamento nucleo abitato', 35);
INSERT INTO efficacia (id, text, value) VALUES ('05', 'Rischio danneggiamento edifici', 30);
INSERT INTO efficacia (id, text, value) VALUES ('06', 'Rischio interruzione viabilita e di isolamento nucleo abitato', 25);
INSERT INTO efficacia (id, text, value) VALUES ('07', 'Interruzione viabilita', 20);
INSERT INTO efficacia (id, text, value) VALUES ('08', 'Rischio interruzione viabilita', 15);
INSERT INTO efficacia (id, text, value) VALUES ('09', 'Casse di espansione-consolidamento argini per contenimento portata trentennale (area urbana/industriale)', 40);
INSERT INTO efficacia (id, text, value) VALUES ('10', 'Casse di espansione-consolidamento argini per contenimento portata trentennale (zone di campagna)', 35);
INSERT INTO efficacia (id, text, value) VALUES ('11', 'Adeguamento sezioni d''alveo area urbana-industriale', 35);
INSERT INTO efficacia (id, text, value) VALUES ('12', 'Sbarramenti-diversivi-scolmatori', 35);
INSERT INTO efficacia (id, text, value) VALUES ('13', 'Casse di espansione-consolidamento argini per contenimento portata TR >30 (area urbana-industriale)', 33);
INSERT INTO efficacia (id, text, value) VALUES ('14', 'Casse di espansione-consolidamento argini per contenimento portata TR>30 (zone di campagna)', 30);
INSERT INTO efficacia (id, text, value) VALUES ('15', 'Adeguamento sezioni d''alveo area campagna', 30);
INSERT INTO efficacia (id, text, value) VALUES ('16', 'Opere longitudinali,trasversali (difese di ponda, Briglie, traverse)', 30);
INSERT INTO efficacia (id, text, value) VALUES ('17', 'Riprofilatura sponde-ripristino officiosita idraulica-idrovore', 25);
INSERT INTO efficacia (id, text, value) VALUES ('18', 'Manutenzioni opere e annessi (cabine di manovra organi di presa,idrovore)', 23);
INSERT INTO efficacia (id, text, value) VALUES ('19', 'Tagli elettivi-manutenzioni straordinarie (attivita di bonifica)', 15);


--
-- TOC entry 3143 (class 0 OID 70487)
-- Dependencies: 207
-- Data for Name: finanziamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO finanziamento (id, text) VALUES ('01', 'Intervento');
INSERT INTO finanziamento (id, text) VALUES ('02', '2015');
INSERT INTO finanziamento (id, text) VALUES ('03', 'Studio');
INSERT INTO finanziamento (id, text) VALUES ('04', 'NO');


--
-- TOC entry 3142 (class 0 OID 70482)
-- Dependencies: 206
-- Data for Name: sostenibilita; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO sostenibilita (id, text, value) VALUES ('01', 'Ingegneria naturalistica + plurifunzionalita', 10);
INSERT INTO sostenibilita (id, text, value) VALUES ('02', 'Solo ingegneria naturalistica', 8);
INSERT INTO sostenibilita (id, text, value) VALUES ('03', 'Plurifunzionalita senza ingegneria naturale', 8);
INSERT INTO sostenibilita (id, text, value) VALUES ('04', 'Parziale ingegneria naturale', 4);
INSERT INTO sostenibilita (id, text, value) VALUES ('05', 'Niente', 0);


--
-- TOC entry 3141 (class 0 OID 70477)
-- Dependencies: 205
-- Data for Name: valorisino; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO valorisino (id, text, value) VALUES ('01', 'SI', -10);
INSERT INTO valorisino (id, text, value) VALUES ('02', 'NO', 0);

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


