--
-- TOC entry 3415 (class 0 OID 21409)
-- Dependencies: 190
-- Data for Name: bacini; Type: TABLE DATA; Schema: public; Owner: postgres
--

-- Bacino idrografico L 183/1989
INSERT INTO bacini (id, text) VALUES ('01', 'Arno');
INSERT INTO bacini (id, text) VALUES ('02', 'Conca - Marecchia');
INSERT INTO bacini (id, text) VALUES ('03', 'Fiora');
INSERT INTO bacini (id, text) VALUES ('04', 'Interregionale nc');
INSERT INTO bacini (id, text) VALUES ('05', 'Magra');
INSERT INTO bacini (id, text) VALUES ('06', 'Ombrone');
INSERT INTO bacini (id, text) VALUES ('07', 'Po');
INSERT INTO bacini (id, text) VALUES ('08', 'Reno');
INSERT INTO bacini (id, text) VALUES ('09', 'Serchio');
INSERT INTO bacini (id, text) VALUES ('10', 'Tevere');
INSERT INTO bacini (id, text) VALUES ('11', 'Toscana Costa');
INSERT INTO bacini (id, text) VALUES ('12', 'Toscana nord');

-- PROVINCE
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('051', 'AREZZO', 'AR');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('048', 'FIRENZE', 'FI');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('053', 'GROSSETO', 'GR');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('049', 'LIVORNO', 'LI');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('046', 'LUCCA', 'LU');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('045', 'MASSA-CARRARA', 'MS');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('050', 'PISA', 'PI');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('100', 'PRATO', 'PO');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('047', 'PISTOIA', 'PT');
INSERT INTO province (cod_prov, nome_prov, sigla_prov) VALUES ('052', 'SIENA', 'SI');


-- COMUNI
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ABBADIA SAN SALVATORE', '052001', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ABETONE', '047001', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('AGLIANA', '047002', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ALTOPASCIO', '046001', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ANGHIARI', '051001', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ARCIDOSSO', '053001', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('AREZZO', '051002', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ASCIANO', '052002', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('AULLA', '045001', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BADIA TEDALDA', '051003', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BAGNI DI LUCCA', '046002', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BAGNO A RIPOLI', '048001', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BAGNONE', '045002', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BARBERINO DI MUGELLO', '048002', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BARBERINO VAL D''ELSA', '048003', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BARGA', '046003', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BIBBIENA', '051004', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BIBBONA', '049001', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BIENTINA', '050001', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BORGO A MOZZANO', '046004', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BORGO SAN LORENZO', '048004', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BUCINE', '051005', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BUGGIANO', '047003', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BUONCONVENTO', '052003', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('BUTI', '050002', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CALCI', '050003', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CALCINAIA', '050004', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CALENZANO', '048005', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMAIORE', '046005', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMPAGNATICO', '053002', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMPI BISENZIO', '048006', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMPIGLIA MARITTIMA', '049002', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMPO NELL''ELBA', '049003', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAMPORGIANO', '046006', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CANTAGALLO', '100001', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPALBIO', '053003', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPANNOLI', '050005', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPANNORI', '046007', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPOLIVERI', '049004', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPOLONA', '051006', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPRAIA E LIMITE', '048008', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPRAIA ISOLA', '049005', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAPRESE MICHELANGELO', '051007', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAREGGINE', '046008', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CARMIGNANO', '100002', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CARRARA', '045003', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASALE MARITTIMO', '050006', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASCIANA TERME LARI', '050040', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASCINA', '050008', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASOLA IN LUNIGIANA', '045004', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASOLE D''ELSA', '052004', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTAGNETO CARDUCCI', '049006', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTEL DEL PIANO', '053004', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTEL FOCOGNANO', '051008', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTEL SAN NICCOLO''', '051010', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELFIORENTINO', '048010', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELFRANCO DI SOTTO', '050009', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELFRANCO PIANDISCO''', '051040', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELL''AZZARA', '053005', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELLINA IN CHIANTI', '052005', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELLINA MARITTIMA', '050010', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELNUOVO BERARDENGA', '052006', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELNUOVO DI GARFAGNANA', '046009', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTELNUOVO DI VAL DI CECINA', '050011', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTIGLION FIBOCCHI', '051011', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTIGLION FIORENTINO', '051012', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTIGLIONE D''ORCIA', '052007', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTIGLIONE DELLA PESCAIA', '053006', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CASTIGLIONE DI GARFAGNANA', '046010', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CAVRIGLIA', '051013', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CECINA', '049007', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CERRETO GUIDI', '048011', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CERTALDO', '048012', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CETONA', '052008', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIANCIANO TERME', '052009', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIANNI', '050012', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIESINA UZZANESE', '047022', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHITIGNANO', '051014', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIUSDINO', '052010', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIUSI DELLA VERNA', '051015', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CHIUSI', '052011', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CINIGIANO', '053007', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CIVITELLA IN VAL DI CHIANA', '051016', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CIVITELLA PAGANICO', '053008', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('COLLE DI VAL D''ELSA', '052012', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('COLLESALVETTI', '049008', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('COMANO', '045005', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('COREGLIA ANTELMINELLI', '046011', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CORTONA', '051017', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CRESPINA LORENZANA', '050041', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('CUTIGLIANO', '047004', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('DICOMANO', '048013', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('EMPOLI', '048014', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FABBRICHE DI VERGEMOLI', '046036', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FAUGLIA', '050014', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FIESOLE', '048015', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FIGLINE E INCISA VALDARNO', '048052', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FILATTIERA', '045006', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FIRENZE', '048017', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FIRENZUOLA', '048018', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FIVIZZANO', '045007', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FOIANO DELLA CHIANA', '051018', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FOLLONICA', '053009', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FORTE DEI MARMI', '046013', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FOSCIANDORA', '046014', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FOSDINOVO', '045008', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('FUCECCHIO', '048019', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GAIOLE IN CHIANTI', '052013', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GALLICANO', '046015', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GAMBASSI TERME', '048020', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GAVORRANO', '053010', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GIUNCUGNANO', '046016', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GREVE IN CHIANTI', '048021', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GROSSETO', '053011', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('GUARDISTALLO', '050015', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('IMPRUNETA', '048022', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ISOLA DEL GIGLIO', '053012', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LAJATICO', '050016', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LAMPORECCHIO', '047005', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LARCIANO', '047006', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LASTRA A SIGNA', '048024', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LATERINA', '051019', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LICCIANA NARDI', '045009', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LIVORNO', '049009', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LONDA', '048025', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LORO CIUFFENNA', '051020', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LUCCA', '046017', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('LUCIGNANO', '051021', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MAGLIANO IN TOSCANA', '053013', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MANCIANO', '053014', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MARCIANA MARINA', '049011', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MARCIANA', '049010', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MARCIANO DELLA CHIANA', '051022', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MARLIANA', '047007', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MARRADI', '048026', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MASSA E COZZILE', '047008', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MASSA MARITTIMA', '053015', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MASSA', '045010', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MASSAROSA', '046018', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MINUCCIANO', '046019', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MOLAZZANA', '046020', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONSUMMANO TERME', '047009', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTAIONE', '048027', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTALCINO', '052014', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTALE', '047010', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTE ARGENTARIO', '053016', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTE SAN SAVINO', '051025', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTECARLO', '046021', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTECATINI TERME', '047011', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTECATINI VAL DI CECINA', '050019', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTELUPO FIORENTINO', '048028', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEMIGNAIO', '051023', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEMURLO', '100003', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEPULCIANO', '052015', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTERCHI', '051024', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTERIGGIONI', '052016', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTERONI D''ARBIA', '052017', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEROTONDO MARITTIMO', '053027', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTESCUDAIO', '050020', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTESPERTOLI', '048030', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEVARCHI', '051026', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTEVERDI MARITTIMO', '050021', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTICIANO', '052018', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTIERI', '053017', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTIGNOSO', '045011', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MONTOPOLI IN VAL D''ARNO', '050022', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MULAZZO', '045012', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('MURLO', '052019', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ORBETELLO', '053018', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ORCIANO PISANO', '050023', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ORTIGNANO RAGGIOLO', '051027', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PALAIA', '050024', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PALAZZUOLO SUL SENIO', '048031', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PECCIOLI', '050025', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PELAGO', '048032', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PERGINE VALDARNO', '051028', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PESCAGLIA', '046022', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PESCIA', '047012', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIANCASTAGNAIO', '052020', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIAZZA AL SERCHIO', '046023', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIENZA', '052021', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIETRASANTA', '046024', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIEVE A NIEVOLE', '047013', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIEVE FOSCIANA', '046025', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIEVE SANTO STEFANO', '051030', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PIOMBINO', '049012', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PISA', '050026', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PISTOIA', '047014', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PITEGLIO', '047015', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PITIGLIANO', '053019', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PODENZANA', '045013', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('POGGIBONSI', '052022', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('POGGIO A CAIANO', '100004', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('POMARANCE', '050027', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PONSACCO', '050028', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PONTASSIEVE', '048033', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PONTE BUGGIANESE', '047016', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PONTEDERA', '050029', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PONTREMOLI', '045014', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('POPPI', '051031', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PORCARI', '046026', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PORTO AZZURRO', '049013', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PORTOFERRAIO', '049014', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PRATO', '100005', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('PRATOVECCHIO STIA', '051041', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('QUARRATA', '047017', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RADDA IN CHIANTI', '052023', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RADICOFANI', '052024', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RADICONDOLI', '052025', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RAPOLANO TERME', '052026', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('REGGELLO', '048035', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RIGNANO SULL''ARNO', '048036', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RIO MARINA', '049015', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RIO NELL''ELBA', '049016', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RIPARBELLA', '050030', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ROCCALBEGNA', '053020', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ROCCASTRADA', '053021', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ROSIGNANO MARITTIMO', '049017', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('RUFINA', '048037', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAMBUCA PISTOIESE', '047018', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN CASCIANO DEI BAGNI', '052027', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN CASCIANO IN VAL DI PESA', '048038', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN GIMIGNANO', '052028', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN GIOVANNI D''ASSO', '052029', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN GIOVANNI VALDARNO', '051033', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN GIULIANO TERME', '050031', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN GODENZO', '048039', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN MARCELLO PISTOIESE', '047019', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN MINIATO', '050032', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN QUIRICO D''ORCIA', '052030', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN ROMANO IN GARFAGNANA', '046027', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SAN VINCENZO', '049018', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SANSEPOLCRO', '051034', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SANTA CROCE SULL''ARNO', '050033', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SANTA FIORA', '053022', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SANTA LUCE', '050034', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SANTA MARIA A MONTE', '050035', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SARTEANO', '052031', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SASSETTA', '049019', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SCANDICCI', '048041', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SCANSANO', '053023', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SCARLINO', '053024', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SCARPERIA E SAN PIERO', '048053', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SEGGIANO', '053025', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SEMPRONIANO', '053028', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SERAVEZZA', '046028', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SERRAVALLE PISTOIESE', '047020', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SESTINO', '051035', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SESTO FIORENTINO', '048043', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SIENA', '052032', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SIGNA', '048044', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SILLANO', '046029', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SINALUNGA', '052033', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SORANO', '053026', 'GROSSETO', '053', 'GR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SOVICILLE', '052034', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('STAZZEMA', '046030', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SUBBIANO', '051037', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('SUVERETO', '049020', 'LIVORNO', '049', 'LI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TALLA', '051038', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TAVARNELLE VAL DI PESA', '048045', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TERRANUOVA BRACCIOLINI', '051039', 'AREZZO', '051', 'AR');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TERRICCIOLA', '050036', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TORRITA DI SIENA', '052035', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TREQUANDA', '052036', 'SIENA', '052', 'SI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('TRESANA', '045015', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('UZZANO', '047021', 'PISTOIA', '047', 'PT');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VAGLI SOTTO', '046031', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VAGLIA', '048046', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VAIANO', '100006', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VECCHIANO', '050037', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VERNIO', '100007', 'PRATO', '100', 'PO');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VIAREGGIO', '046033', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VICCHIO', '048049', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VICOPISANO', '050038', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VILLA BASILICA', '046034', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VILLA COLLEMANDINA', '046035', 'LUCCA', '046', 'LU');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VILLAFRANCA IN LUNIGIANA', '045016', 'MASSA-CARRARA', '045', 'MS');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VINCI', '048050', 'FIRENZE', '048', 'FI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('VOLTERRA', '050039', 'PISA', '050', 'PI');
INSERT INTO comuni (nom_com, cod_com, nome_prov, cod_prov, sigla_prov) VALUES ('ZERI', '045017', 'MASSA-CARRARA', '045', 'MS');

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

INSERT INTO efficacia (id, text, value) VALUES ('00', 'Nessun valore - vedi cantierabilita', null);
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
INSERT INTO efficacia (id, text, value) VALUES ('20', 'Opere di urbanizzazione', 0);



--
-- TOC entry 3142 (class 0 OID 70482)
-- Dependencies: 206
-- Data for Name: sostenibilita; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO sostenibilita (id, text, value) VALUES ('00', 'Nessun valore - vedi cantierabilita', null);
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

INSERT INTO valorisino (id, text, value) VALUES ('00', 'Nessun valore - vedi cantierabilita', null);
INSERT INTO valorisino (id, text, value) VALUES ('01', 'Necessaria e ancora da attuare', -10);
INSERT INTO valorisino (id, text, value) VALUES ('02', 'Non necessaria oppure gia attuata', 0);

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

INSERT INTO studio_intervento (id, text) VALUES ('01', 'PROGETTO/STUDIO');
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
INSERT INTO tipologia_intervento (id, text) VALUES ('02', 'Manutenzione Straordinaria');

--
-- TOC entry 3169 (class 0 OID 72610)
-- Dependencies: 218
-- Data for Name: categoria_opera; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO categoria_opera (id, text) VALUES ('01', '2 categoria');
INSERT INTO categoria_opera (id, text) VALUES ('02', '3 categoria');
INSERT INTO categoria_opera (id, text) VALUES ('03', '4 categoria');
INSERT INTO categoria_opera (id, text) VALUES ('04', '5 categoria');
INSERT INTO categoria_opera (id, text) VALUES ('05', 'opere di bonifica');
INSERT INTO categoria_opera (id, text) VALUES ('06', 'non classificato');

-- Completed on 2014-06-10 16:51:17

--
-- PostgreSQL database dump complete
--

INSERT INTO genio_civile_bacini (id, text) VALUES ('01', 'GENIO CIVILE DI BACINO TOSCANA NORD E SERVIZIO IDROLOGICO REGIONALE');
INSERT INTO genio_civile_bacini (id, text) VALUES ('02', 'GENIO CIVILE DI BACINO ARNO - TOSCANA CENTRO');
INSERT INTO genio_civile_bacini (id, text) VALUES ('03', 'GENIO CIVILE DI BACINO TOSCANA SUD E OPERE MARITTIME');


--
-- Categoria dell'Intervento
--

INSERT INTO categoria_intervento (id, text) VALUES ('01', 'Interventi ad efficacia autonoma');
INSERT INTO categoria_intervento (id, text) VALUES ('02', 'Interventi complessi di area vasta');
INSERT INTO categoria_intervento (id, text) VALUES ('03', 'Interventi integrati di mitigazione e recupero (infrastrutture verdi)');


