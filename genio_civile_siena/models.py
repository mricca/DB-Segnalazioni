# -*- coding: utf-8 -*-
from django.contrib.gis.db import models as gismodels
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError
from django.forms.widgets import NullBooleanSelect
from django.utils.translation import ugettext_lazy

class  CategoriaIntervento(models.Model):
    id = models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=150)

    class Meta:
        db_table = 'categoria_intervento'

    def __unicode__(self):
        return self.text

class  GenioCivileBacino(models.Model):
    id = models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=150)

    class Meta:
        db_table = 'genio_civile_bacini'

    def __unicode__(self):
        return self.text

class  CategoriaOperaAll(models.Model):
    id = models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=30)

    class Meta:
        db_table = 'categoria_opera'

    def __unicode__(self):
        return self.text

class  EnteProponenteAll(models.Model):
    id = models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=80)

    class Meta:
        db_table = 'ente_proponente_si'

    def __unicode__(self):
        return self.text

class  EnteAttuatoreAll(models.Model):
    id = models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=80)

    class Meta:
        db_table = 'ente_attuatore'

    def __unicode__(self):
        return self.text

class  BaciniAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=30)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = 'bacini'

    def __unicode__(self):
        return self.text

class  ComprensorioAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=20)

    class Meta:
        db_table = 'comprensorio'

    def __unicode__(self):
        return self.text

class  FenomenoAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=20)

    class Meta:
        db_table = 'fenomeno'

    def __unicode__(self):
        return self.text

class  StudioInterventoAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=20)

    class Meta:
        db_table = 'studio_intervento'

    def __unicode__(self):
        return self.text

class  TipologiaInterventoAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipologia_intervento'

    def __unicode__(self):
        return self.text

class  TipoOperaAll(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipo_opera'

    def __unicode__(self):
        return self.text

class  ComuniAll(models.Model):
    nom_com = models.CharField(max_length=40)
    cod_com =  models.CharField(max_length=6, unique=True, blank=False, primary_key=True, editable=False)
    nome_prov = models.CharField(max_length=40)
    cod_prov = models.CharField(max_length=3)
    sigla_prov = models.CharField(max_length=2)

    class Meta:
        db_table = 'comuni'

    def __unicode__(self):
        return self.nom_com

class  ProvinceAll(models.Model):
    cod_prov =  models.CharField(max_length=3, unique=True, blank=False, primary_key=True, editable=False)
    nome_prov = models.CharField(max_length=40)
    sigla_prov = models.CharField(max_length=2)

    class Meta:
        db_table = 'province'

    def __unicode__(self):
        return self.sigla_prov

class  ArchiSi(models.Model):
    ri05_nome = models.CharField(max_length=100)
    sibapo =  models.CharField(max_length=20, unique=True, blank=False, primary_key=True, editable=False)
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=40)

    class Meta:
        db_table = 'archi_si'

    def __unicode__(self):
        return self.ri05_nome

class  ValoriSiNo(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'valorisino'

    def __unicode__(self):
        return self.text

class  Sostenibilita(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'sostenibilita'

    def __unicode__(self):
        return self.text

#class  Finanziamento(models.Model):
#    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
#    text = models.CharField(max_length=255)#

#    class Meta:
#        db_table = 'finanziamento'

#    def __unicode__(self):
#        return self.text

class  Cantierabilita(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        db_table = 'cantierabilita'

    def __unicode__(self):
        return self.text

class  Efficacia(models.Model):
    id = models.CharField(max_length=2, unique=True, blank=False, primary_key=True, editable=False)
    text = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        db_table = 'efficacia'

    def __unicode__(self):
        return self.text

class Intervento(gismodels.Model):

    # Create your models here.

    ############################
    # INFORMAZIONI GEOGRAFICHE #
    ############################

    # Codice intervento composto da i seguenti DA & ANNO & SIGLA PROVINCIA & Numero progressivo interno al DB COMPOSTO DA 4 CIFRE  ES: DA2014AR0001.
    codice_intervento = gismodels.CharField(max_length=12, unique=True, blank=False, primary_key=True, editable=False, db_column='codint')
    #codint = gismodels.CharField(max_length=12, unique=True, blank=False)

    # Modifica i campi added e updated
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Bacino idrografico L 183/1989
    BACINO_CHOICES = (
        ('Arno','Arno'),
        ('Conca - Marecchia','Conca - Marecchia'),
        ('Fiora','Fiora'),
        ('Interregionale nc','Interregionale nc'),
        ('Magra','Magra'),
        ('Ombrone','Ombrone'),
        ('Po','Po'),
        ('Reno','Reno'),
        ('Serchio','Serchio'),
        ('Tevere','Tevere'),
        ('Toscana Costa','Toscana Costa'),
        ('Toscana nord','Toscana nord'),
    )
    #bacino_idrografico = gismodels.CharField(max_length=50, choices=BACINO_CHOICES, blank=False, db_column='bacidro', help_text='Bacino idrografico L 183/1989')
    bacino_idrografico = gismodels.ForeignKey(BaciniAll, related_name='bacini_siena', db_column='bacidro', help_text='Bacino idrografico L 183/1989')

    # Comprensorio LR 79/2012
    comprensorio = gismodels.ForeignKey(ComprensorioAll, related_name='comprensori_siena', help_text='Comprensorio LR 79/2012')

    #provincia = gismodels.CharField(max_length=2, choices=PROVINCIA_CHOICES, default='AR', blank=False)
    provincia = gismodels.ForeignKey(ProvinceAll, related_name='provincia_siena')

    comune = gismodels.ForeignKey(ComuniAll, related_name='comune_siena')

    # Localita (testo libero)
    localita = gismodels.TextField(blank=True)

    # Corso d'acqua
    corso_acqua = gismodels.ForeignKey(ArchiSi, blank=True, null=True, db_column='corsoacqua')

    # Reticolo di gestione DCR 57/2013
    reticolo_gestione = gismodels.BooleanField(db_column='retgest', help_text='Reticolo di gestione DCR 57/2013')

    # GEOMETRIA PUNTUALE
    fenomeno_aggiunto = gismodels.PointField(srid=3003,db_index=True,db_column='geom')
    objects = gismodels.GeoManager()

    #####################################################
    # INFORMAZIONI GENERALI INTERVENTO/STUDI E PROGETTI #
    #####################################################

    #CONSIDERARE DI INSERIRE IN CHOICE IL VALORE FOREIGNKEY DI UNA TABELLA DI DECODIFICA
    TIPO_FENOMENO_CHOICES = (
        ('Idraulica','Idraulica'),
        ('Frana','Frana'),
        ('Idraulica e Frana','Idraulica e Frana'),
    )
    #fenomeno = gismodels.CharField(max_length=20, choices=TIPO_FENOMENO_CHOICES)
    fenomeno = gismodels.ForeignKey(FenomenoAll, related_name='fenomeno_siena')

    # Studio o Intervento
    STUDIO_INTERVENTO_CHOICES = (
        ('STUDIO','STUDIO'),
        ('INTERVENTO','INTERVENTO'),
    )
    #studio_intervento = gismodels.CharField(max_length=12, choices=STUDIO_INTERVENTO_CHOICES, help_text='Studio o Intervento')
    studio_intervento = gismodels.ForeignKey(StudioInterventoAll, verbose_name="Progetto/Studio o Intervento", related_name='studio_intervento_siena', default='02')

    # Tipologia Intervento (Obbligatorio solo se il campo "Studio o Intervento == Intervento")
    TIPO_INTERVENTO_CHOICES = (
        ('Nuova Realizzazione','Nuova Realizzazione'),
        ('Manutenzione Ordinaria','Manutenzione Ordinaria'),
        ('Manutenzione Straordinaria','Manutenzione Straordinaria'),
    )
    #tipologia_intervento = gismodels.CharField(max_length=30, choices=TIPO_INTERVENTO_CHOICES, blank=True, null=True)
    tipologia_intervento = gismodels.ForeignKey(TipologiaInterventoAll, related_name='tipologia_intervento_siena', blank=True, null=True)

    #Elenco di tutte le opere. DropDown. Argine, Cassa di Espansione, ecc...
    TIPO_OPERA_CHOICES = (
        ('Argine','Argine'),
        ('Cassa di espansione','Cassa di espansione'),
        ('Laghetto collinare','Laghetto collinare'),
        ('Canale Scolmatore','Canale Scolmatore'),
        ('Canali di bonifica','Canali di bonifica'),
        ('Briglia','Briglia'),
        ('Briglia selettiva','Briglia selettiva'),
        ('Soglia','Soglia'),
        ('Cunettoni','Cunettoni'),
        ('Protezione di sponda','Protezione di sponda'),
        ('Rivestimento','Rivestimento'),
        ('Presidio al piede di sponda','Presidio al piede di sponda'),
        ('Opera contro colate di detriti e fango','Opera contro colate di detriti e fango'),
        ('Movimenti di terra','Movimenti di terra'),
        ('Drenaggio','Drenaggio'),
        ('Sistemazioni idraulico-forestali','Sistemazioni idraulico-forestali'),
        ('Sostegno','Sostegno'),
        ('Protezione','Protezione'),
        ('Altro (specificare nel campo successivo)','Altro (specificare nel campo successivo)'),
    )
    #tipo_di_opera = gismodels.CharField(max_length=200, choices=TIPO_OPERA_CHOICES, blank=True, null=True, db_column='tipo_opera')
    tipo_di_opera = gismodels.ForeignKey(TipoOperaAll, related_name='tipo_opera_siena', blank=True, null=True)

    cat_int = gismodels.ForeignKey(CategoriaIntervento, db_column='cat_int', verbose_name="Categoria dell'intervento", blank=True, null=True)

    area_vasta_rif = gismodels.TextField(blank=True, null=True, db_column='area_vasta_rif', verbose_name='Area vasta di riferimento', help_text='Da compilare se è stato selezionato categoria intervento <b>"Interventi complessi di area vasta"</b>')

    # Titolo Intervento/Studio
    titolo_intervento_studio = gismodels.CharField(verbose_name="Titolo intervento/progetto/studio", max_length=100,db_column='t_intstu', help_text='Max 100 caratteri')

    # Descrizione sintetica intervento/studio
    descrizione_sintetica_intervento_studio = gismodels.TextField(verbose_name="Descrizione sintetica intervento/progetto/studio", db_column='d_intstu')

    # Categoria Idraulica dell'Opera
    categoria_idr_opera = gismodels.ForeignKey(CategoriaOperaAll, verbose_name="Categoria idraulica dell'opera", db_column='cat_idr_op', related_name='categoria_opera_siena', blank=True, null=True)

    # Perimetrazione Autorita di Bacino
    perimetrazione_autorita_di_bacino = gismodels.BooleanField(db_column='perim_adb')

    # Codice pericolosita AdB - PAI. (Obbligatorio se il campo "perimetrazione_adb" == si)
    codice_pericolosita_adb_pai = gismodels.TextField(blank=True, null=True, db_column='codice_peric', help_text='Classe di pericolosità PAI o Piano di Gestione RA nella situazione attuale', verbose_name="Classe pericolosita PAI o PGRA attuale")

    #################################
    ######## START RENDIS ###########
    #################################

    # Classe di rischio PAI o Piano di Gestione (RENDIS)
    classe_rischio_pai = gismodels.TextField(blank=True, null=True, db_column='classe_risc', help_text='Classe di rischio PAI o Piano di Gestione RA nella situazione attuale', verbose_name='Classe rischio PAI o PGRA attuale')

    # perimetrazione_pericolosita_attuale
    perimetrazione_pericolosita_attuale  = gismodels.FileField(upload_to='documents/perim_peric_attuale/%Y/%m/%d',null=True, blank=True, db_column='perim_peric_attuale', help_text='caricare lo shape file della classe di pericolosità PAI o Piano di Gestione RA prima della realizzazione dell\'intervento')

    # perimetrazione_pericolosita_post_intervento
    perimetrazione_pericolosita_post_intervento = gismodels.FileField(upload_to='documents/perim_peric_post/%Y/%m/%d',null=True, blank=True, db_column='perim_peric_post', help_text='caricare lo shape file della classe di pericolosità PAI o Piano di Gestione RA dopo la realizzazione dell\'intervento')

    #Stima persone a rischio diretto nella situazione attuale
    stima_rischio_diretto_attuale = gismodels.PositiveIntegerField(verbose_name="Stima persone a rischio diretto nella situazione attuale", null=True, blank=True, db_column='stima_ris_dir_at', validators=[MaxValueValidator(99999)])

    #Stima persone a rischio indiretto nella situazione attuale
    stima_rischio_indiretto_attuale = gismodels.PositiveIntegerField(verbose_name="Stima persone a rischio indiretto nella situazione attuale", null=True, blank=True, db_column='stima_ris_ind_at', validators=[MaxValueValidator(99999)], help_text="<b>Numero di persone esposte a rischio indiretto (perdita posto lavoro, isolate per interruzione viabilità, ecc) in relazione all'area di influenza dell'intervento proposto</b>")

    #Stima persone a rischio diretto dopo la realizzazione dell'intervento
    stima_rischio_diretto_intervento = gismodels.PositiveIntegerField(verbose_name="Stima persone a rischio diretto dopo la realizzazione dell'intervento", null=True, blank=True, db_column='stima_ris_dir_int', validators=[MaxValueValidator(99999)])

    #Stima persone a rischio indiretto dopo la realizzazione dell'intervento
    stima_rischio_indiretto_intervento = gismodels.PositiveIntegerField(verbose_name="Stima persone a rischio indiretto dopo la realizzazione dell'intervento", null=True, blank=True, db_column='stima_ris_ind_int', validators=[MaxValueValidator(99999)], help_text="<b>Numero di persone esposte a rischio indiretto (perdita posto lavoro, isolate per interruzione viabilità, ecc) in relazione all'area di influenza dell'intervento proposto</b>")

    #################################
    ########## END RENDIS ###########
    #################################

    # Ente proponente
    ente_proponente = gismodels.ForeignKey(EnteProponenteAll, related_name='ente_proponente_siena', db_column='ente_prop', verbose_name='Ente proponente', help_text='Ente Proponente')

    # Ente attuatore competente ai sensi della normativa vigente. (elenco Comuni + Elenco Province + Elenco Consorzi di Bonifica (vedi foglio C.B.) + valore "Regione Toscana")
    ente_attuatore_competente = gismodels.ForeignKey(EnteAttuatoreAll, related_name='ente_attuatore_siena', verbose_name='Ente attuatore competente ai sensi della normativa vigente', db_column='ente_attuat', help_text='Ente attuatore competente ai sensi della normativa vigente.<BR/><b><a style="color:#FF0000">Compilazione riservata Regione Toscana.</a></b>', blank=True, null=True)

    # Nominativo tecnico di riferimento
    nominativo = gismodels.CharField(max_length=100, db_column='nom_t_rif', help_text="Nominativo Rup", verbose_name="Nominativo Rup")

    # Email tecnico di riferimento
    email = gismodels.EmailField(db_column='mail_t_rif', help_text="Email Rup", verbose_name="Email Rup")

    # Recapito telefonico tecnico di riferimento
    recapito_telefonico = gismodels.CharField(max_length=100, db_column='rec_t_rif', help_text="Recapito telefonico Rup", verbose_name="Recapito telefonico Rup")

    # Interventi correlati
    interventi_correlati = gismodels.TextField(blank=True,db_column='int_corr')

    # Stralcio funzionale
    stralcio_funzionale = gismodels.BooleanField(blank=True,db_column='stral_funz')

    # Accordo di programma
    accordo_di_programma = gismodels.TextField(blank=True,db_column='acc_prog')

    # Note
    note = gismodels.TextField(blank=True)

    #########################################################################################
    #                                   CRONOPROGRAMMA                                      #
    # (TUTTA LA SEZIONE E' DA COMPILARE SOLO SE IL CAMPO STUDIO O INTERVENTO == INTERVENTO) #
    #########################################################################################

    #PROGETTO PRELIMINARE

    progetto_preliminare = gismodels.BooleanField(default=True, db_column='prog_p', help_text="Spunta questa casella se &#232; previsto il progetto preliminare")

    mesi_approvazione_progetto_preliminare = gismodels.PositiveSmallIntegerField(verbose_name="Progetto preliminare [n°mesi previsti]", null=True, blank=True, db_column='mesi_app_pp', help_text="<b>Indicare il numero di mesi totali previsti conteggiati a partire dalla data di finanziamento.<BR/>Indicare 0 mesi se il progetto preliminare è già stato approvato oppure se non è previsto</b>")

    # Data approvazione progetto preliminare (SOLO SE INTERVENTO)
    #data_approvazione_progetto_preliminare = gismodels.DateField(null=True, blank=True, validators=[validate_even])
    data_approvazione_progetto_preliminare = gismodels.DateField(null=True, blank=True, db_column='data_app_pp')

    # Riferimento determina di approvazione PP
    riferimento_determina_approvazione_pp = gismodels.TextField(verbose_name="Data e riferimento determina approvazione pp", null=True, blank=True, db_column='rif_det_app_pp')

    # Allega determina di approvazione PP (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PP E' STATO COMPILATO)
    allegato_determina_approvazione_pp = gismodels.FileField(upload_to='documents/approvazione_pp/%Y/%m/%d',null=True, blank=True, db_column='all_det_app_pp')

    # Data della determina di approvazione PP  (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PP E' STATO COMPILATO)
    #data_determina_approvazione_pp = gismodels.DateField(null=True, blank=True, db_column='data_det_app_pp')



    #PROGETTO DEFINITIVO
    progetto_definitivo = gismodels.BooleanField(default=True, db_column='prog_d', help_text="Spunta questa casella se &#232; previsto il progetto definitivo")

    mesi_approvazione_progetto_definitivo = gismodels.PositiveSmallIntegerField(verbose_name="Progetto definitivo [n°mesi previsti]", null=True, blank=True, db_column='mesi_app_pd', help_text="<b>Indicare il numero di mesi totali previsti conteggiati a partire dalla data di finanziamento.<BR/>Indicare 0 mesi se il progetto definitivo è già stato approvato oppure se non è previsto</b>")

    # Data approvazionepprovazione progetto definitivo (SOLO SE INTERVENTO)
    data_approvazione_progetto_definitivo = gismodels.DateField(null=True, blank=True, db_column='data_app_pd')

    # Riferimento determina di approvazione PD (SOLO SE INTERVENTO)
    riferimento_determina_approvazione_pd = gismodels.TextField(verbose_name="Data e riferimento determina approvazione pd", null=True, blank=True, db_column='rif_det_app_pd')

    # Allega determina di approvazione PD (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PD E' STATO COMPILATO)
    allegato_determina_approvazione_pd = gismodels.FileField(null=True, upload_to='documents/approvazione_pd/%Y/%m/%d',blank=True, db_column='all_det_app_pd')

    # Data della determina di approvazione PD  (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PD E' STATO COMPILATO)
    #data_determina_approvazione_pd = gismodels.DateField(null=True, blank=True, db_column='data_det_app_pd')



    #PROGETTO ESECUTIVO

    mesi_approvazione_progetto_esecutivo = gismodels.PositiveSmallIntegerField(verbose_name="Progetto esecutivo [n°mesi previsti]", null=True, blank=True, db_column='mesi_app_pe', help_text="<b>Indicare il numero di mesi totali previsti conteggiati a partire dalla data di finanziamento.<BR/>Indicare 0 mesi se il progetto esecutivo è già stato approvato oppure se non è previsto</b>")

    # Data approvazionepprovazione progetto esecutivo (SOLO SE INTERVENTO)
    data_approvazione_progetto_esecutivo = gismodels.DateField(null=True, blank=True, db_column='data_app_pe')

    # Riferimento determina di approvazione PE (SOLO SE INTERVENTO)
    riferimento_determina_approvazione_pe = gismodels.TextField(verbose_name="Data e riferimento determina approvazione pe", null=True, blank=True, db_column='rif_det_app_pe')

    # Allega determina di approvazione PE (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PE E' STATO COMPILATO)
    allegato_determina_approvazione_pe = gismodels.FileField(null=True, upload_to='documents/approvazione_pe/%Y/%m/%d',blank=True, db_column='all_det_app_pe')

    # Data della determina di approvazione PE  (SOLO SE INTERVENTO E SE RIFERIMENTO_DETERMINA_PE E' STATO COMPILATO)
    #data_determina_approvazione_pe = gismodels.DateField(null=True, blank=True, db_column='data_det_app_pe')


    #LAVORI

    # Inizio lavori (SOLO SE INTERVENTO)
    mesi_inizio_lavori = gismodels.PositiveSmallIntegerField(verbose_name="Inizio lavori [n°mesi previsti]", null=True, blank=True)
    inizio_lavori = gismodels.DateField(null=True, blank=True)

    # Fine lavori (SOLO SE INTERVENTO)
    mesi_fine_lavori = gismodels.PositiveSmallIntegerField(verbose_name="Fine lavori [n°mesi previsti]", null=True, blank=True)
    fine_lavori = gismodels.DateField(null=True, blank=True)

    # Elaborati progettuali (SOLO SE STUDIO)
    elaborati_progettuali = gismodels.FileField(verbose_name="Elaborati progettuali (.. in file compresso)", null=True, upload_to='documents/elaborati_prog/%Y/%m/%d',blank=True, db_column='elaborati_prog', help_text="<b>Nel caso di PROGETTO DEFINITIVO caricare gli elaborati progettuali comprensivi di:<ul><li>Elenco elaborati,</li><li>Verbale di Verifica</li></ul> Nel caso di PROGETTO ESECUTIVO caricare gli elaborati progettuali comprensivi di:<ul><li>Elenco elaborati,</li><li>Verbale di Verifica,</li><li>Verbale di validazione,</li><li>Atti gara (lettera di invito e/o bando e disciplinare di gara).</li></ul></b>")

    descrizione_elaborati_prog = gismodels.TextField(blank=True, null=True, db_column='desc_elab_prog', verbose_name='Descrizione Elaborati Progettuali')

    # RELAZIONI IN CASO DI STUDIO

    # Conclusione Relazione Metodologica (SOLO SE STUDIO)
    #conclusione_relazione_metodologica = gismodels.DateField(verbose_name="Conclusione Documento Preliminare alla Progettazione (se Progetto) o Conclusione Relazione Metodologica (se Studio)", null=True, blank=True, db_column='conc_rel_met')

    allegato_documento_preliminare = gismodels.FileField(verbose_name="Allega Documento Preliminare alla Progettazione (se Progetto) o Relazione Metodologica (se Studio)", null=True, upload_to='documents/allegato_doc_prelim/%Y/%m/%d',blank=True, db_column='all_doc_pre')

    mesi_conclusione_relazione_finale = gismodels.PositiveSmallIntegerField(verbose_name="Conclusione Progetto o Conclusione Relazione finale [n°mesi previsti]", null=True, blank=True, db_column='mesi_conc_rel_fin')

    # Conclusione Relazione Finale (SOLO SE STUDIO)
    conclusione_relazione_finale = gismodels.DateField(verbose_name="Conclusione Progetto o Conclusione Relazione finale", null=True, blank=True, db_column='conc_rel_fin')

    #################################
    ######## START RENDIS ###########
    #################################

    # Elencare i pareri da acquisire o acquisiti (pareri, autorizzazioni, intese, concessioni, licenze, nulla osta, autorizzazioni ed assensi, comunque denominati necessari per la realizzazione e l’esercizio del Progetto) testo libero (RENDIS)
    elenco_pareri = gismodels.TextField(blank=True, null=True, db_column='elenco_pareri', verbose_name='Elenco pareri da acquisire o acquisiti', help_text="Elencare i pareri da acquisire o acquisiti (pareri, autorizzazioni, intese, concessioni, licenze, nulla osta, autorizzazioni ed assensi, comunque denominati necessari per la realizzazione e l'esercizio del Progetto) testo libero")

    # Atto di validazione del progetto - art.55 del D.P.R. 207/2010 (indicare se presente ed allegare in caso affermativo)
    atto_valutazione = gismodels.BooleanField(default=False, verbose_name="Atto di validazione del progetto", db_column='atto_val', help_text="Spunta questa casella se è presente l'Atto di validazione del progetto - art.55 del D.P.R. 207/2010")

    # Allegato Atto di validazione del progetto - art.55 del D.P.R. 207/2010 (indicare se presente ed allegare in caso affermativo)
    allegato_atto_valutazione = gismodels.FileField(verbose_name="Allegato Atto di validazione del progetto", upload_to='documents/atto_valutazione_rendis/%Y/%m/%d',null=True, blank=True, db_column='all_atto_val', help_text="Atto di validazione del progetto - art.55 del D.P.R. 207/2010 (indicare se presente ed allegare in caso affermativo)")

    # Codice Unico di Progetto (CUP) obbligatorio ai sensi dell'art. 11 della Legge 3/2003
    codice_unico_progetto = gismodels.CharField(blank=True, null=True, max_length=20, db_column='cod_un_prog', help_text="Obbligatorio ai sensi dell'art. 11 della Legge 3/2003", verbose_name="Codice Unico di Progetto (CUP)")

    # Atto di nomina del RUP
    atto_nomina_rup = gismodels.BooleanField(default=False, verbose_name="Atto di nomina del RUP", db_column='atto_nom_rup', help_text="Spunta questa casella se è presente l'Atto di nomina del RUP")

    # Allegato Atto di nomina del RUP
    allegato_atto_nomina_rup = gismodels.FileField(verbose_name="Allegato Atto di nomina del RUP", upload_to='documents/atto_nomina_rup_rendis/%Y/%m/%d',null=True, blank=True, db_column='all_atto_nom_rup')

    # Intervento con opere accessorie: (SI/NO)
    intervento_opere_accessorie = gismodels.BooleanField(default=False, db_column='int_opere_acc', verbose_name="Intervento con opere accessorie")

    # Presenza di vincoli sovraordinati: (SI/NO)
    presenza_vincoli_sovraordinati = gismodels.NullBooleanField(blank=True, db_column='pres_vinc_sovr', verbose_name="Presenza di vincoli sovraordinati")

    # Descrizione delle opere accessorie strumentali
    desc_opere_acc_strum = gismodels.TextField(blank=True, null=True, db_column='desc_op_acc_strum', verbose_name='Descrizione delle opere accessorie strumentali', help_text="<b>Ai fini delle valutazioni sulla coerenza con le finalità di mitigazione del rischio idrogeologico, previste dal DPCM 24/02/2015 e s.m.i., vengono definite opere ammissibili quelle che appaiono in grado di incidere sulle cause o sugli effetti di un fenomeno di dissesto idrogeologico, contrastandone l'evoluzione e/o mitigandone gli effetti dannosi.<BR/>"
        "È quindi necessario che il proponente provveda ad individuare e scorporare, nell’insieme delle diverse opere che costituiscono il progetto, tutte quelle a cui non sia connesso un oggettivo ed evidente contribuito alle finalità di mitigazione del rischio idrogeologico, ripartendole nelle seguenti tipologie:<BR/><BR/>"
        "<ol type='a'><li> opere accessorie strumentali alla realizzazione, gestione, manutenzione dell'intervento principale;</li>"
        "<li> opere di compensazione e mitigazione volte a ridurre gli impatti negativi dell’intervento (ove presenti) o compensarli con altre azioni di valenza ambientale o naturalistica;</li>"
        "<li> ulteriori opere accessorie prive di efficacia diretta sulle cause o sugli effetti di un fenomeno di dissesto idrogeologico.</li></ol>"
        "Per ciascuna tipologia è richiesto che nella scheda venga fornita sia una descrizione delle opere considerate che la relativa quantificazione economica. "
        "Qualora le eventuali opere accessorie risultino correlate alla presenza di vincoli sovraordinati, questo andrà indicato nella scheda, riportandone sia la descrizione che i riferimenti normativi o, se del caso, allegando tra gli elaborati di progetto anche le note ufficiali con le prescrizioni ricevute. "
        "Se le opere accessorie strumentali incidono oltre il 10% del finanziamento statale è richiesta la dichiarazione (caricamento file) che l’importo eccedente non sarà a carico della quota statale (detratte, eventualmente, le opere conseguenti a vincoli sovraordinati, da descrivere e motivare dettagliatamente)."
        "Nel caso che, nella scheda, siano indicate opere di compensazione e mitigazione, la descrizione deve evidenziare gli impatti negativi dell’intervento che ne costituiscono il necessario presupposto."
        "Si segnala che gli interventi di ripristino di opere, manufatti ed infrastrutture danneggiati in conseguenza di un fenomeno di dissesto, sono sempre da considerare nella tipologia delle ulteriori opere accessorie (non strumentali), a meno che non svolgano essi stessi funzioni di mitigazione del rischio idrogeologico o risultino funzionali alla realizzazione, gestione e manutenzione dell’intervento principale."
        "Per contro le opere di ripristino connesse alle esigenze operative di cantiere sono da considerare opere accessorie strumentali in quanto parte integrante e conseguente all’intervento di mitigazione del rischio idrogeologico. Laddove, però, detti ripristini prevedano anche ampliamenti e miglioramenti tipologici dei manufatti coinvolti, la corrispondente quota di costo deve essere scorporata e riportata nella tipologia ulteriori opere accessorie.</b>")

    # Importo delle opere accessorie strumentali
    importo_opere_accessorie_strumentali = gismodels.DecimalField(blank=True, null=True, verbose_name="Importo delle opere accessorie strumentali", max_digits=11, decimal_places=2, db_column='imp_opere_acc_strum')

    # Descrizione delle ulteriori opere accessorie (non strumentali)
    desc_opere_acc_no_strum = gismodels.TextField(blank=True, null=True, db_column='desc_op_acc_no_strum', verbose_name='Descrizione delle ulteriori opere accessorie (non strumentali)')

    # Importo delle ulteriori opere accessorie (non strumentali)
    importo_opere_accessorie_no_strumentali = gismodels.DecimalField(blank=True, null=True, verbose_name="Importo delle ulteriori opere accessorie (non strumentali)", max_digits=11, decimal_places=2, db_column='imp_opere_acc_no_strum')

    # Intervento con opere di mitigazione o compensazione ambientale: (SI/NO)
    intervento_opere_mitigazione_compensazione = gismodels.BooleanField(default=False, db_column='int_opere_mitig_comp', verbose_name="Intervento con opere di mitigazione o compensazione ambientale")

    # Descrizione delle opere di mitigazione o compensazione ambientale
    desc_int_opere_mitig_comp = gismodels.TextField(blank=True, null=True, db_column='desc_int_opere_mitig_comp', verbose_name='Descrizione delle opere di mitigazione o compensazione ambientale')

    # Importo delle opere di mitigazione o compensazione ambientale
    importo_opere_mitig_comp = gismodels.DecimalField(blank=True, null=True, verbose_name="Importo delle opere di mitigazione o compensazione ambientale", max_digits=11, decimal_places=2, db_column='imp_opere_mitig_comp')

    #################################
    ########## END RENDIS ###########
    #################################

    ######################
    # RISORSE ECONOMICHE #
    ######################

    # Importo totale dell'Intervento (EURO)
    importo_totale_intervento = gismodels.DecimalField(verbose_name="Importo totale", max_digits=11, decimal_places=2, db_column='imp_tot_i', help_text="Importo totale dell'Intervento o del Progetto/Studio (Euro)")

    # Importo Richiesto (EURO)
    importo_richiesto = gismodels.DecimalField(max_digits=11, decimal_places=2, db_column='imp_ric', help_text="Importo richiesto (Euro)")

    # Importo Cofinanziato Altri (EURO)
    importo_cofinanziato_altri = gismodels.DecimalField(max_digits=11, decimal_places=2, db_column='imp_cof_a', help_text="Importo cofinanziato altri (Euro)")

    # Importo Cofinanziato Altri (EURO)
    ente_cofinanziatore = gismodels.TextField(db_column='ente_cofin', help_text="Ente cofinanziatore", null=True, blank=True)


    ###############
    # VALUTAZIONE #
    ###############

    # Efficacia
    efficacia = gismodels.ForeignKey(Efficacia, db_column='eff')

    # Efficacia Val (valore che viene calcolato dal programma in funzione del campo "Efficacia")
    efficacia_val = gismodels.SmallIntegerField(blank=False, db_column='eff_val')

    # Cantirabilita (SOLO SE INTERVENTO)
    cantierabilita = gismodels.ForeignKey(Cantierabilita,null=True, blank=True, db_column='cant', help_text='<b>Sono ammessi a finanziamento gli interventi che hanno almeno il progetto definitivo approvato dopo conferenza dei servizi, ai restanti interventi sar&#224; attribuito punteggio totale nullo e saranno acquisiti come segnalazione</b>')

    # Cantirabilita Val (SOLO SE INTERVENTO) (valore che viene calcolato dal programma in funzione del campo "Cantierabilita" )
    cantierabilita_val = gismodels.SmallIntegerField(null=True, blank=True, db_column='cant_val')

    # Necessita di variante urbanistica per vincolo preordinato all'esproprio (SOLO SE INTERVENTO)
    variante_urbanistica = gismodels.ForeignKey(ValoriSiNo,null=True, blank=True, related_name='valorisino_variante_urbanistica', db_column='var_urb', help_text="Necessita di variante urbanistica per vincolo preordinato all'esproprio")

    # Var urb Val (SOLO SE INTERVENTO) (valore che viene calcolato dal programma in funzione del campo "Necessita di variante urbanistica per vincolo preordinato all'esproprio" )
    variante_urbanistica_val = gismodels.SmallIntegerField(null=True, blank=True, db_column='var_urb_val')

    # Necessita di valutazione impatto ambientale (SOLO SE INTERVENTO)
    valutazione_impatto_ambientale = gismodels.ForeignKey(ValoriSiNo,null=True, blank=True, related_name='valorisino_valutazione_impatto_ambientale', db_column='val_imp_a', help_text="Necessita di valutazione impatto ambientale")

    # VIA Val (SOLO SE INTERVENTO) (valore che viene calcolato dal programma in funzione del campo "Necessita di valutazione impatto ambientale" )
    valutazione_impatto_ambientale_val = gismodels.SmallIntegerField(null=True, blank=True, db_column='val_imp_a_val')

    # Necessita di procedure di esproprio (SOLO SE INTERVENTO)
    esproprio = gismodels.ForeignKey(ValoriSiNo,null=True, blank=True, related_name='valorisino_esproprio', db_column='espr', help_text="Necessita di procedure di esproprio")

    # Espr Val (SOLO SE INTERVENTO) (valore che viene calcolato dal programma in funzione del campo "Necessita di procedure di esproprio" )
    esproprio_val = gismodels.SmallIntegerField(null=True, blank=True, db_column='espr_val')

    # Sostenibilita (SOLO SE INTERVENTO)
    sostenibilita = gismodels.ForeignKey(Sostenibilita,null=True, blank=True, db_column='sost')

    # Sostenibilita Val (SOLO SE INTERVENTO) (valore che viene calcolato dal programma in funzione del campo "Sostenibilita" )
    sostenibilita_val = gismodels.SmallIntegerField(null=True, blank=True, db_column='sost_val')

    # TOTALE (valore che viene calcolato dal programma e la somma  delle celle con la dicitura Val )
    totale = gismodels.SmallIntegerField(verbose_name="Punteggio provvisoriamente assegnato")

    ###########################
    # CONCLUSIONE ISTRUTTORIA #
    ###########################

    # Conclusione istruttoria
    conclusione_istruttoria = gismodels.NullBooleanField(blank=True, db_column='istruttoria', help_text="Se viene cliccato il pulsante <u><b><a style='color:#44AD41'>Istruttoria conclusa - Salva ed invia a ENTI + RT-Difesa Suolo</a></b></u> l'Istruttoria sar&#224; impostata come conclusa e verr&#224; inviata una email contenente un report della stessa ai seguenti indirizzi:<BR/> <ul><li><b>difesasuolo@regione.toscana.it,</b></li> <li><b>e-mail compilatore presente modulo,</b></li> <li><b>e-mail RUP</b></li><li><b>e-mail Provincia territorialmente competente</b></li><li><b>e-mail AdB territorialmente competente</b></li></ul></BR>Se viene cliccato il pulsante <u><b><a style='color:#44AD41'>Istruttoria conclusa - Salva ed invia SOLO a RT-Difesa Suolo</a></b></u> l'Istruttoria sar&#224; impostata come conclusa e verr&#224; inviata una email contenente un report della stessa al seguente indirizzo:<BR/> <ul><li><b>difesasuolo@regione.toscana.it</b></li></ul></BR>Se viene cliccato il pulsante <u><b><a style='color:#FF0000'>Istruttoria non conclusa - SALVA IN BOZZA</a></b></u> l'Istruttoria sar&#224; impostata come non conclusa e sar&#224; possibile inviarla in un secondo momento</BR><b>NOTA BENE: </b> Il pulsante SALVA IN BOZZA reimposta sempre l'istruttoria come non conclusa anche se precedentemente inviata")

    # Nominativo compilatore presente modulo
    nominativo_compilatore = gismodels.CharField(max_length=100, db_column='nom_c_mod', help_text="Nominativo compilatore presente modulo")

    # Email compilatore presente modulo
    email_comp = gismodels.EmailField(db_column='mail_c_mod', help_text="Email compilatore presente modulo")

    nuovi_geni_civili = gismodels.ForeignKey(GenioCivileBacino, null=True, blank=True, db_column='genio_c_bac',verbose_name="Genio Civile di Bacino") #models.CharField(blank=True, null=True, max_length=255, db_column='gen_civ_new')

    # Priorita 2
    #priorita = gismodels.ForeignKey(ValoriSiNo,null=True, blank=True, related_name='valorisino_priorita', db_column='priorita', help_text="Indicare SI se la richiesta/documentazione &#232; stata acquisita dopo il 16/10/14 <BR/> oppure se, nel caso di intervento l'avvio lavori &#232; successivo al 30/05/14")
    priorita = gismodels.NullBooleanField(blank=True, default=False, db_column='priorita', verbose_name="Priorita 2", help_text="Indicare <b><a style='color:#0000FF'>SI</a></b> se la richiesta/documentazione &#232; stata acquisita dopo il <b>16/10/14</b> <BR/> oppure se, nel caso di intervento, l'avvio lavori &#232; successivo al <b>30/05/14</b>")

    # Codice RENDIS
    codice_rendis = gismodels.CharField(blank=True, null=True, verbose_name="Codice RENDIS", max_length=20, db_column='cod_rendis')

    # Intervento con finanziamento totale già acquisito
    int_fin_tot_acq = gismodels.BooleanField(default=False, db_column='int_fin_tot_acq', verbose_name="Intervento con finanziamento totale già acquisito")

    # Estremi atto di finanziamento
    estremi_atto_fin = gismodels.CharField(null=True, blank=True, max_length=50, db_column='estremi_atto_fin', verbose_name="Estremi atto di finanziamento")
    
    # Data inserimento
    data_trasmissione_istruttoria = gismodels.DateTimeField(null=True, blank=True, db_column='data_trasm_istr')
    #sostenibilita = gismodels.ForeignKey(Sostenibilita,null=True, blank=True, db_column='sost')

    ######################
    # SEZIONE INTERNA RT #
    ######################

    # Finanziato anche in parte
    #finanziato_anche_in_parte = gismodels.NullBooleanField(blank=True, db_column='fin_parte')

    # A finanziamento
    #a_finanziamento = gismodels.NullBooleanField(blank=True, db_column='a_finanz')
    #nuovi_geni_civili = models.CharField(blank=True, null=True, max_length=255, db_column='gen_civ_new')

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.progetto_preliminare == True and self.progetto_definitivo == True:
            if self.mesi_approvazione_progetto_preliminare is not None and self.mesi_approvazione_progetto_definitivo is not None:
                if self.mesi_approvazione_progetto_preliminare > self.mesi_approvazione_progetto_definitivo:
                    raise ValidationError('Il numero di mesi per l\'APPROVAZIONE DEL PROGETTO DEFINITIVO non puo essere minore del numero di mesi per l\'APPROVAZIONE DEL PROGETTO PRELIMINARE')
                if self.mesi_approvazione_progetto_preliminare > self.mesi_approvazione_progetto_esecutivo:
                    raise ValidationError('Il numero di mesi per l\'APPROVAZIONE DEL PROGETTO ESECUTIVO non puo essere minore del numero di mesi per l\'APPROVAZIONE DEL PROGETTO PRELIMINARE')
                if self.mesi_approvazione_progetto_definitivo > self.mesi_approvazione_progetto_esecutivo:
                    raise ValidationError('Il numero di mesi per l\'APPROVAZIONE DEL PROGETTO ESECUTIVO non puo essere minore del numero di mesi per l\'APPROVAZIONE DEL PROGETTO DEFINITIVO')

            if self.progetto_preliminare == True and self.progetto_definitivo == False:
                if self.mesi_approvazione_progetto_preliminare > self.mesi_approvazione_progetto_esecutivo:
                    raise ValidationError('Il numero di mesi per l\'APPROVAZIONE DEL PROGETTO ESECUTIVO non puo essere minore del numero di mesi per l\'APPROVAZIONE DEL PROGETTO PRELIMINARE')

            if self.progetto_preliminare == False and self.progetto_definitivo == True:
                if self.mesi_approvazione_progetto_definitivo > self.mesi_approvazione_progetto_esecutivo:
                    raise ValidationError('Il numero di mesi per l\'APPROVAZIONE DEL PROGETTO ESECUTIVO non puo essere minore del numero di mesi per l\'APPROVAZIONE DEL PROGETTO DEFINITIVO')

    class Meta:
        verbose_name_plural = "Studi e Interventi"

    def __unicode__(self):
        return u"%s" % (self.codice_intervento)

#class Foto(models.Model):
#    intervento = models.ForeignKey(Intervento)
#    name = models.CharField(max_length=255)
#    foto = models.ImageField(upload_to='media')

#    class Meta:
#        verbose_name_plural = "Foto"
#
#    def __unicode__(self):
#        return self.name
#
#    def image_url(self):
#        return u'<img src="%s" alt="%s" width="80"></img>' % (self.foto.url, self.name)
#        image_url.allow_tags = True
