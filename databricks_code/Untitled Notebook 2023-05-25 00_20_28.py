# Databricks notebook source
df5 = ['/raw/crw/aco_brasil/prod_aco_nacional/',
 '/raw/crw/aneel/gera_energia_distrib/',
 '/raw/crw/banco_mundial/documentacao_indica/',
 '/raw/crw/banco_mundial/documentacao_paises/',
 '/raw/crw/banco_mundial/indicadores_selecionados/',
 '/raw/crw/banco_mundial/preco_commodity/',
 '/raw/crw/catho/vagas/',
 '/raw/crw/fmi_proj/grupo_paises/',
 '/raw/crw/fmi_proj/pais/',
 '/raw/crw/fred/indicadores_selecionados/',
 '/raw/crw/ibge/cnae_subclasses/',
 '/raw/crw/ibge/deflatores/',
 '/raw/crw/ibge/ipca/',
 '/raw/crw/ibge/ipca_indice_desagregado/',
 '/raw/crw/ibge/ipp_cnae_div/',
 '/raw/crw/ibge/pia_produto_vti/',
 '/raw/crw/ibge/piaemp/',
 '/raw/crw/ibge/piaemp_aquisicoes/',
 '/raw/crw/ibge/pimpf/',
 '/raw/crw/ibge/pintec_bio_nano/',
 '/raw/crw/ibge/pintec_bio_nano_po/',
 '/raw/crw/ibge/pintec_grau_nov_imp/',
 '/raw/crw/ibge/pintec_grau_obst_cnae/',
 '/raw/crw/ibge/pintec_inov_prod_proces_cnae/',
 '/raw/crw/ibge/pintec_n_grau_obst_cnae/',
 '/raw/crw/ibge/pintec_org_mkt/',
 '/raw/crw/ibge/pintec_org_mkt_po/',
 '/raw/crw/ibge/pintec_prob_obst/',
 '/raw/crw/ibge/pintec_prob_obst_po/',
 '/raw/crw/ibge/pintec_proc_neg_func_cnae/',
 '/raw/crw/ibge/pintec_prod_vend_int/',
 '/raw/crw/ibge/pintec_prod_vend_int_po/',
 '/raw/crw/ibge/pintec_rel_coop/',
 '/raw/crw/ibge/pintec_rel_coop_loc/',
 '/raw/crw/ibge/pintec_rel_coop_loc_po/',
 '/raw/crw/ibge/pintec_rel_coop_po/',
 '/raw/crw/ibge/pintec_resp_imp/',
 '/raw/crw/ibge/pintec_tipo_inov_proj/',
 '/raw/crw/ibge/pintec_tipo_programa/',
 '/raw/crw/ibge/pintec_tipo_programa_po/',
 '/raw/crw/ibge/pnadc/',
 '/raw/crw/ibge/pnadc_a_deflatores/',
 '/raw/crw/ibge/pnadc_a_trim4/',
 '/raw/crw/ibge/pnadc_a_visita1/',
 '/raw/crw/ibge/pnadc_a_visita2/',
 '/raw/crw/ibge/pnadc_a_visita5/',
 '/raw/crw/ibge/pop_estimada/',
 '/raw/crw/ibge/pop_projetada_expectativa_txmortal/',
 '/raw/crw/ibge/pop_projetada_indicadores_implicitos/',
 '/raw/crw/ibge/pop_projetada_pessoas_prop/',
 '/raw/crw/ibge/pop_projetada_pop_sex_idade/',
 '/raw/crw/ibge/pop_projetada_txfecund/',
 '/raw/crw/ibge/relatorio_dtb_brasil_municipio/',
 '/raw/crw/ibge/scnt_conta_financeira_unificado/',
 '/raw/crw/ibge/scnt_contas_economicas_unificado/',
 '/raw/crw/ibge/scnt_valor_preco1995_saz_unificado/',
 '/raw/crw/ibge/scnt_valor_preco1995_unificado/',
 '/raw/crw/ibge/scnt_valor_preco_correntes_unificado/',
 '/raw/crw/ibge/scnt_volume_saz_se_unificado/',
 '/raw/crw/ibge/scnt_volume_se_unificado/',
 '/raw/crw/ibge/scnt_volume_tx_unificado/',
 '/raw/crw/iea/carvao_estatisticas/',
 '/raw/crw/inep_afd/brasil_regioes_e_ufs/',
 '/raw/crw/inep_afd/escolas/',
 '/raw/crw/inep_afd/municipios/',
 '/raw/crw/inep_atu/brasil_regioes_e_ufs/',
 '/raw/crw/inep_atu/escolas/',
 '/raw/crw/inep_atu/municipios/',
 '/raw/crw/inep_censo_escolar/curso_educacao_profissional/',
 '/raw/crw/inep_censo_escolar/docente/',
 '/raw/crw/inep_censo_escolar/escola/',
 '/raw/crw/inep_censo_escolar/etapa_ensino/',
 '/raw/crw/inep_censo_escolar/gestor/',
 '/raw/crw/inep_censo_escolar/matriculas/',
 '/raw/crw/inep_censo_escolar/turmas/',
 '/raw/crw/inep_dsu/brasil_regioes_e_ufs/',
 '/raw/crw/inep_dsu/escolas/',
 '/raw/crw/inep_dsu/municipios/',
 '/raw/crw/inep_enem/enem_escola/',
 '/raw/crw/inep_enem/enem_escola_dicionario/',
 '/raw/crw/inep_enem/microdados_enem/',
 '/raw/crw/inep_had/brasil_regioes_e_ufs/',
 '/raw/crw/inep_had/escolas/',
 '/raw/crw/inep_had/municipios/',
 '/raw/crw/inep_icg/escolas/',
 '/raw/crw/inep_ideb/ideb/',
 '/raw/crw/inep_inse/socioeconomico/',
 '/raw/crw/inep_iqes/cpc/',
 '/raw/crw/inep_iqes/icg/',
 '/raw/crw/inep_ird/escolas/',
 '/raw/crw/inep_prova_brasil/ts_quest_aluno/',
 '/raw/crw/inep_prova_brasil/ts_resposta_aluno/',
 '/raw/crw/inep_prova_brasil/ts_resultado_aluno/',
 '/raw/crw/inep_rmd/brasil_regioes_e_ufs/',
 '/raw/crw/inep_rmd/municipios/',
 '/raw/crw/inep_saeb/prova_brasil_2013/',
 '/raw/crw/inep_saeb/prova_brasil_2015/',
 '/raw/crw/inep_saeb/prova_brasil_2017/',
 '/raw/crw/inep_saeb/prova_brasil_2019/',
 '/raw/crw/inep_saeb/saeb_aluno_unificado/',
 '/raw/crw/inep_saeb/saeb_diretor_unificada/',
 '/raw/crw/inep_saeb/saeb_escola_unificada/',
 '/raw/crw/inep_saeb/saeb_professor_unificada/',
 '/raw/crw/inep_saeb/saeb_resultado_brasil_unificado/',
 '/raw/crw/inep_saeb/saeb_resultado_municipio_unificado/',
 '/raw/crw/inep_saeb/saeb_resultado_regiao_unificado/',
 '/raw/crw/inep_saeb/saeb_resultado_uf_unificado/',
 '/raw/crw/inep_saeb/ts_quest_aluno/',
 '/raw/crw/inep_saeb/ts_resposta_aluno/',
 '/raw/crw/inep_saeb/ts_resultado_aluno/',
 '/raw/crw/inep_taxa_rendimento/brasil_regioes_e_ufs/',
 '/raw/crw/inep_taxa_rendimento/escolas/',
 '/raw/crw/inep_taxa_rendimento/municipios/',
 '/raw/crw/inep_tdi/brasil_regioes_e_ufs/',
 '/raw/crw/inep_tdi/escolas/',
 '/raw/crw/inep_tdi/municipios/',
 '/raw/crw/infojobs/vagas/',
 '/raw/crw/inguru/news/',
 '/raw/crw/inss/cat/',
 '/raw/crw/me/caged/',
 '/raw/crw/me/caged_ajustes/',
 '/raw/crw/me/comex/isic_cuci/',
 '/raw/crw/me/comex/mun_exp/',
 '/raw/crw/me/comex/mun_imp/',
 '/raw/crw/me/comex/ncm_cgce/',
 '/raw/crw/me/comex/ncm_cuci/',
 '/raw/crw/me/comex/ncm_exp/',
 '/raw/crw/me/comex/ncm_fat_agreg/',
 '/raw/crw/me/comex/ncm_imp/',
 '/raw/crw/me/comex/ncm_isic/',
 '/raw/crw/me/comex/ncm_ppe/',
 '/raw/crw/me/comex/ncm_ppi/',
 '/raw/crw/me/comex/ncm_sh/',
 '/raw/crw/me/comex/ncm_siit/',
 '/raw/crw/me/comex/ncm_unidade/',
 '/raw/crw/me/comex/pais/',
 '/raw/crw/me/comex/pais_bloco/',
 '/raw/crw/me/comex/uf/',
 '/raw/crw/me/comex/uf_mun/',
 '/raw/crw/me/comex/urf/',
 '/raw/crw/me/comex/via/',
 '/raw/crw/me/novo_caged_exc/',
 '/raw/crw/me/novo_caged_for/',
 '/raw/crw/me/novo_caged_mov/',
 '/raw/crw/mec/pnp_efi/',
 '/raw/crw/mec/pnp_fin/',
 '/raw/crw/mec/pnp_mat/',
 '/raw/crw/mec/pnp_ser/',
 '/raw/crw/ms/sih_rd/',
 '/raw/crw/ms/sih_sp/',
 '/raw/crw/ms/sim/',
 '/raw/crw/ms_sinan/acbi/',
 '/raw/crw/ms_sinan/acgr/',
 '/raw/crw/ms_sinan/anim/',
 '/raw/crw/ms_sinan/canc/',
 '/raw/crw/ms_sinan/derm/',
 '/raw/crw/ms_sinan/iexo/',
 '/raw/crw/ms_sinan/lerd/',
 '/raw/crw/ms_sinan/ment/',
 '/raw/crw/ms_sinan/pair/',
 '/raw/crw/ms_sinan/pneu/',
 '/raw/crw/mtp_aeat/acid_obi_mun/',
 '/raw/crw/mtp_aeat/conseq_clas/',
 '/raw/crw/mtp_aeat/conseq_div/',
 '/raw/crw/mtp_aeat/motivo_cid/',
 '/raw/crw/mtp_aeat/motivo_class/',
 '/raw/crw/mtp_aeat/motivo_div/',
 '/raw/crw/mtp_aeat/motivo_ida_sex/',
 '/raw/crw/ocde/projecoes_economicas/',
 '/raw/crw/oni/bacen/cotacao/dolar_americano/',
 '/raw/crw/oni/bacen/cotacao/euro/',
 '/raw/crw/oni/bacen/cotacao/libra_esterlina/',
 '/raw/crw/oni/ibge/gini/',
 '/raw/crw/rfb/cno/cno/',
 '/raw/crw/rfb/cno/cno_areas/',
 '/raw/crw/rfb/cno/cno_cnaes/',
 '/raw/crw/rfb/cno/cno_totais/',
 '/raw/crw/rfb/cno/cno_vinculos/',
 '/raw/crw/rfb_cnpj/cadastro_empresa/',
 '/raw/crw/rfb_cnpj/cadastro_estbl/',
 '/raw/crw/rfb_cnpj/cadastro_simples/',
 '/raw/crw/rfb_cnpj/cadastro_socio/',
 '/raw/crw/rfb_cnpj/regime_tributario/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/cnae/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/motivo/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/municipio/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/nat_juridica/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/pais/',
 '/raw/crw/rfb_cnpj/tabelas_auxiliares/qualif_socio/',
 '/raw/crw/vagascertas/vagas/',
 '/raw/crw/vagascom/vagas/',
 '/raw/crw/worldsteel/indicadores_selecionados/',
 '/raw/usr/fiesc/IBGE/SIDRA/IPCA/',
 '/raw/usr/fiesc/MEC/INEP/CENSO_ES/CURSOS/',
 '/raw/usr/fiesc/MEC/INEP/CENSO_ES/IES/',
 '/raw/usr/fiesc/bacen/BACEN_METAS_DE_INFLACAO/',
 '/raw/usr/fiesc/bacen/expec_mercado/anual/',
 '/raw/usr/fiesc/bacen/expec_mercado/trimestral/',
 '/raw/usr/fiesc/bacen/expec_prod_ind/',
 '/raw/usr/fiesc/bacen/expec_selic/',
 '/raw/usr/fiesc/bacen/expec_tx_cambio/',
 '/raw/usr/fiesc/bacen/igp-m/',
 '/raw/usr/fiesc/bacen/igpm/',
 '/raw/usr/fiesc/bacen/inadimplencia_em_credito/',
 '/raw/usr/fiesc/bacen/ind_atv_eco/IBC/IBCR/',
 '/raw/usr/fiesc/bacen/inpc/',
 '/raw/usr/fiesc/bacen/taxa/cambio/nominal/',
 '/raw/usr/fiesc/datasus/CNES/LT/',
 '/raw/usr/fiesc/datasus/CNES/PF/',
 '/raw/usr/fiesc/datasus/CNES/ST/',
 '/raw/usr/fiesc/ibge/inpc/7063/',
 '/raw/usr/fiesc/ibge/paic/is_sidra_paic/',
 '/raw/usr/fiesc/ibge/pesq_men_com/8188_BR/',
 '/raw/usr/fiesc/ibge/pib/municipios/5938_BR/',
 '/raw/usr/fiesc/ibge/pms/is_sidra_pms/',
 '/raw/usr/fiesc/ibge/sidra/pim_pf/',
 '/raw/usr/fiesc/me/comex/export/mun/',
 '/raw/usr/fiesc/me/comex/export/ncm/',
 '/raw/usr/fiesc/me/comex/import/mun/',
 '/raw/usr/fiesc/me/comex/import/ncm/',
 '/raw/usr/fiesc/sidra/1849_FATO/',
 '/raw/usr/ibge/deflator_pnad/',
 '/raw/usr/inep_censo_escolar/etapa_ensino_agrupada/',
 '/raw/usr/inep_enem/parametros_rampa/',
 '/raw/usr/inep_saeb/competencias_e_habilidades_ajuste_lp/',
 '/raw/usr/inep_saeb/competencias_e_habilidades_ajuste_mt/',
 '/raw/usr/inep_saeb/competencias_e_habilidades_lp/',
 '/raw/usr/inep_saeb/competencias_e_habilidades_mt/',
 '/raw/usr/inep_saeb/mascara_escolas_sesi/',
 '/raw/usr/me/cadastro_cbo/',
 '/raw/usr/me/cadastro_cbo_familia/',
 '/raw/usr/me/cadastro_cbo_perfil_ocupacional/',
 '/raw/usr/me/cadastro_cbo_sinonimo/',
 '/raw/usr/me/rais_estabelecimento/',
 '/raw/usr/me/rais_vinculo/',
 '/raw/usr/ocde/intensidade_tecnol/',
 '/raw/usr/oni/bases_do_projeto/aprendizagem/codigo_familia/',
 '/raw/usr/oni/bases_do_projeto/aprendizagem/tam_estabelecimentos/',
 '/raw/usr/oni/bases_do_projeto/aprendizagem/tipo_vinculo_rais/',
 '/raw/usr/oni/bases_do_projeto/mapa_do_trabalho/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/clt/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/estagio/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/jovem_aprendiz/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/pj/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/temporario/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/trabalho_hibrido/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/dicionarios/trabalho_remoto/',
 '/raw/usr/oni/bases_do_projeto/monitor_de_vagas/padroes_regex/nivel_formacao/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/contribuintes/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/faixa_etaria/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/grau_instrucao_pnad/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/grau_instrucao_rais/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/pib/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/raca_rais/',
 '/raw/usr/oni/bases_do_projeto/painel_dos_estados/tam_estabelecimento/',
 '/raw/usr/oni/ibge/geo_municipios/',
 '/raw/usr/oni/ibge/geo_uf/',
 '/raw/usr/oni/ibge/municipios_amazonia_legal/',
 '/raw/usr/oni/ibge/uf/',
 '/raw/usr/uniepro/base_escolas/',
 '/raw/usr/uniepro/cnae_industrial/',
 '/raw/usr/uniepro/faixa_etaria/',
 '/raw/usr/uniepro/fmi_proj/',
 '/raw/usr/uniepro/grau_instrucao/',
 '/raw/usr/uniepro/ibge_cnae_classe/',
 '/raw/usr/uniepro/ibge_municipios/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/clt/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/estagio/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/jovem_aprendiz/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/pj/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/temporario/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/trabalho_hibrido/',
 '/raw/usr/uniepro/monitor_de_vagas/dicionarios/trabalho_remoto/',
 '/raw/usr/uniepro/monitor_de_vagas/padroes_regex/nivel_formacao/',
 '/raw/usr/uniepro/monitor_de_vagas/uf/',
 '/raw/usr/uniepro/ocup_indust_cbodom/',
 '/raw/usr/uniepro/rfb/siafi/',
 '/raw/usr/uniepro/saude_cid/']

# COMMAND ----------

df5 = ['/raw/crw/aco_brasil/prod_aco_nacional/',
 '/raw/crw/aneel/gera_energia_distrib/',
 '/raw/crw/banco_mundial/documentacao_indica/']

# COMMAND ----------

from pyspark.sql.window import Window
import pyspark.sql.functions as f
from pyspark.sql.functions import *
from pyspark.sql.functions import sha2
from pyspark.sql.types import *
from pyspark.sql.functions import datediff,col,when,greatest

count = []
for i in df5:
  var_adls_uri = 'abfss://datalake@cnibigdatadlsgen2.dfs.core.windows.net'
  path = f'{var_adls_uri}/{i}'
  try:
    Q = spark.read.format("parquet").option("mergeSchema", False).load(path)
    Q = len(Q.columns)
    #print(Q)
  except:
    pass
  count.append({'counts_columns':Q})

df_ct = spark.createDataFrame(data=count)
df_ct.select(sum('counts_columns')).show()

# COMMAND ----------

