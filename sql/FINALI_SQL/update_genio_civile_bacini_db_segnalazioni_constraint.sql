ALTER TABLE genio_civile_arezzo_intervento ADD CONSTRAINT genio_civile_arezzo_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_firenze_intervento ADD CONSTRAINT genio_civile_firenze_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_grosseto_intervento ADD CONSTRAINT genio_civile_grosseto_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_livorno_intervento ADD CONSTRAINT genio_civile_livorno_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_lucca_intervento ADD CONSTRAINT genio_civile_lucca_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_massa_carrara_intervento ADD CONSTRAINT genio_civile_massa_carrara_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_pisa_intervento ADD CONSTRAINT genio_civile_pisa_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_pistoia_intervento ADD CONSTRAINT genio_civile_pistoia_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_prato_intervento ADD CONSTRAINT genio_civile_prato_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;

ALTER TABLE genio_civile_siena_intervento ADD CONSTRAINT genio_civile_siena_intervento_genio_c_bac_fkey FOREIGN KEY (genio_c_bac)
REFERENCES genio_civile_bacini (id) MATCH SIMPLE
ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED;



-- priorita

ALTER TABLE genio_civile_arezzo_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_firenze_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_grosseto_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_livorno_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_lucca_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_massa_carrara_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_pisa_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_pistoia_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_prato_intervento
ADD priorita boolean;

ALTER TABLE genio_civile_siena_intervento
ADD priorita boolean;

