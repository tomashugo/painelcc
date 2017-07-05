import time 
import datetime 
import os 
from datetime import date
from datetime import timedelta
import sys

os.system("cls")

cont=1
nome_diretorio=str(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
tempo_teste_zerado_V =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
tempo_teste_zerado_V_desp =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
tempo_teste_zerado_I =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
tempo_teste_zerado_I_desp =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
tempo_teste_saturado_I =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
queda_tensao =float(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
hora_corrente_inicio =str(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
hora_corrente_fim =str(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
hora_corrente_desp_inicio =str(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
hora_corrente_desp_fim =str(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
porc_carga_oper_inst =float(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
Dif_I_pri_sec_380 =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')])
cont=cont+2
Dif_I_pri_sec_13 =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('\n')]) 
cont=cont+2
Dif_I_pri_sec_34_69 =int(parametros[cont][parametros[cont].find('=')+2:parametros[cont].find('=')+2+10])



nome_diretorio="E:\\CEMAR\\ALGORITMOS\\ALLAS JONY\\PYTHON\\CELPA\\"
nome_arq=os.listdir(nome_diretorio)

ii=0


medidor_mm_VA=[]
nome_arq_VA=[]

ultimo_intervalo_demanda=[]
primeiro_intervalo_demanda=[]
data_todos_arquiv = []

#Deman_media_tot=[]
#Deman_max_tot=[]
#fat_carga_tot=[]
medidor_mm=[]
data_leitura_tot=[]
dia_semana_leit_tot=[]
#fat_carga_med_util_tot=[]
#fat_carga_med_n_util_tot=[]

#Energia_MM_tot=[]
#Energia_mes_30D_tot=[]
#demanda_mes_max_util_tot=[]
#demanda_mes_min_util_tot=[]
#demanda_mes_max_n_util_tot=[]
#demanda_mes_min_n_util_tot=[]
#demanda_desvpad_tot=[]
hora_trab_dia_util_tot=[]
hora_trab_dia_n_util_tot=[]
#Energia_mes_30D_util_tot=[]
#Energia_mes_30D_n_util_tot=[]

DATA_FIM_MEMO_V_Neg_TOT=[]
DATA_FIM_MEMO_V_ZERO_TOT=[]
DATA_FIM_MEMO_V_DESP_TOT=[]
DATA_FIM_MEMO_I_Neg_TOT=[]
DATA_FIM_MEMO_I_sat_TOT=[]
DATA_FIM_MEMO_I_ZERO_TOT=[]
DATA_FIM_MEMO_I_DESP_TOT=[]

medidor_corr_II_comp= []
medidor_tens_VV_comp= []
medidor_pot_WW_comp= []

data_pot_WW_comp=[]
data_corr_II_comp=[]
data_tens_VV_comp=[]

medidor_Vabc = []
alerta_Va_tot = []
data_alerta_Va_tot= []
alerta_Vb_tot= []
data_alerta_Vb_tot= []
alerta_Vc_tot= []
data_alerta_Vc_tot= []
cont_max_Va_tot= []
cont_max_Vb_tot= []
cont_max_Vc_tot= []
alerta_desp_V= []
data_alerta_desp_V= []
cont_max_desp_tot= []
cont_max_desp_V_tot = []
data_inic_alerta_Va_tot = []
data_inic_alerta_Vb_tot = []
data_inic_alerta_Vc_tot = []
data_inic_alerta_desp_V = []

media_Va_tot_tot= []
media_Vb_tot_tot= []
media_Vc_tot_tot= []

media_VVVaa_tot_tot= []
media_VVVab_tot_tot= []
media_VVVac_tot_tot= []
media_VVVba_tot_tot= []
media_VVVbb_tot_tot= []
media_VVVbc_tot_tot= []
media_VVVca_tot_tot= []
media_VVVcb_tot_tot= []
media_VVVcc_tot_tot= []

media_VVVMMaa_tot_tot= []
media_VVVMMab_tot_tot= []
media_VVVMMac_tot_tot= []
media_VVVMMba_tot_tot= []
media_VVVMMbb_tot_tot= []
media_VVVMMbc_tot_tot= []
media_VVVMMca_tot_tot= []
media_VVVMMcb_tot_tot= []
media_VVVMMcc_tot_tot= []

media_IIIMMaa_tot_tot= []
media_IIIMMab_tot_tot= []
media_IIIMMac_tot_tot= []
media_IIIMMba_tot_tot= []
media_IIIMMbb_tot_tot= []
media_IIIMMbc_tot_tot= []
media_IIIMMca_tot_tot= []
media_IIIMMcb_tot_tot= []
media_IIIMMcc_tot_tot= []

ARQ_V_ZERO_Neg_TOT = []
MED_V_ZERO_Neg_TOT= []
data_inic_alerta_Vc_Neg_tot= []
data_inic_alerta_Vb_Neg_tot= []
data_inic_alerta_Va_Neg_tot= []
cont_max_Vc_Neg_tot= []
cont_max_Vb_Neg_tot= []
cont_max_Va_Neg_tot= []
alerta_Va_Neg_tot= []
data_alerta_Va_Neg_tot= []
alerta_Vb_Neg_tot= []
data_alerta_Vb_Neg_tot= []
alerta_Vc_Neg_tot= []
data_alerta_Vc_Neg_tot= []


medidor_Iabc = []
alerta_Ia_tot = []
data_alerta_Ia_tot= []
alerta_Ib_tot= []
data_alerta_Ib_tot= []
alerta_Ic_tot= []
data_alerta_Ic_tot= []
cont_max_Ia_tot= []
cont_max_Ib_tot= []
cont_max_Ic_tot= []
alerta_desp_I= []
data_alerta_desp_I= []
cont_max_desp_I_tot= []
cont_max_I_desp_tot = []

media_Ia_tot_tot= []
media_Ib_tot_tot= []
media_Ic_tot_tot= []

data_inic_alerta_Ia_tot= []
data_inic_alerta_Ib_tot= []
data_inic_alerta_Ic_tot= []
data_inic_alerta_desp_I = []


MED_V_ZERO_TOT = []
ARQ_V_ZERO_TOT  = []
MED_V_DESP_TOT = []
ARQ_V_DESP_TOT = []


MED_I_ZERO_TOT= []
ARQ_I_ZERO_TOT =[]
MED_I_DESP_TOT= []
ARQ_I_DESP_TOT =[]


ARQ_I_ZERO_Neg_TOT =[]
MED_I_ZERO_Neg_TOT=[]
data_inic_alerta_Ia_Neg_tot=[]
data_inic_alerta_Ib_Neg_tot=[]
data_inic_alerta_Ic_Neg_tot=[]
cont_max_Ia_Neg_tot=[]
cont_max_Ib_Neg_tot=[]
cont_max_Ic_Neg_tot=[]
alerta_Ia_Neg_tot=[]
data_alerta_Ia_Neg_tot=[]
alerta_Ib_Neg_tot=[]
data_alerta_Ib_Neg_tot=[]
alerta_Ic_Neg_Neg_tot=[]
data_alerta_Ic_Neg_tot=[]



alerta_Ia_sat_tot=[]
data_alerta_Ia_sat_tot=[]
alerta_Ib_sat_tot=[]
data_alerta_Ib_sat_tot=[]
alerta_Ic_sat_tot=[]
data_alerta_Ic_sat_tot=[]

cont_max_Ia_sat_tot=[]
cont_max_Ib_sat_tot=[]
cont_max_Ic_sat_tot=[]

media_IIIMMaa_tot_sat_tot=[]
media_IIIMMab_tot_sat_tot=[]
media_IIIMMac_tot_sat_tot=[]

media_IIIMMba_tot_sat_tot=[]
media_IIIMMbb_tot_sat_tot=[]
media_IIIMMbc_tot_sat_tot=[]

media_IIIMMca_tot_sat_tot=[]
media_IIIMMcb_tot_sat_tot=[]
media_IIIMMcc_tot_sat_tot=[]


data_inic_alerta_Ia_sat_tot=[]
data_inic_alerta_Ib_sat_tot=[]
data_inic_alerta_Ic_sat_tot=[]

ARQ_I_ZERO_sat_TOT=[]
MED_I_ZERO_sat_TOT=[]

for i in nome_arq:        
    if i.find('&') >= 0 and i.find('¢') < 0:
        caminho_arq=nome_diretorio+i
        memo_massa = open(caminho_arq)
        arquivo=""
        for j in memo_massa:                        
            linha=j.split('\r\n')           
            arquivo=arquivo+linha[0]
            if arquivo.find("CONT") >= 0:
                palavras = arquivo[152:158]            
            else:
                if arquivo.find("SALV")>=0:
                    palavras = arquivo[158:164]
                else:
                    palavras = 3            

        medidor_mm.append(arquivo[0:8])
        medidor_mm[len(medidor_mm)-1]=''+medidor_mm[len(medidor_mm)-1]
        print(i)
        print(medidor_mm[ii])
        print('ttttttt')

        if int(arquivo[36:38]) >=1 and int(arquivo[36:38]) <= 12:

            ultimo_intervalo_demanda=datetime.datetime(2000+int(arquivo[38:40]),int(arquivo[36:38]),int(arquivo[34:36]),int(arquivo[28:30]),int(arquivo[30:32]),int(arquivo[32:34]))
            delta = timedelta(minutes=int(palavras)/3*5-5)
            intervalo_5_minutos = timedelta(minutes=5)

            primeiro_intervalo_demanda=ultimo_intervalo_demanda - delta

            print(arquivo[2311:2315])

            date2 =""
            if arquivo[2315:2321] == "011011":
                medidor_pot_WW_comp.append(medidor_mm[ii])
                date2 = str(ultimo_intervalo_demanda.date())
                data_pot_WW_comp.append(date2)
        
            if (arquivo[2315:2321] == "363738" or arquivo[2315:2321] == "202122" or arquivo[2315:2321] == "171819"):
                medidor_mm_VA.append(medidor_mm[ii])
                nome_arq_VA.append(i)
                data_todos_arquiv.append(str(ultimo_intervalo_demanda.date()))

        const_mult=0
        if (arquivo[2315:2321] == "363738" or arquivo[2315:2321] == "202122" or arquivo[2315:2321] == "171819"):
            if int(arquivo[266:272]) != 0:
                const_mult=int(arquivo[260:266])/(int(arquivo[266:272]))
        if (const_mult == 0.0125 or const_mult == 0) and (arquivo[2315:2321] == "363738" or arquivo[2315:2321] == "202122" or arquivo[2315:2321] == "171819"):
            medidor_Vabc.append(medidor_mm)

            Va = []
            Vb = []
            Vc = []

            j=0
            indice=0
            while j<len(arquivo):
                increm=4
                inicio=j+12
                fim=j+12+increm
                ind=j+1
               
                if arquivo[j:j+4].find("CONT") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Va.append(int(arquivo[inicio:fim]))
                            #if arquivo[2296:2300] != '0000':
                                #print(inicio)
                                #print(fim)
                                #print(arquivo[inicio:fim])
                                #print(arquivo[2296:2300])
                                #quest = sys.stdin.readline()
                            inicio=fim
                            fim=fim+increm
                            Vb.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vc.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                            
                if arquivo[j:j+4].find("SALV") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Va.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vb.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vc.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                            
                j=j+1


            if Va != [] and Vb != [] and Vc != []:
            
                data_leitura=[]
                hora_leitura = []
                date1 = str(primeiro_intervalo_demanda.date())
                date2 = str(ultimo_intervalo_demanda.date())
                hora1 = str(primeiro_intervalo_demanda.time())
                hora2 = str(ultimo_intervalo_demanda.time())
                data_tens_VV_comp.append(date2)
                medidor_tens_VV_comp.append(medidor_mm[ii])
                
                while (date1<date2) or (hora1 <= hora2):
                    data_leitura.append(str(primeiro_intervalo_demanda))
                    delta = timedelta(minutes=5)
                    primeiro_intervalo_demanda = primeiro_intervalo_demanda + delta
                    date1 = str(primeiro_intervalo_demanda.date())
                    hora1 = str(primeiro_intervalo_demanda.time())
                
                j=0
                cont_V = 0
                test_V = 0
                cont_V2a = 0
                cont_V2b = 0
                cont_V2c = 0
                cont_V2aaa = 0
                alerta_Vb = []
                alerta_Va = []
                alerta_desp_Va = []
                alerta_Vc = []
                data_alerta_desp_Va = []
                data_alerta_Va = []
                data_alerta_Vb= []
                data_alerta_Vc= []
                cont_max=[]
                cont_max_a=[]
                cont_max_b=[]
                cont_max_c=[]
                data_inic_alerta_Va=[]
                data_inic_alerta_Vb=[]
                data_inic_alerta_Vc=[]
                data_fim_alerta_Va=[]
                data_fim_alerta_Vb=[]
                data_fim_alerta_Vc=[]
                inicio_test_a=[]
                inicio_test_b=[]
                inicio_test_c=[]
                cont_VVa = 0
                cont_VVb = 0
                cont_VVc = 0
                test_passou = 0
                kwk=1
                aux_data_a=[]
                aux_data_b=[]
                aux_data_c=[]
                media_VVVaa=[]
                media_VVVab=[]
                media_VVVac=[]
                media_VVVaa_tot= []
                media_VVVab_tot= []
                media_VVVac_tot= []

                media_VVVba=[]
                media_VVVbb=[]
                media_VVVbc=[]
                media_VVVba_tot= []
                media_VVVbb_tot= []
                media_VVVbc_tot= []

                media_VVVca=[]
                media_VVVcb=[]
                media_VVVcc=[]
                media_VVVca_tot= []
                media_VVVcb_tot= []
                media_VVVcc_tot= []
                while j<len(Va):
                    

                    if Va[j] >=2048:
                        if cont_VVa==0:
                            inicio_test_a = data_leitura[j]
                        cont_VVa =cont_VVa+1
                        media_VVVaa.append(Va[j])
                        media_VVVab.append(Vb[j])
                        media_VVVac.append(Vc[j])

                        if cont_VVa>1 and data_alerta_Va !=[]:
                            del data_alerta_Va[len(data_alerta_Va) -1]
                            del media_VVVaa_tot[len(media_VVVaa_tot) -1]
                            del media_VVVab_tot[len(media_VVVab_tot) -1]
                            del media_VVVac_tot[len(media_VVVac_tot) -1]
                        data_alerta_Va.append(data_leitura[j])
                        test_passou = 1
                        aux_data_a=inicio_test_a
                        
                        media_VVVaa_tot.append(sum(media_VVVaa)/(len(media_VVVaa)))
                        
                        
                        media_VVVab_tot.append(sum(media_VVVab)/(len(media_VVVab)))
                        
                        
                        media_VVVac_tot.append(sum(media_VVVac)/(len(media_VVVac)))
                        
                        if j+1==len(Va):
                            data_inic_alerta_Va.append(inicio_test_a)
                            data_fim_alerta_Va.append(data_alerta_Va[len(data_alerta_Va)-1])
                            alerta_Va.append("LIGAÇÃO TP INVERTIDA")
                    else:
                        if cont_VVa>0:
                            data_inic_alerta_Va.append(inicio_test_a)
                            data_fim_alerta_Va.append(data_alerta_Va[len(data_alerta_Va)-1])
                            alerta_Va.append("LIGAÇÃO TP INVERTIDA")
                        cont_VVa = 0
                        aux_data_a=[]
                        cont_V = 0
                        media_VVVaa=[]
                        media_VVVab=[]
                        media_VVVac=[]
                
                    
                    if Vb[j] >=2048:
                        if cont_VVb==0:
                            inicio_test_b = data_leitura[j]
                        cont_VVb =cont_VVb+1
                        media_VVVba.append(Va[j])
                        media_VVVbb.append(Vb[j])
                        media_VVVbc.append(Vc[j])

                        if cont_VVb>1 and data_alerta_Vb !=[]:
                            del data_alerta_Vb[len(data_alerta_Vb) -1]
                            del media_VVVba_tot[len(media_VVVba_tot) -1]
                            del media_VVVbb_tot[len(media_VVVbb_tot) -1]
                            del media_VVVbc_tot[len(media_VVVbc_tot) -1]
                        data_alerta_Vb.append(data_leitura[j])
                        test_passou = 1
                        aux_data_b=inicio_test_b
                        
                        media_VVVba_tot.append(sum(media_VVVba)/(len(media_VVVba)))
                        
                        
                        media_VVVbb_tot.append(sum(media_VVVbb)/(len(media_VVVbb)))
                        
                        
                        media_VVVbc_tot.append(sum(media_VVVbc)/(len(media_VVVbc)))
                        
                        if j+1==len(Va):
                            data_inic_alerta_Vb.append(inicio_test_b)
                            data_fim_alerta_Vb.append(data_alerta_Vb[len(data_alerta_Vb)-1])
                            alerta_Vb.append("LIGAÇÃO TP INVERTIDA")
                        
                    else:
                        if cont_VVb>0:
                            data_inic_alerta_Vb.append(inicio_test_b)
                            data_fim_alerta_Vb.append(data_alerta_Vb[len(data_alerta_Vb)-1])
                            alerta_Vb.append("LIGAÇÃO TP INVERTIDA")
                        cont_VVb = 0
                        aux_data_b=[]
                        media_VVVba=[]
                        media_VVVbb=[]
                        media_VVVbc=[]

                        
                    if Vc[j] >=2048:
                        if cont_VVc==0:
                            inicio_test_c = data_leitura[j]
                        cont_VVc =cont_VVc+1
                        media_VVVca.append(Va[j])
                        media_VVVcb.append(Vb[j])
                        media_VVVcc.append(Vc[j])

                        if cont_VVc>1 and data_alerta_Vc !=[]:
                            del data_alerta_Vc[len(data_alerta_Vc) -1]
                            del media_VVVca_tot[len(media_VVVca_tot) -1]
                            del media_VVVcb_tot[len(media_VVVcb_tot) -1]
                            del media_VVVcc_tot[len(media_VVVcc_tot) -1]
                        data_alerta_Vc.append(data_leitura[j])
                        test_passou = 1
                        aux_data_c=inicio_test_c
                        
                        media_VVVca_tot.append(sum(media_VVVca)/(len(media_VVVca)))
                        
                        
                        media_VVVcb_tot.append(sum(media_VVVcb)/(len(media_VVVcb)))
                        
                        
                        media_VVVcc_tot.append(sum(media_VVVcc)/(len(media_VVVcc)))
                        

                        if j+1==len(Va):
                            data_inic_alerta_Vc.append(inicio_test_c)
                            data_fim_alerta_Vc.append(data_alerta_Vc[len(data_alerta_Vc)-1])
                            alerta_Vc.append("LIGAÇÃO TP INVERTIDA")
                       
                    else:
                        if cont_VVc>0:
                            data_inic_alerta_Vc.append(inicio_test_c)
                            data_fim_alerta_Vc.append(data_alerta_Vc[len(data_alerta_Vc)-1])
                            alerta_Vc.append("LIGAÇÃO TP INVERTIDA")
                        cont_VVc = 0
                        aux_data_c=[]
                        media_VVVca=[]
                        media_VVVcb=[]
                        media_VVVcc=[]

                        
                    date=[]
                    date_a=[]
                    date_b=[]
                    date_c=[]
                    test_max_tam=data_inic_alerta_Va
                    test_max_tam_fim=data_fim_alerta_Va
                    if data_inic_alerta_Vb!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Vb) and data_inic_alerta_Vb[len(data_inic_alerta_Vb)-1]!=[]:
                            test_max_tam=data_inic_alerta_Vb
                            test_max_tam_fim=data_fim_alerta_Vb
                    if data_inic_alerta_Vc!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Vc) and data_inic_alerta_Vc[len(data_inic_alerta_Vc)-1]!=[]:
                            test_max_tam=data_inic_alerta_Vc
                            test_max_tam_fim=data_fim_alerta_Vc
                    if test_max_tam!=[]:
                        date_fim = datetime.datetime.strptime(test_max_tam_fim[len(test_max_tam_fim)-1], '%Y-%m-%d %H:%M:%S')
                        date=datetime.datetime.strptime(test_max_tam[len(test_max_tam)-1], '%Y-%m-%d %H:%M:%S')

                    if aux_data_a!=[]:
                        date_a=datetime.datetime.strptime(aux_data_a, '%Y-%m-%d %H:%M:%S')
                   
                    if aux_data_b!=[]:
                        date_b=datetime.datetime.strptime(aux_data_b, '%Y-%m-%d %H:%M:%S')
                    
                    if aux_data_c!=[]:
                        date_c=datetime.datetime.strptime(aux_data_c, '%Y-%m-%d %H:%M:%S')

                    
                    if date_a!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Va[len(data_alerta_Va)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Va)<len(test_max_tam):             
                            if date.date()<date_a.date() or j+1==len(Va) or (date.date()>date_a.date() and len(data_inic_alerta_Va)>0 and (date_interm).date()!=date_fim.date()):

                                alerta_Va.append("LIGACAO TP INVERTIDA")
                                data_fim_alerta_Va.append([])
                                data_inic_alerta_Va.append([])
                                media_VVVaa_tot.append([])
                                media_VVVab_tot.append([])
                                media_VVVac_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Va)<len(test_max_tam):
                            alerta_Va.append("LIGACAO TP INVERTIDA")
                            data_fim_alerta_Va.append([])
                            data_inic_alerta_Va.append([])
                            media_VVVaa_tot.append([])
                            media_VVVab_tot.append([])
                            media_VVVac_tot.append([])
                            
                    if date_b!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Vb[len(data_alerta_Vb)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Vb)<len(test_max_tam):                        
                            if date.date()<date_b.date() or j+1==len(Va) or (date.date()>date_b.date() and len(data_inic_alerta_Vb)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Vb.append("LIGACAO TP INVERTIDA")
                                data_fim_alerta_Vb.append([])
                                data_inic_alerta_Vb.append([])
                                media_VVVba_tot.append([])
                                media_VVVbb_tot.append([])
                                media_VVVbc_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Vb)<len(test_max_tam):
                            alerta_Vb.append("LIGACAO TP INVERTIDA")
                            data_fim_alerta_Vb.append([])
                            data_inic_alerta_Vb.append([])
                            media_VVVba_tot.append([])
                            media_VVVbb_tot.append([])
                            media_VVVbc_tot.append([])
                            
                    if date_c!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Vc[len(data_alerta_Vc)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Vc)<len(test_max_tam):                    
                            if date.date()<date_c.date() or j+1==len(Va) or (date.date()>date_c.date() and len(data_inic_alerta_Vc)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Vc.append("LIGACAO TP INVERTIDA")
                                data_fim_alerta_Vc.append([])
                                data_inic_alerta_Vc.append([])
                                media_VVVca_tot.append([])
                                media_VVVcb_tot.append([])
                                media_VVVcc_tot.append([])
                            else:
                                break
                            
                    else:
                        while len(data_inic_alerta_Vc)<len(test_max_tam):
                            alerta_Vc.append("LIGACAO TP INVERTIDA")
                            data_fim_alerta_Vc.append([])
                            data_inic_alerta_Vc.append([])  
                            media_VVVca_tot.append([])
                            media_VVVcb_tot.append([])
                            media_VVVcc_tot.append([])
                    j=j+1


                if test_passou != 0:
                    DATA_FIM_MEMO_V_Neg_TOT.append(data_leitura[j-1])

                if alerta_Va!=[] or alerta_Vb!=[] or alerta_Vc!=[]:
                    alerta_Va_Neg_tot.append(alerta_Va)
                    data_alerta_Va_Neg_tot.append(data_fim_alerta_Va)
                
                    alerta_Vb_Neg_tot.append(alerta_Vb)
                    data_alerta_Vb_Neg_tot.append(data_fim_alerta_Vb)
                
                    alerta_Vc_Neg_tot.append(alerta_Vc)
                    data_alerta_Vc_Neg_tot.append(data_fim_alerta_Vc)

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Va):
                    if data_fim_alerta_Va[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Va[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Va[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_a.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_a.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Vb):
                    if data_fim_alerta_Vb[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Vb[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Vb[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_b.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_b.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Vc):
                    if data_fim_alerta_Vc[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Vc[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Vc[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_c.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_c.append(0)
                    j=j+1

                if cont_max_a!=[] or cont_max_b!=[] or cont_max_c!=[]:
                    cont_max_Va_Neg_tot.append(cont_max_a)
                
                    cont_max_Vb_Neg_tot.append(cont_max_b)
                
                    cont_max_Vc_Neg_tot.append(cont_max_c)

                if media_VVVaa_tot != [] or media_VVVab_tot != [] or media_VVVac_tot != []:

                    media_VVVaa_tot_tot.append(media_VVVaa_tot)
                    media_VVVab_tot_tot.append(media_VVVab_tot)
                    media_VVVac_tot_tot.append(media_VVVac_tot)

                if media_VVVba_tot != [] or media_VVVbb_tot != [] or media_VVVbc_tot != []:

                    media_VVVba_tot_tot.append(media_VVVba_tot)
                    media_VVVbb_tot_tot.append(media_VVVbb_tot)
                    media_VVVbc_tot_tot.append(media_VVVbc_tot)

                if media_VVVca_tot != [] or media_VVVcb_tot != [] or media_VVVcc_tot != []:

                    media_VVVca_tot_tot.append(media_VVVca_tot)
                    media_VVVcb_tot_tot.append(media_VVVcb_tot)
                    media_VVVcc_tot_tot.append(media_VVVcc_tot)
            
                if data_inic_alerta_Va!=[] or data_inic_alerta_Vb!=[] or data_inic_alerta_Vc!=[]:
                    data_inic_alerta_Va_Neg_tot.append(data_inic_alerta_Va)
                    
                    data_inic_alerta_Vb_Neg_tot.append(data_inic_alerta_Vb)
                
                    data_inic_alerta_Vc_Neg_tot.append(data_inic_alerta_Vc)

                
                if test_passou != 0:
                    ARQ_V_ZERO_Neg_TOT.append(i)
                    MED_V_ZERO_Neg_TOT.append(medidor_mm[ii])
                    
            Va = []
            Vb = []
            Vc = []


            j=0
            indice=0
            while j<len(arquivo):
                increm=4
                inicio=j+12
                fim=j+12+increm
                ind=j+1
               
                if arquivo[j:j+4].find("CONT") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
    
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Va.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vb.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vc.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                            
                if arquivo[j:j+4].find("SALV") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Va.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vb.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Vc.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                            
                            
                j=j+1


            if Va != [] and Vb != [] and Vc != []:
            
                j=0
                cont_V = 0
                test_V = 0
                cont_V2a = 0
                cont_V2b = 0
                cont_V2c = 0
                cont_V2aaa = 0
                alerta_Vb = []
                alerta_Va = []
                alerta_desp_Va = []
                alerta_Vc = []
                data_alerta_desp_Va = []
                data_alerta_Va = []
                data_alerta_Vb= []
                data_alerta_Vc= []
                cont_max=[]
                cont_max_a=[]
                cont_max_b=[]
                cont_max_c=[]
                data_inic_alerta_Va=[]
                data_inic_alerta_Vb=[]
                data_inic_alerta_Vc=[]
                data_fim_alerta_Va=[]
                data_fim_alerta_Vb=[]
                data_fim_alerta_Vc=[]
                inicio_test_a=[]
                inicio_test_b=[]
                inicio_test_c=[]
                cont_VVa = 0
                cont_VVb = 0
                cont_VVc = 0
                test_passou = 0
                test_passou =0
                kwk=1
                aux_data_a=[]
                aux_data_b=[]
                aux_data_c=[]

                media_VVVaa=[]
                media_VVVab=[]
                media_VVVac=[]
                media_VVVaa_tot= []
                media_VVVab_tot= []
                media_VVVac_tot= []

                media_VVVba=[]
                media_VVVbb=[]
                media_VVVbc=[]
                media_VVVba_tot= []
                media_VVVbb_tot= []
                media_VVVbc_tot= []

                media_VVVca=[]
                media_VVVcb=[]
                media_VVVcc=[]
                media_VVVca_tot= []
                media_VVVcb_tot= []
                media_VVVcc_tot= []

                #tempo_teste_zerado_V = 4

                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""select cod_un_cons_reu FROM rel_equip_uc@ri_carga
    WHERE (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result_uc_med = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora


                result_2elem = []
                if result_uc_med != []:
                    cursor.execute("""SELECT COD_UN_CONS_REU, COD_TIPO_EQIP_REU,  COUNT (COD_TIPO_EQIP_REU) contador 
FROM REL_EQUIP_UC@ri_carga
WHERE COD_UN_CONS_REU  = %s
and COD_TIPO_EQIP_REU = 'TP' 
AND DTA_RETI_REU IS NULL
group by COD_UN_CONS_REU, COD_TIPO_EQIP_REU
HAVING (Count(COD_TIPO_EQIP_REU) = 2)""" %result_uc_med[0][0])
                    result_2elem = cursor.fetchall()  # busca o resultado da consulta

                
                
                while j<len(Va):
                        

                    if Va[j] == 0:
                        if cont_VVa==0:
                            inicio_test_a = data_leitura[j]
                        cont_VVa =cont_VVa+1
                        media_VVVaa.append(Va[j])
                        media_VVVab.append(Vb[j])
                        media_VVVac.append(Vc[j])
                        if j+1==len(Va) and cont_VVa >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Va.append(inicio_test_a)
                            data_fim_alerta_Va.append(data_alerta_Va[len(data_alerta_Va)-1])
                            alerta_Va.append("TENSÃO ZERADA")
                    else:
                        if cont_VVa >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Va.append(inicio_test_a)
                            data_fim_alerta_Va.append(data_alerta_Va[len(data_alerta_Va)-1])
                            alerta_Va.append("TENSÃO ZERADA")
                        cont_VVa = 0
                        aux_data_a=[]
                        media_VVVaa=[]
                        media_VVVab=[]
                        media_VVVac=[]
                
                    if cont_VVa >= tempo_teste_zerado_V*12:
                        if cont_VVa > tempo_teste_zerado_V*12 and data_alerta_Va !=[]:
                            del data_alerta_Va[len(data_alerta_Va) -1]
                            del media_VVVaa_tot[len(media_VVVaa_tot) -1]
                            del media_VVVab_tot[len(media_VVVab_tot) -1]
                            del media_VVVac_tot[len(media_VVVac_tot) -1]
                        data_alerta_Va.append(data_leitura[j])
                        cont_V2a = cont_V2a+1
                        test_passou=1
                        aux_data_a=inicio_test_a
                        media_VVVaa_tot.append(sum(media_VVVaa)/(len(media_VVVaa)))
                        media_VVVab_tot.append(sum(media_VVVab)/(len(media_VVVab)))
                        media_VVVac_tot.append(sum(media_VVVac)/(len(media_VVVac)))
                        #print(media_VVVaa_tot)
                        #quest = sys.stdin.readline()
                        
                        



                            
                         
                    if Vb[j] == 0 and result_2elem == []:
                        if cont_VVb==0:
                            inicio_test_b = data_leitura[j]
                        cont_VVb =cont_VVb+1
                        media_VVVba.append(Va[j])
                        media_VVVbb.append(Vb[j])
                        media_VVVbc.append(Vc[j])

                        if j+1==len(Va) and cont_VVb >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Vb.append(inicio_test_b)
                            data_fim_alerta_Vb.append(data_alerta_Vb[len(data_alerta_Vb)-1])
                            alerta_Vb.append("TENSÃO ZERADA")
                    else:
                        if cont_VVb >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Vb.append(inicio_test_b)
                            data_fim_alerta_Vb.append(data_alerta_Vb[len(data_alerta_Vb)-1])
                            alerta_Vb.append("TENSÃO ZERADA")
                        cont_VVb = 0
                        aux_data_b=[]
                        media_VVVba=[]
                        media_VVVbb=[]
                        media_VVVbc=[]
                
                    if cont_VVb >= tempo_teste_zerado_V*12:
                        if cont_VVb > tempo_teste_zerado_V*12 and data_alerta_Vb !=[]:
                            del data_alerta_Vb[len(data_alerta_Vb) -1]
                            del media_VVVba_tot[len(media_VVVba_tot) -1]
                            del media_VVVbb_tot[len(media_VVVbb_tot) -1]
                            del media_VVVbc_tot[len(media_VVVbc_tot) -1]
                        data_alerta_Vb.append(data_leitura[j])
                        cont_V2b = cont_V2b+1
                        test_passou=1
                        aux_data_b=inicio_test_b
                        media_VVVba_tot.append(sum(media_VVVba)/(len(media_VVVba)))
                        media_VVVbb_tot.append(sum(media_VVVbb)/(len(media_VVVbb)))
                        media_VVVbc_tot.append(sum(media_VVVbc)/(len(media_VVVbc)))
                
                        
                        
                    if Vc[j] == 0:
                        if cont_VVc==0:
                            inicio_test_c = data_leitura[j]
                        cont_VVc =cont_VVc+1
                        media_VVVca.append(Va[j])
                        media_VVVcb.append(Vb[j])
                        media_VVVcc.append(Vc[j])
    ##                        print(cont_VVc)
    ##                        print(data_leitura[j])
    ##                        print(data_inic_alerta_Vc)
    ##                        print(data_alerta_Vc)
    ##                        print(cont_antigo_c)
    ##                        print(cont_max_c)
    ##                        quest = sys.stdin.readline()
                        if j+1==len(Va) and cont_VVc >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Vc.append(inicio_test_c)
                            data_fim_alerta_Vc.append(data_alerta_Vc[len(data_alerta_Vc)-1])
                            alerta_Vc.append("TENSÃO ZERADA")
                    else:
                        if cont_VVc >= tempo_teste_zerado_V*12:
                            data_inic_alerta_Vc.append(inicio_test_c)
                            data_fim_alerta_Vc.append(data_alerta_Vc[len(data_alerta_Vc)-1])
                            alerta_Vc.append("TENSÃO ZERADA")
                        cont_VVc = 0
                        aux_data_c=[]
                        media_VVVca=[]
                        media_VVVcb=[]
                        media_VVVcc=[]
                
                    if cont_VVc >= tempo_teste_zerado_V*12:
                        if cont_VVc > tempo_teste_zerado_V*12 and data_alerta_Vc !=[]:
                            del data_alerta_Vc[len(data_alerta_Vc) -1]
                            del media_VVVca_tot[len(media_VVVca_tot) -1]
                            del media_VVVcb_tot[len(media_VVVcb_tot) -1]
                            del media_VVVcc_tot[len(media_VVVcc_tot) -1]
                        data_alerta_Vc.append(data_leitura[j])
                        cont_V2c = cont_V2c+1
                        test_passou=1
                        aux_data_c=inicio_test_c
                        media_VVVca_tot.append(sum(media_VVVca)/(len(media_VVVca)))
                        media_VVVcb_tot.append(sum(media_VVVcb)/(len(media_VVVcb)))
                        media_VVVcc_tot.append(sum(media_VVVcc)/(len(media_VVVcc)))
                        
                    
                    


                    date=[]
                    date_a=[]
                    date_b=[]
                    date_c=[]
                    test_max_tam=data_inic_alerta_Va
                    test_max_tam_fim=data_fim_alerta_Va
                    if data_inic_alerta_Vb!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Vb) and data_inic_alerta_Vb[len(data_inic_alerta_Vb)-1]!=[]:
                            test_max_tam=data_inic_alerta_Vb
                            test_max_tam_fim=data_fim_alerta_Vb
                    if data_inic_alerta_Vc!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Vc) and data_inic_alerta_Vc[len(data_inic_alerta_Vc)-1]!=[]:
                            test_max_tam=data_inic_alerta_Vc
                            test_max_tam_fim=data_fim_alerta_Vc
                    if test_max_tam!=[]:
                        date_fim = datetime.datetime.strptime(test_max_tam_fim[len(test_max_tam_fim)-1], '%Y-%m-%d %H:%M:%S')
                        date=datetime.datetime.strptime(test_max_tam[len(test_max_tam)-1], '%Y-%m-%d %H:%M:%S')

                    if aux_data_a!=[]:
                        date_a=datetime.datetime.strptime(aux_data_a, '%Y-%m-%d %H:%M:%S')
                   
                    if aux_data_b!=[]:
                        date_b=datetime.datetime.strptime(aux_data_b, '%Y-%m-%d %H:%M:%S')
                    
                    if aux_data_c!=[]:
                        date_c=datetime.datetime.strptime(aux_data_c, '%Y-%m-%d %H:%M:%S')


        ##                #str(date_a.date())=='2014-11-13'
        ##                if  date_a!= []:      
        ##                    if i == '03100&ob.omf' and date!=[] and len(data_inic_alerta_Vb)>=2:
        ##                                print(data_inic_alerta_Va)
        ##                                print(data_inic_alerta_Vb)
        ##                                print(data_inic_alerta_Vc)
        ##                                print(date.date())
        ##                                print(date_a)
        ##                                quest = sys.stdin.readline()

                    
                    if date_a!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Va[len(data_alerta_Va)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Va)<len(test_max_tam):             
                            if date.date()<date_a.date() or j+1==len(Va) or (date.date()>date_a.date() and len(data_inic_alerta_Va)>0 and (date_interm).date()!=date_fim.date()):

                                alerta_Va.append("TENSÃO ZERADA")
                                data_fim_alerta_Va.append([])
                                data_inic_alerta_Va.append([])
                                media_VVVaa_tot.append([])
                                media_VVVab_tot.append([])
                                media_VVVac_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Va)<len(test_max_tam):
                            alerta_Va.append("TENSÃO ZERADA")
                            data_fim_alerta_Va.append([])
                            data_inic_alerta_Va.append([])
                            media_VVVaa_tot.append([])
                            media_VVVab_tot.append([])
                            media_VVVac_tot.append([])
                            
                         
                    if date_b!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Vb[len(data_alerta_Vb)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Vb)<len(test_max_tam):                        
                            if date.date()<date_b.date() or j+1==len(Va) or (date.date()>date_b.date() and len(data_inic_alerta_Vb)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Vb.append("TENSÃO ZERADA")
                                data_fim_alerta_Vb.append([])
                                data_inic_alerta_Vb.append([])
                                media_VVVba_tot.append([])
                                media_VVVbb_tot.append([])
                                media_VVVbc_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Vb)<len(test_max_tam):
                            alerta_Vb.append("TENSÃO ZERADA")
                            data_fim_alerta_Vb.append([])
                            data_inic_alerta_Vb.append([])
                            media_VVVba_tot.append([])
                            media_VVVbb_tot.append([])
                            media_VVVbc_tot.append([])
                            
                    if date_c!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Vc[len(data_alerta_Vc)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Vc)<len(test_max_tam):                    
                            if date.date()<date_c.date() or j+1==len(Va) or (date.date()>date_c.date() and len(data_inic_alerta_Vc)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Vc.append("TENSÃO ZERADA")
                                data_fim_alerta_Vc.append([])
                                data_inic_alerta_Vc.append([])
                                media_VVVca_tot.append([])
                                media_VVVcb_tot.append([])
                                media_VVVcc_tot.append([])
                            else:
                                break
                            
                    else:
                        while len(data_inic_alerta_Vc)<len(test_max_tam):
                            alerta_Vc.append("TENSÃO ZERADA")
                            data_fim_alerta_Vc.append([])
                            data_inic_alerta_Vc.append([])  
                            media_VVVca_tot.append([])
                            media_VVVcb_tot.append([])
                            media_VVVcc_tot.append([])
                    j=j+1


                if test_passou !=0:
                    DATA_FIM_MEMO_V_ZERO_TOT.append(data_leitura[j-1])
                
                if alerta_Va!=[] or alerta_Vb!=[] or alerta_Vc!=[]:
                    alerta_Va_tot.append(alerta_Va)
                    data_alerta_Va_tot.append(data_fim_alerta_Va)
               
                    alerta_Vb_tot.append(alerta_Vb)
                    data_alerta_Vb_tot.append(data_fim_alerta_Vb)
                
                    alerta_Vc_tot.append(alerta_Vc)
                    data_alerta_Vc_tot.append(data_fim_alerta_Vc)


                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Va):
                    if data_inic_alerta_Va[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Va[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Va[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_a.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_a.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Vb):
                    if data_inic_alerta_Vb[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Vb[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Vb[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_b.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_b.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Vc):
                    if data_inic_alerta_Vc[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Vc[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Vc[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_c.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_c.append(0)
                    j=j+1



                if cont_max_a!=[] or cont_max_b!=[] or cont_max_c!=[]:
                    cont_max_Va_tot.append(cont_max_a)
                
                    cont_max_Vb_tot.append(cont_max_b)
                
                    cont_max_Vc_tot.append(cont_max_c)


                
                if media_VVVaa_tot != [] or media_VVVab_tot != [] or media_VVVac_tot != []:
        
                    media_VVVMMaa_tot_tot.append(media_VVVaa_tot)
                    media_VVVMMab_tot_tot.append(media_VVVab_tot)
                    media_VVVMMac_tot_tot.append(media_VVVac_tot)

                if media_VVVba_tot != [] or media_VVVbb_tot != [] or media_VVVbc_tot != []:
        
                    media_VVVMMba_tot_tot.append(media_VVVba_tot)
                    media_VVVMMbb_tot_tot.append(media_VVVbb_tot)
                    media_VVVMMbc_tot_tot.append(media_VVVbc_tot)

                if media_VVVca_tot != [] or media_VVVcb_tot != [] or media_VVVcc_tot != []:
        
                    media_VVVMMca_tot_tot.append(media_VVVca_tot)
                    media_VVVMMcb_tot_tot.append(media_VVVcb_tot)
                    media_VVVMMcc_tot_tot.append(media_VVVcc_tot)



                if data_inic_alerta_Va !=[] or data_inic_alerta_Vb!=[] or data_inic_alerta_Vc!=[]:
                    data_inic_alerta_Va_tot.append(data_inic_alerta_Va)
                
                    data_inic_alerta_Vb_tot.append(data_inic_alerta_Vb)
                
                    data_inic_alerta_Vc_tot.append(data_inic_alerta_Vc)


                
                if test_passou !=0:
                    ARQ_V_ZERO_TOT.append(i)
                    MED_V_ZERO_TOT.append(medidor_mm[ii])
                    
            


                #cursor.execute("""select T.UC , T.RTP, QTD_TENS_SEC_UEE AS TENS_PRI, QTD_TENS_SEC_UEE/(T.RTP*1.7) AS TENS_SEC  FROM auxi_table100, cad_uc_ee@ri_carga, C_ALTA_TENSAO2 TA
    #WHERE UC = COD_UN_CONS_UEE
    #AND T.UC = TA.UC
    #AND TA.MED = %s """, (medidor_mm[ii]))
                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""select T.UC_RTP , T.RTP  FROM RTP_TABLE T, rel_equip_uc@ri_carga TA
    WHERE T.UC_RTP = TA.cod_un_cons_reu
    and (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND TA.num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora


                if result == []:
                    aux_rtp_ee = 1
                else:
                    aux_rtp_ee = result[0][1]
                cursor.execute("""select QTD_TENS_LIG_UEE AS TENS_PRI, QTD_TENS_LIG_UEE/('%s'*1.7) AS TENS_SEC  FROM cad_uc_ee@ri_carga,rel_equip_uc@ri_carga 
     WHERE cod_un_cons_uee = cod_un_cons_reu
    and (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND num_eqip_reu = '%s' """ %(aux_rtp_ee,date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result_desp = cursor.fetchall()  # busca o resultado da consulta

                #print('ççççççççç')
                #quest = sys.stdin.readline()
                

                media_Va=[]
                media_Vb=[]
                media_Vc=[]
                media_Va_tot= []
                media_Vb_tot= []
                media_Vc_tot= []
                j=0
                #digitar valor em horas ####################
                #tempo_teste_zerado_V_desp = 4
                #PORCENTAGEM DE QUEDA DE TENSAO NORMAL
                #queda_tensao=0.25
                inicio_test=0
                data_inic_alerta_desp_Va=[]
                test_passou = 0
                eueueue=0
                while j<len(Va):
                    
                    

                    Vmax=Va[j]
                    if Vmax<=Vb[j]:
                        Vmax=Vb[j]
                    if Vmax<=Vc[j]:
                        Vmax=Vc[j]

                    Vmin=Va[j]
                    if Vmin>=Vb[j]:
                        Vmin=Vb[j]
                    if Vmin>=Vc[j]:
                        Vmin=Vc[j]

                    if result_desp == []:
                        V_padrao = Vmax
                        
                    if result_desp != [] and aux_rtp_ee!=1:
                        V_padrao = result_desp[0][1]
                    if result_desp != [] and aux_rtp_ee==1:
                        V_padrao = 115
                    #if len(result) >1:
                       # wwjk=0
                       # while wwjk<=(len(result)-1):
                       # if result[wwjk][3] is not None:
                            #RTC = result[wwjk][3]
                       # wwjk=wwjk+1

                    
                    if (Vmax > 0 and Vmin>0):
                        if ((1 -Vmin/Vmax) >= queda_tensao or (1 -Vmin/V_padrao)>= queda_tensao or (1 -Vmax/V_padrao)>= queda_tensao) and (Vmax > 0 and Vmin>0):
                            

                            if cont_V==0:
                                inicio_test = data_leitura[j]
                            cont_V =cont_V+1
                            media_Va.append(Va[j])
                            media_Vb.append(Vb[j])
                            media_Vc.append(Vc[j])

                            if j+1==len(Va)and cont_V >= tempo_teste_zerado_V_desp*12:
                                data_inic_alerta_desp_Va.append(inicio_test)
                               
                        else:
                            if cont_V >= tempo_teste_zerado_V_desp*12:
                                data_inic_alerta_desp_Va.append(inicio_test)
                            cont_V = 0
                            media_Va=[]
                            media_Vb=[]
                            media_Vc=[]

                            

                           
                        if Vmax > 0 and Vmin>0:
                            if cont_V >= tempo_teste_zerado_V_desp*12:
                                if cont_V > tempo_teste_zerado_V_desp*12 and data_alerta_desp_Va !=[]:
                                        del alerta_desp_Va[len(alerta_desp_Va) -1]
                                        del data_alerta_desp_Va[len(data_alerta_desp_Va) -1]
                                        del media_Va_tot[len(media_Va_tot) -1]
                                        del media_Vb_tot[len(media_Vb_tot) -1]
                                        del media_Vc_tot[len(media_Vc_tot) -1]
                                alerta_desp_Va.append("TENSÕES DESPROPORCIONAIS/ABAIXO DO MÍNIMO")
                                data_alerta_desp_Va.append(data_leitura[j])
                                cont_V2aaa = cont_V2aaa+1
                                test_passou = 1
                                media_Va_tot.append(sum(media_Va)/(len(media_Va)))
                                media_Vb_tot.append(sum(media_Vb)/(len(media_Vb)))
                                media_Vc_tot.append(sum(media_Vc)/(len(media_Vc)))

                    else:
                        if cont_V >= tempo_teste_zerado_V_desp*12:
                            data_inic_alerta_desp_Va.append(inicio_test)
                        cont_V = 0
                    j=j+1


                if test_passou !=0:
                    DATA_FIM_MEMO_V_DESP_TOT.append(data_leitura[j-1])
                
                if alerta_desp_Va!=[]:
                    alerta_desp_V.append(alerta_desp_Va)
                    data_alerta_desp_V.append(data_alerta_desp_Va)

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_desp_Va):
                    date2=datetime.datetime.strptime(data_alerta_desp_Va[j], '%Y-%m-%d %H:%M:%S')
                    date1=datetime.datetime.strptime(data_inic_alerta_desp_Va[j], '%Y-%m-%d %H:%M:%S')
                    cont_max.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    j=j+1
                
                if cont_max!=[]:
                    cont_max_desp_V_tot.append(cont_max)


                test_max_tam=len(media_Va_tot)
                if test_max_tam<len(media_Vb_tot):
                    test_max_tam=len(media_Vb_tot)
                if test_max_tam<len(media_Vc_tot):
                    test_max_tam=len(media_Vc_tot)
                j=0
                while len(media_Va_tot)<test_max_tam:
                    media_Va_tot.append([])
                while len(media_Vb_tot)<test_max_tam:
                    media_Vb_tot.append([])
                while len(media_Vc_tot)<test_max_tam:
                    media_Vc_tot.append([])


                
                if media_Va_tot != [] or media_Vb_tot != [] or media_Vc_tot != []:
        
                    media_Va_tot_tot.append(media_Va_tot)
                    media_Vb_tot_tot.append(media_Vb_tot)
                    media_Vc_tot_tot.append(media_Vc_tot)
                
                if data_inic_alerta_desp_Va != []:
                    data_inic_alerta_desp_V.append(data_inic_alerta_desp_Va)
                    
                if test_passou !=0:
                    ARQ_V_DESP_TOT.append(i)
                    MED_V_DESP_TOT.append(medidor_mm[ii])
                    DATA_FIM_MEMO_V_DESP_TOT.append(data_leitura[j])
            


###################################################################################################################
###################################################################################################################
###################################################################################################################
#CONVERTER VARIAVEIS V EM I
        

                    
        const_mult=0
        if (arquivo[2315:2321] == "363738" or arquivo[2315:2321] == "202122" or arquivo[2315:2321] == "171819"):
            if int(arquivo[266:272]) !=0:
                const_mult=int(arquivo[260:266])/(int(arquivo[266:272]))
        if const_mult == 0.0005 and (arquivo[2315:2321] == "363738" or arquivo[2315:2321] == "202122" or arquivo[2315:2321] == "171819"):
        #if arquivo[2315:2321] == "171819":
            
            medidor_Iabc.append(medidor_mm)
            #const_mult=int(arquivo[260:266])/(int(arquivo[266:272]))
            #if const_mult ==0.0125:
                #const_mult =0.0005
            


 #ALERTA GRANDEZAS NEGATIVAS         
########################################################################################################################################
##########################################################################################################################################

            Ia = []
            Ib = []
            Ic = []

            j=0
            indice=0
            while j<len(arquivo):
                increm=4
                inicio=j+12
                fim=j+12+increm
                ind=j+1
               
                if arquivo[j:j+4].find("CONT") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                    #arquivo[inicio:inicio+1] != '\n':
                    #arquivo[ind:ind+4].find("CONT") < 0:
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                if arquivo[j:j+4].find("SALV") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                              
                j=j+1


            if Ia != [] and Ib != [] and Ic != []:

                data_leitura=[]
                hora_leitura = []
                date1 = str(primeiro_intervalo_demanda.date())
                date2 = str(ultimo_intervalo_demanda.date())

                hora1 = str(primeiro_intervalo_demanda.time())
                hora2 = str(ultimo_intervalo_demanda.time())
                data_corr_II_comp.append(date2)
                medidor_corr_II_comp.append(medidor_mm[ii])
                
                while (date1<date2) or (hora1 <= hora2):
                    data_leitura.append(str(primeiro_intervalo_demanda))
                    delta = timedelta(minutes=5)
                    primeiro_intervalo_demanda = primeiro_intervalo_demanda + delta

                    date1 = str(primeiro_intervalo_demanda.date())
                    hora1 = str(primeiro_intervalo_demanda.time())
                    
                
                j=0
                indice=0
                cont_IIa=0
                cont_IIb=0
                cont_IIc=0
                cont_I = 0
                test_I = 0
                cont_I2a = 0
                cont_I2b = 0
                cont_I2c = 0
                cont_I2aaa = 0
                alerta_Ib = []
                alerta_Ia = []
                alerta_desp_Ia = []
                alerta_Ic = []
                data_alerta_desp_Ia = []
                data_alerta_Ia = []
                data_alerta_Ib= []
                data_alerta_Ic= []
                cont_antigo=0
                cont_atual=0
                cont_max=[]
                cont_antigo_a=1
                cont_atual_a=0
                cont_antigo_b=1
                cont_atual_b=0
                cont_antigo_c=1
                cont_atual_c=0
                fim_semana = 0
                cont_max_a=[]
                cont_max_b=[]
                cont_max_c=[]
                #digitar valor em horas ####################
                #tempo_teste_zerado_I = 1/12
                data_inic_alerta_Ia=[]
                data_inic_alerta_Ib=[]
                data_inic_alerta_Ic=[]
                data_fim_alerta_Ia=[]
                data_fim_alerta_Ib=[]
                data_fim_alerta_Ic=[]
                inicio_test_a=[]
                inicio_test_b=[]
                inicio_test_c=[]
                test_passou =0
                kwk=1
                aux_data_a=[]
                aux_data_b=[]
                aux_data_c=[]
                while j<len(Ia):
                    

                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    if fim_semana<=6:
                        if Ia[j] >=2048:
                            if cont_IIa==0:
                                inicio_test_a = data_leitura[j]
                            cont_IIa =cont_IIa+1
                            if j+1==len(Ia) and cont_IIa >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("LIGAÇÃO TC INVERTIDA")
                        else:
                            if cont_IIa >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("LIGAÇÃO TC INVERTIDA")
                            cont_IIa = 0
                            aux_data_a=[]
                    
                        if cont_IIa >= tempo_teste_zerado_I*12:
                            if cont_IIa > tempo_teste_zerado_I*12 and data_alerta_Ia !=[]:
                                del data_alerta_Ia[len(data_alerta_Ia) -1]
                            data_alerta_Ia.append(data_leitura[j])
                            cont_I2a = cont_I2a+1
                            test_passou=1
                            aux_data_a=inicio_test_a
                    else:
                        if cont_IIa >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ia.append(inicio_test_a)
                            data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                            alerta_Ia.append("LIGAÇÃO TC INVERTIDA")
                        cont_IIa = 0
                        aux_data_a=[]
                    



                        
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    if fim_semana<=6:
                        if Ib[j] >=2048:
                            if cont_IIb==0:
                                inicio_test_b = data_leitura[j]
                            cont_IIb =cont_IIb+1

                            if j+1==len(Ia) and cont_IIb >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("LIGAÇÃO TC INVERTIDA")
                        else:
                            if cont_IIb >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("LIGAÇÃO TC INVERTIDA")
                            cont_IIb = 0
                            aux_data_b=[]
                    
                        if cont_IIb >= tempo_teste_zerado_I*12:
                            if cont_IIb > tempo_teste_zerado_I*12 and data_alerta_Ib !=[]:
                                del data_alerta_Ib[len(data_alerta_Ib) -1]
                            data_alerta_Ib.append(data_leitura[j])
                            cont_I2b = cont_I2b+1
                            test_passou=1
                            aux_data_b=inicio_test_b
                    else:
                        if cont_IIb >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ib.append(inicio_test_b)
                            data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                            alerta_Ib.append("LIGAÇÃO TC INVERTIDA")
                        cont_IIb = 0
                        aux_data_b=[]



                        
                        
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    if fim_semana<=6:
                        if Ic[j] >=2048:
                            if cont_IIc==0:
                                inicio_test_c = data_leitura[j]
                            cont_IIc =cont_IIc+1
    ##                        print(cont_IIc)
    ##                        print(data_leitura[j])
    ##                        print(data_inic_alerta_Ic)
    ##                        print(data_alerta_Ic)
    ##                        print(cont_antigo_c)
    ##                        print(cont_max_c)
    ##                        quest = sys.stdin.readline()
                            if j+1==len(Ia) and cont_IIc >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("LIGAÇÃO TC INVERTIDA")
                        else:
                            if cont_IIc >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("LIGAÇÃO TC INVERTIDA")
                            cont_IIc = 0
                            aux_data_c=[]
                    
                        if cont_IIc >= tempo_teste_zerado_I*12:
                            if cont_IIc > tempo_teste_zerado_I*12 and data_alerta_Ic !=[]:
                                del data_alerta_Ic[len(data_alerta_Ic) -1]
                            data_alerta_Ic.append(data_leitura[j])
                            cont_I2c = cont_I2c+1
                            test_passou=1
                            aux_data_c=inicio_test_c
                            
                    else:
                        if cont_IIc >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ic.append(inicio_test_c)
                            data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                            alerta_Ic.append("LIGAÇÃO TC INVERTIDA")
                        cont_IIc = 0
                        aux_data_c=[]


                    date=[]
                    date_a=[]
                    date_b=[]
                    date_c=[]
                    test_max_tam=data_inic_alerta_Ia
                    test_max_tam_fim=data_fim_alerta_Ia
                    if data_inic_alerta_Ib!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ib) and data_inic_alerta_Ib[len(data_inic_alerta_Ib)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ib
                            test_max_tam_fim=data_fim_alerta_Ib
                    if data_inic_alerta_Ic!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ic) and data_inic_alerta_Ic[len(data_inic_alerta_Ic)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ic
                            test_max_tam_fim=data_fim_alerta_Ic
                    if test_max_tam!=[]:
                        date_fim = datetime.datetime.strptime(test_max_tam_fim[len(test_max_tam_fim)-1], '%Y-%m-%d %H:%M:%S')
                        date=datetime.datetime.strptime(test_max_tam[len(test_max_tam)-1], '%Y-%m-%d %H:%M:%S')

                    if aux_data_a!=[]:
                        date_a=datetime.datetime.strptime(aux_data_a, '%Y-%m-%d %H:%M:%S')
                   
                    if aux_data_b!=[]:
                        date_b=datetime.datetime.strptime(aux_data_b, '%Y-%m-%d %H:%M:%S')
                    
                    if aux_data_c!=[]:
                        date_c=datetime.datetime.strptime(aux_data_c, '%Y-%m-%d %H:%M:%S')


    ##                #str(date_a.date())=='2014-11-13'
    ##                if  date_a!= []:      
    ##                    if i == '03100&ob.omf' and date!=[] and len(data_inic_alerta_Ib)>=2:
    ##                                print(data_inic_alerta_Ia)
    ##                                print(data_inic_alerta_Ib)
    ##                                print(data_inic_alerta_Ic)
    ##                                print(date.date())
    ##                                print(date_a)
    ##                                quest = sys.stdin.readline()
                    
                    if date_a!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ia[len(data_alerta_Ia)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ia)<len(test_max_tam):             
                            if date.date()<date_a.date() or j+1==len(Ia) or (date.date()>date_a.date() and len(data_inic_alerta_Ia)>0 and (date_interm).date()!=date_fim.date()):

                                alerta_Ia.append("LIGAÇÃO TC INVERTIDA")
                                data_fim_alerta_Ia.append([])
                                data_inic_alerta_Ia.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ia)<len(test_max_tam):
                            alerta_Ia.append("LIGAÇÃO TC INVERTIDA")
                            data_fim_alerta_Ia.append([])
                            data_inic_alerta_Ia.append([])
                            
                    if date_b!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ib[len(data_alerta_Ib)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ib)<len(test_max_tam):                        
                            if date.date()<date_b.date() or j+1==len(Ia) or (date.date()>date_b.date() and len(data_inic_alerta_Ib)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ib.append("LIGAÇÃO TC INVERTIDA")
                                data_fim_alerta_Ib.append([])
                                data_inic_alerta_Ib.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ib)<len(test_max_tam):
                            alerta_Ib.append("LIGAÇÃO TC INVERTIDA")
                            data_fim_alerta_Ib.append([])
                            data_inic_alerta_Ib.append([])
                            
                    if date_c!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ic[len(data_alerta_Ic)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ic)<len(test_max_tam):                    
                            if date.date()<date_c.date() or j+1==len(Ia) or (date.date()>date_c.date() and len(data_inic_alerta_Ic)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ic.append("LIGAÇÃO TC INVERTIDA")
                                data_fim_alerta_Ic.append([])
                                data_inic_alerta_Ic.append([])
                            else:
                                break
                            
                    else:
                        while len(data_inic_alerta_Ic)<len(test_max_tam):
                            alerta_Ic.append("LIGAÇÃO TC INVERTIDA")
                            data_fim_alerta_Ic.append([])
                            data_inic_alerta_Ic.append([])  
                        
                    j=j+1


                if test_passou !=0:
                    DATA_FIM_MEMO_I_Neg_TOT.append(data_leitura[j-1])
                
                if alerta_Ia!=[] or alerta_Ib!=[] or alerta_Ic!=[]:
                    alerta_Ia_Neg_tot.append(alerta_Ia)
                    data_alerta_Ia_Neg_tot.append(data_fim_alerta_Ia)
               
                    alerta_Ib_Neg_tot.append(alerta_Ib)
                    data_alerta_Ib_Neg_tot.append(data_fim_alerta_Ib)
                
                    alerta_Ic_Neg_Neg_tot.append(alerta_Ic)
                    data_alerta_Ic_Neg_tot.append(data_fim_alerta_Ic)


                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ia):
                    if data_fim_alerta_Ia[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_a.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_a.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ib):
                    if data_fim_alerta_Ib[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_b.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_b.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ic):
                    if data_fim_alerta_Ic[j] != []:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_c.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_c.append(0)
                    j=j+1



                if cont_max_a!=[] or cont_max_b!=[] or cont_max_c!=[]:
                    cont_max_Ia_Neg_tot.append(cont_max_a)
                
                    cont_max_Ib_Neg_tot.append(cont_max_b)
                
                    cont_max_Ic_Neg_tot.append(cont_max_c)


                if data_inic_alerta_Ia !=[] or data_inic_alerta_Ib!=[] or data_inic_alerta_Ic!=[]:
                    data_inic_alerta_Ia_Neg_tot.append(data_inic_alerta_Ia)
                
                    data_inic_alerta_Ib_Neg_tot.append(data_inic_alerta_Ib)
                
                    data_inic_alerta_Ic_Neg_tot.append(data_inic_alerta_Ic)


                if test_passou !=0:
                    ARQ_I_ZERO_Neg_TOT.append(i)
                    MED_I_ZERO_Neg_TOT.append(medidor_mm[ii])
                    




 #ALERTA SATURAÇÃO DOS TC'S      
########################################################################################################################################
#############################################################################################################
            Ia = []
            Ib = []
            Ic = []

            j=0
            indice=0
            while j<len(arquivo):
                increm=4
                inicio=j+12
                fim=j+12+increm
                ind=j+1
               
                if arquivo[j:j+4].find("CONT") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                if arquivo[j:j+4].find("SALV") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                              
                j=j+1


            if Ia != [] and Ib != [] and Ic != []:
            
                j=0
                indice=0
                cont_IIa=0
                cont_IIb=0
                cont_IIc=0
                cont_I = 0
                test_I = 0
                cont_I2a = 0
                cont_I2b = 0
                cont_I2c = 0
                cont_I2aaa = 0
                alerta_Ib = []
                alerta_Ia = []
                alerta_desp_Ia = []
                alerta_Ic = []
                data_alerta_desp_Ia = []
                data_alerta_Ia = []
                data_alerta_Ib= []
                data_alerta_Ic= []
                cont_antigo=0
                cont_atual=0
                cont_max=[]
                cont_antigo_a=1
                cont_atual_a=0
                cont_antigo_b=1
                cont_atual_b=0
                cont_antigo_c=1
                cont_atual_c=0
                fim_semana = 0
                cont_max_a=[]
                cont_max_b=[]
                cont_max_c=[]
                #digitar valor em horas ####################
                #tempo_teste_saturado_I = 4
                data_inic_alerta_Ia=[]
                data_inic_alerta_Ib=[]
                data_inic_alerta_Ic=[]
                data_fim_alerta_Ia=[]
                data_fim_alerta_Ib=[]
                data_fim_alerta_Ic=[]
                inicio_test_a=[]
                inicio_test_b=[]
                inicio_test_c=[]
                test_passou =0
                kwk=1
                aux_data_a=[]
                aux_data_b=[]
                aux_data_c=[]

                media_IIIaa=[]
                media_IIIab=[]
                media_IIIac=[]
                media_IIIaa_tot= []
                media_IIIab_tot= []
                media_IIIac_tot= []

                media_IIIba=[]
                media_IIIbb=[]
                media_IIIbc=[]
                media_IIIba_tot= []
                media_IIIbb_tot= []
                media_IIIbc_tot= []

                media_IIIca=[]
                media_IIIcb=[]
                media_IIIcc=[]
                media_IIIca_tot= []
                media_IIIcb_tot= []
                media_IIIcc_tot= []

                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""select T.UC_RTC , T.RTC FROM RTC_TABLE T,  rel_equip_uc@ri_carga TA
    WHERE T.UC_RTC = TA.cod_un_cons_reu
        and (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND TA.num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora

                if result == []:
                        RTC = 1
                else:
                        RTC = result[0][1]

                
                while j<len(Ia):
                    

                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if fim_semana<=6:
                        if Ia[j] >6 and RTC != 1:
                            if cont_IIa==0:
                                inicio_test_a = data_leitura[j]
                            cont_IIa =cont_IIa+1
                            media_IIIaa.append(Ia[j])
                            media_IIIab.append(Ib[j])
                            media_IIIac.append(Ic[j])
                            if j+1==len(Ia) and cont_IIa >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("TC SATURADO")
                        else:
                            if cont_IIa >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("TC SATURADO")
                            cont_IIa = 0
                            aux_data_a=[]
                            media_IIIaa=[]
                            media_IIIab=[]
                            media_IIIac=[]
                    
                        if cont_IIa >= tempo_teste_saturado_I*12:
                            if cont_IIa > tempo_teste_saturado_I*12 and data_alerta_Ia !=[]:
                                del data_alerta_Ia[len(data_alerta_Ia) -1]
                                del media_IIIaa_tot[len(media_IIIaa_tot) -1]
                                del media_IIIab_tot[len(media_IIIab_tot) -1]
                                del media_IIIac_tot[len(media_IIIac_tot) -1]
                            data_alerta_Ia.append(data_leitura[j])
                            cont_I2a = cont_I2a+1
                            test_passou=1
                            aux_data_a=inicio_test_a
                            media_IIIaa_tot.append(sum(media_IIIaa)/(len(media_IIIaa)))
                            media_IIIab_tot.append(sum(media_IIIab)/(len(media_IIIab)))
                            media_IIIac_tot.append(sum(media_IIIac)/(len(media_IIIac)))
                            #print(media_IIIaa_tot)
                            #quest = sys.stdin.readline()
                    else:
                        if cont_IIa >= tempo_teste_saturado_I*12:
                            data_inic_alerta_Ia.append(inicio_test_a)
                            data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                            alerta_Ia.append("TC SATURADO")
                        cont_IIa = 0
                        aux_data_a=[]
                        media_IIIaa=[]
                        media_IIIab=[]
                        media_IIIac=[]
                    



                        
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if fim_semana<=6:
                        if Ib[j] >6 and RTC != 1 :
                            if cont_IIb==0:
                                inicio_test_b = data_leitura[j]
                            cont_IIb =cont_IIb+1
                            media_IIIba.append(Ia[j])
                            media_IIIbb.append(Ib[j])
                            media_IIIbc.append(Ic[j])

                            if j+1==len(Ia) and cont_IIb >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("TC SATURADO")
                        else:
                            if cont_IIb >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("TC SATURADO")
                            cont_IIb = 0
                            aux_data_b=[]
                            media_IIIba=[]
                            media_IIIbb=[]
                            media_IIIbc=[]
                    
                        if cont_IIb >= tempo_teste_saturado_I*12:
                            if cont_IIb > tempo_teste_saturado_I*12 and data_alerta_Ib !=[]:
                                del data_alerta_Ib[len(data_alerta_Ib) -1]
                                del media_IIIba_tot[len(media_IIIba_tot) -1]
                                del media_IIIbb_tot[len(media_IIIbb_tot) -1]
                                del media_IIIbc_tot[len(media_IIIbc_tot) -1]
                            data_alerta_Ib.append(data_leitura[j])
                            cont_I2b = cont_I2b+1
                            test_passou=1
                            aux_data_b=inicio_test_b
                            media_IIIba_tot.append(sum(media_IIIba)/(len(media_IIIba)))
                            media_IIIbb_tot.append(sum(media_IIIbb)/(len(media_IIIbb)))
                            media_IIIbc_tot.append(sum(media_IIIbc)/(len(media_IIIbc)))
                    else:
                        if cont_IIb >= tempo_teste_saturado_I*12:
                            data_inic_alerta_Ib.append(inicio_test_b)
                            data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                            alerta_Ib.append("TC SATURADO")
                        cont_IIb = 0
                        aux_data_b=[]
                        media_IIIba=[]
                        media_IIIbb=[]
                        media_IIIbc=[]



                        
                        
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if fim_semana<=6:
                        if Ic[j] >6 and RTC !=1 :
                            if cont_IIc==0:
                                inicio_test_c = data_leitura[j]
                            cont_IIc =cont_IIc+1
                            media_IIIca.append(Ia[j])
                            media_IIIcb.append(Ib[j])
                            media_IIIcc.append(Ic[j])
    ##                        print(cont_IIc)
    ##                        print(data_leitura[j])
    ##                        print(data_inic_alerta_Ic)
    ##                        print(data_alerta_Ic)
    ##                        print(cont_antigo_c)
    ##                        print(cont_max_c)
    ##                        quest = sys.stdin.readline()
                            if j+1==len(Ia) and cont_IIc >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("TC SATURADO")
                        else:
                            if cont_IIc >= tempo_teste_saturado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("TC SATURADO")
                            cont_IIc = 0
                            aux_data_c=[]
                            media_IIIca=[]
                            media_IIIcb=[]
                            media_IIIcc=[]
                    
                        if cont_IIc >= tempo_teste_saturado_I*12:
                            if cont_IIc > tempo_teste_saturado_I*12 and data_alerta_Ic !=[]:
                                del data_alerta_Ic[len(data_alerta_Ic) -1]
                                del media_IIIca_tot[len(media_IIIca_tot) -1]
                                del media_IIIcb_tot[len(media_IIIcb_tot) -1]
                                del media_IIIcc_tot[len(media_IIIcc_tot) -1]
                            data_alerta_Ic.append(data_leitura[j])
                            cont_I2c = cont_I2c+1
                            test_passou=1
                            aux_data_c=inicio_test_c
                            media_IIIca_tot.append(sum(media_IIIca)/(len(media_IIIca)))
                            media_IIIcb_tot.append(sum(media_IIIcb)/(len(media_IIIcb)))
                            media_IIIcc_tot.append(sum(media_IIIcc)/(len(media_IIIcc)))
                            
                    else:
                        if cont_IIc >= tempo_teste_saturado_I*12:
                            data_inic_alerta_Ic.append(inicio_test_c)
                            data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                            alerta_Ic.append("TC SATURADO")
                        cont_IIc = 0
                        aux_data_c=[]
                        media_IIIca=[]
                        media_IIIcb=[]
                        media_IIIcc=[]


                    date=[]
                    date_a=[]
                    date_b=[]
                    date_c=[]
                    test_max_tam=data_inic_alerta_Ia
                    test_max_tam_fim=data_fim_alerta_Ia
                    if data_inic_alerta_Ib!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ib) and data_inic_alerta_Ib[len(data_inic_alerta_Ib)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ib
                            test_max_tam_fim=data_fim_alerta_Ib
                    if data_inic_alerta_Ic!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ic) and data_inic_alerta_Ic[len(data_inic_alerta_Ic)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ic
                            test_max_tam_fim=data_fim_alerta_Ic
                    if test_max_tam!=[]:
                        date_fim = datetime.datetime.strptime(test_max_tam_fim[len(test_max_tam_fim)-1], '%Y-%m-%d %H:%M:%S')
                        date=datetime.datetime.strptime(test_max_tam[len(test_max_tam)-1], '%Y-%m-%d %H:%M:%S')

                    if aux_data_a!=[]:
                        date_a=datetime.datetime.strptime(aux_data_a, '%Y-%m-%d %H:%M:%S')
                   
                    if aux_data_b!=[]:
                        date_b=datetime.datetime.strptime(aux_data_b, '%Y-%m-%d %H:%M:%S')
                    
                    if aux_data_c!=[]:
                        date_c=datetime.datetime.strptime(aux_data_c, '%Y-%m-%d %H:%M:%S')


    ##                #str(date_a.date())=='2014-11-13'
    ##                if  date_a!= []:      
    ##                    if i == '03100&ob.omf' and date!=[] and len(data_inic_alerta_Ib)>=2:
    ##                                print(data_inic_alerta_Ia)
    ##                                print(data_inic_alerta_Ib)
    ##                                print(data_inic_alerta_Ic)
    ##                                print(date.date())
    ##                                print(date_a)
    ##                                quest = sys.stdin.readline()
                    
                    if date_a!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ia[len(data_alerta_Ia)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ia)<len(test_max_tam):             
                            if date.date()<date_a.date() or j+1==len(Ia) or (date.date()>date_a.date() and len(data_inic_alerta_Ia)>0 and (date_interm).date()!=date_fim.date()):

                                alerta_Ia.append("TC SATURADO")
                                data_fim_alerta_Ia.append([])
                                data_inic_alerta_Ia.append([])
                                media_IIIaa_tot.append([])
                                media_IIIab_tot.append([])
                                media_IIIac_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ia)<len(test_max_tam):
                            alerta_Ia.append("TC SATURADO")
                            data_fim_alerta_Ia.append([])
                            data_inic_alerta_Ia.append([])
                            media_IIIaa_tot.append([])
                            media_IIIab_tot.append([])
                            media_IIIac_tot.append([])
                            
                    if date_b!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ib[len(data_alerta_Ib)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ib)<len(test_max_tam):                        
                            if date.date()<date_b.date() or j+1==len(Ia) or (date.date()>date_b.date() and len(data_inic_alerta_Ib)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ib.append("TC SATURADO")
                                data_fim_alerta_Ib.append([])
                                data_inic_alerta_Ib.append([])
                                media_IIIba_tot.append([])
                                media_IIIbb_tot.append([])
                                media_IIIbc_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ib)<len(test_max_tam):
                            alerta_Ib.append("TC SATURADO")
                            data_fim_alerta_Ib.append([])
                            data_inic_alerta_Ib.append([])
                            media_IIIba_tot.append([])
                            media_IIIbb_tot.append([])
                            media_IIIbc_tot.append([])
                            
                    if date_c!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ic[len(data_alerta_Ic)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ic)<len(test_max_tam):                    
                            if date.date()<date_c.date() or j+1==len(Ia) or (date.date()>date_c.date() and len(data_inic_alerta_Ic)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ic.append("TC SATURADO")
                                data_fim_alerta_Ic.append([])
                                data_inic_alerta_Ic.append([])
                                media_IIIca_tot.append([])
                                media_IIIcb_tot.append([])
                                media_IIIcc_tot.append([])
                            else:
                                break
                            
                    else:
                        while len(data_inic_alerta_Ic)<len(test_max_tam):
                            alerta_Ic.append("TC SATURADO")
                            data_fim_alerta_Ic.append([])
                            data_inic_alerta_Ic.append([])  
                            media_IIIca_tot.append([])
                            media_IIIcb_tot.append([])
                            media_IIIcc_tot.append([])
                    j=j+1


                if test_passou !=0:
                    DATA_FIM_MEMO_I_sat_TOT.append(data_leitura[j-1])
                
                
                if alerta_Ia!=[] or alerta_Ib!=[] or alerta_Ic!=[]:
                    alerta_Ia_sat_tot.append(alerta_Ia)
                    data_alerta_Ia_sat_tot.append(data_fim_alerta_Ia)
               
                    alerta_Ib_sat_tot.append(alerta_Ib)
                    data_alerta_Ib_sat_tot.append(data_fim_alerta_Ib)
                
                    alerta_Ic_sat_tot.append(alerta_Ic)
                    data_alerta_Ic_sat_tot.append(data_fim_alerta_Ic)


                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ia):
                    if data_inic_alerta_Ia[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_a.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_a.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ib):
                    if data_inic_alerta_Ib[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_b.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_b.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ic):
                    if data_inic_alerta_Ic[j] != []:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_c.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_c.append(0)
                    j=j+1



                if cont_max_a!=[] or cont_max_b!=[] or cont_max_c!=[]:
                    cont_max_Ia_sat_tot.append(cont_max_a)
                
                    cont_max_Ib_sat_tot.append(cont_max_b)
                
                    cont_max_Ic_sat_tot.append(cont_max_c)


                
                if media_IIIaa_tot != [] or media_IIIab_tot != [] or media_IIIac_tot != []:
        
                    media_IIIMMaa_tot_sat_tot.append(media_IIIaa_tot)
                    media_IIIMMab_tot_sat_tot.append(media_IIIab_tot)
                    media_IIIMMac_tot_sat_tot.append(media_IIIac_tot)

                if media_IIIba_tot != [] or media_IIIbb_tot != [] or media_IIIbc_tot != []:
        
                    media_IIIMMba_tot_sat_tot.append(media_IIIba_tot)
                    media_IIIMMbb_tot_sat_tot.append(media_IIIbb_tot)
                    media_IIIMMbc_tot_sat_tot.append(media_IIIbc_tot)

                if media_IIIca_tot != [] or media_IIIcb_tot != [] or media_IIIcc_tot != []:
        
                    media_IIIMMca_tot_sat_tot.append(media_IIIca_tot)
                    media_IIIMMcb_tot_sat_tot.append(media_IIIcb_tot)
                    media_IIIMMcc_tot_sat_tot.append(media_IIIcc_tot)



                if data_inic_alerta_Ia !=[] or data_inic_alerta_Ib!=[] or data_inic_alerta_Ic!=[]:
                    data_inic_alerta_Ia_sat_tot.append(data_inic_alerta_Ia)
                
                    data_inic_alerta_Ib_sat_tot.append(data_inic_alerta_Ib)
                
                    data_inic_alerta_Ic_sat_tot.append(data_inic_alerta_Ic)


                if test_passou !=0:
                    ARQ_I_ZERO_sat_TOT.append(i)
                    MED_I_ZERO_sat_TOT.append(medidor_mm[ii])
                    
########################################################################################################################################
##########################################################################################################################################




            
            Ia = []
            Ib = []
            Ic = []

            j=0
            indice=0
            while j<len(arquivo):
                increm=4
                inicio=j+12
                fim=j+12+increm
                ind=j+1
               
                if arquivo[j:j+4].find("CONT") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                if arquivo[j:j+4].find("SALV") >= 0:
                    while arquivo[inicio:inicio+1] != '\n':
                        if arquivo[inicio:fim] == "    ":
                            break
                        else:
                            Ia.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ib.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            Ic.append(12*const_mult*int(arquivo[inicio:fim]))
                            inicio=fim
                            fim=fim+increm
                            ind=ind+1
                              
                j=j+1


            if Ia != [] and Ib != [] and Ic != []:
            
                j=0
                indice=0
                cont_IIa=0
                cont_IIb=0
                cont_IIc=0
                cont_I = 0
                test_I = 0
                cont_I2a = 0
                cont_I2b = 0
                cont_I2c = 0
                cont_I2aaa = 0
                alerta_Ib = []
                alerta_Ia = []
                alerta_desp_Ia = []
                alerta_Ic = []
                data_alerta_desp_Ia = []
                data_alerta_Ia = []
                data_alerta_Ib= []
                data_alerta_Ic= []
                cont_antigo=0
                cont_atual=0
                cont_max=[]
                cont_antigo_a=1
                cont_atual_a=0
                cont_antigo_b=1
                cont_atual_b=0
                cont_antigo_c=1
                cont_atual_c=0
                fim_semana = 0
                cont_max_a=[]
                cont_max_b=[]
                cont_max_c=[]
                #digitar valor em horas ####################
                #tempo_teste_zerado_I = 4
                data_inic_alerta_Ia=[]
                data_inic_alerta_Ib=[]
                data_inic_alerta_Ic=[]
                data_fim_alerta_Ia=[]
                data_fim_alerta_Ib=[]
                data_fim_alerta_Ic=[]
                inicio_test_a=[]
                inicio_test_b=[]
                inicio_test_c=[]
                test_passou =0
                kwk=1
                aux_data_a=[]
                aux_data_b=[]
                aux_data_c=[]

                media_IIIaa=[]
                media_IIIab=[]
                media_IIIac=[]
                media_IIIaa_tot= []
                media_IIIab_tot= []
                media_IIIac_tot= []

                media_IIIba=[]
                media_IIIbb=[]
                media_IIIbc=[]
                media_IIIba_tot= []
                media_IIIbb_tot= []
                media_IIIbc_tot= []

                media_IIIca=[]
                media_IIIcb=[]
                media_IIIcc=[]
                media_IIIca_tot= []
                media_IIIcb_tot= []
                media_IIIcc_tot= []

                #HORA DE INICIO DA ANALISE
                #hora_corrente_inicio = '08:00:00'
                #HORA DE FIM DA ANALISE
                #hora_corrente_fim = '22:00:00'
                result_2elem = []

                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""select T.UC_RTC , T.RTC FROM RTC_TABLE T,  rel_equip_uc@ri_carga TA
    WHERE T.UC_RTC = TA.cod_un_cons_reu
    and (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND TA.num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora

                if result == []:
                        RTC = 1
                else:
                        RTC = result[0][1]
                        

                result_2elem = []
                if result != []:
                    cursor.execute("""SELECT COD_UN_CONS_REU, COD_TIPO_EQIP_REU,  COUNT (COD_TIPO_EQIP_REU) contador 
FROM REL_EQUIP_UC@ri_carga
WHERE COD_UN_CONS_REU  = %s
and COD_TIPO_EQIP_REU = 'TC' 
AND DTA_RETI_REU IS NULL
group by COD_UN_CONS_REU, COD_TIPO_EQIP_REU
HAVING (Count(COD_TIPO_EQIP_REU) = 2)""" %result[0][0])
                    result_2elem = cursor.fetchall()  # busca o resultado da consulta

                min_I_zerada = 7
                if RTC == 1:
                    min_I_zerada = 1
                while j<len(Ia):
                    
                    #print(str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S')))
                    #print(Ia[j])
                    #print(RTC)
                    #print(min_I_zerada)
                    #quest = sys.stdin.readline()
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if (Ia[j] == 0 and cont_IIa >= tempo_teste_zerado_I*12) or (fim_semana<=4 and (date_desp>=hora_corrente_inicio and date_desp<=hora_corrente_fim)):
                        #print('kkkkkkkk')
                        if Ia[j] == 0 and ((Ib[j]*RTC==0 and Ic[j]*RTC==0) or (Ib[j]*RTC==0 and Ic[j]*RTC>=min_I_zerada) or (Ic[j]*RTC==0 and Ib[j]*RTC>=min_I_zerada) or (Ic[j]*RTC>=min_I_zerada and Ib[j]*RTC>=min_I_zerada)) :
                            #print('aaaaaaaaaaaaaa')
                            if cont_IIa==0:
                                inicio_test_a = data_leitura[j]
                            cont_IIa =cont_IIa+1
                            media_IIIaa.append(Ia[j])
                            media_IIIab.append(Ib[j])
                            media_IIIac.append(Ic[j])
                            if j+1==len(Ia) and cont_IIa >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("CORRENTE ZERADA")
                        else:
                            if cont_IIa >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ia.append(inicio_test_a)
                                data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                                alerta_Ia.append("CORRENTE ZERADA")
                            cont_IIa = 0
                            aux_data_a=[]
                            media_IIIaa=[]
                            media_IIIab=[]
                            media_IIIac=[]
                    
                        if cont_IIa >= tempo_teste_zerado_I*12:
                            if cont_IIa > tempo_teste_zerado_I*12 and data_alerta_Ia !=[]:
                                del data_alerta_Ia[len(data_alerta_Ia) -1]
                                del media_IIIaa_tot[len(media_IIIaa_tot) -1]
                                del media_IIIab_tot[len(media_IIIab_tot) -1]
                                del media_IIIac_tot[len(media_IIIac_tot) -1]
                            data_alerta_Ia.append(data_leitura[j])
                            cont_I2a = cont_I2a+1
                            test_passou=1
                            aux_data_a=inicio_test_a
                            media_IIIaa_tot.append(sum(media_IIIaa)/(len(media_IIIaa)))
                            media_IIIab_tot.append(sum(media_IIIab)/(len(media_IIIab)))
                            media_IIIac_tot.append(sum(media_IIIac)/(len(media_IIIac)))
                            #print(media_IIIaa_tot)
                            #quest = sys.stdin.readline()
                    else:
                        if cont_IIa >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ia.append(inicio_test_a)
                            data_fim_alerta_Ia.append(data_alerta_Ia[len(data_alerta_Ia)-1])
                            alerta_Ia.append("CORRENTE ZERADA")
                        cont_IIa = 0
                        aux_data_a=[]
                        media_IIIaa=[]
                        media_IIIab=[]
                        media_IIIac=[]
                    


                    #print(fim_semana)
                    #print(data_leitura[j])
                    #print(result_2elem)
                    #print(Ib[j])
                    #print(cont_IIb)
                    #print(inicio_test_b)
                    #print(data_inic_alerta_Ib)
                    #print(data_fim_alerta_Ib)
                    #quest = sys.stdin.readline()
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if (Ib[j] == 0 and cont_IIb >= tempo_teste_zerado_I*12) or (fim_semana<=4 and (date_desp>=hora_corrente_inicio and date_desp<=hora_corrente_fim)):
                        if Ib[j] == 0  and result_2elem == [] and ((Ia[j]*RTC==0 and Ic[j]*RTC==0) or (Ia[j]*RTC==0 and Ic[j]*RTC>=min_I_zerada) or (Ic[j]*RTC==0 and Ia[j]*RTC>=min_I_zerada) or (Ic[j]*RTC>=min_I_zerada and Ia[j]*RTC>=min_I_zerada)) :
                            #print('kkkkkkkk')
                            #quest = sys.stdin.readline()
                            if cont_IIb==0:
                                inicio_test_b = data_leitura[j]
                            cont_IIb =cont_IIb+1
                            media_IIIba.append(Ia[j])
                            media_IIIbb.append(Ib[j])
                            media_IIIbc.append(Ic[j])

                            if j+1==len(Ia) and cont_IIb >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("CORRENTE ZERADA")
                        else:
                            if cont_IIb >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ib.append(inicio_test_b)
                                data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                                alerta_Ib.append("CORRENTE ZERADA")
                            cont_IIb = 0
                            aux_data_b=[]
                            media_IIIba=[]
                            media_IIIbb=[]
                            media_IIIbc=[]
                    
                        if cont_IIb >= tempo_teste_zerado_I*12:
                            if cont_IIb > tempo_teste_zerado_I*12 and data_alerta_Ib !=[]:
                                del data_alerta_Ib[len(data_alerta_Ib) -1]
                                del media_IIIba_tot[len(media_IIIba_tot) -1]
                                del media_IIIbb_tot[len(media_IIIbb_tot) -1]
                                del media_IIIbc_tot[len(media_IIIbc_tot) -1]
                            data_alerta_Ib.append(data_leitura[j])
                            cont_I2b = cont_I2b+1
                            test_passou=1
                            aux_data_b=inicio_test_b
                            media_IIIba_tot.append(sum(media_IIIba)/(len(media_IIIba)))
                            media_IIIbb_tot.append(sum(media_IIIbb)/(len(media_IIIbb)))
                            media_IIIbc_tot.append(sum(media_IIIbc)/(len(media_IIIbc)))
                    else:
                        if cont_IIb >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ib.append(inicio_test_b)
                            data_fim_alerta_Ib.append(data_alerta_Ib[len(data_alerta_Ib)-1])
                            alerta_Ib.append("CORRENTE ZERADA")
                        cont_IIb = 0
                        aux_data_b=[]
                        media_IIIba=[]
                        media_IIIbb=[]
                        media_IIIbc=[]



                        
                        
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if (Ic[j] == 0 and cont_IIc >= tempo_teste_zerado_I*12) or (fim_semana<=4 and (date_desp>=hora_corrente_inicio and date_desp<=hora_corrente_fim)):
                        if Ic[j] == 0 and ((Ib[j]*RTC==0 and Ia[j]*RTC==0) or (Ib[j]*RTC==0 and Ia[j]*RTC>=min_I_zerada) or (Ia[j]*RTC==0 and Ib[j]*RTC>=min_I_zerada) or (Ia[j]*RTC>=min_I_zerada and Ib[j]*RTC>=min_I_zerada)) :
                            if cont_IIc==0:
                                inicio_test_c = data_leitura[j]
                            cont_IIc =cont_IIc+1
                            media_IIIca.append(Ia[j])
                            media_IIIcb.append(Ib[j])
                            media_IIIcc.append(Ic[j])
    ##                        print(cont_IIc)
    ##                        print(data_leitura[j])
    ##                        print(data_inic_alerta_Ic)
    ##                        print(data_alerta_Ic)
    ##                        print(cont_antigo_c)
    ##                        print(cont_max_c)
    ##                        quest = sys.stdin.readline()
                            if j+1==len(Ia) and cont_IIc >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("CORRENTE ZERADA")
                        else:
                            if cont_IIc >= tempo_teste_zerado_I*12:
                                data_inic_alerta_Ic.append(inicio_test_c)
                                data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                                alerta_Ic.append("CORRENTE ZERADA")
                            cont_IIc = 0
                            aux_data_c=[]
                            media_IIIca=[]
                            media_IIIcb=[]
                            media_IIIcc=[]
                    
                        if cont_IIc >= tempo_teste_zerado_I*12:
                            if cont_IIc > tempo_teste_zerado_I*12 and data_alerta_Ic !=[]:
                                del data_alerta_Ic[len(data_alerta_Ic) -1]
                                del media_IIIca_tot[len(media_IIIca_tot) -1]
                                del media_IIIcb_tot[len(media_IIIcb_tot) -1]
                                del media_IIIcc_tot[len(media_IIIcc_tot) -1]
                            data_alerta_Ic.append(data_leitura[j])
                            cont_I2c = cont_I2c+1
                            test_passou=1
                            aux_data_c=inicio_test_c
                            media_IIIca_tot.append(sum(media_IIIca)/(len(media_IIIca)))
                            media_IIIcb_tot.append(sum(media_IIIcb)/(len(media_IIIcb)))
                            media_IIIcc_tot.append(sum(media_IIIcc)/(len(media_IIIcc)))
                            
                    else:
                        if cont_IIc >= tempo_teste_zerado_I*12:
                            data_inic_alerta_Ic.append(inicio_test_c)
                            data_fim_alerta_Ic.append(data_alerta_Ic[len(data_alerta_Ic)-1])
                            alerta_Ic.append("CORRENTE ZERADA")
                        cont_IIc = 0
                        aux_data_c=[]
                        media_IIIca=[]
                        media_IIIcb=[]
                        media_IIIcc=[]


                    date=[]
                    date_a=[]
                    date_b=[]
                    date_c=[]
                    test_max_tam=data_inic_alerta_Ia
                    test_max_tam_fim=data_fim_alerta_Ia
                    if data_inic_alerta_Ib!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ib) and data_inic_alerta_Ib[len(data_inic_alerta_Ib)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ib
                            test_max_tam_fim=data_fim_alerta_Ib
                    if data_inic_alerta_Ic!=[]:
                        if len(test_max_tam)<=len(data_inic_alerta_Ic) and data_inic_alerta_Ic[len(data_inic_alerta_Ic)-1]!=[]:
                            test_max_tam=data_inic_alerta_Ic
                            test_max_tam_fim=data_fim_alerta_Ic
                    if test_max_tam!=[]:
                        date_fim = datetime.datetime.strptime(test_max_tam_fim[len(test_max_tam_fim)-1], '%Y-%m-%d %H:%M:%S')
                        date=datetime.datetime.strptime(test_max_tam[len(test_max_tam)-1], '%Y-%m-%d %H:%M:%S')

                    if aux_data_a!=[]:
                        date_a=datetime.datetime.strptime(aux_data_a, '%Y-%m-%d %H:%M:%S')
                   
                    if aux_data_b!=[]:
                        date_b=datetime.datetime.strptime(aux_data_b, '%Y-%m-%d %H:%M:%S')
                    
                    if aux_data_c!=[]:
                        date_c=datetime.datetime.strptime(aux_data_c, '%Y-%m-%d %H:%M:%S')


    ##                #str(date_a.date())=='2014-11-13'
    ##                if  date_a!= []:      
    ##                    if i == '03100&ob.omf' and date!=[] and len(data_inic_alerta_Ib)>=2:
    ##                                print(data_inic_alerta_Ia)
    ##                                print(data_inic_alerta_Ib)
    ##                                print(data_inic_alerta_Ic)
    ##                                print(date.date())
    ##                                print(date_a)
    ##                                quest = sys.stdin.readline()
                    
                    if date_a!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ia[len(data_alerta_Ia)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ia)<len(test_max_tam):             
                            if date.date()<date_a.date() or j+1==len(Ia) or (date.date()>date_a.date() and len(data_inic_alerta_Ia)>0 and (date_interm).date()!=date_fim.date()):

                                alerta_Ia.append("CORRENTE ZERADA")
                                data_fim_alerta_Ia.append([])
                                data_inic_alerta_Ia.append([])
                                media_IIIaa_tot.append([])
                                media_IIIab_tot.append([])
                                media_IIIac_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ia)<len(test_max_tam):
                            alerta_Ia.append("CORRENTE ZERADA")
                            data_fim_alerta_Ia.append([])
                            data_inic_alerta_Ia.append([])
                            media_IIIaa_tot.append([])
                            media_IIIab_tot.append([])
                            media_IIIac_tot.append([])
                            
                    if date_b!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ib[len(data_alerta_Ib)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ib)<len(test_max_tam):                        
                            if date.date()<date_b.date() or j+1==len(Ia) or (date.date()>date_b.date() and len(data_inic_alerta_Ib)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ib.append("CORRENTE ZERADA")
                                data_fim_alerta_Ib.append([])
                                data_inic_alerta_Ib.append([])
                                media_IIIba_tot.append([])
                                media_IIIbb_tot.append([])
                                media_IIIbc_tot.append([])
                            else:
                                break

                    else:
                        while len(data_inic_alerta_Ib)<len(test_max_tam):
                            alerta_Ib.append("CORRENTE ZERADA")
                            data_fim_alerta_Ib.append([])
                            data_inic_alerta_Ib.append([])
                            media_IIIba_tot.append([])
                            media_IIIbb_tot.append([])
                            media_IIIbc_tot.append([])
                            
                    if date_c!=[]:
                        date_interm=datetime.datetime.strptime(data_alerta_Ic[len(data_alerta_Ic)-1], '%Y-%m-%d %H:%M:%S')
                        while len(data_inic_alerta_Ic)<len(test_max_tam):                    
                            if date.date()<date_c.date() or j+1==len(Ia) or (date.date()>date_c.date() and len(data_inic_alerta_Ic)>0 and (date_interm).date()!=date_fim.date()):
                                alerta_Ic.append("CORRENTE ZERADA")
                                data_fim_alerta_Ic.append([])
                                data_inic_alerta_Ic.append([])
                                media_IIIca_tot.append([])
                                media_IIIcb_tot.append([])
                                media_IIIcc_tot.append([])
                            else:
                                break
                            
                    else:
                        while len(data_inic_alerta_Ic)<len(test_max_tam):
                            alerta_Ic.append("CORRENTE ZERADA")
                            data_fim_alerta_Ic.append([])
                            data_inic_alerta_Ic.append([])  
                            media_IIIca_tot.append([])
                            media_IIIcb_tot.append([])
                            media_IIIcc_tot.append([])
                    j=j+1


                if test_passou !=0:
                    DATA_FIM_MEMO_I_ZERO_TOT.append(data_leitura[j-1])
                
                if alerta_Ia!=[] or alerta_Ib!=[] or alerta_Ic!=[]:
                    alerta_Ia_tot.append(alerta_Ia)
                    data_alerta_Ia_tot.append(data_fim_alerta_Ia)
               
                    alerta_Ib_tot.append(alerta_Ib)
                    data_alerta_Ib_tot.append(data_fim_alerta_Ib)
                
                    alerta_Ic_tot.append(alerta_Ic)
                    data_alerta_Ic_tot.append(data_fim_alerta_Ic)


                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ia):
                    if data_inic_alerta_Ia[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ia[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_a.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                        #print(date2)
                        #print(date1)
                        #print(cont_max_a[len(cont_max_a)-1])
                        #quest = sys.stdin.readline()
                    else:
                        cont_max_a.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ib):
                    if data_inic_alerta_Ib[j]!=[]:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ib[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_b.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_b.append(0)
                    j=j+1

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_Ic):
                    if data_inic_alerta_Ic[j] != []:
                        date2=datetime.datetime.strptime(data_fim_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        date1=datetime.datetime.strptime(data_inic_alerta_Ic[j], '%Y-%m-%d %H:%M:%S')
                        cont_max_c.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    else:
                        cont_max_c.append(0)
                    j=j+1



                if cont_max_a!=[] or cont_max_b!=[] or cont_max_c!=[]:
                    cont_max_Ia_tot.append(cont_max_a)
                
                    cont_max_Ib_tot.append(cont_max_b)
                
                    cont_max_Ic_tot.append(cont_max_c)


                
                if media_IIIaa_tot != [] or media_IIIab_tot != [] or media_IIIac_tot != []:
        
                    media_IIIMMaa_tot_tot.append(media_IIIaa_tot)
                    media_IIIMMab_tot_tot.append(media_IIIab_tot)
                    media_IIIMMac_tot_tot.append(media_IIIac_tot)

                if media_IIIba_tot != [] or media_IIIbb_tot != [] or media_IIIbc_tot != []:
        
                    media_IIIMMba_tot_tot.append(media_IIIba_tot)
                    media_IIIMMbb_tot_tot.append(media_IIIbb_tot)
                    media_IIIMMbc_tot_tot.append(media_IIIbc_tot)

                if media_IIIca_tot != [] or media_IIIcb_tot != [] or media_IIIcc_tot != []:
        
                    media_IIIMMca_tot_tot.append(media_IIIca_tot)
                    media_IIIMMcb_tot_tot.append(media_IIIcb_tot)
                    media_IIIMMcc_tot_tot.append(media_IIIcc_tot)



                if data_inic_alerta_Ia !=[] or data_inic_alerta_Ib!=[] or data_inic_alerta_Ic!=[]:
                    data_inic_alerta_Ia_tot.append(data_inic_alerta_Ia)
                
                    data_inic_alerta_Ib_tot.append(data_inic_alerta_Ib)
                
                    data_inic_alerta_Ic_tot.append(data_inic_alerta_Ic)


                if test_passou !=0:
                    ARQ_I_ZERO_TOT.append(i)
                    MED_I_ZERO_TOT.append(medidor_mm[ii])
                
                   
                
    ##            quest = sys.stdin.readline()
                V_cad=[]
                date_leitura_cad=[]
                j=0
                Ia_max_max = Ia[0]
                Ib_max_max = Ib[0]
                Ic_max_max = Ic[0]

                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""select T.UC_RTC , T.RTC FROM RTC_TABLE T,  rel_equip_uc@ri_carga TA
    WHERE T.UC_RTC = TA.cod_un_cons_reu
    and (dta_ins_reu -1)<= '%s'
    and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
    AND TA.num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                result = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora

                
                date_leitura_cad = str(datetime.datetime.strptime(data_leitura[len(data_leitura)-1], '%Y-%m-%d %H:%M:%S').date())
                from datetime import datetime
                date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
                cursor.execute("""SELECT qtd_tens_lig_uee  from cad_uc_ee@ri_carga,REL_EQUIP_UC@ri_carga 
where cod_un_cons_uee = cod_un_cons_reu
and (dta_ins_reu -1)<= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND NUM_EQIP_REU = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm[ii]))
                V_cad = cursor.fetchall()  # busca o resultado da consulta
                import time # biblioteca de temporização
                import datetime # biblioteca de operações avançadas com data e hora
                if V_cad == []:
                    V_cad.append([13800,13800])
                
                
                if result == []:
                        RTC = 1
                        
                else:
                        RTC = result[0][1]
                if len(result) >1:
                    wwjk=0
                    while wwjk<=(len(result)-1):
                        if result[wwjk][1] is not None:
                            RTC = result[wwjk][1]
                        wwjk=wwjk+1
                
                while j<len(Ia):
                    
                    if Ia[j] > Ia_max_max:
                        Ia_max_max = Ia[j]

                    if Ib[j] > Ib_max_max:
                        Ib_max_max = Ib[j]

                    if Ic[j] > Ic_max_max:
                        Ic_max_max = Ic[j]

                    j=j+1

                media_Ia=[]
                media_Ib=[]
                media_Ic=[]
                j=0
                media_Ia_tot= []
                media_Ib_tot= []
                media_Ic_tot= []
                #digitar valor em horas####################
                tempo_teste_zerado_I_desp = 4
                cont_II =0
                inicio_test = 0
                data_inic_alerta_desp_Ia=[]
                date_desp =[]
                test_passou =0
                #hora_corrente_desp_inicio = '08:00:00'
                #hora_corrente_desp_fim = '18:00:00'
                #porc_carga_oper_inst = 0.35
                #Dif_I_pri_sec_380=30
                Dif_I_pri_sec_13=30
                Dif_I_pri_sec_34_69=30
    
                while j<len(Ia):
                    
                    Imax=Ia[j]
                    if Imax<=Ib[j]:
                        Imax=Ib[j]
                    if Imax<=Ic[j]:
                        Imax=Ic[j]

                    Imin=Ia[j]
                    if Imin>=Ib[j]:
                        Imin=Ib[j]
                    if Imin>=Ic[j]:
                        Imin=Ic[j]

                    test_desprop_continuo=0
                    if Imax > 0 and Imin > 0 and ((RTC>=1 and V_cad[0][0]==380 and (Imax-Imin)*RTC >= Dif_I_pri_sec_380) or (RTC>=1 and V_cad[0][0]==13800 and (Imax-Imin)*RTC >= Dif_I_pri_sec_13) or (RTC>=1 and (V_cad[0][0]==34500 or V_cad[0][0]==69000) and (Imax-Imin)*RTC >= Dif_I_pri_sec_34_69)):
                        test_desprop_continuo = 1
                    fim_semana = datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').weekday()
                    date_desp = str(datetime.datetime.strptime(data_leitura[j], '%Y-%m-%d %H:%M:%S').time())
                    if (test_desprop_continuo==1 and cont_II >= tempo_teste_zerado_I_desp*12) or fim_semana<=4:
                        if Imax > 0 and Imin > 0 and ((RTC>=1 and V_cad[0][0]==380 and (Imax-Imin)*RTC >= Dif_I_pri_sec_380) or (RTC>=1 and V_cad[0][0]==13800 and (Imax-Imin)*RTC >= Dif_I_pri_sec_13) or (RTC>=1 and (V_cad[0][0]==34500 or V_cad[0][0]==69000) and (Imax-Imin)*RTC >= Dif_I_pri_sec_34_69)):
                            #if data_alerta_desp_Ia!= []:
##                                if data_alerta_desp_Ia[len(data_alerta_desp_Ia)-1] == '2015-05-05 14:20:00':
##                                    print(data_inic_alerta_desp_Ia)
##                                    print(data_alerta_desp_Ia)
##                                    print(cont_II)
##                                    quest = sys.stdin.readline()
                                
                            if (Ia[j]>=0.35*Ia_max_max or Ib[j]>=0.35*Ib_max_max or Ic[j]>=0.35*Ic_max_max):
                                
                                if  date_desp>=hora_corrente_desp_inicio and date_desp<=hora_corrente_desp_fim:
                                    
                                    if cont_II==0:
                                        inicio_test = data_leitura[j]
                                    cont_II =cont_II+1
                                    media_Ia.append(Ia[j])
                                    media_Ib.append(Ib[j])
                                    media_Ic.append(Ic[j])
                                if j+1==len(Ia) and cont_II >= tempo_teste_zerado_I_desp*12:
                                    data_inic_alerta_desp_Ia.append(inicio_test)

                            else:
                                if cont_II >= tempo_teste_zerado_I_desp*12:
                                    data_inic_alerta_desp_Ia.append(inicio_test)
                                cont_II = 0
                                media_Ia= []
                                media_Ib= []
                                media_Ic= []

                        

                            if  date_desp>=hora_corrente_desp_inicio and date_desp<=hora_corrente_desp_fim:               
                                if cont_II >= tempo_teste_zerado_I_desp*12:
                                    
                                    if cont_II > tempo_teste_zerado_I_desp*12 and data_alerta_desp_Ia !=[]:
                                            del alerta_desp_Ia[len(alerta_desp_Ia) -1]
                                            del data_alerta_desp_Ia[len(data_alerta_desp_Ia) -1]

                                            del media_Ia_tot[len(media_Ia_tot) -1]
                                            del media_Ib_tot[len(media_Ib_tot) -1]
                                            del media_Ic_tot[len(media_Ic_tot) -1]
                                    alerta_desp_Ia.append("CORRENTES DESPROPORCIONAIS")
                                    data_alerta_desp_Ia.append(data_leitura[j])
                                    cont_I2aaa = cont_I2aaa+1
                                    test_passou=1
                                    media_Ia_tot.append(sum(media_Ia)/(len(media_Ia)))
                                    media_Ib_tot.append(sum(media_Ib)/(len(media_Ib)))
                                    media_Ic_tot.append(sum(media_Ic)/(len(media_Ic)))

                        else:
                            if cont_II >= tempo_teste_zerado_I_desp*12:
                                data_inic_alerta_desp_Ia.append(inicio_test)
                            cont_II = 0
                            media_Ia= []
                            media_Ib= []
                            media_Ic= []  
                        
                    else:
                        if cont_II >= tempo_teste_zerado_I_desp*12:
                            data_inic_alerta_desp_Ia.append(inicio_test)
                        cont_II = 0

                    j=j+1
                

                if test_passou !=0:
                    DATA_FIM_MEMO_I_DESP_TOT.append(data_leitura[j-1])
                
                if alerta_desp_Ia!=[]:
                    alerta_desp_I.append(alerta_desp_Ia)
                    data_alerta_desp_I.append(data_alerta_desp_Ia)

                j=0
                date2=[]
                date1=[]
                while j<len(data_inic_alerta_desp_Ia):
                    date2=datetime.datetime.strptime(data_alerta_desp_Ia[j], '%Y-%m-%d %H:%M:%S')
                    date1=datetime.datetime.strptime(data_inic_alerta_desp_Ia[j], '%Y-%m-%d %H:%M:%S')
                    cont_max.append(((date2 - date1).days*24*60*60 + (date2 - date1).seconds)/3600)
                    j=j+1

                if cont_max!=[]:
                    cont_max_I_desp_tot.append(cont_max)


                test_max_tam=len(media_Ia_tot)
                if test_max_tam<len(media_Ib_tot):
                    test_max_tam=len(media_Ib_tot)
                if test_max_tam<len(media_Ic_tot):
                    test_max_tam=len(media_Ic_tot)
                j=0
                while len(media_Ia_tot)<test_max_tam:
                    media_Ia_tot.append([])
                while len(media_Ib_tot)<test_max_tam:
                    media_Ib_tot.append([])
                while len(media_Ic_tot)<test_max_tam:
                    media_Ic_tot.append([])


                
                if media_Ia_tot != [] or media_Ib_tot != [] or media_Ic_tot != []:
                    
                    media_Ia_tot_tot.append(media_Ia_tot)
                    media_Ib_tot_tot.append(media_Ib_tot)
                    media_Ic_tot_tot.append(media_Ic_tot)

                if data_inic_alerta_desp_Ia!=[]:
                    data_inic_alerta_desp_I.append(data_inic_alerta_desp_Ia)

                if test_passou !=0:
                    ARQ_I_DESP_TOT.append(i)
                    MED_I_DESP_TOT.append(medidor_mm[ii])

                  
        ii=ii+1            
###################################################################################################################
###################################################################################################################
###################################################################################################################
result2=[]
result3=[]
result4 = []
vetor_alerta=[]
vetor_alerta_media_a=[]
vetor_alerta_media_b=[]
vetor_alerta_media_c=[]
vetor_alerta_I=[]
vetor_alerta_Neg_I=[]
vetor_alerta_Neg = []

import csv
with open('RELATÓRIO_ALERTAS.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['UC','ARQUIVO','MEDIDOR','DATA_INSTAL_MED','NOME_CLIENTE','SITUACAO','RTP_RTC','ATIVIDADE','ALERTA','F_A MÉDIO','F_A DATA INÍCIO','F_A DATA FIM','F_A DURAÇÃO','F_B MÉDIO','F_B DATA INÍCIO','F_B DATA FIM','F_B DURAÇÃO','F_C MÉDIO','F_C DATA INÍCIO','F_C DATA FIM','F_C DURAÇÃO'])

    jj=0
    while jj<= (len(MED_V_ZERO_Neg_TOT)-1):
        if MED_V_ZERO_Neg_TOT!=[]:
            ww=0
            data_med_reu=[]
            #if data_inic_alerta_Va_Neg_tot[jj][len(data_inic_alerta_Va_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Va_Neg_tot[jj][len(data_inic_alerta_Va_Neg_tot[jj])-1]
            #if data_inic_alerta_Vb_Neg_tot[jj][len(data_inic_alerta_Vb_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Vb_Neg_tot[jj][len(data_inic_alerta_Vb_Neg_tot[jj])-1]
            #if data_inic_alerta_Vc_Neg_tot[jj][len(data_inic_alerta_Vc_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Vc_Neg_tot[jj][len(data_inic_alerta_Vc_Neg_tot[jj])-1]
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_V_Neg_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_Neg_TOT[jj]))
            result = cursor.fetchall()
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_Neg_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_Neg_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_V_ZERO_Neg_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_Va_Neg_tot[jj])-1):
                if media_VVVaa_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVaa_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVab_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVac_tot_tot[jj][ww]
                if media_VVVbb_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVba_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVbb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVbc_tot_tot[jj][ww]
                if media_VVVcc_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVca_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVcb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVcc_tot_tot[jj][ww]
                if alerta_Va_Neg_tot[jj][ww] == "LIGAÇÃO TP INVERTIDA":
                    vetor_alerta_Neg=alerta_Va_Neg_tot
                if alerta_Vb_Neg_tot[jj][ww] == "LIGAÇÃO TP INVERTIDA":
                    vetor_alerta_Neg=alerta_Vb_Neg_tot
                if alerta_Vc_Neg_tot[jj][ww] == "LIGAÇÃO TP INVERTIDA":
                    vetor_alerta_Neg=alerta_Vc_Neg_tot
                if alerta_Va_Neg_tot!=[]:
                    
                    duracao_fa = str(round(cont_max_Va_Neg_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fb = str(round(cont_max_Vb_Neg_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fc = str(round(cont_max_Vc_Neg_tot[jj][ww], 1)).replace('.', ',')    
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_V_ZERO_Neg_TOT[jj],MED_V_ZERO_Neg_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,vetor_alerta_Neg[jj][ww],round(vetor_alerta_media_a, 2),data_inic_alerta_Va_Neg_tot[jj][ww],data_alerta_Va_Neg_tot[jj][ww],duracao_fa,round(vetor_alerta_media_b, 2),data_inic_alerta_Vb_Neg_tot[jj][ww],data_alerta_Vb_Neg_tot[jj][ww],duracao_fb,round(vetor_alerta_media_c, 2),data_inic_alerta_Vc_Neg_tot[jj][ww],data_alerta_Vc_Neg_tot[jj][ww],duracao_fc])
                ww=ww+1
        jj=jj+1

    
    jj=0
    while jj<= (len(MED_V_ZERO_TOT)-1):
        if MED_V_ZERO_TOT!=[]:
            ww=0
            data_med_reu=[]
            #if data_inic_alerta_Va_tot[jj][len(data_inic_alerta_Va_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Va_tot[jj][len(data_inic_alerta_Va_tot[jj])-1]
            #if data_inic_alerta_Vb_tot[jj][len(data_inic_alerta_Vb_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Vb_tot[jj][len(data_inic_alerta_Vb_tot[jj])-1]
            #if data_inic_alerta_Vc_tot[jj][len(data_inic_alerta_Vc_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Vc_tot[jj][len(data_inic_alerta_Vc_tot[jj])-1]
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_V_ZERO_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_TOT[jj]))
            result = cursor.fetchall()

            
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_ZERO_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_V_ZERO_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_Va_tot[jj])-1):
                if media_VVVMMaa_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVMMaa_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVMMab_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVMMac_tot_tot[jj][ww]
                if media_VVVMMbb_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVMMba_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVMMbb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVMMbc_tot_tot[jj][ww]
                if media_VVVMMcc_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_VVVMMca_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_VVVMMcb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_VVVMMcc_tot_tot[jj][ww]
                if alerta_Va_tot[jj][ww] == "TENSÃO ZERADA":
                    vetor_alerta=alerta_Va_tot
                if alerta_Vb_tot[jj][ww] == "TENSÃO ZERADA":
                    vetor_alerta=alerta_Vb_tot
                if alerta_Vc_tot[jj][ww] == "TENSÃO ZERADA":
                    vetor_alerta=alerta_Vc_tot
                if alerta_Va_tot!=[]:
                                            
                    duracao_fa = str(round(cont_max_Va_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fb = str(round(cont_max_Vb_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fc = str(round(cont_max_Vc_tot[jj][ww], 1)).replace('.', ',')
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_V_ZERO_TOT[jj],MED_V_ZERO_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,vetor_alerta[jj][ww],round(vetor_alerta_media_a, 2),data_inic_alerta_Va_tot[jj][ww],data_alerta_Va_tot[jj][ww],duracao_fa,round(vetor_alerta_media_b, 2),data_inic_alerta_Vb_tot[jj][ww],data_alerta_Vb_tot[jj][ww],duracao_fb,round(vetor_alerta_media_c, 2),data_inic_alerta_Vc_tot[jj][ww],data_alerta_Vc_tot[jj][ww],duracao_fc])
                ww=ww+1
        jj=jj+1


    jj=0
    while jj<= (len(MED_V_DESP_TOT)-1):
        if MED_V_DESP_TOT!=[]:
            ww=0
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_V_DESP_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_DESP_TOT[jj]))
            result = cursor.fetchall()
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_DESP_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_V_DESP_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_V_DESP_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_desp_V[jj])-1):
                if alerta_desp_V!=[]:
                    
                    duracao_fa = str(round(cont_max_desp_V_tot[jj][ww], 1)).replace('.', ',')
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_V_DESP_TOT[jj],MED_V_DESP_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,alerta_desp_V[jj][ww],round(media_Va_tot_tot[jj][ww],2),data_inic_alerta_desp_V[jj][ww],data_alerta_desp_V[jj][ww],duracao_fa,round(media_Vb_tot_tot[jj][ww], 2),'','','',round(media_Vc_tot_tot[jj][ww], 2),'','',''])
                ww=ww+1
        jj=jj+1


    jj=0
    while jj<= (len(MED_I_ZERO_Neg_TOT)-1):
        if MED_I_ZERO_Neg_TOT!=[]:
            ww=0
            data_med_reu=[]
            #if data_inic_alerta_Ia_Neg_tot[jj][len(data_inic_alerta_Ia_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ia_Neg_tot[jj][len(data_inic_alerta_Ia_Neg_tot[jj])-1]
            #if data_inic_alerta_Ib_Neg_tot[jj][len(data_inic_alerta_Ib_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ib_Neg_tot[jj][len(data_inic_alerta_Ib_Neg_tot[jj])-1]
            #if data_inic_alerta_Ic_Neg_tot[jj][len(data_inic_alerta_Ic_Neg_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ic_Neg_tot[jj][len(data_inic_alerta_Ic_Neg_tot[jj])-1]
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_I_Neg_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_Neg_TOT[jj]))
            result = cursor.fetchall()
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_Neg_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_Neg_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_I_ZERO_Neg_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_Ia_Neg_tot[jj])-1):
                if alerta_Ia_Neg_tot[jj][ww] == "LIGAÇÃO TC INVERTIDA":
                    vetor_alerta_Neg_I=alerta_Ia_Neg_tot
                if alerta_Ib_Neg_tot[jj][ww] == "LIGAÇÃO TC INVERTIDA":
                    vetor_alerta_Neg_I=alerta_Ib_Neg_tot
                if alerta_Ic_Neg_Neg_tot[jj][ww] == "LIGAÇÃO TC INVERTIDA":
                    vetor_alerta_Neg_I=alerta_Ic_Neg_Neg_tot
                if alerta_Ia_Neg_tot!=[]:
                    
                    duracao_fa = str(round(cont_max_Ia_Neg_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fb = str(round(cont_max_Ib_Neg_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fc = str(round(cont_max_Ic_Neg_tot[jj][ww], 1)).replace('.', ',')
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_I_ZERO_Neg_TOT[jj],MED_I_ZERO_Neg_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,vetor_alerta_Neg_I[jj][ww],'',data_inic_alerta_Ia_Neg_tot[jj][ww],data_alerta_Ia_Neg_tot[jj][ww],duracao_fa,'',data_inic_alerta_Ib_Neg_tot[jj][ww],data_alerta_Ib_Neg_tot[jj][ww],duracao_fb,'',data_inic_alerta_Ic_Neg_tot[jj][ww],data_alerta_Ic_Neg_tot[jj][ww],duracao_fc])
                ww=ww+1
        jj=jj+1


    jj=0
    while jj<= (len(MED_I_ZERO_TOT)-1):
        if MED_I_ZERO_TOT!=[]:
            ww=0
            data_med_reu=[]
            #if data_inic_alerta_Ia_tot[jj][len(data_inic_alerta_Ia_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ia_tot[jj][len(data_inic_alerta_Ia_tot[jj])-1]
            #if data_inic_alerta_Ib_tot[jj][len(data_inic_alerta_Ib_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ib_tot[jj][len(data_inic_alerta_Ib_tot[jj])-1]
            #if data_inic_alerta_Ic_tot[jj][len(data_inic_alerta_Ic_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ic_tot[jj][len(data_inic_alerta_Ic_tot[jj])-1]
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_I_ZERO_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_TOT[jj]))
            result = cursor.fetchall()

            #print(result[0][0])
            #quest = sys.stdin.readline()
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_I_ZERO_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_Ia_tot[jj])-1):
                if media_IIIMMaa_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMaa_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMab_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMac_tot_tot[jj][ww]
                if media_IIIMMbb_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMba_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMbb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMbc_tot_tot[jj][ww]
                if media_IIIMMcc_tot_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMca_tot_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMcb_tot_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMcc_tot_tot[jj][ww]
                if alerta_Ia_tot[jj][ww] == "CORRENTE ZERADA":
                    vetor_alerta_I=alerta_Ia_tot
                if alerta_Ib_tot[jj][ww] == "CORRENTE ZERADA":
                    vetor_alerta_I=alerta_Ib_tot
                if alerta_Ic_tot[jj][ww] == "CORRENTE ZERADA":
                    vetor_alerta_I=alerta_Ic_tot
                if alerta_Ia_tot!=[]:
                    
                    duracao_fa = str(round(cont_max_Ia_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fb = str(round(cont_max_Ib_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fc = str(round(cont_max_Ic_tot[jj][ww], 1)).replace('.', ',')     
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_I_ZERO_TOT[jj],MED_I_ZERO_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,vetor_alerta_I[jj][ww],round(vetor_alerta_media_a, 2),data_inic_alerta_Ia_tot[jj][ww],data_alerta_Ia_tot[jj][ww],duracao_fa,round(vetor_alerta_media_b, 2),data_inic_alerta_Ib_tot[jj][ww],data_alerta_Ib_tot[jj][ww],duracao_fb,round(vetor_alerta_media_c, 2),data_inic_alerta_Ic_tot[jj][ww],data_alerta_Ic_tot[jj][ww],duracao_fc])
                ww=ww+1
        jj=jj+1




    jj=0
    while jj<= (len(MED_I_ZERO_sat_TOT)-1):
        if MED_I_ZERO_sat_TOT!=[]:
            ww=0
            data_med_reu=[]
            #if data_inic_alerta_Ia_sat_tot[jj][len(data_inic_alerta_Ia_sat_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ia_sat_tot[jj][len(data_inic_alerta_Ia_sat_tot[jj])-1]
            #if data_inic_alerta_Ib_sat_tot[jj][len(data_inic_alerta_Ib_sat_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ib_sat_tot[jj][len(data_inic_alerta_Ib_sat_tot[jj])-1]
            #if data_inic_alerta_Ic_sat_tot[jj][len(data_inic_alerta_Ic_sat_tot[jj])-1] !=[]:
                #data_med_reu = data_inic_alerta_Ic_sat_tot[jj][len(data_inic_alerta_Ic_sat_tot[jj])-1]
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_I_sat_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_sat_TOT[jj]))
            result = cursor.fetchall()
            
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_sat_TOT[jj]))
            result2 = cursor.fetchall()
            
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_ZERO_sat_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_I_ZERO_sat_TOT[jj])
            result4 = cursor.fetchall()

            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
            if result == []:
                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
                
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            while ww<= (len(alerta_Ia_sat_tot[jj])-1):
                if media_IIIMMaa_tot_sat_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMaa_tot_sat_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMab_tot_sat_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMac_tot_sat_tot[jj][ww]
                if media_IIIMMbb_tot_sat_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMba_tot_sat_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMbb_tot_sat_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMbc_tot_sat_tot[jj][ww]
                if media_IIIMMcc_tot_sat_tot[jj][ww] !=[]:
                    vetor_alerta_media_a=media_IIIMMca_tot_sat_tot[jj][ww]
                    vetor_alerta_media_b=media_IIIMMcb_tot_sat_tot[jj][ww]
                    vetor_alerta_media_c=media_IIIMMcc_tot_sat_tot[jj][ww]
                if alerta_Ia_sat_tot[jj][ww] == "TC SATURADO":
                    vetor_alerta_I=alerta_Ia_sat_tot
                if alerta_Ib_sat_tot[jj][ww] == "TC SATURADO":
                    vetor_alerta_I=alerta_Ib_sat_tot
                if alerta_Ic_sat_tot[jj][ww] == "TC SATURADO":
                    vetor_alerta_I=alerta_Ic_sat_tot
                if alerta_Ia_sat_tot!=[]:
                    
                    duracao_fa = str(round(cont_max_Ia_sat_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fb = str(round(cont_max_Ib_sat_tot[jj][ww], 1)).replace('.', ',')
                    duracao_fc = str(round(cont_max_Ic_sat_tot[jj][ww], 1)).replace('.', ',')
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_I_ZERO_sat_TOT[jj],MED_I_ZERO_sat_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,vetor_alerta_I[jj][ww],round(vetor_alerta_media_a, 2),data_inic_alerta_Ia_sat_tot[jj][ww],data_alerta_Ia_sat_tot[jj][ww],duracao_fa,round(vetor_alerta_media_b, 2),data_inic_alerta_Ib_sat_tot[jj][ww],data_alerta_Ib_sat_tot[jj][ww],duracao_fb,round(vetor_alerta_media_c, 2),data_inic_alerta_Ic_sat_tot[jj][ww],data_alerta_Ic_sat_tot[jj][ww],duracao_fc])
                ww=ww+1
        jj=jj+1



        
    jj=0
    UC_despr=''
    while jj<= (len(MED_I_DESP_TOT)-1):
        if MED_I_DESP_TOT!=[]:
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_I_DESP_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_DESP_TOT[jj]))
            result = cursor.fetchall()
            if result != []:
                UC_despr = UC_despr+str(abs(result[0][0]))+(",")
        jj=jj+1
    UC_despr=UC_despr[0:len(UC_despr)-1]
    if UC_despr!='':
        cursor.execute("drop table auxi_MAX_DATA")
        cursor.execute("""CREATE TABLE auxi_MAX_DATA as (
        SELECT COD_UN_CONS AS UC, MAX(DTA_SERV) AS SERV_DTA FROM clpdw.PI_INSPECAO@biraprd
        WHERE COD_UN_CONS in (%s)
        and cod_300 = 1
        GROUP BY COD_UN_CONS)""" %(UC_despr))

        
        
        cursor.execute("drop table auxi_table_desp")
        cursor.execute("""CREATE TABLE auxi_table_desp as (
    select COD_UN_CONS_COS,cod_simpl_os_cos,num_seq_oper_cos,num_seq_ger_cos, DTA_SERV from cad_ord_serv@celpapr, clpdw.PI_INSPECAO@biraprd,auxi_MAX_DATA
    WHERE COD_UN_CONS_COS = COD_UN_CONS
    AND COD_UN_CONS_COS = UC
    AND cod_simpl_os_cos=cod_simpl_os
    and cod_300 = 1
    AND DTA_SERV> = SERV_DTA)""")

        #cursor.execute("""SELECT COD_UN_CONS_COS,cod_simpl_os_cos,num_seq_oper_cos,num_seq_ger_cos, DTA_SERV FROM
#auxi_table_desp""")
        #resultkkkkkk = cursor.fetchall()
        #print(resultkkkkkk)

       
        cursor.execute("drop table auxi_table4_desp")
        cursor.execute("""CREATE TABLE auxi_table4_desp as ( 
    select t.COD_UN_CONS_COS, ca.vlr_corr_ramal_01_ldt as IA, ca.vlr_corr_ramal_02_ldt as IB, ca.vlr_corr_ramal_03_ldt AS IC, vlr_corr_borne_01_ldt as IA2, vlr_corr_borne_02_ldt as IB2, vlr_corr_borne_03_ldt as IC2   from cad_laudo_tecnico_fraude@celpapr ca, auxi_table_desp t 
    where ca.num_seq_oper_ldt = t.num_seq_oper_cos 
    and ca.num_seq_ger_ldt = t.num_seq_ger_cos) """)


    

    jj=0
    while jj<= (len(MED_I_DESP_TOT)-1):
        if MED_I_DESP_TOT!=[]:
            from datetime import datetime
            date_leitura_cad = str(datetime.strptime(DATA_FIM_MEMO_I_DESP_TOT[jj], '%Y-%m-%d %H:%M:%S').date())
            from datetime import datetime
            date_leitura_cad = datetime.strptime(date_leitura_cad, '%Y-%m-%d').strftime('%d/%m/%Y')
            cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee from TAB_CLASSE_CONSUMO@celpapr,CAD_UC_EE@celpapr, C_ALTA_TENSAO2,REL_EQUIP_UC@celpapr 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND cod_un_cons_reu = UC
and COD_UN_CONS_UEE = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_DESP_TOT[jj]))
            result = cursor.fetchall()
                    
            cursor.execute("""SELECT RTC from RTC_TABLE,rel_equip_uc@celpapr
WHERE UC_RTC = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_DESP_TOT[jj]))
            result2 = cursor.fetchall()
                    
            cursor.execute("""SELECT RTP from RTP_TABLE,rel_equip_uc@celpapr
WHERE UC_RTP = cod_un_cons_reu
and (dta_ins_reu - 1) <= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,MED_I_DESP_TOT[jj]))
            result3 = cursor.fetchall()
            cursor.execute("""select DTA_INS_REU FROM REL_EQUIP_UC@celpapr 
where DTA_RETI_REU IS NULL
AND NUM_EQIP_REU = '%s' """ %MED_I_DESP_TOT[jj])
            result4 = cursor.fetchall()
            
            if result4 == []:
                INSTAL_MED = "NÃO INSTALADO"
            else:
                INSTAL_MED =result4[0][0]
            if result2 == []:
                RTP_RTC = "SEM RTC"
            else:
                RTP_RTC = 'RTC='+str(result2[0][0])
            if result3 == []:
                RTP_RTC = RTP_RTC + " E SEM RTP"
            else:
                RTP_RTC = RTP_RTC + ' ' +'RTP='+str(result3[0][0])
                
            if result == []:

                UC = "SEM UC"
                ATIVIDADE ="SEM ATIVIDADE"
                NOME_CLIENTE = "SEM NOME"
                SITUACAO ="SEM SITUAÇÃO"
            else:
                UC = abs(result[0][0])
                ATIVIDADE = result[0][1]
                NOME_CLIENTE = result[0][2]
                SITUACAO = result[0][3]
                ATIVIDADE = ATIVIDADE.replace(';', '.')
            result5=[]
            if UC != "SEM UC":
                cursor.execute("""select COD_UN_CONS_COS, IA, IB, IC, IA2,IB2, IC2 from auxi_table4_desp 
where COD_UN_CONS_COS = '%s' """ %UC)
                result5 = cursor.fetchall()
            if result5==[]:
                iaa = "Ia = []" 
                ibb = "Ib = []"
                icc = "Ic = []"
            else:
                if result5[0][4] is not None:
                    iaa = "Ia = " + str(round(result5[0][4], 2))
                else:
                    iaa = "Ia = " + str(result5[0][4])
                if result5[0][5] is not None:
                    ibb = "Ib = " + str(round(result5[0][5], 2))
                else:
                    ibb = "Ib = " + str(result5[0][5])
                if result5[0][6] is not None:
                    icc = "Ic = " + str(round(result5[0][6], 2))
                else:
                    icc = "Ic = " + str(result5[0][6])
            #print('KKKKKKK')
            #quest = sys.stdin.readline()
            ww=0
            while ww<= (len(alerta_desp_I[jj])-1):
                if alerta_desp_I!=[] and ATIVIDADE!='ADMINISTRACAO PUBLICA ESTADUAL' and ATIVIDADE!= 'ADMINISTRACAO PUBLICA FEDERAL' and ATIVIDADE!='ADMINISTRACAO PUBLICA MUNICIPAL':
                    
                    duracao_fa = str(round(cont_max_I_desp_tot[jj][ww], 1)).replace('.', ',')
                    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
                    spamwriter.writerow([UC,ARQ_I_DESP_TOT[jj],MED_I_DESP_TOT[jj],INSTAL_MED,NOME_CLIENTE,SITUACAO,RTP_RTC,ATIVIDADE,alerta_desp_I[jj][ww],round(media_Ia_tot_tot[jj][ww], 2),data_inic_alerta_desp_I[jj][ww],data_alerta_desp_I[jj][ww],duracao_fa,round(media_Ib_tot_tot[jj][ww], 2),iaa,ibb,icc,round(media_Ic_tot_tot[jj][ww], 2),'','',''])
                ww=ww+1
        jj=jj+1

csvfile.close()



import csv
with open('RELATÓRIO_Clientes_Analisados.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['UC','ARQUIVO','MEDIDOR','NOME_CLIENTE','ATIVIDADE','SITUACAO','DATA_SITUACAO','LOCALIDADE','REGIONAL','ETAPA'])

    jj=0
    while jj<= (len(medidor_mm_VA)-1):
        #from datetime import datetime
        #date_leitura_cad = str(datetime.strptime(data_todos_arquiv[0], '%Y-%m-%d %H:%M:%S').date())
        from datetime import datetime
        date_leitura_cad = datetime.strptime(data_todos_arquiv[len(data_todos_arquiv)-1], '%Y-%m-%d').strftime('%d/%m/%Y')
        cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee,dta_situ_uee, LOCALIDADE, REGIONAL from TAB_CLASSE_CONSUMO@ri_carga,CAD_UC_EE@ri_carga, C_ALTA_TENSAO2,REL_EQUIP_UC@ri_carga 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND COD_UN_CONS_reu = UC
AND COD_UN_CONS_UEE = UC
and (dta_ins_reu -1)<= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,medidor_mm_VA[jj]))
        result = cursor.fetchall()
        if result == []:
            UC = "SEM UC"
            ATIVIDADE ="SEM ATIVIDADE"
            NOME_CLIENTE = "SEM NOME"
            SITUACAO ="SEM SITUAÇÃO"
            DATA_SITUACAO ="SEM SITUAÇÃO"
            LOCALIDADE ="SEM LOCALIDADE"
            REGIONAL ="SEM REGIONAL"
            #ETAPA ="SEM ETAPA"
        else:
            UC = abs(result[0][0])
            ATIVIDADE = result[0][1]
            NOME_CLIENTE = result[0][2]
            SITUACAO = result[0][3]
            DATA_SITUACAO = result[0][4]
            LOCALIDADE = result[0][5]
            REGIONAL = result[0][6]
            ATIVIDADE = ATIVIDADE.replace(';', '.')
            #ETAPA = result[0][7]
        spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([UC,nome_arq_VA[jj],medidor_mm_VA[jj],NOME_CLIENTE,ATIVIDADE,SITUACAO,DATA_SITUACAO,LOCALIDADE,REGIONAL])       
        jj=jj+1


Falta_VV = []
Falta_II = []
Data_Falta_VV = []
Data_Falta_II = []
jj=0
while jj<= (len(medidor_pot_WW_comp)-1):
    kk=0
    teste_comp_WV = 0
    while kk<= (len(medidor_tens_VV_comp)-1):
        if (medidor_pot_WW_comp[jj] == medidor_tens_VV_comp[kk]) and (data_pot_WW_comp[jj]==data_tens_VV_comp[kk]):
            teste_comp_WV = 1
        kk=kk+1
    if teste_comp_WV ==0:
        Falta_VV.append(medidor_pot_WW_comp[jj])
        Data_Falta_VV.append(data_pot_WW_comp[jj])
    jj=jj+1

jj=0
while jj<= (len(medidor_pot_WW_comp)-1):
    kk=0
    teste_comp_WI = 0
    while kk<= (len(medidor_corr_II_comp)-1):
        if (medidor_pot_WW_comp[jj] == medidor_corr_II_comp[kk]) and (data_pot_WW_comp[jj] == data_corr_II_comp[kk]):
            teste_comp_WI = 1
        kk=kk+1
    if teste_comp_WI ==0:
        Falta_II.append(medidor_pot_WW_comp[jj])
        Data_Falta_II.append(data_pot_WW_comp[jj])
    jj=jj+1

UC_ANT= 0
import csv
with open('RELATÓRIO_Clientes_Sem_ARQUIVOS_VI.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['UC','TIPO_ARQUIVO','MEDIDOR','DATA LEITURA','NOME_CLIENTE','ATIVIDADE','SITUACAO','DATA_SITUACAO','LOCALIDADE','REGIONAL'])

    jj=0
    while jj<= (len(Falta_VV)-1):
        #from datetime import datetime
        #date_leitura_cad = str(datetime.strptime(Data_Falta_VV[0], '%Y-%m-%d %H:%M:%S').date())
        from datetime import datetime
        date_leitura_cad = datetime.strptime(Data_Falta_VV[len(Data_Falta_VV)-1], '%Y-%m-%d').strftime('%d/%m/%Y')
        cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee,dta_situ_uee, LOCALIDADE, REGIONAL from TAB_CLASSE_CONSUMO@ri_carga,CAD_UC_EE@ri_carga, C_ALTA_TENSAO2,REL_EQUIP_UC@ri_carga 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND COD_UN_CONS_reu = UC
AND COD_UN_CONS_UEE = UC
and (dta_ins_reu -1)<= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,Falta_VV[jj]))
        result = cursor.fetchall()
        if result == []:
            UC = "SEM UC"
            ATIVIDADE ="SEM ATIVIDADE"
            NOME_CLIENTE = "SEM NOME"
            SITUACAO ="SEM SITUAÇÃO"
            DATA_SITUACAO ="SEM SITUAÇÃO"
            LOCALIDADE ="SEM LOCALIDADE"
            REGIONAL ="SEM REGIONAL"
           # ETAPA ="SEM ETAPA"
        else:
            UC = abs(result[0][0])
            ATIVIDADE = result[0][1]
            NOME_CLIENTE = result[0][2]
            SITUACAO = result[0][3]
            DATA_SITUACAO = result[0][4]
            LOCALIDADE = result[0][5]
            REGIONAL = result[0][6]
            ATIVIDADE = ATIVIDADE.replace(';', '.')
            #ETAPA = result[0][7]
        if UC!=UC_ANT:
            spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([UC,'TENSÃO',Falta_VV[jj],Data_Falta_VV[jj],NOME_CLIENTE,ATIVIDADE,SITUACAO,DATA_SITUACAO,LOCALIDADE,REGIONAL])       
        UC_ANT=UC
        jj=jj+1



    UC_ANT= 0
    jj=0
    while jj<= (len(Falta_II)-1):
        #from datetime import datetime
        #date_leitura_cad = str(datetime.strptime(Data_Falta_II[0], '%Y-%m-%d %H:%M:%S').date())
        from datetime import datetime
        date_leitura_cad = datetime.strptime(Data_Falta_II[len(Data_Falta_II)-1], '%Y-%m-%d').strftime('%d/%m/%Y')
        cursor.execute("""SELECT COD_UN_CONS_UEE, DES_CLAS_CONS_CLA,NOME_CLIENTE, cod_situ_uee,dta_situ_uee, LOCALIDADE, REGIONAL from TAB_CLASSE_CONSUMO@ri_carga,CAD_UC_EE@ri_carga, C_ALTA_TENSAO2,REL_EQUIP_UC@ri_carga 
WHERE COD_CLAS_CONS_UEE = COD_CLAS_CONS_CLA
AND COD_UN_CONS_reu = UC
AND COD_UN_CONS_UEE = UC
and (dta_ins_reu -1)<= '%s'
and ((dta_reti_reu+1) >= '%s' or dta_reti_reu is null)
AND num_eqip_reu = '%s' """ %(date_leitura_cad,date_leitura_cad,Falta_II[jj]))
        result = cursor.fetchall()
        if result == []:
            UC = "SEM UC"
            ATIVIDADE ="SEM ATIVIDADE"
            NOME_CLIENTE = "SEM NOME"
            SITUACAO ="SEM SITUAÇÃO"
            DATA_SITUACAO ="SEM SITUAÇÃO"
            LOCALIDADE ="SEM LOCALIDADE"
            REGIONAL ="SEM REGIONAL"
            #ETAPA ="SEM ETAPA"
        else:
            UC = abs(result[0][0])
            ATIVIDADE = result[0][1]
            NOME_CLIENTE = result[0][2]
            SITUACAO = result[0][3]
            DATA_SITUACAO = result[0][4]
            LOCALIDADE = result[0][5]
            REGIONAL = result[0][6]
            ATIVIDADE = ATIVIDADE.replace(';', '.')
            #ETAPA = result[0][7]
        if UC!=UC_ANT:
            spamwriter = csv.writer(csvfile, delimiter=';',quotechar=';', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([UC,'CORRENTE',Falta_II[jj],Data_Falta_II[jj],NOME_CLIENTE,ATIVIDADE,SITUACAO,DATA_SITUACAO,LOCALIDADE,REGIONAL])       
        UC_ANT=UC
        jj=jj+1

    
quest = sys.stdin.readline()


connection.close()


