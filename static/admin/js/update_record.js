(function($) {
    $(document).ready(function() {
        
        //CHECK RENDIS FIELDS
        /*if(document.getElementById("id_presenza_vincoli_sovraordinati")){
            $('.field-presenza_vincoli_sovraordinati').css('display','none');
        }
        if(document.getElementById("id_desc_opere_acc_strum")){
            $('.field-desc_opere_acc_strum').css('display','none');
        }
        if(document.getElementById("id_importo_opere_accessorie_strumentali")){
            $('.field-importo_opere_accessorie_strumentali').css('display','none');
        }
        if(document.getElementById("id_desc_opere_acc_no_strum")){
            $('.field-desc_opere_acc_no_strum').css('display','none');
        }
        if(document.getElementById("id_importo_opere_accessorie_no_strumentali")){
            $('.field-importo_opere_accessorie_no_strumentali').css('display','none');
        }*/
                
        $('input[id=id_intervento_opere_accessorie]').change(function(){
            if($('input[id=id_intervento_opere_accessorie]').is(':checked')){
                $('.field-presenza_vincoli_sovraordinati').css('display','inline');
                $('.field-desc_opere_acc_strum').css('display','inline');
                $('.field-importo_opere_accessorie_strumentali').css('display','inline');
                $('.field-desc_opere_acc_no_strum').css('display','inline');
                $('.field-importo_opere_accessorie_no_strumentali').css('display','inline');
            }else{
                $('.field-presenza_vincoli_sovraordinati').css('display','none');
                $('.field-desc_opere_acc_strum').css('display','none');
                $('.field-importo_opere_accessorie_strumentali').css('display','none');
                $('.field-desc_opere_acc_no_strum').css('display','none');
                $('.field-importo_opere_accessorie_no_strumentali').css('display','none');
            }
        })
        
        $('input[id=id_intervento_opere_mitigazione_compensazione]').change(function(){
            if($('input[id=id_intervento_opere_mitigazione_compensazione]').is(':checked')){
                $('.field-desc_int_opere_mitig_comp').css('display','inline');
                $('.field-importo_opere_mitig_comp').css('display','inline');
            }else{
                $('.field-desc_int_opere_mitig_comp').css('display','none');
                $('.field-importo_opere_mitig_comp').css('display','none');
            }
        })        
        
        //SET READ ONLY COORD FIELDS
        if(document.getElementById("id_coord_x") && document.getElementById("id_coord_y") && document.getElementById("id_lat") && document.getElementById("id_lon")){
            document.getElementById("id_coord_x").readOnly = true;
            document.getElementById("id_coord_y").readOnly = true;
            document.getElementById("id_lat").readOnly = true;
            document.getElementById("id_lon").readOnly = true;
        }        
                
        //DISABLE DATA FIELDS
        if(document.getElementById("id_data_approvazione_progetto_preliminare")){
            document.getElementById("id_data_approvazione_progetto_preliminare").readOnly = true;
        }
        
        if(document.getElementById("id_data_approvazione_progetto_definitivo")){
            document.getElementById("id_data_approvazione_progetto_definitivo").readOnly = true;
        }

        if(document.getElementById("id_data_approvazione_progetto_esecutivo")){
            document.getElementById("id_data_approvazione_progetto_esecutivo").readOnly = true;
        }

        if(document.getElementById("id_inizio_lavori")){
            document.getElementById("id_inizio_lavori").readOnly = true;
        }        
        
        if(document.getElementById("id_fine_lavori")){
            document.getElementById("id_fine_lavori").readOnly = true;
        }        
        
        if(document.getElementById("id_conclusione_relazione_finale")){
            document.getElementById("id_conclusione_relazione_finale").readOnly = true;
        }         
        
        var valore = new Object();

        if (document.getElementById("id_efficacia")){
            var hide_efficacia_val = document.getElementById("id_efficacia");
            hide_efficacia_val[20].hidden = true;
        }
        
        if (document.getElementById("id_variante_urbanistica")){
            var hide_variante_urbanistica_val = document.getElementById("id_variante_urbanistica");
            hide_variante_urbanistica_val[3].hidden = true;
        }

        if (document.getElementById("id_valutazione_impatto_ambientale")){
            var hide_valutazione_impatto_ambientale_val = document.getElementById("id_valutazione_impatto_ambientale");
            hide_valutazione_impatto_ambientale_val[3].hidden = true;
        }        
        
        if (document.getElementById("id_esproprio")){
            var hide_esproprio_val = document.getElementById("id_esproprio");
            hide_esproprio_val[3].hidden = true;
        }          
        
        if (document.getElementById("id_sostenibilita")){
            var hide_sostenibilita_val = document.getElementById("id_sostenibilita");
            hide_sostenibilita_val[6].hidden = true;
        }        
                
        var disableFieldVal = function() {

            $('.field-efficacia').css('display','none');
            $('.field-variante_urbanistica').css('display','none');
            $('.field-valutazione_impatto_ambientale').css('display','none');
            $('.field-esproprio').css('display','none');
            $('.field-sostenibilita').css('display','none');
            
            // ReadOnly Fields
            if (document.getElementById("id_efficacia")){
                var ccc = document.getElementById("id_efficacia");
                document.getElementById("id_efficacia").hidden = true;   
                //document.getElementById("id_efficacia").disabled = true;
                document.getElementById("id_efficacia").value = "00";
                $("#id_efficacia_val").val(0);
            }
            
            if (document.getElementById("id_variante_urbanistica")){
                document.getElementById("id_variante_urbanistica").hidden = true; 
                //document.getElementById("id_variante_urbanistica").disabled = true;
                document.getElementById("id_variante_urbanistica").value = "00";
                $("#id_variante_urbanistica_val").val(0);
            }
            
            if (document.getElementById("id_valutazione_impatto_ambientale")){    
                document.getElementById("id_valutazione_impatto_ambientale").hidden = true;
                //document.getElementById("id_valutazione_impatto_ambientale").disabled = true;
                document.getElementById("id_valutazione_impatto_ambientale").value = "00";
                $("#id_valutazione_impatto_ambientale_val").val(0);           
            }
            
            if (document.getElementById("id_esproprio")){    
                document.getElementById("id_esproprio").hidden = true;
                //document.getElementById("id_esproprio").disabled = true;
                document.getElementById("id_esproprio").value = "00";
                $("#id_esproprio_val").val(0);
            }
            
            if (document.getElementById("id_sostenibilita")){    
                document.getElementById("id_sostenibilita").hidden = true;
                //document.getElementById("id_sostenibilita").disabled = true;
                document.getElementById("id_sostenibilita").value = "00";
                $("#id_sostenibilita_val").val(0);
            }
                
            $("#id_totale").val(0);
            
            valore = {
                efficacia                      : 0,
                cantierabilita                 : 0,
                variante_urbanistica           : 0,
                valutazione_impatto_ambientale : 0,
                esproprio                      : 0,
                sostenibilita                  : 0
            };              
            
            return;
        
        };        
        
        var enableFieldVal = function() {
        
            if (document.getElementById("id_efficacia")){
                document.getElementById("id_efficacia").readOnly = false;   
                document.getElementById("id_efficacia").disabled = false;
                if(document.getElementById("id_efficacia").hidden === true){
                    document.getElementById("id_efficacia").hidden = false;
                    $("#id_efficacia").val("");
                    $("#id_efficacia_val").val("");
                }
            }
            
            if (document.getElementById("id_variante_urbanistica")){
                document.getElementById("id_variante_urbanistica").readOnly = false; 
                document.getElementById("id_variante_urbanistica").disabled = false;
                if(document.getElementById("id_variante_urbanistica").hidden === true){
                    document.getElementById("id_variante_urbanistica").hidden = false;
                    $("#id_variante_urbanistica").val("");
                    $("#id_variante_urbanistica_val").val("");
                }                
            }
            
            if (document.getElementById("id_valutazione_impatto_ambientale")){    
                document.getElementById("id_valutazione_impatto_ambientale").readOnly = false;
                document.getElementById("id_valutazione_impatto_ambientale").disabled = false;
                if(document.getElementById("id_valutazione_impatto_ambientale").hidden === true){
                    document.getElementById("id_valutazione_impatto_ambientale").hidden = false;
                    $("#id_valutazione_impatto_ambientale").val("");
                    $("#id_valutazione_impatto_ambientale_val").val("");
                }                     
            }
            
            if (document.getElementById("id_esproprio")){    
                document.getElementById("id_esproprio").readOnly = false;
                document.getElementById("id_esproprio").disabled = false;
                if(document.getElementById("id_esproprio").hidden === true){
                    document.getElementById("id_esproprio").hidden = false;
                    $("#id_esproprio").val("");
                    $("#id_esproprio_val").val("");
                } 
            }
            
            if (document.getElementById("id_sostenibilita")){    
                document.getElementById("id_sostenibilita").readOnly = false;
                document.getElementById("id_sostenibilita").disabled = false;
                if(document.getElementById("id_sostenibilita").hidden === true){
                    document.getElementById("id_sostenibilita").hidden = false;
                    $("#id_sostenibilita").val("");
                    $("#id_sostenibilita_val").val("");
                }
            }
                
                
            $('.field-efficacia').css('display','inline');
            $('.field-variante_urbanistica').css('display','inline');
            $('.field-valutazione_impatto_ambientale').css('display','inline');
            $('.field-esproprio').css('display','inline');
            $('.field-sostenibilita').css('display','inline');
        
        };
        
        /*$('input[id=id_progetto_preliminare]').change(function(){
            if($('input[id=id_progetto_preliminare]').is(':checked')){
                    if (document.getElementById("id_data_approvazione_progetto_preliminare"))
                        document.getElementById("id_data_approvazione_progetto_preliminare").readOnly = false;
                        $(".field-data_approvazione_progetto_preliminare").css('display','inline');
                    if (document.getElementById("id_riferimento_determina_approvazione_pp"))
                        document.getElementById("id_riferimento_determina_approvazione_pp").readOnly = false;
                        $(".field-riferimento_determina_approvazione_pp").css('display','inline');
                    if (document.getElementById("id_allegato_determina_approvazione_pp"))
                        document.getElementById("id_allegato_determina_approvazione_pp").readOnly = false;
                        $(".field-allegato_determina_approvazione_pp").css('display','inline');
                } else {
                    if (document.getElementById("id_data_approvazione_progetto_preliminare"))
                        document.getElementById("id_data_approvazione_progetto_preliminare").readOnly = true;
                        $(".field-data_approvazione_progetto_preliminare").css('display','none');
                    if (document.getElementById("id_riferimento_determina_approvazione_pp"))
                        document.getElementById("id_riferimento_determina_approvazione_pp").readOnly = true;      
                        $(".field-riferimento_determina_approvazione_pp").css('display','none');
                    if (document.getElementById("id_allegato_determina_approvazione_pp"))
                        document.getElementById("id_allegato_determina_approvazione_pp").readOnly = true;
                        $(".field-allegato_determina_approvazione_pp").css('display','none');
                }
        });
        
        $('input[id=id_progetto_definitivo]').change(function(){
            if($('input[id=id_progetto_definitivo]').is(':checked')){
                    if (document.getElementById("id_data_approvazione_progetto_definitivo"))
                        document.getElementById("id_data_approvazione_progetto_definitivo").readOnly = false;
                        $(".field-data_approvazione_progetto_definitivo").css('display','inline');
                    if (document.getElementById("id_riferimento_determina_approvazione_pd"))
                        document.getElementById("id_riferimento_determina_approvazione_pd").readOnly = false;
                        $(".field-riferimento_determina_approvazione_pd").css('display','inline');
                    if (document.getElementById("id_allegato_determina_approvazione_pd"))
                        document.getElementById("id_allegato_determina_approvazione_pd").readOnly = false;
                        $(".field-allegato_determina_approvazione_pd").css('display','inline');
                } else {
                    if (document.getElementById("id_data_approvazione_progetto_definitivo"))
                        document.getElementById("id_data_approvazione_progetto_definitivo").readOnly = true;
                        $(".field-data_approvazione_progetto_definitivo").css('display','none');
                    if (document.getElementById("id_riferimento_determina_approvazione_pd"))
                        document.getElementById("id_riferimento_determina_approvazione_pd").readOnly = true;      
                        $(".field-riferimento_determina_approvazione_pd").css('display','none');
                    if (document.getElementById("id_allegato_determina_approvazione_pd"))
                        document.getElementById("id_allegato_determina_approvazione_pd").readOnly = true;
                        $(".field-allegato_determina_approvazione_pd").css('display','none');
                }
        });*/
    
        var cantierabilita_val = $("#id_cantierabilita").val();
        if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03'){
            $('.field-efficacia').css('display','none');
            document.getElementById("id_efficacia").hidden = true;  
            $('.field-variante_urbanistica').css('display','none');
            document.getElementById("id_variante_urbanistica").hidden = true;  
            $('.field-valutazione_impatto_ambientale').css('display','none');
            document.getElementById("id_valutazione_impatto_ambientale").hidden = true;  
            $('.field-esproprio').css('display','none');
            document.getElementById("id_esproprio").hidden = true;  
            $('.field-sostenibilita').css('display','none');        
            document.getElementById("id_sostenibilita").hidden = true;  
        }

        var studio_intervento = $("#id_studio_intervento").val();
        if (studio_intervento == '02'){
                
            $('.field-allegato_documento_preliminare').css('display','none');
            $('.field-conclusione_relazione_finale').css('display','none');
            $('.field-mesi_conclusione_relazione_finale').css('display','none');
            
            $('.field-progetto_preliminare').css('display','inline');
            $('.field-progetto_definitivo').css('display','inline');
            
            $('.field-mesi_approvazione_progetto_preliminare').css('display','inline');
            
            var data_approvazione_progetto_preliminareValue = document.getElementById("id_data_approvazione_progetto_preliminare").value;
            if (!data_approvazione_progetto_preliminareValue) {
                $('.field-data_approvazione_progetto_preliminare').css('display','none');
            }else{
                $('.field-data_approvazione_progetto_preliminare').css('display','inline');
            }
            //$('.field-data_approvazione_progetto_preliminare').css('display','inline');
            
            $('.field-riferimento_determina_approvazione_pp').css('display','inline');
            $('.field-allegato_determina_approvazione_pp').css('display','inline');
            //$('.field-data_determina_approvazione_pp').css('display','inline');
            
            $('.field-mesi_approvazione_progetto_definitivo').css('display','inline');
            
            var data_approvazione_progetto_definitivoValue = document.getElementById("id_data_approvazione_progetto_definitivo").value;
            if (!data_approvazione_progetto_definitivoValue) {
                $('.field-data_approvazione_progetto_definitivo').css('display','none');
            }else{
                $('.field-data_approvazione_progetto_definitivo').css('display','inline');            
            }
            //$('.field-data_approvazione_progetto_definitivo').css('display','inline');
            
            $('.field-riferimento_determina_approvazione_pd').css('display','inline');
            $('.field-allegato_determina_approvazione_pd').css('display','inline');
            //$('.field-data_determina_approvazione_pd').css('display','inline');
            
            $('.field-mesi_approvazione_progetto_esecutivo').css('display','inline');
            
            var data_approvazione_progetto_esecutivoValue = document.getElementById("id_data_approvazione_progetto_esecutivo").value;
            if (!data_approvazione_progetto_esecutivoValue) {
                $('.field-data_approvazione_progetto_esecutivo').css('display','none');
            }else{
                $('.field-data_approvazione_progetto_esecutivo').css('display','inline');
            }
            //$('.field-data_approvazione_progetto_esecutivo').css('display','inline');
            
            $('.field-riferimento_determina_approvazione_pe').css('display','inline');
            $('.field-allegato_determina_approvazione_pe').css('display','inline');
            //$('.field-data_determina_approvazione_pe').css('display','inline');
            
            $('.field-mesi_inizio_lavori').css('display','inline');
            
            var inizio_lavoriValue = document.getElementById("id_inizio_lavori").value;
            if (!inizio_lavoriValue) {
                $('.field-inizio_lavori').css('display','none');
            }else{
                $('.field-inizio_lavori').css('display','inline');
            }            
            //$('.field-inizio_lavori').css('display','inline');
            
            $('.field-mesi_fine_lavori').css('display','inline');
            
            var fine_lavoriValue = document.getElementById("id_fine_lavori").value;
            if (!fine_lavoriValue) {
                $('.field-fine_lavori').css('display','none');
            }else{
                $('.field-fine_lavori').css('display','inline');
            }            
            //$('.field-fine_lavori').css('display','inline');
            
            $('.field-elaborati_progettuali').css('display','inline');
            
            //CAMPI RENDIS SOLAMENTE IN INTERVENTO (INFORMAZIONI GENERALI INTERVENTO/PROGETTI/STUDI)
            $('.field-classe_rischio_pai').css('display','inline');
            $('.field-stima_rischio_diretto_attuale').css('display','inline');
            $('.field-stima_rischio_indiretto_attuale').css('display','inline');
            $('.field-stima_rischio_diretto_intervento').css('display','inline');
            $('.field-stima_rischio_indiretto_intervento').css('display','inline');
            
            //CAMPI RENDIS SOLAMENTE IN INTERVENTO (CRONOPROGRAMMA)
            $('.field-elenco_pareri').css('display','inline');            
            $('.field-atto_valutazione').css('display','inline');            
            $('.field-allegato_atto_valutazione').css('display','inline');            
            $('.field-codice_unico_progetto').css('display','inline');            
            $('.field-atto_nomina_rup').css('display','inline');            
            $('.field-allegato_atto_nomina_rup').css('display','inline');            
            $('.field-intervento_opere_accessorie').css('display','inline');
            
            if($('input[id=id_intervento_opere_accessorie]').is(':checked')){
                $('.field-presenza_vincoli_sovraordinati').css('display','inline');
                $('.field-desc_opere_acc_strum').css('display','inline');
                $('.field-importo_opere_accessorie_strumentali').css('display','inline');
                $('.field-desc_opere_acc_no_strum').css('display','inline');
                $('.field-importo_opere_accessorie_no_strumentali').css('display','inline');
            }else{
                $('.field-presenza_vincoli_sovraordinati').css('display','none');
                $('.field-desc_opere_acc_strum').css('display','none');
                $('.field-importo_opere_accessorie_strumentali').css('display','none');
                $('.field-desc_opere_acc_no_strum').css('display','none');
                $('.field-importo_opere_accessorie_no_strumentali').css('display','none');
            }            
            
            //$('.field-presenza_vincoli_sovraordinati').css('display','inline');            
            //$('.field-desc_opere_acc_strum').css('display','inline');            
            //$('.field-importo_opere_accessorie_strumentali').css('display','inline');            
            //$('.field-desc_opere_acc_no_strum').css('display','inline');            
            //$('.field-importo_opere_accessorie_no_strumentali').css('display','inline');            
            $('.field-intervento_opere_mitigazione_compensazione').css('display','inline');

            if($('input[id=id_intervento_opere_mitigazione_compensazione]').is(':checked')){
                $('.field-desc_int_opere_mitig_comp').css('display','inline');
                $('.field-importo_opere_mitig_comp').css('display','inline');
            }else{
                $('.field-desc_int_opere_mitig_comp').css('display','none');
                $('.field-importo_opere_mitig_comp').css('display','none');
            }
            
            //$('.field-desc_int_opere_mitig_comp').css('display','inline');            
            //$('.field-importo_opere_mitig_comp').css('display','inline');            
            
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-efficacia').css('display','inline');
                
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-cantierabilita').css('display','inline');
                
            $('.field-cantierabilita_val').css('display','inline');
            
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-variante_urbanistica').css('display','inline');
                
            $('.field-variante_urbanistica_val').css('display','inline');
            
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-valutazione_impatto_ambientale').css('display','inline');
                            
            $('.field-valutazione_impatto_ambientale_val').css('display','inline');
            
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-esproprio').css('display','inline');
                
            $('.field-esproprio_val').css('display','inline');
            
            if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-sostenibilita').css('display','inline');
                
            $('.field-sostenibilita_val').css('display','inline');
            
            valore = {
                efficacia: $("#id_efficacia_val").val() ===  "" ? 0 : $("#id_efficacia_val").val(),
                cantierabilita: $("#id_cantierabilita_val").val() === "" ? 0 : $("#id_cantierabilita_val").val(),
                variante_urbanistica: $("#id_variante_urbanistica_val").val() === "" ? 0 : $("#id_variante_urbanistica_val").val(),
                valutazione_impatto_ambientale: $("#id_valutazione_impatto_ambientale_val").val() === "" ? 0 : $("#id_valutazione_impatto_ambientale_val").val(),
                esproprio: $("#id_esproprio_val").val() === "" ? 0 : $("#id_esproprio_val").val(),
                sostenibilita: $("#id_sostenibilita_val").val() === "" ? 0 : $("#id_sostenibilita_val").val()
            };
            
        }else{

            $('.field-allegato_documento_preliminare').css('display','inline');
            $('.field-conclusione_relazione_finale').css('display','inline');
            $('.field-mesi_conclusione_relazione_finale').css('display','inline');

            $('.field-progetto_preliminare').css('display','none');
            $('.field-progetto_definitivo').css('display','none');
            
            $('.field-mesi_approvazione_progetto_preliminare').css('display','none');
            $('.field-data_approvazione_progetto_preliminare').css('display','none');
            $('.field-riferimento_determina_approvazione_pp').css('display','none');
            $('.field-allegato_determina_approvazione_pp').css('display','none');
            //$('.field-data_determina_approvazione_pp').css('display','none');
            
            $('.field-mesi_approvazione_progetto_definitivo').css('display','none');
            $('.field-data_approvazione_progetto_definitivo').css('display','none');
            $('.field-riferimento_determina_approvazione_pd').css('display','none');
            $('.field-allegato_determina_approvazione_pd').css('display','none');
            //$('.field-data_determina_approvazione_pd').css('display','none');
            
            $('.field-mesi_approvazione_progetto_esecutivo').css('display','none');
            $('.field-data_approvazione_progetto_esecutivo').css('display','none');
            $('.field-riferimento_determina_approvazione_pe').css('display','none');
            $('.field-allegato_determina_approvazione_pe').css('display','none');
            //$('.field-data_determina_approvazione_pe').css('display','none');
            
            $('.field-mesi_inizio_lavori').css('display','none');
            $('.field-inizio_lavori').css('display','none');
            
            $('.field-mesi_fine_lavori').css('display','none');
            $('.field-fine_lavori').css('display','none');
            
            $('.field-elaborati_progettuali').css('display','none');

            //CAMPI RENDIS SOLAMENTE IN INTERVENTO (INFORMAZIONI GENERALI INTERVENTO/PROGETTI/STUDI)
            $('.field-classe_rischio_pai').css('display','none');
            $('.field-stima_rischio_diretto_attuale').css('display','none');
            $('.field-stima_rischio_indiretto_attuale').css('display','none');
            $('.field-stima_rischio_diretto_intervento').css('display','none');
            $('.field-stima_rischio_indiretto_intervento').css('display','none');
            
            //CAMPI RENDIS SOLAMENTE IN INTERVENTO (CRONOPROGRAMMA)
            $('.field-elenco_pareri').css('display','none');            
            $('.field-atto_valutazione').css('display','none');            
            $('.field-allegato_atto_valutazione').css('display','none');            
            $('.field-codice_unico_progetto').css('display','none');            
            $('.field-atto_nomina_rup').css('display','none');            
            $('.field-allegato_atto_nomina_rup').css('display','none');            
            $('.field-intervento_opere_accessorie').css('display','none');            
            $('.field-presenza_vincoli_sovraordinati').css('display','none');            
            $('.field-desc_opere_acc_strum').css('display','none');            
            $('.field-importo_opere_accessorie_strumentali').css('display','none');            
            $('.field-desc_opere_acc_no_strum').css('display','none');            
            $('.field-importo_opere_accessorie_no_strumentali').css('display','none');            
            $('.field-intervento_opere_mitigazione_compensazione').css('display','none');            
            $('.field-desc_int_opere_mitig_comp').css('display','none');            
            $('.field-importo_opere_mitig_comp').css('display','none');
            
            $('.field-cantierabilita').css('display','none');
            $('.field-cantierabilita_val').css('display','none');
            $('.field-variante_urbanistica').css('display','none');
            $('.field-variante_urbanistica_val').css('display','none');
            $('.field-valutazione_impatto_ambientale').css('display','none');
            $('.field-valutazione_impatto_ambientale_val').css('display','none');
            $('.field-esproprio').css('display','none');
            $('.field-esproprio_val').css('display','none');
            $('.field-sostenibilita').css('display','none');
            $('.field-sostenibilita_val').css('display','none');
            
            valore = {
                efficacia: $("#id_efficacia_val").val() === "" ? 0 : $("#id_efficacia_val").val()
            };            
                
        }    
    
        $("#id_studio_intervento").on('change', function(e) {
            //var valore = new Object();
            var studio_intervento = $("#id_studio_intervento").val();
            if (studio_intervento == '02'){
            
                $('.field-allegato_documento_preliminare').css('display','none');
                $('.field-conclusione_relazione_finale').css('display','none');
                $('.field-mesi_conclusione_relazione_finale').css('display','none');
                
                /*$('#id_allegato_documento_preliminare').val("");
                $('#id_conclusione_relazione_finale').val("");
                $('#id_mesi_conclusione_relazione_finale').val("");*/
                
                $('#id_efficacia').val("");
                $('#id_efficacia_val').val("");                
                $('#id_totale').val("");

                $('#id_progetto_preliminare').attr('checked', true);
                $('#id_progetto_definitivo').attr('checked', true);
                
                $('.field-progetto_preliminare').css('display','inline');
                $('.field-progetto_definitivo').css('display','inline');
                
                $('.field-mesi_approvazione_progetto_preliminare').css('display','inline');
                
                var data_approvazione_progetto_preliminareValue = document.getElementById("id_data_approvazione_progetto_preliminare").value;
                if (!data_approvazione_progetto_preliminareValue) {
                    $('.field-data_approvazione_progetto_preliminare').css('display','none');
                }else{
                    $('.field-data_approvazione_progetto_preliminare').css('display','inline');
                }                
                //$('.field-data_approvazione_progetto_preliminare').css('display','inline');
                
                $('.field-riferimento_determina_approvazione_pp').css('display','inline');
                $('.field-allegato_determina_approvazione_pp').css('display','inline');
                //$('.field-data_determina_approvazione_pp').css('display','inline');
                
                $('.field-mesi_approvazione_progetto_definitivo').css('display','inline');
                
                var data_approvazione_progetto_definitivoValue = document.getElementById("id_data_approvazione_progetto_definitivo").value;
                if (!data_approvazione_progetto_definitivoValue) {
                    $('.field-data_approvazione_progetto_definitivo').css('display','none');
                }else{
                    $('.field-data_approvazione_progetto_definitivo').css('display','inline');
                }                
                //$('.field-data_approvazione_progetto_definitivo').css('display','inline');
                
                $('.field-riferimento_determina_approvazione_pd').css('display','inline');
                $('.field-allegato_determina_approvazione_pd').css('display','inline');
                //$('.field-data_determina_approvazione_pd').css('display','inline');
                
                $('.field-mesi_approvazione_progetto_esecutivo').css('display','inline');
                
                var data_approvazione_progetto_esecutivoValue = document.getElementById("id_data_approvazione_progetto_esecutivo").value;
                if (!data_approvazione_progetto_esecutivoValue) {
                    $('.field-data_approvazione_progetto_esecutivo').css('display','none');
                }else{
                    $('.field-data_approvazione_progetto_esecutivo').css('display','inline');
                }                                
                //$('.field-data_approvazione_progetto_esecutivo').css('display','inline');
                
                $('.field-riferimento_determina_approvazione_pe').css('display','inline');
                $('.field-allegato_determina_approvazione_pe').css('display','inline');
                //$('.field-data_determina_approvazione_pe').css('display','inline');
                
                $('.field-mesi_inizio_lavori').css('display','inline');
                
                var inizio_lavoriValue = document.getElementById("id_inizio_lavori").value;
                if (!inizio_lavoriValue) {
                    $('.field-inizio_lavori').css('display','none');
                }else{
                    $('.field-inizio_lavori').css('display','inline');
                }                
                //$('.field-inizio_lavori').css('display','inline');
                
                $('.field-mesi_fine_lavori').css('display','inline');
                
                var fine_lavoriValue = document.getElementById("id_fine_lavori").value;
                if (!fine_lavoriValue) {
                    $('.field-fine_lavori').css('display','none');
                }else{
                    $('.field-fine_lavori').css('display','inline');
                }                
                //$('.field-fine_lavori').css('display','inline');
                
                $('.field-elaborati_progettuali').css('display','inline');

                //CAMPI RENDIS SOLAMENTE IN INTERVENTO (INFORMAZIONI GENERALI INTERVENTO/PROGETTI/STUDI)
                $('.field-classe_rischio_pai').css('display','inline');
                $('.field-stima_rischio_diretto_attuale').css('display','inline');
                $('.field-stima_rischio_indiretto_attuale').css('display','inline');
                $('.field-stima_rischio_diretto_intervento').css('display','inline');
                $('.field-stima_rischio_indiretto_intervento').css('display','inline');
                
                //CAMPI RENDIS SOLAMENTE IN INTERVENTO (CRONOPROGRAMMA)
                $('.field-elenco_pareri').css('display','inline');            
                $('.field-atto_valutazione').css('display','inline');            
                $('.field-allegato_atto_valutazione').css('display','inline');            
                $('.field-codice_unico_progetto').css('display','inline');            
                $('.field-atto_nomina_rup').css('display','inline');            
                $('.field-allegato_atto_nomina_rup').css('display','inline');            
                $('.field-intervento_opere_accessorie').css('display','inline');            

                if($('input[id=id_intervento_opere_accessorie]').is(':checked')){
                    $('.field-presenza_vincoli_sovraordinati').css('display','inline');
                    $('.field-desc_opere_acc_strum').css('display','inline');
                    $('.field-importo_opere_accessorie_strumentali').css('display','inline');
                    $('.field-desc_opere_acc_no_strum').css('display','inline');
                    $('.field-importo_opere_accessorie_no_strumentali').css('display','inline');
                }else{
                    $('.field-presenza_vincoli_sovraordinati').css('display','none');
                    $('.field-desc_opere_acc_strum').css('display','none');
                    $('.field-importo_opere_accessorie_strumentali').css('display','none');
                    $('.field-desc_opere_acc_no_strum').css('display','none');
                    $('.field-importo_opere_accessorie_no_strumentali').css('display','none');
                }
            
                //$('.field-presenza_vincoli_sovraordinati').css('display','inline');            
                //$('.field-desc_opere_acc_strum').css('display','inline');            
                //$('.field-importo_opere_accessorie_strumentali').css('display','inline');            
                //$('.field-desc_opere_acc_no_strum').css('display','inline');            
                //$('.field-importo_opere_accessorie_no_strumentali').css('display','inline');            
                $('.field-intervento_opere_mitigazione_compensazione').css('display','inline');            

                if($('input[id=id_intervento_opere_mitigazione_compensazione]').is(':checked')){
                    $('.field-desc_int_opere_mitig_comp').css('display','inline');
                    $('.field-importo_opere_mitig_comp').css('display','inline');
                }else{
                    $('.field-desc_int_opere_mitig_comp').css('display','none');
                    $('.field-importo_opere_mitig_comp').css('display','none');
                }                
                
                //$('.field-desc_int_opere_mitig_comp').css('display','inline');            
                //$('.field-importo_opere_mitig_comp').css('display','inline');
            
                /*if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-efficacia').css('display','none');
                    
                if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-cantierabilita').css('display','inline');
                    
                $('.field-cantierabilita_val').css('display','inline');
                
                if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-variante_urbanistica').css('display','none');
                    
                $('.field-variante_urbanistica_val').css('display','inline');
                
                if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-valutazione_impatto_ambientale').css('display','none');
                                
                $('.field-valutazione_impatto_ambientale_val').css('display','inline');
                
                if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-esproprio').css('display','none');
                    
                $('.field-esproprio_val').css('display','inline');
                
                if(cantierabilita_val === '01' || cantierabilita_val === '02' || cantierabilita_val === '03')
                    $('.field-sostenibilita').css('display','none');
                    
                $('.field-sostenibilita_val').css('display','inline');*/
            
                $('.field-cantierabilita').css('display','inline');
                document.getElementById("id_cantierabilita").hidden = false;                
                $('.field-cantierabilita_val').css('display','inline');
                
                $('.field-variante_urbanistica').css('display','inline');
                document.getElementById("id_variante_urbanistica").hidden = false;                
                $('.field-variante_urbanistica_val').css('display','inline');
                
                $('.field-valutazione_impatto_ambientale').css('display','inline');
                document.getElementById("id_valutazione_impatto_ambientale").hidden = false;      
                $('.field-valutazione_impatto_ambientale_val').css('display','inline');
                
                $('.field-esproprio').css('display','inline');
                document.getElementById("id_esproprio").hidden = false;  
                $('.field-esproprio_val').css('display','inline');
                
                $('.field-sostenibilita').css('display','inline');
                document.getElementById("id_sostenibilita").hidden = false;  
                $('.field-sostenibilita_val').css('display','inline');
                
                valore = {
                    efficacia                      : 0,
                    cantierabilita                 : 0,
                    variante_urbanistica           : 0,
                    valutazione_impatto_ambientale : 0,
                    esproprio                      : 0,
                    sostenibilita                  : 0
                };                
                
            }else{
            
                $('.field-allegato_documento_preliminare').css('display','inline');
                $('.field-conclusione_relazione_finale').css('display','inline');
                $('.field-mesi_conclusione_relazione_finale').css('display','inline');

                $('.field-progetto_preliminare').css('display','none');
                $('.field-progetto_definitivo').css('display','none');         
                
                $('.field-mesi_approvazione_progetto_preliminare').css('display','none');
                $('.field-data_approvazione_progetto_preliminare').css('display','none');
                $('.field-riferimento_determina_approvazione_pp').css('display','none');
                $('.field-allegato_determina_approvazione_pp').css('display','none');
                //$('.field-data_determina_approvazione_pp').css('display','none');
                
                $('.field-mesi_approvazione_progetto_definitivo').css('display','none');
                $('.field-data_approvazione_progetto_definitivo').css('display','none');
                $('.field-riferimento_determina_approvazione_pd').css('display','none');
                $('.field-allegato_determina_approvazione_pd').css('display','none');
                //$('.field-data_determina_approvazione_pd').css('display','none');
                
                $('.field-mesi_approvazione_progetto_esecutivo').css('display','none');
                $('.field-data_approvazione_progetto_esecutivo').css('display','none');
                $('.field-riferimento_determina_approvazione_pe').css('display','none');
                $('.field-allegato_determina_approvazione_pe').css('display','none');
                //$('.field-data_determina_approvazione_pe').css('display','none');
                
                $('.field-mesi_inizio_lavori').css('display','none');
                $('.field-inizio_lavori').css('display','none');
                
                $('.field-mesi_fine_lavori').css('display','none');
                $('.field-fine_lavori').css('display','none');
                
                $('.field-elaborati_progettuali').css('display','none');

                //CAMPI RENDIS SOLAMENTE IN INTERVENTO (INFORMAZIONI GENERALI INTERVENTO/PROGETTI/STUDI)
                $('.field-classe_rischio_pai').css('display','none');
                $('.field-stima_rischio_diretto_attuale').css('display','none');
                $('.field-stima_rischio_indiretto_attuale').css('display','none');
                $('.field-stima_rischio_diretto_intervento').css('display','none');
                $('.field-stima_rischio_indiretto_intervento').css('display','none');
                
                //CAMPI RENDIS SOLAMENTE IN INTERVENTO (CRONOPROGRAMMA)
                $('.field-elenco_pareri').css('display','none');            
                $('.field-atto_valutazione').css('display','none');            
                $('#id_atto_valutazione').attr('checked', false);
        
                $('.field-allegato_atto_valutazione').css('display','none');            
                $('.field-codice_unico_progetto').css('display','none');            
                $('.field-atto_nomina_rup').css('display','none');            
                $('#id_atto_nomina_rup').attr('checked', false);        
                
                $('.field-allegato_atto_nomina_rup').css('display','none');            
                $('.field-intervento_opere_accessorie').css('display','none');            
                $('.field-presenza_vincoli_sovraordinati').css('display','none');            
                $('.field-desc_opere_acc_strum').css('display','none');            
                $('.field-importo_opere_accessorie_strumentali').css('display','none');            
                $('.field-desc_opere_acc_no_strum').css('display','none');            
                $('.field-importo_opere_accessorie_no_strumentali').css('display','none');            
                $('.field-intervento_opere_mitigazione_compensazione').css('display','none');            
                $('.field-desc_int_opere_mitig_comp').css('display','none');            
                $('.field-importo_opere_mitig_comp').css('display','none');
            
                //if(cantierabilita_val !== '01' && cantierabilita_val !== '02' && cantierabilita_val !== '03')
                $('.field-efficacia').css('display','inline');
                document.getElementById("id_efficacia").hidden = false;
                    
                $('.field-cantierabilita').css('display','none');
                $('.field-cantierabilita_val').css('display','none');
                $('.field-variante_urbanistica').css('display','none');
                $('.field-variante_urbanistica_val').css('display','none');
                $('.field-valutazione_impatto_ambientale').css('display','none');
                $('.field-valutazione_impatto_ambientale_val').css('display','none');
                $('.field-esproprio').css('display','none');
                $('.field-esproprio_val').css('display','none');
                $('.field-sostenibilita').css('display','none');
                $('.field-sostenibilita_val').css('display','none');

                $('#id_efficacia').val("");
                $('#id_efficacia_val').val("");                
                $('#id_totale').val("");

                //$('#id_progetto_preliminare').attr('checked', false);
                //$('#id_progetto_definitivo').attr('checked', false);
                
                //DA VERIFICARE MEGLIO
                /*$('#id_mesi_approvazione_progetto_preliminare').val("");
                $('#id_data_approvazione_progetto_preliminare').val("");
                $('#id_riferimento_determina_approvazione_pp').val("");
                $('#id_allegato_determina_approvazione_pp').val("");
                
                $('#id_mesi_approvazione_progetto_definitivo').val("");
                $('#id_data_approvazione_progetto_definitivo').val("");
                $('#id_riferimento_determina_approvazione_pd').val("");
                $('#id_allegato_determina_approvazione_pd').val("");
                
                $('#id_mesi_approvazione_progetto_esecutivo').val("");
                $('#id_data_approvazione_progetto_esecutivo').val("");
                $('#id_riferimento_determina_approvazione_pe').val("");
                $('#id_allegato_determina_approvazione_pe').val("");
                
                $('#id_mesi_inizio_lavori').val("");
                $('#id_inizio_lavori').val("");
                
                $('#id_mesi_fine_lavori').val("");
                $('#id_fine_lavori').val("");*/
                
                $('#id_cantierabilita').val("");
                $('#id_cantierabilita_val').val("");
                $('#id_variante_urbanistica').val("");
                $('#id_variante_urbanistica_val').val("");
                $('#id_valutazione_impatto_ambientale').val("");
                $('#id_valutazione_impatto_ambientale_val').val("");
                $('#id_esproprio').val("");
                $('#id_esproprio_val').val("");
                $('#id_sostenibilita').val("");
                $('#id_sostenibilita_val').val("");
                
                valore = {
                    efficacia : 0
                };                            
                
            }
        });
        
        // ReadOnly Fields
        if (document.getElementById("id_efficacia_val"))
            document.getElementById("id_efficacia_val").readOnly = true;        
        if (document.getElementById("id_cantierabilita_val"))
            document.getElementById("id_cantierabilita_val").readOnly = true;     
        if (document.getElementById("id_variante_urbanistica_val"))
            document.getElementById("id_variante_urbanistica_val").readOnly = true; 
        if (document.getElementById("id_valutazione_impatto_ambientale_val"))    
            document.getElementById("id_valutazione_impatto_ambientale_val").readOnly = true;        
        if (document.getElementById("id_sostenibilita_val"))    
            document.getElementById("id_sostenibilita_val").readOnly = true;        
        if (document.getElementById("id_esproprio_val"))    
            document.getElementById("id_esproprio_val").readOnly = true;        
        if (document.getElementById("id_totale"))    
            document.getElementById("id_totale").readOnly = true;                 
        
        // Aggiorno il campo efficacia val in base al campo efficacia secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_efficacia").on('change', function(e) {
            var efficacia = $("#id_efficacia").val();
            switch(efficacia) {
                case '01':
                case '09':                
                    valore.efficacia = '40'
                    break;
                case '02':
                case '03':
                case '04':                
                case '10':                
                case '11':
                case '12':
                    valore.efficacia = '35'
                    break;
                case '05':
                case '14':
                case '15':
                case '16':
                    valore.efficacia = '30'
                    break;
                case '06':
                case '17':
                    valore.efficacia = '25'
                    break;
                case '07':
                    valore.efficacia = '20'
                    break;
                case '08':
                case '19':
                    valore.efficacia = '15'
                    break;
                case '13':
                    valore.efficacia = '33'
                    break;
                case '18':
                    valore.efficacia = '23'
                    break;
                case '20':
                    valore.efficacia = '0'
                    break;                    
            }
            $("#id_efficacia_val").val(valore.efficacia);
            
            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });
        
        // Aggiorno il campo cantierabilita val in base al campo cantierabilita secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_cantierabilita").on('change', function(e) {
            var cantierabilita = $("#id_cantierabilita").val();
            switch(cantierabilita) {
                case '01':
                case '02':
                case '03':
                    disableFieldVal();
                    break;
                case '06':
                    enableFieldVal();
                    valore.cantierabilita = '0'
                    break;
                case '04':
                    enableFieldVal();
                    valore.cantierabilita = '30'
                    break;
                case '05':
                    enableFieldVal();
                    valore.cantierabilita = '50'
                    break;
            }
            $("#id_cantierabilita_val").val(valore.cantierabilita);
            
            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });

        // Aggiorno il campo variante_urbanistica val in base al campo variante_urbanistica secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_variante_urbanistica").on('change', function(e) {
            var variante_urbanistica = $("#id_variante_urbanistica").val();
            switch(variante_urbanistica) {
                case '01':
                    valore.variante_urbanistica = '-10'
                    break;
                case '02':
                    valore.variante_urbanistica = '0'
                    break;
            }
            $("#id_variante_urbanistica_val").val(valore.variante_urbanistica);
            
            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });      

        // Aggiorno il campo valutazione_impatto_ambientale val in base al campo valutazione_impatto_ambientale secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_valutazione_impatto_ambientale").on('change', function(e) {
            var valutazione_impatto_ambientale = $("#id_valutazione_impatto_ambientale").val();
            switch(valutazione_impatto_ambientale) {
                case '01':
                    valore.valutazione_impatto_ambientale = '-10'
                    break;
                case '02':
                    valore.valutazione_impatto_ambientale = '0'
                    break;
            }
            $("#id_valutazione_impatto_ambientale_val").val(valore.valutazione_impatto_ambientale);
            
            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });
        
        // Aggiorno il campo valutazione_impatto_ambientale val in base al campo valutazione_impatto_ambientale secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_esproprio").on('change', function(e) {
            var esproprio = $("#id_esproprio").val();
            switch(esproprio) {
                case '01':
                    valore.esproprio = '-10'
                    break;
                case '02':
                    valore.esproprio = '0'
                    break;
            }
            $("#id_esproprio_val").val(valore.esproprio);
            
            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });

        // Aggiorno il campo sostenibilita val in base al campo sostenibilita secondo
        // la tabella eff-cant-sost fornita da Regione Toscana
        $("#id_sostenibilita").on('change', function(e) {
            var sostenibilita = $("#id_sostenibilita").val();
            switch(sostenibilita) {
                case '01':
                    valore.sostenibilita = '10'
                    break;
                case '02':
                case '03':
                    valore.sostenibilita = '8'
                    break;
                case '04':
                    valore.sostenibilita = '4'
                    break;                   
                case '05':
                    valore.sostenibilita = '0'
                    break;                    
            }
            $("#id_sostenibilita_val").val(valore.sostenibilita);

            var totale = 0;
            var obj = valore;
            
            // Visit non-inherited enumerable keys
            Object.keys(obj).forEach(function(key) {
                totale = totale + parseInt(obj[key]);
            }); 

            $("#id_totale").val(totale);
        });        
        
    });

})(django.jQuery);

// Closure
(function() {
  /**
   * Decimal adjustment of a number.
   *
   * @param {String}  type  The type of adjustment.
   * @param {Number}  value The number.
   * @param {Integer} exp   The exponent (the 10 logarithm of the adjustment base).
   * @returns {Number} The adjusted value.
   */
  function decimalAdjust(type, value, exp) {
    // If the exp is undefined or zero...
    if (typeof exp === 'undefined' || +exp === 0) {
      return Math[type](value);
    }
    value = +value;
    exp = +exp;
    // If the value is not a number or the exp is not an integer...
    if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0)) {
      return NaN;
    }
    // Shift
    value = value.toString().split('e');
    value = Math[type](+(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp)));
    // Shift back
    value = value.toString().split('e');
    return +(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp));
  }

  // Decimal round
  if (!Math.round10) {
    Math.round10 = function(value, exp) {
      return decimalAdjust('round', value, exp);
    };
  }
  // Decimal floor
  if (!Math.floor10) {
    Math.floor10 = function(value, exp) {
      return decimalAdjust('floor', value, exp);
    };
  }
  // Decimal ceil
  if (!Math.ceil10) {
    Math.ceil10 = function(value, exp) {
      return decimalAdjust('ceil', value, exp);
    };
  }
})();