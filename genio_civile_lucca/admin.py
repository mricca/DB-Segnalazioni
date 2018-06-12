# -*- coding: utf-8 -*-
from django.core.mail import EmailMessage
#FOR REPORT PDF OUTPUT
from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, BaseDocTemplate
from reportlab.platypus.flowables import KeepTogether
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import styles, colors
from reportlab.pdfgen import canvas

from django.utils.encoding import smart_str

from django.contrib.gis.geos import GEOSGeometry
from django.http import HttpResponse
from django import forms
import datetime
from django.utils import timezone
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.contrib.gis import admin
from olwidget.admin import GeoModelAdmin
#from ajax_select import make_ajax_form
#from ajax_select.admin import AjaxSelectAdmin

from file_resubmit.admin import AdminResubmitImageWidget, AdminResubmitFileWidget

from models import Intervento, ComprensorioAll

from django.http import HttpResponseRedirect
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django import template
from django.contrib import messages
from django.utils.encoding import force_text
register = template.Library()

# Register your models here.

class RequiredFormSet(forms.models.BaseInlineFormSet):
      def __init__(self, *args, **kwargs):
          super(RequiredFormSet, self).__init__(*args, **kwargs)
          self.forms[0].empty_permitted = False

#class FotoAdminInline(admin.StackedInline):
#    model = Foto
#    extra = 1
#    formset = RequiredFormSet
#    list_display = [
#        'name',
#        'image_url',
#    ]

class CronoprogrammaAdminForm(forms.ModelForm):

    #coord_x = forms.DecimalField(label='Gauss Boaga [EPSG:3003] - X')
    #coord_y = forms.DecimalField(label='Gauss Boaga [EPSG:3003] - Y')
    #lat = forms.DecimalField(label='WGS84 [EPSG:4326] - LATITUDINE')
    #lon = forms.DecimalField(label='WGS84 [EPSG:4326]  - LONGITUDINE')

    #def __init__(self, *args, **kwargs):

    #    super(CronoprogrammaAdminForm,self).__init__(*args, **kwargs)
    #    self.fields['coord_x'].initial = 0
    #    self.fields['coord_y'].initial = 0
    #    self.fields['lat'].initial = 0
    #    self.fields['lon'].initial = 0

    class Meta:
        model = Intervento
        fields = '__all__'
        widgets = {
          'localita': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'descrizione_sintetica_intervento_studio': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'area_vasta_rif': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'codice_pericolosita_adb_pai': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'interventi_correlati': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'accordo_di_programma': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'note': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'riferimento_determina_approvazione_pp': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'riferimento_determina_approvazione_pd': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'riferimento_determina_approvazione_pe': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'classe_rischio_pai': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'ente_cofinanziatore': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'elenco_pareri': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'desc_opere_acc_strum': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'desc_opere_acc_no_strum': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'desc_int_opere_mitig_comp': forms.Textarea(attrs={'rows':2, 'cols':80}),
          'allegato_determina_approvazione_pp': AdminResubmitFileWidget,
          'allegato_determina_approvazione_pd': AdminResubmitFileWidget,
          'allegato_determina_approvazione_pe': AdminResubmitFileWidget,
          'allegato_documento_preliminare': AdminResubmitFileWidget,
          'allegato_atto_valutazione': AdminResubmitFileWidget,
          'allegato_atto_nomina_rup': AdminResubmitFileWidget,
          #'elaborati_progettuali': AdminResubmitFileWidget,
        }

    # PARTE DI CONTROLLO PER LE DATE CON CANTIRABILITA
    #def clean_cantierabilita(self):
    #    progetto_preliminare = self.cleaned_data['progetto_preliminare']
    #    cantierabilita = self.cleaned_data['cantierabilita'].id
    #    data_approvazione_progetto_preliminare = self.cleaned_data['data_approvazione_progetto_preliminare']
    #    today = datetime.date.today()
    #    studio_intervento = self.cleaned_data['studio_intervento'].text
    #    if studio_intervento == 'INTERVENTO' and progetto_preliminare == True:
    #        if isinstance(data_approvazione_progetto_preliminare, datetime.date):
    #            if data_approvazione_progetto_preliminare < today:
    #                raise forms.ValidationError("Hai toppato!")
    #    return cantierabilita

    # PARTE DI CONTROLLO PER IL PROGETTO PRELIMINARE

    def clean_mesi_approvazione_progetto_preliminare(self):
        #progetto_preliminare = self.cleaned_data['progetto_preliminare']
        mesi_approvazione_progetto_preliminare = self.cleaned_data['mesi_approvazione_progetto_preliminare']
        data_approvazione_progetto_preliminare = self.cleaned_data['data_approvazione_progetto_preliminare']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        #if studio_intervento == 'INTERVENTO' and progetto_preliminare == True:
        if studio_intervento == 'INTERVENTO':
            if (mesi_approvazione_progetto_preliminare is None) and not isinstance(data_approvazione_progetto_preliminare, datetime.date):
                #raise forms.ValidationError("Hai indicato come obbligatorio l'inserimento dei MESI di approvazione progetto preliminare!")
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return mesi_approvazione_progetto_preliminare

    def clean_allegato_determina_approvazione_pp(self):
        allegato_determina_approvazione_pp = self.cleaned_data['allegato_determina_approvazione_pp']
        riferimento_determina_approvazione_pp = self.cleaned_data['riferimento_determina_approvazione_pp']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        strip_text = riferimento_determina_approvazione_pp.strip()
        if studio_intervento == 'INTERVENTO' and strip_text != "":
            if allegato_determina_approvazione_pp is None:
                raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pp. Questo campo è obbligatorio!")
        return allegato_determina_approvazione_pp

    #def clean_data_determina_approvazione_pp(self):
    #    data_determina_approvazione_pp = self.cleaned_data['data_determina_approvazione_pp']
    #    riferimento_determina_approvazione_pp = self.cleaned_data['riferimento_determina_approvazione_pp']
    #    studio_intervento = self.cleaned_data['studio_intervento'].text
    #    strip_text = riferimento_determina_approvazione_pp.strip()
    #    if studio_intervento == 'INTERVENTO' and strip_text != "":
    #        if not isinstance(data_determina_approvazione_pp, datetime.date):
    #            raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pp. Questo campo e obbligatorio!")
    #    return data_determina_approvazione_pp

    # PARTE DI CONTROLLO PER IL PROGETTO DEFINITIVO
    def clean_mesi_approvazione_progetto_definitivo(self):
        #progetto_definitivo = self.cleaned_data['progetto_definitivo']
        mesi_approvazione_progetto_definitivo = self.cleaned_data['mesi_approvazione_progetto_definitivo']
        data_approvazione_progetto_definitivo = self.cleaned_data['data_approvazione_progetto_definitivo']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        #if studio_intervento == 'INTERVENTO' and progetto_definitivo == True:
        if studio_intervento == 'INTERVENTO':
            if (mesi_approvazione_progetto_definitivo is None) and not isinstance(data_approvazione_progetto_definitivo, datetime.date):
                #raise forms.ValidationError("Hai indicato come obbligatorio l'inserimento dei MESI di approvazione progetto definitivo!")
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return mesi_approvazione_progetto_definitivo

    def clean_allegato_determina_approvazione_pd(self):
        allegato_determina_approvazione_pd = self.cleaned_data['allegato_determina_approvazione_pd']
        riferimento_determina_approvazione_pd = self.cleaned_data['riferimento_determina_approvazione_pd']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        strip_text = riferimento_determina_approvazione_pd.strip()
        if studio_intervento == 'INTERVENTO' and strip_text != "":
            if allegato_determina_approvazione_pd is None:
                raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pd. Questo campo e obbligatorio!")
        return allegato_determina_approvazione_pd

    #def clean_data_determina_approvazione_pd(self):
    #    data_determina_approvazione_pd = self.cleaned_data['data_determina_approvazione_pd']
    #    riferimento_determina_approvazione_pd = self.cleaned_data['riferimento_determina_approvazione_pd']
    #    studio_intervento = self.cleaned_data['studio_intervento'].text
    #    strip_text = riferimento_determina_approvazione_pd.strip()
    #    if studio_intervento == 'INTERVENTO' and strip_text != "":
    #        if not isinstance(data_determina_approvazione_pd, datetime.date):
    #            raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pd. Questo campo e obbligatorio!")
    #    return data_determina_approvazione_pd

    # PARTE DI CONTROLLO PER IL PROGETTO ESECUTIVO
    def clean_mesi_approvazione_progetto_esecutivo(self):
        mesi_approvazione_progetto_esecutivo = self.cleaned_data['mesi_approvazione_progetto_esecutivo']
        data_approvazione_progetto_esecutivo = self.cleaned_data['data_approvazione_progetto_esecutivo']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if (mesi_approvazione_progetto_esecutivo is None) and not isinstance(data_approvazione_progetto_esecutivo, datetime.date):
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return mesi_approvazione_progetto_esecutivo

    def clean_allegato_determina_approvazione_pe(self):
        allegato_determina_approvazione_pe = self.cleaned_data['allegato_determina_approvazione_pe']
        riferimento_determina_approvazione_pe = self.cleaned_data['riferimento_determina_approvazione_pe']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        strip_text = riferimento_determina_approvazione_pe.strip()
        if studio_intervento == 'INTERVENTO' and strip_text != "":
            if allegato_determina_approvazione_pe is None:
                raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pe. Questo campo e obbligatorio!")
        return allegato_determina_approvazione_pe

    #def clean_data_determina_approvazione_pe(self):
    #    data_determina_approvazione_pe = self.cleaned_data['data_determina_approvazione_pe']
    #    riferimento_determina_approvazione_pe = self.cleaned_data['riferimento_determina_approvazione_pe']
    #    studio_intervento = self.cleaned_data['studio_intervento'].text
    #    strip_text = riferimento_determina_approvazione_pe.strip()
    #    if studio_intervento == 'INTERVENTO' and strip_text != "":
    #        if not isinstance(data_determina_approvazione_pe, datetime.date):
    #            raise forms.ValidationError("Hai riempito il campo riferimento_determina_approvazione_pe. Questo campo e obbligatorio!")
    #    return data_determina_approvazione_pe

    # PARTE DI CONTROLLO INIZIO-FINE LAVORI
    def clean_mesi_inizio_lavori(self):
        mesi_inizio_lavori = self.cleaned_data['mesi_inizio_lavori']
        inizio_lavori = self.cleaned_data['inizio_lavori']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if (mesi_inizio_lavori is None or mesi_inizio_lavori == 0) and not isinstance(inizio_lavori, datetime.date):
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return mesi_inizio_lavori

    def clean_mesi_fine_lavori(self):
        mesi_fine_lavori = self.cleaned_data['mesi_fine_lavori']
        fine_lavori = self.cleaned_data['fine_lavori']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if (mesi_fine_lavori is None or mesi_fine_lavori == 0) and not isinstance(fine_lavori, datetime.date):
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return mesi_fine_lavori

    def clean_elaborati_progettuali(self):
        elaborati_progettuali = self.cleaned_data['elaborati_progettuali']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if elaborati_progettuali is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Devi inserire gli Elaborati Progettuali!")
        return elaborati_progettuali

    def clean_descrizione_elaborati_prog(self):
        descrizione_elaborati_prog = self.cleaned_data['descrizione_elaborati_prog']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        strip_text = descrizione_elaborati_prog.strip()
        if studio_intervento == 'INTERVENTO':
            if strip_text == "":
                raise forms.ValidationError("Hai selezionato INTERVENTO. Devi inserire l'elenco degli Elaborati Progettuali!")
        return descrizione_elaborati_prog

    def clean_elenco_pareri(self):
        elenco_pareri = self.cleaned_data['elenco_pareri'].strip()
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if elenco_pareri == "":
                raise forms.ValidationError("Hai selezionato INTERVENTO. Devi inserire l'Elenco pareri da acquisire o acquisiti!")
        return elenco_pareri

    ################################################################################
    #PARTE DI VALIDAZIONE PER I CAMPI CORRELATI A "Intervento con opere accessorie"#
    ################################################################################

    def clean_presenza_vincoli_sovraordinati(self):
        presenza_vincoli_sovraordinati = self.cleaned_data['presenza_vincoli_sovraordinati']
        intervento_opere_accessorie = self.cleaned_data['intervento_opere_accessorie']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_accessorie == True:
            if presenza_vincoli_sovraordinati is None:
                raise forms.ValidationError("Hai selezionato Intervento con opere accessorie. Il campo Presenza di vincoli sovraordinati è obbligatorio!")
        return presenza_vincoli_sovraordinati

    def clean_desc_opere_acc_strum(self):
        desc_opere_acc_strum = self.cleaned_data['desc_opere_acc_strum'].strip()
        intervento_opere_accessorie = self.cleaned_data['intervento_opere_accessorie']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_accessorie == True:
            if desc_opere_acc_strum == "":
                raise forms.ValidationError("Hai selezionato Intervento con opere accessorie. Il campo Descrizione delle opere accessorie strumentali è obbligatorio!")
        return desc_opere_acc_strum

    def clean_importo_opere_accessorie_strumentali(self):
        importo_opere_accessorie_strumentali = self.cleaned_data['importo_opere_accessorie_strumentali']
        intervento_opere_accessorie = self.cleaned_data['intervento_opere_accessorie']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_accessorie == True:
            if importo_opere_accessorie_strumentali is None:
                raise forms.ValidationError("Hai selezionato Intervento con opere accessorie. Il campo Importo delle opere accessorie strumentali è obbligatorio!")
        return importo_opere_accessorie_strumentali

    def clean_desc_opere_acc_no_strum(self):
        desc_opere_acc_no_strum = self.cleaned_data['desc_opere_acc_no_strum'].strip()
        intervento_opere_accessorie = self.cleaned_data['intervento_opere_accessorie']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_accessorie == True:
            if desc_opere_acc_no_strum == "":
                raise forms.ValidationError("Hai selezionato Intervento con opere accessorie. Il campo Descrizione delle ulteriori opere accessorie (non strumentali) è obbligatorio!")
        return desc_opere_acc_no_strum

    def clean_importo_opere_accessorie_no_strumentali(self):
        importo_opere_accessorie_no_strumentali = self.cleaned_data['importo_opere_accessorie_no_strumentali']
        intervento_opere_accessorie = self.cleaned_data['intervento_opere_accessorie']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_accessorie == True:
            if importo_opere_accessorie_no_strumentali is None:
                raise forms.ValidationError("Hai selezionato Intervento con opere accessorie. Il campo Importo delle ulteriori opere accessorie (non strumentali) è obbligatorio!")
        return importo_opere_accessorie_no_strumentali

    ###########################################################################################
    #PARTE DI VALIDAZIONE PER I CAMPI CORRELATI A "intervento_opere_mitigazione_compensazione"#
    ###########################################################################################

    def clean_desc_int_opere_mitig_comp(self):
        desc_int_opere_mitig_comp = self.cleaned_data['desc_int_opere_mitig_comp'].strip()
        intervento_opere_mitigazione_compensazione = self.cleaned_data['intervento_opere_mitigazione_compensazione']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_mitigazione_compensazione == True:
            if desc_int_opere_mitig_comp == "":
                raise forms.ValidationError("Hai selezionato Intervento con opere di mitigazione o compensazione ambientale. Il campo Descrizione delle opere accessorie strumentali è obbligatorio!")
        return desc_int_opere_mitig_comp

    def clean_importo_opere_mitig_comp(self):
        importo_opere_mitig_comp = self.cleaned_data['importo_opere_mitig_comp']
        intervento_opere_mitigazione_compensazione = self.cleaned_data['intervento_opere_mitigazione_compensazione']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO' and intervento_opere_mitigazione_compensazione == True:
            if importo_opere_mitig_comp is None:
                raise forms.ValidationError("Hai selezionato Intervento con opere di mitigazione o compensazione ambientale. Il campo Importo delle opere di mitigazione o compensazione ambientale è obbligatorio!")
        return importo_opere_mitig_comp

    # PARTE DI CONTROLLOIN CASO DI PROGETTO/STUDIO MODIFICARE PER IL NUOVO CAMPO
    def clean_allegato_documento_preliminare(self):
        allegato_documento_preliminare = self.cleaned_data['allegato_documento_preliminare']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'PROGETTO/STUDIO':
            #if not isinstance(allegato_documento_preliminare, datetime.date):
            if allegato_documento_preliminare is None:
                raise forms.ValidationError("Hai selezionato PROGETTO/STUDIO. Questo campo e obbligatorio!")
        return allegato_documento_preliminare

    def clean_mesi_conclusione_relazione_finale(self):
        mesi_conclusione_relazione_finale = self.cleaned_data['mesi_conclusione_relazione_finale']
        conclusione_relazione_finale = self.cleaned_data['conclusione_relazione_finale']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'PROGETTO/STUDIO':
            if (mesi_conclusione_relazione_finale is None or mesi_conclusione_relazione_finale == 0) and not isinstance(conclusione_relazione_finale, datetime.date):
                raise forms.ValidationError("Hai selezionato PROGETTO/STUDIO. Questo campo e obbligatorio!")
        return mesi_conclusione_relazione_finale

    # PARTE DI CONTROLLO IN CASO DI INTERVENTO PER IL FIELDSET VALUTAZIONE
    def clean_cantierabilita(self):
        cantierabilita = self.cleaned_data['cantierabilita']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if cantierabilita is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return cantierabilita

    def clean_variante_urbanistica(self):
        variante_urbanistica = self.cleaned_data['variante_urbanistica']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if variante_urbanistica is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return variante_urbanistica

    def clean_valutazione_impatto_ambientale(self):
        valutazione_impatto_ambientale = self.cleaned_data['valutazione_impatto_ambientale']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if valutazione_impatto_ambientale is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return valutazione_impatto_ambientale

    def clean_esproprio(self):
        esproprio = self.cleaned_data['esproprio']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if esproprio is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return esproprio

    def clean_sostenibilita(self):
        sostenibilita = self.cleaned_data['sostenibilita']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if sostenibilita is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return sostenibilita

    def clean_tipologia_intervento(self):
        tipologia_intervento = self.cleaned_data['tipologia_intervento']
        studio_intervento = self.cleaned_data['studio_intervento'].text
        if studio_intervento == 'INTERVENTO':
            if tipologia_intervento is None:
                raise forms.ValidationError("Hai selezionato INTERVENTO. Questo campo e obbligatorio!")
        return tipologia_intervento

    def clean_cat_int(self):
        categoria_intervento = self.cleaned_data['cat_int']
        if categoria_intervento is None:
            raise forms.ValidationError("Questo campo e obbligatorio!")
        return categoria_intervento

    def clean_area_vasta_rif(self):
        area_vasta = self.cleaned_data['area_vasta_rif']
        try:
            self.cleaned_data['cat_int']
            categoria_intervento = self.cleaned_data['cat_int'].id
            strip_text = area_vasta.strip()
            if categoria_intervento == '02' and strip_text == "":
                raise forms.ValidationError("Hai selezionato 'Interventi complessi di area vasta'. La compilazione è obbligatoria!")
        except KeyError:
            return area_vasta

    def clean_codice_pericolosita_adb_pai(self):
        codice_pericolosita_adb_pai = self.cleaned_data['codice_pericolosita_adb_pai']
        perimetrazione_autorita_di_bacino = self.cleaned_data['perimetrazione_autorita_di_bacino']
        strip_text = codice_pericolosita_adb_pai.strip()
        if perimetrazione_autorita_di_bacino is True:
            if strip_text == "":
                raise forms.ValidationError("Hai selezionato Perimetrazione Autorita di Bacino. Questo campo e obbligatorio!")
        return codice_pericolosita_adb_pai

    def clean_allegato_atto_valutazione(self):
        atto_valutazione = self.cleaned_data['atto_valutazione']
        allegato_atto_valutazione = self.cleaned_data['allegato_atto_valutazione']
        if atto_valutazione == True:
            if (allegato_atto_valutazione is None):
                raise forms.ValidationError("Hai indicato che è presente l'Atto di validazione del progetto! Inserisci l'allegato")
        return allegato_atto_valutazione

    def clean_allegato_atto_nomina_rup(self):
        atto_nomina_rup = self.cleaned_data['atto_nomina_rup']
        allegato_atto_nomina_rup = self.cleaned_data['allegato_atto_nomina_rup']
        if atto_nomina_rup == True:
            if (allegato_atto_nomina_rup is None):
                raise forms.ValidationError("Hai indicato che è presente l'Atto di nomina del RUP! Inserisci l'allegato")
        return allegato_atto_nomina_rup

    def clean_estremi_atto_fin(self):
        int_fin_tot_acq = self.cleaned_data['int_fin_tot_acq']
        estremi_atto_fin = self.cleaned_data['estremi_atto_fin']
        strip_text = estremi_atto_fin.strip()
        if int_fin_tot_acq == True:
            if strip_text == "":
                raise forms.ValidationError("Hai indicato che l'intervento ha un finanziamento totale già acquisito! Questo campo è obbligatorio!")
        return estremi_atto_fin

def export_pdf_single(modeladmin, request, queryset, cod = None):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Studi_Intervento_Lucca.pdf"'

    buffer = BytesIO()

    #p = canvas.Canvas(buffer)
    p = SimpleDocTemplate(buffer,pagesize=A4)
    styles = getSampleStyleSheet()
    Catalog = []
    #I = Image('http://172.16.1.141:8081/static/admin/images/logoregione.png')
    I = Image('http://159.213.57.81/static/admin/images/logoregione.png')
    Catalog.append(I)
    style = styles["BodyText"]
    style.alignment = TA_LEFT

    header = Paragraph('''<para align=center spaceb=3><b><font color=red >Studi e Interventi Lucca</font></b></para>''', style)
    Catalog.append(header)

    headings = ('Attributo', 'Valore')
    allproducts = []

    for obj in queryset:
        if obj.codice_intervento == cod:
            allproducts.append([Paragraph(smart_str(u"codice_intervento"),style),Paragraph(smart_str(obj.codice_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"bacino_idrografico"),style),Paragraph(smart_str(obj.bacino_idrografico),style)])
            allproducts.append([Paragraph(smart_str(u"comprensorio"),style),Paragraph(smart_str(obj.comprensorio),style)])
            allproducts.append([Paragraph(smart_str(u"provincia"),style),Paragraph(smart_str(obj.provincia),style)])
            allproducts.append([Paragraph(smart_str(u"comune"),style),Paragraph(smart_str(obj.comune),style)])
            allproducts.append([Paragraph(smart_str(u"localita"),style),Paragraph(smart_str(obj.localita),style)])
            allproducts.append([Paragraph(smart_str(u"corso_acqua"),style),Paragraph(smart_str(obj.corso_acqua),style)])
            allproducts.append([Paragraph(smart_str(u"reticolo_gestione"),style),Paragraph(smart_str(obj.reticolo_gestione),style)])
            allproducts.append([Paragraph(smart_str(u"geometria"),style),Paragraph(smart_str(obj.fenomeno_aggiunto),style)])
            allproducts.append([Paragraph(smart_str(u"fenomeno"),style),Paragraph(smart_str(obj.fenomeno),style)])
            allproducts.append([Paragraph(smart_str(u"studio_intervento"),style),Paragraph(smart_str(obj.studio_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"tipologia_intervento"),style),Paragraph(smart_str(obj.tipologia_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"tipo_di_opera"),style),Paragraph(smart_str(obj.tipo_di_opera),style)])
            allproducts.append([Paragraph(smart_str(u"cat_int"),style),Paragraph(smart_str(obj.cat_int),style)])
            allproducts.append([Paragraph(smart_str(u"area_vasta_rif"),style),Paragraph(smart_str(obj.area_vasta_rif),style)])
            allproducts.append([Paragraph(smart_str(u"titolo_intervento_studio"),style),Paragraph(smart_str(obj.titolo_intervento_studio),style)])
            allproducts.append([Paragraph(smart_str(u"descrizione_sintetica_intervento_studio"),style),Paragraph(smart_str(obj.descrizione_sintetica_intervento_studio),style)])
            allproducts.append([Paragraph(smart_str(u"categoria_idr_opera"),style),Paragraph(smart_str(obj.categoria_idr_opera),style)])
            allproducts.append([Paragraph(smart_str(u"perimetrazione_autorita_di_bacino"),style),Paragraph(smart_str(obj.perimetrazione_autorita_di_bacino),style)])
            allproducts.append([Paragraph(smart_str(u"Classe pericolosita PAI o PGRA attuale"),style),Paragraph(smart_str(obj.codice_pericolosita_adb_pai),style)])
            allproducts.append([Paragraph(smart_str(u"Classe rischio PAI o PGRA attuale"),style),Paragraph(smart_str(obj.classe_rischio_pai),style)])
            allproducts.append([Paragraph(smart_str(u"perimetrazione_pericolosita_attuale"),style),Paragraph(smart_str(obj.perimetrazione_pericolosita_attuale),style)])
            allproducts.append([Paragraph(smart_str(u"perimetrazione_pericolosita_post_intervento"),style),Paragraph(smart_str(obj.perimetrazione_pericolosita_post_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"stima_rischio_diretto_attuale"),style),Paragraph(smart_str(obj.stima_rischio_diretto_attuale),style)])
            allproducts.append([Paragraph(smart_str(u"stima_rischio_indiretto_attuale"),style),Paragraph(smart_str(obj.stima_rischio_indiretto_attuale),style)])
            allproducts.append([Paragraph(smart_str(u"stima_rischio_diretto_intervento"),style),Paragraph(smart_str(obj.stima_rischio_diretto_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"stima_rischio_indiretto_intervento"),style),Paragraph(smart_str(obj.stima_rischio_indiretto_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"ente_proponente"),style),Paragraph(smart_str(obj.ente_proponente),style)])
            allproducts.append([Paragraph(smart_str(u"ente_attuatore_competente"),style),Paragraph(smart_str(obj.ente_attuatore_competente),style)])
            allproducts.append([Paragraph(smart_str(u"nominativo"),style),Paragraph(smart_str(obj.nominativo),style)])
            allproducts.append([Paragraph(smart_str(u"email"),style),Paragraph(smart_str(obj.email),style)])
            allproducts.append([Paragraph(smart_str(u"recapito_telefonico"),style),Paragraph(smart_str(obj.recapito_telefonico),style)])
            allproducts.append([Paragraph(smart_str(u"interventi_correlati"),style),Paragraph(smart_str(obj.interventi_correlati),style)])
            allproducts.append([Paragraph(smart_str(u"stralcio_funzionale"),style),Paragraph(smart_str(obj.stralcio_funzionale),style)])
            allproducts.append([Paragraph(smart_str(u"accordo_di_programma"),style),Paragraph(smart_str(obj.accordo_di_programma),style)])
            allproducts.append([Paragraph(smart_str(u"note"),style),Paragraph(smart_str(obj.note),style)])
            allproducts.append([Paragraph(smart_str(u"progetto_preliminare"),style),Paragraph(smart_str(obj.progetto_preliminare),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_preliminare"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_preliminare),style)])
            allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_preliminare"),style),Paragraph(smart_str(obj.data_approvazione_progetto_preliminare),style)])
            allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pp"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pp),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pp"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pp),style)])
            allproducts.append([Paragraph(smart_str(u"progetto_definitivo"),style),Paragraph(smart_str(obj.progetto_definitivo),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_definitivo"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_definitivo),style)])
            allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_definitivo"),style),Paragraph(smart_str(obj.data_approvazione_progetto_definitivo),style)])
            allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pd"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pd),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pd"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pd),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_esecutivo"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_esecutivo),style)])
            allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_esecutivo"),style),Paragraph(smart_str(obj.data_approvazione_progetto_esecutivo),style)])
            allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pe"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pe),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pe"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pe),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_inizio_lavori"),style),Paragraph(smart_str(obj.mesi_inizio_lavori),style)])
            allproducts.append([Paragraph(smart_str(u"inizio_lavori"),style),Paragraph(smart_str(obj.inizio_lavori),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_fine_lavori"),style),Paragraph(smart_str(obj.mesi_fine_lavori),style)])
            allproducts.append([Paragraph(smart_str(u"fine_lavori"),style),Paragraph(smart_str(obj.fine_lavori),style)])
            allproducts.append([Paragraph(smart_str(u"elaborati_progettuali"),style),Paragraph(smart_str(obj.elaborati_progettuali),style)])
            allproducts.append([Paragraph(smart_str(u"descrizione_elaborati_prog"),style),Paragraph(smart_str(obj.descrizione_elaborati_prog),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_documento_preliminare"),style),Paragraph(smart_str(obj.allegato_documento_preliminare),style)])
            allproducts.append([Paragraph(smart_str(u"conclusione_relazione_finale"),style),Paragraph(smart_str(obj.conclusione_relazione_finale),style)])
            allproducts.append([Paragraph(smart_str(u"mesi_conclusione_relazione_finale"),style),Paragraph(smart_str(obj.mesi_conclusione_relazione_finale),style)])
            allproducts.append([Paragraph(smart_str(u"elenco_pareri"),style),Paragraph(smart_str(obj.elenco_pareri),style)])
            allproducts.append([Paragraph(smart_str(u"atto_valutazione"),style),Paragraph(smart_str(obj.atto_valutazione),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_atto_valutazione"),style),Paragraph(smart_str(obj.allegato_atto_valutazione),style)])
            allproducts.append([Paragraph(smart_str(u"codice_unico_progetto"),style),Paragraph(smart_str(obj.codice_unico_progetto),style)])
            allproducts.append([Paragraph(smart_str(u"atto_nomina_rup"),style),Paragraph(smart_str(obj.atto_nomina_rup),style)])
            allproducts.append([Paragraph(smart_str(u"allegato_atto_nomina_rup"),style),Paragraph(smart_str(obj.allegato_atto_nomina_rup),style)])
            allproducts.append([Paragraph(smart_str(u"intervento_opere_accessorie"),style),Paragraph(smart_str(obj.intervento_opere_accessorie),style)])
            allproducts.append([Paragraph(smart_str(u"presenza_vincoli_sovraordinati"),style),Paragraph(smart_str(obj.presenza_vincoli_sovraordinati),style)])
            allproducts.append([Paragraph(smart_str(u"desc_opere_acc_strum"),style),Paragraph(smart_str(obj.desc_opere_acc_strum),style)])
            allproducts.append([Paragraph(smart_str(u"importo_opere_accessorie_strumentali"),style),Paragraph(smart_str(obj.importo_opere_accessorie_strumentali),style)])
            allproducts.append([Paragraph(smart_str(u"desc_opere_acc_no_strum"),style),Paragraph(smart_str(obj.desc_opere_acc_no_strum),style)])
            allproducts.append([Paragraph(smart_str(u"importo_opere_accessorie_no_strumentali"),style),Paragraph(smart_str(obj.importo_opere_accessorie_no_strumentali),style)])
            allproducts.append([Paragraph(smart_str(u"intervento_opere_mitigazione_compensazione"),style),Paragraph(smart_str(obj.intervento_opere_mitigazione_compensazione),style)])
            allproducts.append([Paragraph(smart_str(u"desc_int_opere_mitig_comp"),style),Paragraph(smart_str(obj.desc_int_opere_mitig_comp),style)])
            allproducts.append([Paragraph(smart_str(u"importo_opere_mitig_comp"),style),Paragraph(smart_str(obj.importo_opere_mitig_comp),style)])
            allproducts.append([Paragraph(smart_str(u"importo_totale_intervento"),style),Paragraph(smart_str(obj.importo_totale_intervento),style)])
            allproducts.append([Paragraph(smart_str(u"importo_richiesto"),style),Paragraph(smart_str(obj.importo_richiesto),style)])
            allproducts.append([Paragraph(smart_str(u"importo_cofinanziato_altri"),style),Paragraph(smart_str(obj.importo_cofinanziato_altri),style)])
            allproducts.append([Paragraph(smart_str(u"ente_cofinanziatore"),style),Paragraph(smart_str(obj.ente_cofinanziatore),style)])
            allproducts.append([Paragraph(smart_str(u"efficacia"),style),Paragraph(smart_str(obj.efficacia),style)])
            #allproducts.append([Paragraph(smart_str(u"efficacia_val"),style),Paragraph(smart_str(obj.efficacia_val),style)])
            allproducts.append([Paragraph(smart_str(u"cantierabilita"),style),Paragraph(smart_str(obj.cantierabilita),style)])
            #allproducts.append([Paragraph(smart_str(u"cantierabilita_val"),style),Paragraph(smart_str(obj.cantierabilita_val),style)])
            allproducts.append([Paragraph(smart_str(u"variante_urbanistica"),style),Paragraph(smart_str(obj.variante_urbanistica),style)])
            #allproducts.append([Paragraph(smart_str(u"variante_urbanistica_val"),style),Paragraph(smart_str(obj.variante_urbanistica_val),style)])
            allproducts.append([Paragraph(smart_str(u"valutazione_impatto_ambientale"),style),Paragraph(smart_str(obj.valutazione_impatto_ambientale),style)])
            #allproducts.append([Paragraph(smart_str(u"valutazione_impatto_ambientale_val"),style),Paragraph(smart_str(obj.valutazione_impatto_ambientale_val),style)])
            allproducts.append([Paragraph(smart_str(u"esproprio"),style),Paragraph(smart_str(obj.esproprio),style)])
            #allproducts.append([Paragraph(smart_str(u"esproprio_val"),style),Paragraph(smart_str(obj.esproprio_val),style)])
            allproducts.append([Paragraph(smart_str(u"sostenibilita"),style),Paragraph(smart_str(obj.sostenibilita),style)])
            #allproducts.append([Paragraph(smart_str(u"sostenibilita_val"),style),Paragraph(smart_str(obj.sostenibilita_val),style)])
            #allproducts.append([Paragraph(smart_str(u"Punteggio provvisoriamente assegnato"),style),Paragraph(smart_str(obj.totale),style)])
            allproducts.append([Paragraph(smart_str(u"conclusione_istruttoria"),style),Paragraph(smart_str(obj.conclusione_istruttoria),style)])
            allproducts.append([Paragraph(smart_str(u"nominativo_compilatore"),style),Paragraph(smart_str(obj.nominativo_compilatore),style)])
            allproducts.append([Paragraph(smart_str(u"email_comp"),style),Paragraph(smart_str(obj.email_comp),style)])
            allproducts.append([Paragraph(smart_str(u"Geni_civili_02_2016"),style),Paragraph(smart_str(obj.nuovi_geni_civili),style)])
            allproducts.append([Paragraph(smart_str(u"priorita"),style),Paragraph(smart_str(obj.priorita),style)])
            allproducts.append([Paragraph(smart_str(u"codice_rendis"),style),Paragraph(smart_str(obj.codice_rendis),style)])
            allproducts.append([Paragraph(smart_str(u"int_fin_tot_acq"),style),Paragraph(smart_str(obj.int_fin_tot_acq),style)])
            allproducts.append([Paragraph(smart_str(u"estremi_atto_fin"),style),Paragraph(smart_str(obj.estremi_atto_fin),style)])
            allproducts.append([Paragraph(smart_str(u"data_trasmissione_istruttoria"),style),Paragraph(smart_str(obj.data_trasmissione_istruttoria),style)])

            #if request.user.is_superuser:
                #allproducts.append([smart_str(u"a_finanziamento"),Paragraph(smart_str(obj.a_finanziamento),style)])

    t = Table([headings] + allproducts,[150,350])
    t.setStyle(TableStyle([('GRID', (0,0), (1,-1), 2, colors.black),('LINEBELOW', (0,0), (-1,0), 2, colors.red),('BACKGROUND', (0, 0), (-1, 0), colors.pink)]))
    Catalog.append(t)
    p.build(Catalog)

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return pdf

def export_pdf(modeladmin, request, queryset):

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Studi_Intervento_Lucca.pdf"'

    buffer = BytesIO()

    #p = canvas.Canvas(buffer)
    p = SimpleDocTemplate(buffer,pagesize=A4)
    styles = getSampleStyleSheet()

    Catalog = []
    #I = Image('http://172.16.1.141:8081/static/admin/images/logoregione.png')
    I = Image('http://159.213.57.81/static/admin/images/logoregione.png')

    Catalog.append(I)
    style = styles["BodyText"]
    style.alignment = TA_LEFT

    header = Paragraph('''<para align=center spaceb=3><b><font color=red >Studi e Interventi Lucca</font></b></para>''', style)
    Catalog.append(header)

    headings = ('Attributo', 'Valore')
    allproducts = []

    for obj in queryset:
        #pnt = GEOSGeometry(obj.fenomeno_aggiunto)

        #left = pnt.extent[0] - 220
        #bottom = pnt.extent[1] - 220
        #right = pnt.extent[2] + 220
        #top = pnt.extent[3] + 220

        #ORTOFOTO = Image('http://web.regione.toscana.it/wmsraster/com.rt.wms.RTmap/wms?map=wmsofc&LAYERS=rt_ofc.10k13&VERSION=1.3.0&FORMAT=image%2Fpng&TRANSPARENT=true&BGCOLOR=%23FFFFFF&EXCEPTIONS=INIMAGE&SERVICE=WMS&REQUEST=GetMap&STYLES=&CRS=EPSG%3A3003&BBOX=' + smart_str(left) + ',' + smart_str(bottom) + ',' + smart_str(right) + ',' + smart_str(top) + '&WIDTH=220&HEIGHT=220')
        #ORTOFOTO.drawHeight = 220
        #ORTOFOTO.drawWidth = 220

        #ORTOFOTOP = Paragraph('''<para align=center spaceb=3>The <b>ReportLab Left<font color=red>Logo</font></b>ORTOFOTO</para>''',style)

        #WMS = Image('http://159.213.57.81/geoserver/wms?LAYERS=db_segnalazioni:genio_civile_pisa_view&VERSION=1.3.0&FORMAT=image/png&TRANSPARENT=true&SERVICE=WMS&REQUEST=GetMap&STYLES=&CRS=EPSG:3003&BBOX=' + smart_str(left) + ',' + smart_str(bottom) + ',' + smart_str(right) + ',' + smart_str(top) + '&WIDTH=220&HEIGHT=220')
        #WMS.drawHeight = 220
        #WMS.drawWidth = 220

        #WMSP = Paragraph('''<para align=center spaceb=3>The <b>ReportLab Left<font color=red>Logo</font></b>WMS</para>''', style)

        allproducts.append([Paragraph(smart_str(u"codice_intervento"),style),Paragraph(smart_str(obj.codice_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"bacino_idrografico"),style),Paragraph(smart_str(obj.bacino_idrografico),style)])
        allproducts.append([Paragraph(smart_str(u"comprensorio"),style),Paragraph(smart_str(obj.comprensorio),style)])
        allproducts.append([Paragraph(smart_str(u"provincia"),style),Paragraph(smart_str(obj.provincia),style)])
        allproducts.append([Paragraph(smart_str(u"comune"),style),Paragraph(smart_str(obj.comune),style)])
        allproducts.append([Paragraph(smart_str(u"localita"),style),Paragraph(smart_str(obj.localita),style)])
        allproducts.append([Paragraph(smart_str(u"corso_acqua"),style),Paragraph(smart_str(obj.corso_acqua),style)])
        allproducts.append([Paragraph(smart_str(u"reticolo_gestione"),style),Paragraph(smart_str(obj.reticolo_gestione),style)])
        allproducts.append([Paragraph(smart_str(u"geometria"),style),Paragraph(smart_str(obj.fenomeno_aggiunto),style)])
        allproducts.append([Paragraph(smart_str(u"fenomeno"),style),Paragraph(smart_str(obj.fenomeno),style)])
        allproducts.append([Paragraph(smart_str(u"studio_intervento"),style),Paragraph(smart_str(obj.studio_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"tipologia_intervento"),style),Paragraph(smart_str(obj.tipologia_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"tipo_di_opera"),style),Paragraph(smart_str(obj.tipo_di_opera),style)])
        allproducts.append([Paragraph(smart_str(u"cat_int"),style),Paragraph(smart_str(obj.cat_int),style)])
        allproducts.append([Paragraph(smart_str(u"area_vasta_rif"),style),Paragraph(smart_str(obj.area_vasta_rif),style)])
        allproducts.append([Paragraph(smart_str(u"titolo_intervento_studio"),style),Paragraph(smart_str(obj.titolo_intervento_studio),style)])
        allproducts.append([Paragraph(smart_str(u"descrizione_sintetica_intervento_studio"),style),Paragraph(smart_str(obj.descrizione_sintetica_intervento_studio),style)])
        allproducts.append([Paragraph(smart_str(u"categoria_idr_opera"),style),Paragraph(smart_str(obj.categoria_idr_opera),style)])
        allproducts.append([Paragraph(smart_str(u"perimetrazione_autorita_di_bacino"),style),Paragraph(smart_str(obj.perimetrazione_autorita_di_bacino),style)])
        allproducts.append([Paragraph(smart_str(u"Classe pericolosita PAI o PGRA attuale"),style),Paragraph(smart_str(obj.codice_pericolosita_adb_pai),style)])
        allproducts.append([Paragraph(smart_str(u"Classe rischio PAI o PGRA attuale"),style),Paragraph(smart_str(obj.classe_rischio_pai),style)])
        allproducts.append([Paragraph(smart_str(u"perimetrazione_pericolosita_attuale"),style),Paragraph(smart_str(obj.perimetrazione_pericolosita_attuale),style)])
        allproducts.append([Paragraph(smart_str(u"perimetrazione_pericolosita_post_intervento"),style),Paragraph(smart_str(obj.perimetrazione_pericolosita_post_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"stima_rischio_diretto_attuale"),style),Paragraph(smart_str(obj.stima_rischio_diretto_attuale),style)])
        allproducts.append([Paragraph(smart_str(u"stima_rischio_indiretto_attuale"),style),Paragraph(smart_str(obj.stima_rischio_indiretto_attuale),style)])
        allproducts.append([Paragraph(smart_str(u"stima_rischio_diretto_intervento"),style),Paragraph(smart_str(obj.stima_rischio_diretto_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"stima_rischio_indiretto_intervento"),style),Paragraph(smart_str(obj.stima_rischio_indiretto_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"ente_proponente"),style),Paragraph(smart_str(obj.ente_proponente),style)])
        allproducts.append([Paragraph(smart_str(u"ente_attuatore_competente"),style),Paragraph(smart_str(obj.ente_attuatore_competente),style)])
        allproducts.append([Paragraph(smart_str(u"nominativo"),style),Paragraph(smart_str(obj.nominativo),style)])
        allproducts.append([Paragraph(smart_str(u"email"),style),Paragraph(smart_str(obj.email),style)])
        allproducts.append([Paragraph(smart_str(u"recapito_telefonico"),style),Paragraph(smart_str(obj.recapito_telefonico),style)])
        allproducts.append([Paragraph(smart_str(u"interventi_correlati"),style),Paragraph(smart_str(obj.interventi_correlati),style)])
        allproducts.append([Paragraph(smart_str(u"stralcio_funzionale"),style),Paragraph(smart_str(obj.stralcio_funzionale),style)])
        allproducts.append([Paragraph(smart_str(u"accordo_di_programma"),style),Paragraph(smart_str(obj.accordo_di_programma),style)])
        allproducts.append([Paragraph(smart_str(u"note"),style),Paragraph(smart_str(obj.note),style)])
        allproducts.append([Paragraph(smart_str(u"progetto_preliminare"),style),Paragraph(smart_str(obj.progetto_preliminare),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_preliminare"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_preliminare),style)])
        allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_preliminare"),style),Paragraph(smart_str(obj.data_approvazione_progetto_preliminare),style)])
        allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pp"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pp),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pp"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pp),style)])
        allproducts.append([Paragraph(smart_str(u"progetto_definitivo"),style),Paragraph(smart_str(obj.progetto_definitivo),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_definitivo"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_definitivo),style)])
        allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_definitivo"),style),Paragraph(smart_str(obj.data_approvazione_progetto_definitivo),style)])
        allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pd"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pd),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pd"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pd),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_approvazione_progetto_esecutivo"),style),Paragraph(smart_str(obj.mesi_approvazione_progetto_esecutivo),style)])
        allproducts.append([Paragraph(smart_str(u"data_approvazione_progetto_esecutivo"),style),Paragraph(smart_str(obj.data_approvazione_progetto_esecutivo),style)])
        allproducts.append([Paragraph(smart_str(u"riferimento_determina_approvazione_pe"),style),Paragraph(smart_str(obj.riferimento_determina_approvazione_pe),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_determina_approvazione_pe"),style),Paragraph(smart_str(obj.allegato_determina_approvazione_pe),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_inizio_lavori"),style),Paragraph(smart_str(obj.mesi_inizio_lavori),style)])
        allproducts.append([Paragraph(smart_str(u"inizio_lavori"),style),Paragraph(smart_str(obj.inizio_lavori),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_fine_lavori"),style),Paragraph(smart_str(obj.mesi_fine_lavori),style)])
        allproducts.append([Paragraph(smart_str(u"fine_lavori"),style),Paragraph(smart_str(obj.fine_lavori),style)])
        allproducts.append([Paragraph(smart_str(u"elaborati_progettuali"),style),Paragraph(smart_str(obj.elaborati_progettuali),style)])
        allproducts.append([Paragraph(smart_str(u"descrizione_elaborati_prog"),style),Paragraph(smart_str(obj.descrizione_elaborati_prog),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_documento_preliminare"),style),Paragraph(smart_str(obj.allegato_documento_preliminare),style)])
        allproducts.append([Paragraph(smart_str(u"conclusione_relazione_finale"),style),Paragraph(smart_str(obj.conclusione_relazione_finale),style)])
        allproducts.append([Paragraph(smart_str(u"mesi_conclusione_relazione_finale"),style),Paragraph(smart_str(obj.mesi_conclusione_relazione_finale),style)])
        allproducts.append([Paragraph(smart_str(u"elenco_pareri"),style),Paragraph(smart_str(obj.elenco_pareri),style)])
        allproducts.append([Paragraph(smart_str(u"atto_valutazione"),style),Paragraph(smart_str(obj.atto_valutazione),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_atto_valutazione"),style),Paragraph(smart_str(obj.allegato_atto_valutazione),style)])
        allproducts.append([Paragraph(smart_str(u"codice_unico_progetto"),style),Paragraph(smart_str(obj.codice_unico_progetto),style)])
        allproducts.append([Paragraph(smart_str(u"atto_nomina_rup"),style),Paragraph(smart_str(obj.atto_nomina_rup),style)])
        allproducts.append([Paragraph(smart_str(u"allegato_atto_nomina_rup"),style),Paragraph(smart_str(obj.allegato_atto_nomina_rup),style)])
        allproducts.append([Paragraph(smart_str(u"intervento_opere_accessorie"),style),Paragraph(smart_str(obj.intervento_opere_accessorie),style)])
        allproducts.append([Paragraph(smart_str(u"presenza_vincoli_sovraordinati"),style),Paragraph(smart_str(obj.presenza_vincoli_sovraordinati),style)])
        allproducts.append([Paragraph(smart_str(u"desc_opere_acc_strum"),style),Paragraph(smart_str(obj.desc_opere_acc_strum),style)])
        allproducts.append([Paragraph(smart_str(u"importo_opere_accessorie_strumentali"),style),Paragraph(smart_str(obj.importo_opere_accessorie_strumentali),style)])
        allproducts.append([Paragraph(smart_str(u"desc_opere_acc_no_strum"),style),Paragraph(smart_str(obj.desc_opere_acc_no_strum),style)])
        allproducts.append([Paragraph(smart_str(u"importo_opere_accessorie_no_strumentali"),style),Paragraph(smart_str(obj.importo_opere_accessorie_no_strumentali),style)])
        allproducts.append([Paragraph(smart_str(u"intervento_opere_mitigazione_compensazione"),style),Paragraph(smart_str(obj.intervento_opere_mitigazione_compensazione),style)])
        allproducts.append([Paragraph(smart_str(u"desc_int_opere_mitig_comp"),style),Paragraph(smart_str(obj.desc_int_opere_mitig_comp),style)])
        allproducts.append([Paragraph(smart_str(u"importo_opere_mitig_comp"),style),Paragraph(smart_str(obj.importo_opere_mitig_comp),style)])
        allproducts.append([Paragraph(smart_str(u"importo_totale_intervento"),style),Paragraph(smart_str(obj.importo_totale_intervento),style)])
        allproducts.append([Paragraph(smart_str(u"importo_richiesto"),style),Paragraph(smart_str(obj.importo_richiesto),style)])
        allproducts.append([Paragraph(smart_str(u"importo_cofinanziato_altri"),style),Paragraph(smart_str(obj.importo_cofinanziato_altri),style)])
        allproducts.append([Paragraph(smart_str(u"ente_cofinanziatore"),style),Paragraph(smart_str(obj.ente_cofinanziatore),style)])
        allproducts.append([Paragraph(smart_str(u"efficacia"),style),Paragraph(smart_str(obj.efficacia),style)])
        allproducts.append([Paragraph(smart_str(u"efficacia_val"),style),Paragraph(smart_str(obj.efficacia_val),style)])
        allproducts.append([Paragraph(smart_str(u"cantierabilita"),style),Paragraph(smart_str(obj.cantierabilita),style)])
        allproducts.append([Paragraph(smart_str(u"cantierabilita_val"),style),Paragraph(smart_str(obj.cantierabilita_val),style)])
        allproducts.append([Paragraph(smart_str(u"variante_urbanistica"),style),Paragraph(smart_str(obj.variante_urbanistica),style)])
        allproducts.append([Paragraph(smart_str(u"variante_urbanistica_val"),style),Paragraph(smart_str(obj.variante_urbanistica_val),style)])
        allproducts.append([Paragraph(smart_str(u"valutazione_impatto_ambientale"),style),Paragraph(smart_str(obj.valutazione_impatto_ambientale),style)])
        allproducts.append([Paragraph(smart_str(u"valutazione_impatto_ambientale_val"),style),Paragraph(smart_str(obj.valutazione_impatto_ambientale_val),style)])
        allproducts.append([Paragraph(smart_str(u"esproprio"),style),Paragraph(smart_str(obj.esproprio),style)])
        allproducts.append([Paragraph(smart_str(u"esproprio_val"),style),Paragraph(smart_str(obj.esproprio_val),style)])
        allproducts.append([Paragraph(smart_str(u"sostenibilita"),style),Paragraph(smart_str(obj.sostenibilita),style)])
        allproducts.append([Paragraph(smart_str(u"sostenibilita_val"),style),Paragraph(smart_str(obj.sostenibilita_val),style)])
        allproducts.append([Paragraph(smart_str(u"Punteggio provvisoriamente assegnato"),style),Paragraph(smart_str(obj.totale),style)])
        allproducts.append([Paragraph(smart_str(u"conclusione_istruttoria"),style),Paragraph(smart_str(obj.conclusione_istruttoria),style)])
        allproducts.append([Paragraph(smart_str(u"nominativo_compilatore"),style),Paragraph(smart_str(obj.nominativo_compilatore),style)])
        allproducts.append([Paragraph(smart_str(u"email_comp"),style),Paragraph(smart_str(obj.email_comp),style)])
        allproducts.append([Paragraph(smart_str(u"Geni_civili_02_2016"),style),Paragraph(smart_str(obj.nuovi_geni_civili),style)])
        allproducts.append([Paragraph(smart_str(u"priorita"),style),Paragraph(smart_str(obj.priorita),style)])
        allproducts.append([Paragraph(smart_str(u"codice_rendis"),style),Paragraph(smart_str(obj.codice_rendis),style)])
        allproducts.append([Paragraph(smart_str(u"int_fin_tot_acq"),style),Paragraph(smart_str(obj.int_fin_tot_acq),style)])
        allproducts.append([Paragraph(smart_str(u"estremi_atto_fin"),style),Paragraph(smart_str(obj.estremi_atto_fin),style)])
        allproducts.append([Paragraph(smart_str(u"data_trasmissione_istruttoria"),style),Paragraph(smart_str(obj.data_trasmissione_istruttoria),style)])

        #if request.user.is_superuser:
            #allproducts.append([smart_str(u"a_finanziamento"),Paragraph(smart_str(obj.a_finanziamento),style)])

        t = Table([headings] + allproducts,[150,350])

        t.setStyle(TableStyle([
            (
                'GRID',
                (0,0),
                (1,-1),
                2,
                colors.black
            ),
            (
                'LINEBELOW',
                (0,0),
                (-1,0),
                2,
                colors.red
            ),
            (
                'BACKGROUND',
                (0, 0),
                (-1, 0),
                colors.pink
            )
        ]))

        Catalog.append(t)

        Catalog.append(PageBreak())

        allproducts = []

    p.build(Catalog)

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
export_pdf.short_description = u"Esporta nel formato PDF"

def export_csv(modeladmin, request, queryset):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=studi_interventi_lucca.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"codice_intervento"),
        smart_str(u"bacino_idrografico"),
        smart_str(u"comprensorio"),
        smart_str(u"provincia"),
        smart_str(u"comune"),
        smart_str(u"localita"),
        smart_str(u"corso_acqua"),
        smart_str(u"reticolo_gestione"),
        smart_str(u"geometria"),
        smart_str(u"coord_x"),
        smart_str(u"coord_y"),
        smart_str(u"lat"),
        smart_str(u"lon"),
        smart_str(u"fenomeno"),
        smart_str(u"studio_intervento"),
        smart_str(u"tipologia_intervento"),
        smart_str(u"tipo_di_opera"),
        smart_str(u"cat_int"),
        smart_str(u"area_vasta_rif"),
        smart_str(u"titolo_intervento_studio"),
        smart_str(u"descrizione_sintetica_intervento_studio"),
        smart_str(u"categoria_idr_opera"),
        smart_str(u"perimetrazione_autorita_di_bacino"),
        smart_str(u"codice_pericolosita_adb_pai"),
        smart_str(u"classe_rischio_pai"),
        smart_str(u"perimetrazione_pericolosita_attuale"),
        smart_str(u"perimetrazione_pericolosita_post_intervento"),
        smart_str(u"stima_rischio_diretto_attuale"),
        smart_str(u"stima_rischio_indiretto_attuale"),
        smart_str(u"stima_rischio_diretto_intervento"),
        smart_str(u"stima_rischio_indiretto_intervento"),
        smart_str(u"ente_proponente"),
        smart_str(u"ente_attuatore_competente"),
        smart_str(u"nominativo"),
        smart_str(u"email"),
        smart_str(u"recapito_telefonico"),
        smart_str(u"interventi_correlati"),
        smart_str(u"stralcio_funzionale"),
        smart_str(u"accordo_di_programma"),
        smart_str(u"note"),
        smart_str(u"progetto_preliminare"),
        smart_str(u"mesi_approvazione_progetto_preliminare"),
        smart_str(u"data_approvazione_progetto_preliminare"),
        smart_str(u"riferimento_determina_approvazione_pp"),
        smart_str(u"allegato_determina_approvazione_pp"),
        smart_str(u"progetto_definitivo"),
        smart_str(u"mesi_approvazione_progetto_definitivo"),
        smart_str(u"data_approvazione_progetto_definitivo"),
        smart_str(u"riferimento_determina_approvazione_pd"),
        smart_str(u"allegato_determina_approvazione_pd"),
        smart_str(u"mesi_approvazione_progetto_esecutivo"),
        smart_str(u"data_approvazione_progetto_esecutivo"),
        smart_str(u"riferimento_determina_approvazione_pe"),
        smart_str(u"allegato_determina_approvazione_pe"),
        smart_str(u"mesi_inizio_lavori"),
        smart_str(u"inizio_lavori"),
        smart_str(u"mesi_fine_lavori"),
        smart_str(u"fine_lavori"),
        smart_str(u"elaborati_progettuali"),
        smart_str(u"descrizione_elaborati_prog"),
        smart_str(u"allegato_documento_preliminare"),
        smart_str(u"conclusione_relazione_finale"),
        smart_str(u"mesi_conclusione_relazione_finale"),
        smart_str(u"elenco_pareri"),
        smart_str(u"atto_valutazione"),
        smart_str(u"allegato_atto_valutazione"),
        smart_str(u"codice_unico_progetto"),
        smart_str(u"atto_nomina_rup"),
        smart_str(u"allegato_atto_nomina_rup"),
        smart_str(u"intervento_opere_accessorie"),
        smart_str(u"presenza_vincoli_sovraordinati"),
        smart_str(u"desc_opere_acc_strum"),
        smart_str(u"importo_opere_accessorie_strumentali"),
        smart_str(u"desc_opere_acc_no_strum"),
        smart_str(u"importo_opere_accessorie_no_strumentali"),
        smart_str(u"intervento_opere_mitigazione_compensazione"),
        smart_str(u"desc_int_opere_mitig_comp"),
        smart_str(u"importo_opere_mitig_comp"),
        smart_str(u"importo_totale_intervento"),
        smart_str(u"importo_richiesto"),
        smart_str(u"importo_cofinanziato_altri"),
        smart_str(u"ente_cofinanziatore"),
        smart_str(u"efficacia"),
        smart_str(u"efficacia_val"),
        smart_str(u"cantierabilita"),
        smart_str(u"cantierabilita_val"),
        smart_str(u"variante_urbanistica"),
        smart_str(u"variante_urbanistica_val"),
        smart_str(u"valutazione_impatto_ambientale"),
        smart_str(u"valutazione_impatto_ambientale_val"),
        smart_str(u"esproprio"),
        smart_str(u"esproprio_val"),
        smart_str(u"sostenibilita"),
        smart_str(u"sostenibilita_val"),
        smart_str(u"Punteggio provvisoriamente assegnato"),
        smart_str(u"conclusione_istruttoria"),
        smart_str(u"nominativo_compilatore"),
        smart_str(u"email_comp"),
        smart_str(u"Geni_civili_02_2016"),
        smart_str(u"priorita"),
        smart_str(u"codice_rendis"),
        smart_str(u"int_fin_tot_acq"),
        smart_str(u"estremi_atto_fin"),
        smart_str(u"data_trasmissione_istruttoria"),
        #smart_str(u"a_finanziamento") if request.user.is_superuser else smart_str(u""),
        #smart_str(u"nuovi_geni_civili") if request.user.is_superuser else smart_str(u""),
    ])

    #if request.user.is_superuser:
    #    writer.writerow([
    #        smart_str(u"a_finanziamento"),
    #    ])

    for obj in queryset:

        pnt = GEOSGeometry(obj.fenomeno_aggiunto, 3003)
        coords = pnt.coords
        coord_x = coords[0]
        coord_y = coords[1]
        newGem = pnt.transform(4326,True)
        newCoords = newGem.coords
        lon = newCoords[0]
        lat = newCoords[1]

        writer.writerow([
            smart_str(obj.codice_intervento),
            smart_str(obj.bacino_idrografico),
            smart_str(obj.comprensorio),
            smart_str(obj.provincia),
            smart_str(obj.comune),
            smart_str(obj.localita),
            smart_str(obj.corso_acqua),
            smart_str(obj.reticolo_gestione),
            smart_str(obj.fenomeno_aggiunto),
            float(smart_str(coord_x)),
            float(smart_str(coord_y)),
            float(smart_str(lat)),
            float(smart_str(lon)),
            smart_str(obj.fenomeno),
            smart_str(obj.studio_intervento),
            smart_str(obj.tipologia_intervento),
            smart_str(obj.tipo_di_opera),
            smart_str(obj.cat_int),
            smart_str(obj.area_vasta_rif),
            smart_str(obj.titolo_intervento_studio),
            smart_str(obj.descrizione_sintetica_intervento_studio),
            smart_str(obj.categoria_idr_opera),
            smart_str(obj.perimetrazione_autorita_di_bacino),
            smart_str(obj.codice_pericolosita_adb_pai),
            smart_str(obj.classe_rischio_pai),
            smart_str(obj.perimetrazione_pericolosita_attuale),
            smart_str(obj.perimetrazione_pericolosita_post_intervento),
            smart_str(obj.stima_rischio_diretto_attuale),
            smart_str(obj.stima_rischio_indiretto_attuale),
            smart_str(obj.stima_rischio_diretto_intervento),
            smart_str(obj.stima_rischio_indiretto_intervento),
            smart_str(obj.ente_proponente),
            smart_str(obj.ente_attuatore_competente),
            smart_str(obj.nominativo),
            smart_str(obj.email),
            smart_str(obj.recapito_telefonico),
            smart_str(obj.interventi_correlati),
            smart_str(obj.stralcio_funzionale),
            smart_str(obj.accordo_di_programma),
            smart_str(obj.note),
            smart_str(obj.progetto_preliminare),
            smart_str(obj.mesi_approvazione_progetto_preliminare),
            smart_str(obj.data_approvazione_progetto_preliminare),
            smart_str(obj.riferimento_determina_approvazione_pp),
            smart_str(obj.allegato_determina_approvazione_pp),
            smart_str(obj.progetto_definitivo),
            smart_str(obj.mesi_approvazione_progetto_definitivo),
            smart_str(obj.data_approvazione_progetto_definitivo),
            smart_str(obj.riferimento_determina_approvazione_pd),
            smart_str(obj.allegato_determina_approvazione_pd),
            smart_str(obj.mesi_approvazione_progetto_esecutivo),
            smart_str(obj.data_approvazione_progetto_esecutivo),
            smart_str(obj.riferimento_determina_approvazione_pe),
            smart_str(obj.allegato_determina_approvazione_pe),
            smart_str(obj.mesi_inizio_lavori),
            smart_str(obj.inizio_lavori),
            smart_str(obj.mesi_fine_lavori),
            smart_str(obj.fine_lavori),
            smart_str(obj.elaborati_progettuali),
            smart_str(obj.descrizione_elaborati_prog),
            smart_str(obj.allegato_documento_preliminare),
            smart_str(obj.conclusione_relazione_finale),
            smart_str(obj.mesi_conclusione_relazione_finale),
            smart_str(obj.elenco_pareri),
            smart_str(obj.atto_valutazione),
            smart_str(obj.allegato_atto_valutazione),
            smart_str(obj.codice_unico_progetto),
            smart_str(obj.atto_nomina_rup),
            smart_str(obj.allegato_atto_nomina_rup),
            smart_str(obj.intervento_opere_accessorie),
            smart_str(obj.presenza_vincoli_sovraordinati),
            smart_str(obj.desc_opere_acc_strum),
            smart_str(obj.importo_opere_accessorie_strumentali),
            smart_str(obj.desc_opere_acc_no_strum),
            smart_str(obj.importo_opere_accessorie_no_strumentali),
            smart_str(obj.intervento_opere_mitigazione_compensazione),
            smart_str(obj.desc_int_opere_mitig_comp),
            smart_str(obj.importo_opere_mitig_comp),
            smart_str(obj.importo_totale_intervento),
            smart_str(obj.importo_richiesto),
            smart_str(obj.importo_cofinanziato_altri),
            smart_str(obj.ente_cofinanziatore),
            smart_str(obj.efficacia),
            smart_str(obj.efficacia_val),
            smart_str(obj.cantierabilita),
            smart_str(obj.cantierabilita_val),
            smart_str(obj.variante_urbanistica),
            smart_str(obj.variante_urbanistica_val),
            smart_str(obj.valutazione_impatto_ambientale),
            smart_str(obj.valutazione_impatto_ambientale_val),
            smart_str(obj.esproprio),
            smart_str(obj.esproprio_val),
            smart_str(obj.sostenibilita),
            smart_str(obj.sostenibilita_val),
            smart_str(obj.totale),
            smart_str(obj.conclusione_istruttoria),
            smart_str(obj.nominativo_compilatore),
            smart_str(obj.email_comp),
            smart_str(obj.nuovi_geni_civili),
            smart_str(obj.priorita),
            smart_str(obj.codice_rendis),
            smart_str(obj.int_fin_tot_acq),
            smart_str(obj.estremi_atto_fin),
            smart_str(obj.data_trasmissione_istruttoria),
            #smart_str(obj.a_finanziamento) if request.user.is_superuser else smart_str(""),
            #smart_str(obj.nuovi_geni_civili) if request.user.is_superuser else smart_str(""),
        ])

        #if request.user.is_superuser:
        #    writer.writerow([
        #        smart_str(obj.a_finanziamento),
        #    ])

    return response
export_csv.short_description = u"Esporta nel formato CSV"

def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=studi_interventi_lucca.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Studi e Interventi Firenze")

    row_num = 0

    columns = [
        (u"codice_intervento", 8000),
        (u"bacino_idrografico", 8000),
        (u"comprensorio", 8000),
        (u"provincia", 8000),
        (u"comune", 8000),
        (u"localita", 8000),
        (u"corso_acqua", 8000),
        (u"reticolo_gestione", 8000),
        (u"geometria", 8000),
        (u"coord_x", 8000),
        (u"coord_y", 8000),
        (u"lat", 8000),
        (u"lon", 8000),
        (u"fenomeno", 8000),
        (u"studio_intervento", 8000),
        (u"tipologia_intervento", 8000),
        (u"tipo_di_opera", 8000),
        (u"cat_int", 8000),
        (u"area_vasta_rif", 8000),
        (u"titolo_intervento_studio", 8000),
        (u"descrizione_sintetica_intervento_studio", 8000),
        (u"categoria_idr_opera", 8000),
        (u"perimetrazione_autorita_di_bacino", 8000),
        (u"codice_pericolosita_adb_pai", 8000),
        (u"classe_rischio_pai", 8000),
        (u"perimetrazione_pericolosita_attuale", 8000),
        (u"perimetrazione_pericolosita_post_intervento", 8000),
        (u"stima_rischio_diretto_attuale", 8000),
        (u"stima_rischio_indiretto_attuale", 8000),
        (u"stima_rischio_diretto_intervento", 8000),
        (u"stima_rischio_indiretto_intervento", 8000),
        (u"ente_proponente", 8000),
        (u"ente_attuatore_competente", 8000),
        (u"nominativo", 8000),
        (u"email", 8000),
        (u"recapito_telefonico", 8000),
        (u"interventi_correlati", 8000),
        (u"stralcio_funzionale", 8000),
        (u"accordo_di_programma", 8000),
        (u"note", 8000),
        (u"progetto_preliminare", 8000),
        (u"mesi_approvazione_progetto_preliminare", 8000),
        (u"data_approvazione_progetto_preliminare", 8000),
        (u"riferimento_determina_approvazione_pp", 8000),
        (u"allegato_determina_approvazione_pp", 8000),
        (u"progetto_definitivo", 8000),
        (u"mesi_approvazione_progetto_definitivo", 8000),
        (u"data_approvazione_progetto_definitivo", 8000),
        (u"riferimento_determina_approvazione_pd", 8000),
        (u"allegato_determina_approvazione_pd", 8000),
        (u"mesi_approvazione_progetto_esecutivo", 8000),
        (u"data_approvazione_progetto_esecutivo", 8000),
        (u"riferimento_determina_approvazione_pe", 8000),
        (u"allegato_determina_approvazione_pe", 8000),
        (u"mesi_inizio_lavori", 8000),
        (u"inizio_lavori", 8000),
        (u"mesi_fine_lavori", 8000),
        (u"fine_lavori", 8000),
        (u"elaborati_progettuali", 8000),
        (u"descrizione_elaborati_prog", 8000),
        (u"allegato_documento_preliminare", 8000),
        (u"conclusione_relazione_finale", 8000),
        (u"mesi_conclusione_relazione_finale", 8000),
        (u"elenco_pareri", 8000),
        (u"atto_valutazione", 8000),
        (u"allegato_atto_valutazione", 8000),
        (u"codice_unico_progetto", 8000),
        (u"atto_nomina_rup", 8000),
        (u"allegato_atto_nomina_rup", 8000),
        (u"intervento_opere_accessorie", 8000),
        (u"presenza_vincoli_sovraordinati", 8000),
        (u"desc_opere_acc_strum", 8000),
        (u"importo_opere_accessorie_strumentali", 8000),
        (u"desc_opere_acc_no_strum", 8000),
        (u"importo_opere_accessorie_no_strumentali", 8000),
        (u"intervento_opere_mitigazione_compensazione", 8000),
        (u"desc_int_opere_mitig_comp", 8000),
        (u"importo_opere_mitig_comp", 8000),
        (u"importo_totale_intervento", 8000),
        (u"importo_richiesto", 8000),
        (u"importo_cofinanziato_altri", 8000),
        (u"ente_cofinanziatore", 8000),
        (u"efficacia", 8000),
        (u"efficacia_val", 8000),
        (u"cantierabilita", 8000),
        (u"cantierabilita_val", 8000),
        (u"variante_urbanistica", 8000),
        (u"variante_urbanistica_val", 8000),
        (u"valutazione_impatto_ambientale", 8000),
        (u"valutazione_impatto_ambientale_val", 8000),
        (u"esproprio", 8000),
        (u"esproprio_val", 8000),
        (u"sostenibilita", 8000),
        (u"sostenibilita_val", 8000),
        (u"Punteggio provvisoriamente assegnato", 8000),
        (u"conclusione_istruttoria", 8000),
        (u"nominativo_compilatore", 8000),
        (u"email_comp", 8000),
        (u"Geni_civili_02_2016", 8000),
        (u"priorita", 8000),
        (u"codice_rendis", 8000),
        (u"int_fin_tot_acq", 8000),
        (u"estremi_atto_fin", 8000),
        (u"data_trasmissione_istruttoria", 8000),
    ]

    #if request.user.is_superuser:
        #columns.append((u"a_finanziamento", 8000)),

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:

        pnt = GEOSGeometry(obj.fenomeno_aggiunto, 3003)
        coords = pnt.coords
        coord_x = coords[0]
        coord_y = coords[1]
        newGem = pnt.transform(4326,True)
        newCoords = newGem.coords
        lon = newCoords[0]
        lat = newCoords[1]

        row_num += 1
        row = [
            smart_str(obj.codice_intervento),
            smart_str(obj.bacino_idrografico),
            smart_str(obj.comprensorio),
            smart_str(obj.provincia),
            smart_str(obj.comune),
            smart_str(obj.localita),
            smart_str(obj.corso_acqua),
            smart_str(obj.reticolo_gestione),
            smart_str(obj.fenomeno_aggiunto),
            float(smart_str(coord_x)),
            float(smart_str(coord_y)),
            float(smart_str(lat)),
            float(smart_str(lon)),
            #smart_str(lon) + "," + smart_str(lat),
            smart_str(obj.fenomeno),
            smart_str(obj.studio_intervento),
            smart_str(obj.tipologia_intervento),
            smart_str(obj.tipo_di_opera),
            smart_str(obj.cat_int),
            smart_str(obj.area_vasta_rif),
            smart_str(obj.titolo_intervento_studio),
            smart_str(obj.descrizione_sintetica_intervento_studio),
            smart_str(obj.categoria_idr_opera),
            smart_str(obj.perimetrazione_autorita_di_bacino),
            smart_str(obj.codice_pericolosita_adb_pai),
            smart_str(obj.classe_rischio_pai),
            smart_str(obj.perimetrazione_pericolosita_attuale),
            smart_str(obj.perimetrazione_pericolosita_post_intervento),
            float(smart_str(obj.stima_rischio_diretto_attuale)) if obj.stima_rischio_diretto_attuale else None,
            float(smart_str(obj.stima_rischio_indiretto_attuale)) if obj.stima_rischio_indiretto_attuale else None,
            float(smart_str(obj.stima_rischio_diretto_intervento)) if obj.stima_rischio_diretto_intervento else None,
            float(smart_str(obj.stima_rischio_indiretto_intervento)) if obj.stima_rischio_indiretto_intervento else None,
            smart_str(obj.ente_proponente),
            smart_str(obj.ente_attuatore_competente),
            smart_str(obj.nominativo),
            smart_str(obj.email),
            smart_str(obj.recapito_telefonico),
            smart_str(obj.interventi_correlati),
            smart_str(obj.stralcio_funzionale),
            smart_str(obj.accordo_di_programma),
            smart_str(obj.note),
            smart_str(obj.progetto_preliminare),
            smart_str(obj.mesi_approvazione_progetto_preliminare),
            smart_str(obj.data_approvazione_progetto_preliminare),
            smart_str(obj.riferimento_determina_approvazione_pp),
            smart_str(obj.allegato_determina_approvazione_pp),
            smart_str(obj.progetto_definitivo),
            smart_str(obj.mesi_approvazione_progetto_definitivo),
            smart_str(obj.data_approvazione_progetto_definitivo),
            smart_str(obj.riferimento_determina_approvazione_pd),
            smart_str(obj.allegato_determina_approvazione_pd),
            smart_str(obj.mesi_approvazione_progetto_esecutivo),
            smart_str(obj.data_approvazione_progetto_esecutivo),
            smart_str(obj.riferimento_determina_approvazione_pe),
            smart_str(obj.allegato_determina_approvazione_pe),
            smart_str(obj.mesi_inizio_lavori),
            smart_str(obj.inizio_lavori),
            smart_str(obj.mesi_fine_lavori),
            smart_str(obj.fine_lavori),
            smart_str(obj.elaborati_progettuali),
            smart_str(obj.descrizione_elaborati_prog),
            smart_str(obj.allegato_documento_preliminare),
            smart_str(obj.conclusione_relazione_finale),
            smart_str(obj.mesi_conclusione_relazione_finale),
            smart_str(obj.elenco_pareri),
            smart_str(obj.atto_valutazione),
            smart_str(obj.allegato_atto_valutazione),
            smart_str(obj.codice_unico_progetto),
            smart_str(obj.atto_nomina_rup),
            smart_str(obj.allegato_atto_nomina_rup),
            smart_str(obj.intervento_opere_accessorie),
            smart_str(obj.presenza_vincoli_sovraordinati),
            smart_str(obj.desc_opere_acc_strum),
            float(smart_str(obj.importo_opere_accessorie_strumentali)) if obj.importo_opere_accessorie_strumentali else None,
            smart_str(obj.desc_opere_acc_no_strum),
            float(smart_str(obj.importo_opere_accessorie_no_strumentali)) if obj.importo_opere_accessorie_no_strumentali else None,
            smart_str(obj.intervento_opere_mitigazione_compensazione),
            smart_str(obj.desc_int_opere_mitig_comp),
            float(smart_str(obj.importo_opere_mitig_comp)) if obj.importo_opere_mitig_comp else None,
            #smart_str(obj.importo_totale_intervento),
            #smart_str(obj.importo_richiesto),
            #smart_str(obj.importo_cofinanziato_altri),
            float(smart_str(obj.importo_totale_intervento)),
            float(smart_str(obj.importo_richiesto)),
            float(smart_str(obj.importo_cofinanziato_altri)),
            smart_str(obj.ente_cofinanziatore),
            smart_str(obj.efficacia),
            float(smart_str(obj.efficacia_val)) if obj.efficacia_val else 0,
            smart_str(obj.cantierabilita),
            float(smart_str(obj.cantierabilita_val)) if obj.cantierabilita_val else 0,
            smart_str(obj.variante_urbanistica),
            float(smart_str(obj.variante_urbanistica_val)) if obj.variante_urbanistica_val else 0,
            smart_str(obj.valutazione_impatto_ambientale),
            float(smart_str(obj.valutazione_impatto_ambientale_val)) if obj.valutazione_impatto_ambientale_val else 0,
            smart_str(obj.esproprio),
            float(smart_str(obj.esproprio_val)) if obj.esproprio_val else 0,
            smart_str(obj.sostenibilita),
            float(smart_str(obj.sostenibilita_val)) if obj.sostenibilita_val else 0,
            float(smart_str(obj.totale)) if smart_str(obj.totale) else 0,
            smart_str(obj.conclusione_istruttoria),
            smart_str(obj.nominativo_compilatore),
            smart_str(obj.email_comp),
            smart_str(obj.nuovi_geni_civili),
            smart_str(obj.priorita),
            smart_str(obj.codice_rendis),
            smart_str(obj.int_fin_tot_acq),
            smart_str(obj.estremi_atto_fin),
            smart_str(obj.data_trasmissione_istruttoria),
        ]

        #if request.user.is_superuser:
            #row.append(smart_str(obj.a_finanziamento)),

        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

export_xls.short_description = u"Esporta nel formato XLS"

class InterventoAdmin(GeoModelAdmin):

    @register.inclusion_tag('admin/submit_line.html', takes_context=True)
    def submit_row(context):
        """
        Displays the row of buttons for delete and save.
        """
        ctx = {
            'show_save_and_mail': True,
        }

        return ctx

    def response_change(self, request, obj):
        """ custom method that cacthes a new 'save and edit next' action
            Remember that the type of 'obj' is the current model instance, so we can use it dynamically!
        """
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        emailTextTitle = 'Documento Operativo per la Difesa del Suolo LR 80/2015'

        msg_dict = {'name': force_text(opts.verbose_name), 'obj': force_text(obj)}

        if "_save_and_send_email" in request.POST:
            #msg = _("""The %(name)s "%(obj)s" was added successfully. Now you're editing the following %(name)s, according to its ID number.""") % {'name': force_unicode(verbose_name), 'obj': obj}
            #msg = ("""Email spedita correttamente.""")
            msg = _('%(name)s "%(obj)s" modificato correttamente. Email spedita correttamente') % msg_dict
            self.message_user(request, msg, messages.SUCCESS)

            obj.conclusione_istruttoria = True

            #updates the date of transmission
            obj.data_trasmissione_istruttoria = datetime.datetime.now()

            obj.save()

            newQueryset = Intervento.objects.all()
            #if obj.conclusione_istruttoria is True:
            email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente", 'dbsegnalazioni@lamma.rete.toscana.it',['documento-annuale-difesa-suolo@regione.toscana.it',obj.email,obj.email_comp,obj.bacino_idrografico.email],['mari@lamma.rete.toscana.it'])
            email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
            email.send(fail_silently=False)
            return self.response_post_save_change(request, obj)
        elif "_save_and_no_send_mail" in request.POST:
            #msg = _("""The %(name)s "%(obj)s" was added successfully. Now you're editing the following %(name)s, according to its ID number.""") % {'name': force_unicode(verbose_name), 'obj': obj}
            #msg = ("""Email spedita correttamente.""")
            msg = _('%(name)s "%(obj)s" modificato correttamente.') % msg_dict
            self.message_user(request, msg, messages.SUCCESS)

            obj.conclusione_istruttoria = True

            #updates the date of transmission
            obj.data_trasmissione_istruttoria = datetime.datetime.now()

            obj.save()

            newQueryset = Intervento.objects.all()
            #if obj.conclusione_istruttoria is True:
            if not request.user.is_superuser:
                email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente" , 'dbsegnalazioni@lamma.rete.toscana.it',['documento-annuale-difesa-suolo@regione.toscana.it'],['mari@lamma.rete.toscana.it'])
                email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
                email.send(fail_silently=False)
                return self.response_post_save_change(request, obj)
            else:
                email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente" , 'dbsegnalazioni@lamma.rete.toscana.it',['mari@lamma.rete.toscana.it'])
                email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
                email.send(fail_silently=False)
                return self.response_post_save_change(request, obj)
        else:
            return super(InterventoAdmin, self).response_change(request, obj)

    def response_add(self, request, obj):
        """ custom method that cacthes a new 'save and edit next' action
            Remember that the type of 'obj' is the current model instance, so we can use it dynamically!
        """
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        emailTextTitle = 'Documento Operativo per la Difesa del Suolo LR 80/2015'

        msg_dict = {'name': force_text(opts.verbose_name), 'obj': force_text(obj)}

        if "_save_and_send_email" in request.POST:
            #msg = _("""The %(name)s "%(obj)s" was added successfully. Now you're editing the following %(name)s, according to its ID number.""") % {'name': force_unicode(verbose_name), 'obj': obj}
            #msg = ("""Email spedita correttamente.""")
            msg = _('%(name)s "%(obj)s" modificato correttamente. Email spedita correttamente') % msg_dict
            self.message_user(request, msg, messages.SUCCESS)

            obj.conclusione_istruttoria = True

            #updates the date of transmission
            obj.data_trasmissione_istruttoria = datetime.datetime.now()

            obj.save()

            newQueryset = Intervento.objects.all()
            #if obj.conclusione_istruttoria is True:
            email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente", 'dbsegnalazioni@lamma.rete.toscana.it',['documento-annuale-difesa-suolo@regione.toscana.it',obj.email,obj.email_comp,obj.bacino_idrografico.email],['mari@lamma.rete.toscana.it'])
            email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
            email.send(fail_silently=False)
            return self.response_post_save_add(request, obj)
        elif "_save_and_no_send_mail" in request.POST:
            #msg = _("""The %(name)s "%(obj)s" was added successfully. Now you're editing the following %(name)s, according to its ID number.""") % {'name': force_unicode(verbose_name), 'obj': obj}
            #msg = ("""Email spedita correttamente.""")
            msg = _('%(name)s "%(obj)s" modificato correttamente.') % msg_dict
            self.message_user(request, msg, messages.SUCCESS)

            obj.conclusione_istruttoria = True

            #updates the date of transmission
            obj.data_trasmissione_istruttoria = datetime.datetime.now()

            obj.save()

            newQueryset = Intervento.objects.all()
            #if obj.conclusione_istruttoria is True:
            if not request.user.is_superuser:
                email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente" , 'dbsegnalazioni@lamma.rete.toscana.it',['documento-annuale-difesa-suolo@regione.toscana.it'],['mari@lamma.rete.toscana.it'])
                email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
                email.send(fail_silently=False)
                return self.response_post_save_add(request, obj)
            else:
                email = EmailMessage(emailTextTitle+'-trasmissione istruttoria', "CODICE INTERVENTO: " + str(obj.codice_intervento) + "\r\rSi comunica che l'Ufficio Tecnico del Genio Civile ha completato l'istruttoria relativa all'intervento/studio sopra indicato, comprensiva del punteggio provvisoriamente assegnato, ai fini della redazione del "+emailTextTitle+". \r\rSi prega pertanto di prendere visione dell'istruttoria allegata alla presente. \rEventuali osservazioni e modifiche debbono essere trasmesse entro 7 giorni dal ricevimento della presente ai destinatari della presente mail. \r\rE' possibile vedere l'intervento georeferenziato all'indirizzo http://geoportale.lamma.rete.toscana.it/segnalazioni/index.html?codint="+str(obj.codice_intervento)+" \r\rDistinti saluti \r\rUfficio Tecnico Genio civile Territorialmente competente" , 'dbsegnalazioni@lamma.rete.toscana.it',['mari@lamma.rete.toscana.it'])
                email.attach(str(obj.codice_intervento)+'_segnalazione.pdf',export_pdf_single(obj, request, newQueryset, cod = obj.codice_intervento),'application/pdf')
                email.send(fail_silently=False)
                return self.response_post_save_add(request, obj)
        else:
            return super(InterventoAdmin, self).response_add(request, obj)

    actions = [export_csv,export_xls,export_pdf]

    def get_actions(self, request):
        actions = super(InterventoAdmin, self).get_actions(request)
        if request.user.is_superuser == False:
            if 'export_csv' in actions:
                del actions['export_csv']
            if 'export_xls' in actions:
                del actions['export_xls']
        return actions

    class Media:
        from django.conf import settings
        static_url = getattr(settings, 'STATIC_URL', '/static')
        js = [ static_url+'admin/js/update_record.js', ]

    form = CronoprogrammaAdminForm

    options = {
        'layers': [
            'geoscopio_intorno_toscana',
            'geoscopio_hillshade',
            'geoscopio_batimetriche',
            'geoscopio_idregione',
            'comprensori',
            'geoscopio_ortofoto',
            'geoscopio_ctr10k',
            'reticolo_gestione',
            'province',
            'comuni',
            'dads2014',
            'lucca',
        ],
        'default_lon': 1243401.13894,
        'default_lat': 5387778.59347,
        'defaultZoom': 1,
    }

    fieldsets = [
        (
        'INFORMAZIONI GEOGRAFICHE',
            {'fields':
                [
                'codice_intervento',
                'bacino_idrografico',
                'comprensorio',
                'provincia',
                'comune',
                'localita',
                'corso_acqua',
                'reticolo_gestione',
                #'coord_x',
                #'coord_y',
                #'lon',
                #'lat',
                'fenomeno_aggiunto',
                ]
            }
        ),
        (
        'INFORMAZIONI GENERALI INTERVENTO/PROGETTI/STUDI',
            {'fields':
                [
                'fenomeno',
                'studio_intervento',
                'tipologia_intervento',
                'tipo_di_opera',
                'cat_int',
                'area_vasta_rif',
                'titolo_intervento_studio',
                'descrizione_sintetica_intervento_studio',
                'categoria_idr_opera',
                'perimetrazione_autorita_di_bacino',
                'codice_pericolosita_adb_pai',
                'classe_rischio_pai',
                'perimetrazione_pericolosita_attuale',
                'perimetrazione_pericolosita_post_intervento',
                'stima_rischio_diretto_attuale',
                'stima_rischio_indiretto_attuale',
                'stima_rischio_diretto_intervento',
                'stima_rischio_indiretto_intervento',
                'ente_proponente',
                'ente_attuatore_competente',
                'nominativo',
                'email',
                'recapito_telefonico',
                'interventi_correlati',
                'stralcio_funzionale',
                'accordo_di_programma',
                'note',
                ],
                'classes': ['collapse']
            }
        ),
        (
        'CRONOPROGRAMMA',
            {
            'description': '<b>Compilare la casella indicando il numero di mesi previsti a partire dalla data di finanziamento. Indicare \'0\' se il passo è già stato realizzato o se non è previsto N.B. per ognuno dei passi va indicato il numero di mesi a partire dal finanziamento e non la durata del singolo passo Esempio: con progetto definitivo già approvato (mesi = 0) e previsione approvazione esecutivo dopo un mese dal finanziamento (mesi = 1), se si stima che per l\'avvio dei lavori occorrono altri due mesi indicare il tempo complessivo dal finanziamento (mesi = 3).</b><BR/><BR/>',
            'fields':
                [
                #'progetto_preliminare',
                'data_approvazione_progetto_preliminare',
                'mesi_approvazione_progetto_preliminare',
                'riferimento_determina_approvazione_pp',
                'allegato_determina_approvazione_pp',
                #'progetto_definitivo',
                'data_approvazione_progetto_definitivo',
                'mesi_approvazione_progetto_definitivo',
                'riferimento_determina_approvazione_pd',
                'allegato_determina_approvazione_pd',
                'data_approvazione_progetto_esecutivo',
                'mesi_approvazione_progetto_esecutivo',
                'riferimento_determina_approvazione_pe',
                'allegato_determina_approvazione_pe',
                'inizio_lavori',
                'mesi_inizio_lavori',
                'fine_lavori',
                'mesi_fine_lavori',
                'elaborati_progettuali',
                'descrizione_elaborati_prog',
                'allegato_documento_preliminare',
                'conclusione_relazione_finale',
                'mesi_conclusione_relazione_finale',
                'elenco_pareri',
                'atto_valutazione',
                'allegato_atto_valutazione',
                'codice_unico_progetto',
                'atto_nomina_rup',
                'allegato_atto_nomina_rup',
                'intervento_opere_accessorie',
                'presenza_vincoli_sovraordinati',
                'desc_opere_acc_strum',
                'importo_opere_accessorie_strumentali',
                'desc_opere_acc_no_strum',
                'importo_opere_accessorie_no_strumentali',
                'intervento_opere_mitigazione_compensazione',
                'desc_int_opere_mitig_comp',
                'importo_opere_mitig_comp',
                ],
                'classes': ['collapse']
            }
        ),
        (
        'RISORSE ECONOMICHE',
            {'fields':
                [
                'importo_totale_intervento',
                'importo_richiesto',
                'importo_cofinanziato_altri',
                'ente_cofinanziatore',
                ],
                'classes': ['collapse']
            }
        ),
        (
        'VALUTAZIONE',
            {'fields':
                [
                'efficacia',
                'efficacia_val',
                'cantierabilita',
                'cantierabilita_val',
                'variante_urbanistica',
                'variante_urbanistica_val',
                'valutazione_impatto_ambientale',
                'valutazione_impatto_ambientale_val',
                'esproprio',
                'esproprio_val',
                'sostenibilita',
                'sostenibilita_val',
                'totale',
                ],
                'classes': ['collapse']
            }
        ),
        (
        'CONCLUSIONE ISTRUTTORIA',
            {'fields':
                [
                'conclusione_istruttoria',
                'nominativo_compilatore',
                'email_comp',
                'nuovi_geni_civili',
                #'priorita',
                'codice_rendis',
                'int_fin_tot_acq',
                'estremi_atto_fin',
                'data_trasmissione_istruttoria',
                ]
            }
        ),
        #(
        #'SEZIONE INTERNA RT',
        #    {'fields':
        #        [
        #        #'finanziato_anche_in_parte',
        #        'a_finanziamento',
        #        ],
        #        'classes': ['collapse']
        #    }
        #),
    ]

    readonly_fields = [
        'codice_intervento',
        'conclusione_istruttoria',
        'data_trasmissione_istruttoria',
    ]

    #inlines = [
    #    FotoAdminInline,
    #]
    #exclude = ('codice_intervento',)
    list_display = (
        'codice_intervento',
        'bacino_idrografico',
        'provincia',
        'comune',
        #'studio_intervento',
        'titolo_intervento_studio',
        'ente_proponente',
        'importo_totale_intervento',
        'conclusione_istruttoria',
        'data_trasmissione_istruttoria',
        #'valutazione_impatto_ambientale',
        #'sostenibilita',
        #'added',
        #'updated',
    )
    ordering = ['-conclusione_istruttoria','-data_trasmissione_istruttoria']
    list_per_page = 50
    list_max_show_all = 10000
    list_filter = ['studio_intervento','ente_attuatore_competente','conclusione_istruttoria',]

    #search_fields = ['valutazione_impatto_ambientale__text', 'esproprio__text','sostenibilita__text',]

    #def get_readonly_fields(self, request, obj=None):
    #    obj.cantierabilita_val = form():
    #        return ('field1', 'field2')
    #    else:
    #        return super(TranslationAdmin, self).get_readonly_fields(request, obj)

    def get_fieldsets(self, request, obj = None):
        fs = super(InterventoAdmin, self).get_fieldsets(request, obj)

        # only allow superusers to see/change owner
        informazioni_geografiche=list(fs[0][1]['fields'])
        informazioni_generali=list(fs[1][1]['fields'])
        cronoprogramma=list(fs[2][1]['fields'])
        risorse_economiche=list(fs[3][1]['fields'])
        valutazione=list(fs[4][1]['fields'])
        conclusione_istruttoria=list(fs[5][1]['fields'])
        #regione=list(fs[6][1]['fields'])

        if not request.user.is_superuser:
            return [
                        ('INFORMAZIONI GEOGRAFICHE', {'fields': tuple(informazioni_geografiche)}),
                        ('INFORMAZIONI GENERALI INTERVENTO/STUDI E PROGETTI', {'fields': tuple(informazioni_generali),'classes': ['collapse']}),
                        ('CRONOPROGRAMMA', {'fields': tuple(cronoprogramma),'classes': ['collapse']}),
                        ('RISORSE ECONOMICHE', {'fields': tuple(risorse_economiche),'classes': ['collapse']}),
                        ('VALUTAZIONE', {'fields': tuple(valutazione),'classes': ['collapse']}),
                        ('CONCLUSIONE ISTRUTTORIA', {'fields': tuple(conclusione_istruttoria)}),
                    ]
        else:
            return fs

    def save_model(self, request, obj, form, change):
        queryset = Intervento.objects.all()
        current_year = timezone.now().year
        codLen = len(obj.codice_intervento)
        if not queryset:
            #codice_intervento = 'DA' + str(current_year) + 'LU' + '0001'
            #codice_intervento = 'DA' + '2014' + 'LU' + '0001'
            codice_intervento = 'DODS-' + 'LU' + '0001'
            obj.codice_intervento = codice_intervento
            if obj.studio_intervento.text == 'INTERVENTO':
                obj.allegato_documento_preliminare = None
                obj.conclusione_relazione_finale = None
                obj.mesi_conclusione_relazione_finale = None

                obj.conclusione_istruttoria = False

                if obj.progetto_preliminare == False:
                    obj.mesi_approvazione_progetto_preliminare = None
                    obj.data_approvazione_progetto_preliminare = None
                    obj.riferimento_determina_approvazione_pp = None
                    obj.allegato_determina_approvazione_pp = None

                if obj.progetto_definitivo == False:
                    obj.mesi_approvazione_progetto_definitivo = None
                    obj.data_approvazione_progetto_definitivo = None
                    obj.riferimento_determina_approvazione_pd = None
                    obj.allegato_determina_approvazione_pd = None

                if obj.atto_valutazione == False:
                    obj.allegato_atto_valutazione = None

                if obj.atto_nomina_rup == False:
                    obj.allegato_atto_nomina_rup = None

                if obj.intervento_opere_accessorie == False or obj.intervento_opere_accessorie is None:
                    obj.presenza_vincoli_sovraordinati = None
                    obj.desc_opere_acc_strum = None
                    obj.importo_opere_accessorie_strumentali = None
                    obj.desc_opere_acc_no_strum = None
                    obj.importo_opere_accessorie_no_strumentali = None

                if obj.intervento_opere_mitigazione_compensazione == False or obj.intervento_opere_mitigazione_compensazione is None:
                    obj.desc_int_opere_mitig_comp = None
                    obj.importo_opere_mitig_comp = None

                obj.save(force_insert=True)

            else:
                obj.classe_rischio_pai = None
                obj.stima_rischio_diretto_attuale = None
                obj.stima_rischio_indiretto_attuale = None
                obj.stima_rischio_diretto_intervento = None
                obj.stima_rischio_indiretto_intervento = None
                obj.progetto_preliminare = False
                obj.progetto_definitivo = False
                obj.mesi_approvazione_progetto_preliminare = None
                obj.data_approvazione_progetto_preliminare = None
                obj.riferimento_determina_approvazione_pp = None
                obj.allegato_determina_approvazione_pp = None
                obj.mesi_approvazione_progetto_definitivo = None
                obj.data_approvazione_progetto_definitivo = None
                obj.riferimento_determina_approvazione_pd = None
                obj.allegato_determina_approvazione_pd = None
                obj.mesi_approvazione_progetto_esecutivo = None
                obj.data_approvazione_progetto_esecutivo = None
                obj.riferimento_determina_approvazione_pe = None
                obj.allegato_determina_approvazione_pe = None
                obj.mesi_inizio_lavori = None
                obj.inizio_lavori = None
                obj.mesi_fine_lavori = None
                obj.fine_lavori = None
                obj.elaborati_progettuali = None
                obj.descrizione_elaborati_prog = None
                obj.elenco_pareri = None
                obj.atto_valutazione = False
                obj.allegato_atto_valutazione = None
                obj.codice_unico_progetto = None
                obj.atto_nomina_rup = False
                obj.allegato_atto_nomina_rup = None
                obj.intervento_opere_accessorie = False
                obj.presenza_vincoli_sovraordinati = None
                obj.desc_opere_acc_strum = None
                obj.importo_opere_accessorie_strumentali = None
                obj.desc_opere_acc_no_strum = None
                obj.importo_opere_accessorie_no_strumentali = None
                obj.intervento_opere_mitigazione_compensazione = False
                obj.desc_int_opere_mitig_comp = None
                obj.importo_opere_mitig_comp = None
                obj.cantierabilita = None
                obj.cantierabilita_val = None
                obj.variante_urbanistica = None
                obj.variante_urbanistica_val = None
                obj.valutazione_impatto_ambientale = None
                obj.valutazione_impatto_ambientale_val = None
                obj.esproprio = None
                obj.esproprio_val = None
                obj.sostenibilita = None
                obj.sostenibilita_val = None

                obj.conclusione_istruttoria = False

                obj.save(force_insert=True)

        else:
            lista_codice_intervento = [self.codice_intervento for self in queryset]
            lista_codice_intervento_trim = [self.codice_intervento[-4:] for self in queryset]
            lista_codice_intervento_trim.sort()
            ultimo_codice_intervento = lista_codice_intervento_trim[-1]
            ultimo_codice_intervento_count = ultimo_codice_intervento
            ultimo_codice_intervento_count_int = int(ultimo_codice_intervento_count)
            ultimo = ['{i:0{width}}'.format(i=i, width=4) for i in range(ultimo_codice_intervento_count_int+1, ultimo_codice_intervento_count_int+2)]

            if codLen == 12:
                codice_intervento = 'DA' + '2014' + 'LU' + ultimo[0]
            else:
                codice_intervento = 'DODS-' + 'LU' + ultimo[0]

            list = []
            for index in range(len(lista_codice_intervento)):
                if obj.codice_intervento == lista_codice_intervento[index]:
                    list.insert(0, obj.codice_intervento)

            if not list:
                obj.codice_intervento = codice_intervento

                if obj.studio_intervento.text == 'INTERVENTO':
                    obj.allegato_documento_preliminare = None
                    obj.conclusione_relazione_finale = None
                    obj.mesi_conclusione_relazione_finale = None

                    #because this is the SALVA IN BOZZA button
                    obj.conclusione_istruttoria = False

                    if obj.progetto_preliminare == False:
                        obj.mesi_approvazione_progetto_preliminare = None
                        obj.data_approvazione_progetto_preliminare = None
                        obj.riferimento_determina_approvazione_pp = None
                        obj.allegato_determina_approvazione_pp = None

                    if obj.progetto_definitivo == False:
                        obj.mesi_approvazione_progetto_definitivo = None
                        obj.data_approvazione_progetto_definitivo = None
                        obj.riferimento_determina_approvazione_pd = None
                        obj.allegato_determina_approvazione_pd = None

                    if obj.atto_valutazione == False:
                        obj.allegato_atto_valutazione = None

                    if obj.atto_nomina_rup == False:
                        obj.allegato_atto_nomina_rup = None

                    if obj.intervento_opere_accessorie == False or obj.intervento_opere_accessorie is None:
                        obj.presenza_vincoli_sovraordinati = None
                        obj.desc_opere_acc_strum = None
                        obj.importo_opere_accessorie_strumentali = None
                        obj.desc_opere_acc_no_strum = None
                        obj.importo_opere_accessorie_no_strumentali = None

                    if obj.intervento_opere_mitigazione_compensazione == False or obj.intervento_opere_mitigazione_compensazione is None:
                        obj.desc_int_opere_mitig_comp = None
                        obj.importo_opere_mitig_comp = None

                    obj.save(force_insert=True)

                else:
                    obj.classe_rischio_pai = None
                    obj.stima_rischio_diretto_attuale = None
                    obj.stima_rischio_indiretto_attuale = None
                    obj.stima_rischio_diretto_intervento = None
                    obj.stima_rischio_indiretto_intervento = None
                    obj.progetto_preliminare = False
                    obj.progetto_definitivo = False
                    obj.mesi_approvazione_progetto_preliminare = None
                    obj.data_approvazione_progetto_preliminare = None
                    obj.riferimento_determina_approvazione_pp = None
                    obj.allegato_determina_approvazione_pp = None
                    obj.mesi_approvazione_progetto_definitivo = None
                    obj.data_approvazione_progetto_definitivo = None
                    obj.riferimento_determina_approvazione_pd = None
                    obj.allegato_determina_approvazione_pd = None
                    obj.mesi_approvazione_progetto_esecutivo = None
                    obj.data_approvazione_progetto_esecutivo = None
                    obj.riferimento_determina_approvazione_pe = None
                    obj.allegato_determina_approvazione_pe = None
                    obj.mesi_inizio_lavori = None
                    obj.inizio_lavori = None
                    obj.mesi_fine_lavori = None
                    obj.fine_lavori = None
                    obj.elaborati_progettuali = None
                    obj.descrizione_elaborati_prog = None
                    obj.elenco_pareri = None
                    obj.atto_valutazione = False
                    obj.allegato_atto_valutazione = None
                    obj.codice_unico_progetto = None
                    obj.atto_nomina_rup = False
                    obj.allegato_atto_nomina_rup = None
                    obj.intervento_opere_accessorie = False
                    obj.presenza_vincoli_sovraordinati = None
                    obj.desc_opere_acc_strum = None
                    obj.importo_opere_accessorie_strumentali = None
                    obj.desc_opere_acc_no_strum = None
                    obj.importo_opere_accessorie_no_strumentali = None
                    obj.intervento_opere_mitigazione_compensazione = False
                    obj.desc_int_opere_mitig_comp = None
                    obj.importo_opere_mitig_comp = None
                    obj.cantierabilita = None
                    obj.cantierabilita_val = None
                    obj.variante_urbanistica = None
                    obj.variante_urbanistica_val = None
                    obj.valutazione_impatto_ambientale = None
                    obj.valutazione_impatto_ambientale_val = None
                    obj.esproprio = None
                    obj.esproprio_val = None
                    obj.sostenibilita = None
                    obj.sostenibilita_val = None

                    #because this is the SALVA IN BOZZA button
                    obj.conclusione_istruttoria = False

                    obj.save(force_insert=True)

            else:
                obj.codice_intervento = obj.codice_intervento
                if obj.studio_intervento.text == 'INTERVENTO':
                    obj.allegato_documento_preliminare = None
                    obj.conclusione_relazione_finale = None
                    obj.mesi_conclusione_relazione_finale = None

                    #because this is the SALVA IN BOZZA button
                    obj.conclusione_istruttoria = False

                    if obj.progetto_preliminare == False:
                        obj.mesi_approvazione_progetto_preliminare = None
                        obj.data_approvazione_progetto_preliminare = None
                        obj.riferimento_determina_approvazione_pp = None
                        obj.allegato_determina_approvazione_pp = None

                    if obj.progetto_definitivo == False:
                        obj.mesi_approvazione_progetto_definitivo = None
                        obj.data_approvazione_progetto_definitivo = None
                        obj.riferimento_determina_approvazione_pd = None
                        obj.allegato_determina_approvazione_pd = None

                    if obj.atto_valutazione == False:
                        obj.allegato_atto_valutazione = None

                    if obj.atto_nomina_rup == False:
                        obj.allegato_atto_nomina_rup = None

                    if obj.intervento_opere_accessorie == False or obj.intervento_opere_accessorie is None:
                        obj.presenza_vincoli_sovraordinati = None
                        obj.desc_opere_acc_strum = None
                        obj.importo_opere_accessorie_strumentali = None
                        obj.desc_opere_acc_no_strum = None
                        obj.importo_opere_accessorie_no_strumentali = None

                    if obj.intervento_opere_mitigazione_compensazione == False or obj.intervento_opere_mitigazione_compensazione is None:
                        obj.desc_int_opere_mitig_comp = None
                        obj.importo_opere_mitig_comp = None

                    obj.save(force_update=True)

                else:
                    obj.classe_rischio_pai = None
                    obj.stima_rischio_diretto_attuale = None
                    obj.stima_rischio_indiretto_attuale = None
                    obj.stima_rischio_diretto_intervento = None
                    obj.stima_rischio_indiretto_intervento = None
                    obj.progetto_preliminare = False
                    obj.progetto_definitivo = False
                    obj.mesi_approvazione_progetto_preliminare = None
                    obj.data_approvazione_progetto_preliminare = None
                    obj.riferimento_determina_approvazione_pp = None
                    obj.allegato_determina_approvazione_pp = None
                    obj.mesi_approvazione_progetto_definitivo = None
                    obj.data_approvazione_progetto_definitivo = None
                    obj.riferimento_determina_approvazione_pd = None
                    obj.allegato_determina_approvazione_pd = None
                    obj.mesi_approvazione_progetto_esecutivo = None
                    obj.data_approvazione_progetto_esecutivo = None
                    obj.riferimento_determina_approvazione_pe = None
                    obj.allegato_determina_approvazione_pe = None
                    obj.mesi_inizio_lavori = None
                    obj.inizio_lavori = None
                    obj.mesi_fine_lavori = None
                    obj.fine_lavori = None
                    obj.elaborati_progettuali = None
                    obj.descrizione_elaborati_prog = None
                    obj.elenco_pareri = None
                    obj.atto_valutazione = False
                    obj.allegato_atto_valutazione = None
                    obj.codice_unico_progetto = None
                    obj.atto_nomina_rup = False
                    obj.allegato_atto_nomina_rup = None
                    obj.intervento_opere_accessorie = False
                    obj.presenza_vincoli_sovraordinati = None
                    obj.desc_opere_acc_strum = None
                    obj.importo_opere_accessorie_strumentali = None
                    obj.desc_opere_acc_no_strum = None
                    obj.importo_opere_accessorie_no_strumentali = None
                    obj.intervento_opere_mitigazione_compensazione = False
                    obj.desc_int_opere_mitig_comp = None
                    obj.importo_opere_mitig_comp = None
                    obj.cantierabilita = None
                    obj.cantierabilita_val = None
                    obj.variante_urbanistica = None
                    obj.variante_urbanistica_val = None
                    obj.valutazione_impatto_ambientale = None
                    obj.valutazione_impatto_ambientale_val = None
                    obj.esproprio = None
                    obj.esproprio_val = None
                    obj.sostenibilita = None
                    obj.sostenibilita_val = None

                    obj.conclusione_istruttoria = False


                    obj.save(force_update=True)


admin.site.register(Intervento, InterventoAdmin)
