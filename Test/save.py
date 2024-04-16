    esfera = ctk.CTkCanvas(master, width=200, height= 200, bg="#464646", highlightbackground="#464646", highlightcolor="#464646")
    esfera.create_aa_circle(fill='#D9D9D9',x_pos=100,y_pos=100,radius=95)
    esfera.pack(pady=10)

    for c in range (0,5):
        task_button(self)

    ctk.CTkButton(self, hover_color="#A0A0A0" ,text="Sair", height=100, width=100, fg_color='#D9D9D9', text_color="#454545", command= lambda: self.quit()).place(relx= 0.7, rely=0.9, relwidth=0.25, relheight=0.09, anchor='nw')

    self.place(relx = 0.81, rely= 0.025, relheight=0.95, relwidth=0.18, anchor='nw')

        def task_button(master):
            botao_teste = ctk.CTkButton(master,hover_color="#A0A0A0", fg_color="#D9D9D9", width=200, height=70, text='teste', command = lambda: print('Teste'), text_color="#454545")
            botao_teste.pack(pady= 5)

            print('entrou no task button')