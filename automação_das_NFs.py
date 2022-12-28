import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time as time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import *
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

def codigo():

    #Começar a automação com o selenium

    i=0
    atualizadas=0
    notas=num1.get("1.0",END)
    notas=notas.split()
    valores=num2.get("1.0",END)
    valores=valores.split()
    cont=(int(len(notas)))
    cont_total=cont
    mensagem=num3.get("1.0",END)
    copiarlogesen=open("Log&Senha.txt", "r")
    colarlogesen=copiarlogesen.read()
    listarlogse=colarlogesen.split()

    #Abrir o site

    driver=webdriver.Chrome()
    driver.get("******************")
    driver.maximize_window()

    time.sleep(1)

    #Logar no site

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
   
    time.sleep(3)

    login=driver.find_element_by_xpath('//*[@id="username"]')
    login.send_keys(listarlogse[0])

    senha=driver.find_element_by_xpath('//*[@id="password"]')
    senha.send_keys(listarlogse[1])

    logar=driver.find_element_by_xpath('//*[@id="btnLoginId"]')
    logar.click()

    #Abrir local do CSC

    time.sleep(2)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'CSC')))

    time.sleep(1)

    first_element = driver.find_element_by_link_text('CSC')
    hover = ActionChains(driver).move_to_element(first_element)
    hover.perform()

    secound_element=driver.find_element_by_link_text('Contas a receber')
    hover2= ActionChains(driver).move_to_element(secound_element)
    hover2.perform()

    third_element=driver.find_element_by_link_text('Listagem (para CSC)')
    hover3=ActionChains(driver).move_to_element(third_element)
    hover3.perform()
    driver.find_element_by_link_text('Listagem (para CSC)').click()

    #Pesquisar NF's

    time.sleep(2)
    
    while cont>=1:
       
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="carteiraSeguradoraTable:j_idt59:filter"]')))

        time.sleep(1)

        busca=driver.find_element_by_xpath('//*[@id="carteiraSeguradoraTable:j_idt59:filter"]')
        busca.clear()
        busca.send_keys(notas[i])

        time.sleep(2)
        
        busca.send_keys(Keys.ENTER)

        time.sleep(2)
       
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'"+valores[i]+"')]")))

            time.sleep(1)

            driver.find_element_by_xpath("//*[contains(text(),'"+valores[i]+"')]").click()

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="j_idt102:j_idt103:itaStatusCobranca"]')))
            
            time.sleep(3)
        
            driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:itaStatusCobranca"]').send_keys(mensagem)
        
            valorstatus=radioValue.get()
            valordep=depValue.get()
        
            time.sleep(1)
        
            if valorstatus==1:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selStatusCSC"]/tbody/tr/td[1]/div/div[2]/span').click()
            if valorstatus==2:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selStatusCSC"]/tbody/tr/td[2]/div/div[2]/span').click()
            if valorstatus==3:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selStatusCSC"]/tbody/tr/td[3]/div/div[2]/span').click()
            if valorstatus==4:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selStatusCSC"]/tbody/tr/td[4]/div/div[2]/span').click()
            
            time.sleep(1)

            if valordep==1:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selResponsavelCSC:0"]').click()
            if valordep==2:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selResponsavelCSC:1"]').click()
            if valordep==3:
                driver.find_element_by_xpath('//*[@id="j_idt102:j_idt103:selResponsavelCSC:2"]').click()
            
            time.sleep(1)
        
            driver.find_element_by_xpath('//*[@id="j_idt102:saveBtn"]/span').click()

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="verDemaisCamposForm"]/div[1]/a/span')))
        
            time.sleep(2)
        
            driver.find_element_by_xpath('//*[@id="verDemaisCamposForm"]/div[1]/a/span').click()
            print("NF ",notas[i]," atualizada")
            i+=1
            cont-=1
            atualizadas+=1
            
        except:
            print("NF ",notas[i]," não localizada no CAD")
            i+=1
            cont-=1
    
    atualizadas_total="Foram atualizadas %d NF's de %d!"%(atualizadas,cont_total)
    pyautogui.alert(atualizadas_total,title="Processo Finalizado")


#Abrir a Interface gráfica para usuário inserir os inputs

janela = Tk()
janela.title("Automação Cobrança Seguradoras")
janela.geometry("800x500")
janela.configure(background="#dde")
Label(janela,text="Olá! Digite seu login CAD:",background="#dde",foreground="#000",font="arial 15").place(x=250,y=50)
num3 = Text(janela,font="arial 12")
num3.place(x=270,y=90,width=200,height=25)
Label(janela,text="Digite sua senha:",background="#dde",foreground="#000",font="arial 15").place(x=290,y=140)
num4 = Text(janela,font="arial 12")
num4.place(x=270,y=180,width=200,height=25)

def guardar():
    guarlogesen = open("Log&Senha.txt", "w")
    textolog = num3.get("1.0",END)
    textosen = num4.get("1.0",END)
    guarlogesen.write(textolog+textosen)

botaocon=Button(janela,text="Continuar",command=lambda:[guardar(),janela.destroy()]).place(x=320,y=230,width=100,height=25)
Label(janela,text='Ou, continuar como:',background="#dde",foreground="#000",font="arial 10").place(x=550,y=80)
ultimolog=open("Log&Senha.txt", "r")
arqlido=ultimolog.readline()
Label(janela,text=arqlido,backgroun="#dde",foreground="#000",font="arial 10").place(x=570,y=110)
botaocon2=Button(janela,text="Continuar",command=janela.destroy).place(x=560,y=140,width=100,height=25)
janela.mainloop()


janela2 = tk.Tk()
janela2.title("Automação Cobrança Seguradoras")
janela2.geometry("800x500")
janela2.configure(background="#dde")

Label(janela2,text="Defina os status que ficarão as NF's:",background="#dde",foreground="#000").place(x=500,y=10)

radioValue = tk.IntVar()

rdioOne = tk.Radiobutton(janela2, text='Pendente unidade',
                                variable=radioValue, value=1,background="#dde",foreground="#000")
rdioOne.place(x=500,y=30)
rdioTwo = tk.Radiobutton(janela2, text='Pagamento programado',
                                variable=radioValue, value=2,background="#dde",foreground="#000")
rdioTwo.place(x=500,y=50)
rdioThree = tk.Radiobutton(janela2, text='Aguardando retorno seguradora',
                                variable=radioValue, value=3,background="#dde",foreground="#000")
rdioThree.place(x=500,y=70)

rdioFour = tk.Radiobutton(janela2, text='CSC tratar',
                                variable=radioValue, value=4,background="#dde",foreground="#000")
rdioFour.place(x=500,y=90)


Label(janela2,text="Defina o Departamento:",background="#dde",foreground="#000").place(x=500,y=130)

depValue = tk.IntVar()

depOne = tk.Radiobutton(janela2, text='Tele Peças',
                                variable=depValue, value=1,background="#dde",foreground="#000")
depOne.place(x=500,y=150)

depTwo = tk.Radiobutton(janela2, text='Crt',
                                variable=depValue, value=2,background="#dde",foreground="#000")
depTwo.place(x=500,y=170)
depThree = tk.Radiobutton(janela2, text='Unidade',
                                variable=depValue, value=3,background="#dde",foreground="#000")
depThree.place(x=500,y=190)

Label(janela2,text="Insira as NF's que deseja atualizar",background="#dde",foreground="#000",anchor=W).place(x=10,y=10,width=200,height=20)
Label(janela2,text="NF's inseridas:",background="#dde",foreground="#000",anchor=W).place(x=10,y=70,width=200,height=20)

num1 = Text(janela2,font="arial 10")
num1.place(x=10,y=90,width=90,height=200)

Label(janela2,text="Insira os valores das NF's",background="#dde",foreground="#000",anchor=W).place(x=250,y=10,width=200,height=20)
Label(janela2,text="Valores:",background="#dde",foreground="#000",anchor=W).place(x=250,y=70,width=200,height=20)

num2 = Text(janela2,font="arial 10")
num2.place(x=250, y= 90, width=90, height=200)

Label(janela2,text="Insira a mensagem que deseja anexar no CAD para cada uma delas",background="#dde",foreground="#000",anchor=W).place(x=10,y=500,width=500,height=20)
Label(janela2,text="Mensagem:",background="#dde",foreground="#000",anchor=W).place(x=10,y=350,width=500,height=20)

num3 = Text(janela2,font="arial 10")
num3.place(x=10,y=370,width=500,height=80)

Button(janela2,text="Confirmar",command=codigo).place(x=10,y=460,width=70,height=20 )

janela2.mainloop()
