# from selenium import webdriver #CRIAR O NAVEGADOR
# from webdriver_manager.chrome import ChromeDriverManager #BAIXAR O MOTOR DO NAVEGADOR CHROME
# from selenium.webdriver.common.by import By #FORMA ATUALIZADA DE INFORMAR O TIPO DE BUSCA DE ELEMENTO
# from selenium.webdriver.chrome.options import Options #CRIAR REGRA PARA NÃO FECHAR O NAVEGADOR AUTOMÁTICO
# from selenium.webdriver.chrome.service import Service #CRIAR O SERVIÇO DE FAZER O DOWNLOAD DO MOTOR MAIS ATUALIZADO
# from selenium.webdriver.common.action_chains import ActionChains #CRIAR A CORRENTE DE AÇÕES
# from selenium.webdriver.support.select import Select #CONTROLADOR DE SELECT
# from datetime import datetime, timedelta #CONTROLE DE DATA
# import time #CONTROLE DE TEMPO (PARA FAZER PAUSAS)
# from selenium.webdriver.support.ui import WebDriverWait #CONTROLADOR DE ESPERA
# from selenium.webdriver.support import expected_conditions as EC #CODIÇÕES DE ESPERA

# #OPTIONS
# opcoes = Options() #INSTÂNCIA DO OBJETO OPTIONS
# opcoes.add_experimental_option("detach", True) #CHAMA O METODO PARA ADICIONAR UMA OPÇÃO, QUE É NÃO FECHAR AO FIM DA EXECUÇÃO

# #SERVICE
# servico = Service(ChromeDriverManager().install()) #FAZ O DOWNLOAD AUTOMÁTICO DO MOTOR MAIS ATUALIZADO DO CHROME

# #NAVEGADOR
# navegador = webdriver.Chrome(service=servico, options=opcoes) #CRIA UM NAVEGADOR USANDO AS OPÇÕES E SERVIÇO PRÉ-DEFINIDOS ANTERIORMENTE
# navegador.maximize_window() #MAXIMIZA A TELA, DEIXANDO EM TELA CHEIA
# navegador.get("https://infinityschool.com.br/") #FAZ O NAVEGADOR ENTRAR NA URL INDICADA

# botao_cursos = navegador.find_element(By.XPATH, '//*[@id="jet-menu-item-7748"]/a') #BUSCA O ELEMENTO DE CURSOS

# #CORRENTE DE AÇÕES
# acao = ActionChains(navegador) #INSTâNCIA DO OBJETO ACTIONCHAINS USANDO O NAVEGADOR DE PARAMETRO
# acao.move_to_element(botao_cursos) #EXECUTA A FUNÇÃO DE MOVER A SETA DO MOUSE PARA CIMA DO ELEMENTO
# acao.perform() #PERFORM GARANTE QUE OS COMANDOS SERÃO EXECUTADOS EM ORDEM

# #ESPERA ATÉ O COMPONENTE RENDERIZAR NA TELA
# wait = WebDriverWait(navegador, 10) #INSTÂNCIA DO OBJETO WebDriverWait, RECEBENDO O NAVEGADOR E O TEMPO DE ESPERA MÁXIMA COMO PARÂMETRO
# #OBS: NÃO É QUE ELE VAI ESPERAR 10 SEGUNDOS, E SIM ATÉ 10 SEGUNDOS, OU SEJA PODE ENCERRAR ANTES A ESPERA SE A CONDIÇÃO FOR OBEDECIDA.
# full_stack = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jet-menu-item-7748"]/div/div/div/div/section/div/div/div[8]/div/div/div[2]/div/div/a'))) #BUSCA O ELEMENTO MAS COM UMA CONDIÇÃO, QUE É QUANDO ESSE ELEMENTO FICAR VISÍVEL, OU SEJA, SÓ VAI BUSCAR O FULL_STACK QUANDO ELE APARECER NA TELA!
# full_stack.click() #CLICA NO ELEMENTO

# botao_contato = navegador.find_element(By.XPATH, '//*[@id="entreContatoCurso"]') #BUSCA O BOTÃO CONTATO
# botao_contato.click() #CLICA NESSE ELEMENTO

# #GERENCIAMENTO DE ABAS
# abas = navegador.window_handles #VARIÁVEL QUE ARMAZENA UMA LISTA COM TODAS AS ABAS
# navegador.switch_to.window(abas[-1]) #NAVEGADOR MUDA PARA A ULTIMA ABA ABERTA

# #PREENCHIMENTO DO FORMULÁRIO
# time.sleep(1) #AGUARDA 1 SEGUNDO
# nome = navegador.find_element(By.XPATH, '//*[@id="geral_home6"]/form/div[1]/input') #BUSCA O INPUT NOME
# nome.send_keys("Testando") #DIGITA O TEXTO INDICADO NO INPUT

# time.sleep(1) #AGUARDA 1 SEGUNDO
# telefone = navegador.find_element("xpath", '//*[@id="geral_home6"]/form/input') #BUSCA O INPUT TELEFONE
# telefone.send_keys("85999999999") #DIGITA O TEXTO INDICADO NO INPUT

# time.sleep(1) #AGUARDA 1 SEGUNDO
# select_unidades = navegador.find_element(By.XPATH, '//*[@id="geral_home6"]/form/center[3]/select[1]') #BUSCA O MENU SUSPENSO DE UNIDADES
# select = Select(select_unidades) #INSTÂCIA DO OBJETO SELECT PASSANDO O MENU SUSPENSO DE UNIDADES
# select.select_by_visible_text("fortaleza") #SELECIONA A OPTION QUE TIVER O TEXTO 'fortaleza'

# time.sleep(1) #AGUARDA 1 SEGUNDO
# select_cursos = navegador.find_element("xpath", '//*[@id="geral_home6"]/form/center[3]/select[2]') #BUSCA O MENU SUSPENSO DE UNIDADES
# select = Select(select_cursos) #INSTÂCIA DO OBJETO SELECT PASSANDO O MENU SUSPENSO DE CURSOS
# select.select_by_visible_text("Programação Full Stack") #SELECIONA A OPTION QUE TIVER O TEXTO 'Programação Full Stack'

# #GERANDO DATA DE AMANHÃ
# data_de_hoje = datetime.now() #BUSCA A DATA DE HOJE
# data_de_amanha = data_de_hoje + timedelta(days=1) #FAZ A DATA DE AMANHÃ
# data_formatada = data_de_amanha.strftime("%d/%m/%Y") #FORMATA PARA UMA STRING DO BRASIL

# time.sleep(1) #AGUARDA 1 SEGUNDO
# data = navegador.find_element("xpath", '//*[@id="geral_home6"]/form/div[2]/input') #BUSCA O INPUT DE DATA
# data.send_keys(data_formatada) #E PREENCHE ELE COM A DATA DE AMANHÃ JÁ FORMATADA

# botao_enviar = navegador.find_element(By.XPATH, '//*[@id="geral_home6"]/form/center[6]/button') #BUSCA O BOTÃO DE ENVIAR
# botao_enviar.click() #CLICA NO BOTÃO

# navegador.quit() #FECHA O NAVEGADOR


# #EXEMPLO DE IMPORTAÇÕES CASO VÁ USAR O FIREFOX
# # from webdriver_manager.firefox import GeckoDriverManager #BAIXAR O MOTOR DO NAVEGADOR FIREFOX
# # servico = Service(GeckoDriverManager().install())  #FAZ O DOWNLOAD AUTOMÁTICO DO MOTOR MAIS ATUALIZADO DO CHROME
# # navegador = webdriver.Firefox(service=servico) #NO FIREFOX NÃO PRECISA DO OPTIONS POIS ELE NÃO FECHA SOZINHO





















from selenium import webdriver #CRIAR O NAVEGADOR
from selenium.webdriver.common.by import By #FORMA ATUALIZADA DE INFORMAR O TIPO DE BUSCA DE ELEMENTO
from selenium.webdriver.chrome.options import Options #CRIAR REGRA PARA NÃO FECHAR O NAVEGADOR AUTOMÁTICO
from selenium.webdriver.chrome.service import Service #CRIAR O SERVIÇO DE FAZER O DOWNLOAD DO MOTOR MAIS ATUALIZADO
from selenium.webdriver.common.action_chains import ActionChains #CRIAR A CORRENTE DE AÇÕES
from selenium.webdriver.support.select import Select #CONTROLADOR DE SELECT
from datetime import datetime, timedelta #CONTROLE DE DATA
import time #CONTROLE DE TEMPO (PARA FAZER PAUSAS)
from selenium.webdriver.support.ui import WebDriverWait #CONTROLADOR DE ESPERA
from selenium.webdriver.support import expected_conditions as EC #CODIÇÕES DE ESPERA

#OPTIONS
opcoes = Options() #INSTÂNCIA DO OBJETO OPTIONS
opcoes.add_experimental_option("detach", True) #CHAMA O METODO PARA ADICIONAR UMA OPÇÃO, QUE É NÃO FECHAR AO FIM DA EXECUÇÃO


#NAVEGADOR
navegador = webdriver.Chrome(options=opcoes) #CRIA UM NAVEGADOR USANDO AS OPÇÕES E SERVIÇO PRÉ-DEFINIDOS ANTERIORMENTE
navegador.maximize_window() #MAXIMIZA A TELA, DEIXANDO EM TELA CHEIA
navegador.get("https://infinityschool.com.br/") #FAZ O NAVEGADOR ENTRAR NA URL INDICADA

botao_cursos = navegador.find_element(By.XPATH, '//*[@id="jet-menu-item-7748"]/a') #BUSCA O ELEMENTO DE CURSOS

#CORRENTE DE AÇÕES
acao = ActionChains(navegador) #INSTâNCIA DO OBJETO ACTIONCHAINS USANDO O NAVEGADOR DE PARAMETRO
acao.move_to_element(botao_cursos) #EXECUTA A FUNÇÃO DE MOVER A SETA DO MOUSE PARA CIMA DO ELEMENTO
acao.perform() #PERFORM GARANTE QUE OS COMANDOS SERÃO EXECUTADOS EM ORDEM

#ESPERA ATÉ O COMPONENTE RENDERIZAR NA TELA
wait = WebDriverWait(navegador, 10) #INSTÂNCIA DO OBJETO WebDriverWait, RECEBENDO O NAVEGADOR E O TEMPO DE ESPERA MÁXIMA COMO PARÂMETRO
#OBS: NÃO É QUE ELE VAI ESPERAR 10 SEGUNDOS, E SIM ATÉ 10 SEGUNDOS, OU SEJA PODE ENCERRAR ANTES A ESPERA SE A CONDIÇÃO FOR OBEDECIDA.
full_stack = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="jet-menu-item-7748"]/div/div/div/div/section/div/div/div[1]/div/div/div[3]/div/div/a'))) #BUSCA O ELEMENTO MAS COM UMA CONDIÇÃO, QUE É QUANDO ESSE ELEMENTO FICAR VISÍVEL, OU SEJA, SÓ VAI BUSCAR O FULL_STACK QUANDO ELE APARECER NA TELA!
full_stack.click() #CLICA NO ELEMENTO

botao_contato = navegador.find_element(By.XPATH, '//*[@id="entreContatoCurso"]') #BUSCA O BOTÃO CONTATO
botao_contato.click() #CLICA NESSE ELEMENTO

#GERENCIAMENTO DE ABAS
abas = navegador.window_handles #VARIÁVEL QUE ARMAZENA UMA LISTA COM TODAS AS ABAS
navegador.switch_to.window(abas[-1]) #NAVEGADOR MUDA PARA A ULTIMA ABA ABERTA

#PREENCHIMENTO DO FORMULÁRIO
time.sleep(1) #AGUARDA 1 SEGUNDO
nome = navegador.find_element(By.XPATH, '//*[@id="geral_home"]/form/input[1]') #BUSCA O INPUT NOME
nome.send_keys("Testando") #DIGITA O TEXTO INDICADO NO INPUT

time.sleep(1) #AGUARDA 1 SEGUNDO
telefone = navegador.find_element("xpath", '//*[@id="geral_home"]/form/input[2]') #BUSCA O INPUT TELEFONE
telefone.send_keys("85999999999") #DIGITA O TEXTO INDICADO NO INPUT

time.sleep(1) #AGUARDA 1 SEGUNDO
select_unidades = navegador.find_element(By.XPATH, '//*[@id="geral_home"]/form/select[1]') #BUSCA O MENU SUSPENSO DE UNIDADES
select = Select(select_unidades) #INSTÂCIA DO OBJETO SELECT PASSANDO O MENU SUSPENSO DE UNIDADES
select.select_by_visible_text("Fortaleza") #SELECIONA A OPTION QUE TIVER O TEXTO 'fortaleza'

time.sleep(1) #AGUARDA 1 SEGUNDO
select_cursos = navegador.find_element("xpath", '//*[@id="geral_home"]/form/select[2]') #BUSCA O MENU SUSPENSO DE UNIDADES
select = Select(select_cursos) #INSTÂCIA DO OBJETO SELECT PASSANDO O MENU SUSPENSO DE CURSOS
select.select_by_visible_text("Programação Full Stack") #SELECIONA A OPTION QUE TIVER O TEXTO 'Programação Full Stack'

#GERANDO DATA DE AMANHÃ
data_de_hoje = datetime.now() #BUSCA A DATA DE HOJE
data_de_amanha = data_de_hoje + timedelta(days=1) #FAZ A DATA DE AMANHÃ
data_formatada = data_de_amanha.strftime("%d/%m/%Y") #FORMATA PARA UMA STRING DO BRASIL

time.sleep(1) #AGUARDA 1 SEGUNDO
data = navegador.find_element("xpath", '//*[@id="geral_home"]/form/input[3]') #BUSCA O INPUT DE DATA
data.send_keys(data_formatada) #E PREENCHE ELE COM A DATA DE AMANHÃ JÁ FORMATADA

botao_enviar = navegador.find_element(By.XPATH, '//*[@id="geral_home"]/form/button') #BUSCA O BOTÃO DE ENVIAR
botao_enviar.click() #CLICA NO BOTÃO

navegador.quit() #FECHA O NAVEGADOR


#EXEMPLO DE IMPORTAÇÕES CASO VÁ USAR O FIREFOX
# from webdriver_manager.firefox import GeckoDriverManager #BAIXAR O MOTOR DO NAVEGADOR FIREFOX
# servico = Service(GeckoDriverManager().install())  #FAZ O DOWNLOAD AUTOMÁTICO DO MOTOR MAIS ATUALIZADO DO CHROME
# navegador = webdriver.Firefox(service=servico) #NO FIREFOX NÃO PRECISA DO OPTIONS POIS ELE NÃO FECHA SOZINHO
