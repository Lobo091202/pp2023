from tkinter import *
import os


def findButton():
    print("findButton")
    
    def backButtonFile():
        profileGuest.destroy()
        print("backButtonFile")
        
    def addAndWithButton():
        print("addAndWithButton")
        
        def addMoneyButton():
            addOrWithdraw.destroy()
            print("addMoneyButton")
            
        def withDrawButton():
            addOrWithdraw.destroy()
            print("withDrawButton")
            
        def backAddButton():
            addOrWithdraw.destroy()
            print("backAddButton")

        addOrWithdraw = Toplevel()

        addOrWithdraw.geometry("430x932")
        addOrWithdraw.title("Add And Withdraw")
        addOrWithdraw.configure(bg = "#ffffff")
        canvas = Canvas(
            addOrWithdraw,
            bg = "#ffffff",
            height = 932,
            width = 430,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background1.png")
        background = canvas.create_image(
            215.0, 466.0,
            image=background_img)


        canvas.create_rectangle(
            23, 142, 23+386, 142+84,
            fill = "#ffffff",
            outline = "#36b1d2")

        canvas.create_text(
            101.0, 183.5,
            text = "Balance",
            fill = "#206fa5",
            font = ("None", int(24.0)))

        canvas.create_text(
            342.0, 183.5,
            text = "9600",
            fill = "#206fa5",
            font = ("None", int(28.0)))


        canvas.create_rectangle(
            23, 251, 23+386, 251+223,
            fill = "#ffffff",
            outline = "#36b1d2")


        canvas.create_rectangle(
            23, 507, 23+386, 507+223,
            fill = "#ffffff",
            outline = "#36b1d2")

        imgAddMoney = PhotoImage(file = f"imgaddmoney.png")
        bAddMoney = Button(
            addOrWithdraw,
            image = imgAddMoney,
            borderwidth = 0,
            highlightthickness = 0,
            command = addMoneyButton,
            relief = "flat")

        bAddMoney.place(
            x = 136, y = 420,
            width = 158,
            height = 42)

        imgWithdraw = PhotoImage(file = f"imgwith.png")
        bWithdraw = Button(
            addOrWithdraw,
            image = imgWithdraw,
            borderwidth = 0,
            highlightthickness = 0,
            command = withDrawButton,
            relief = "flat")

        bWithdraw.place(
            x = 136, y = 676,
            width = 158,
            height = 42)

        canvas.create_text(
            83.5, 316.0,
            text = "Amount",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        canvas.create_text(
            83.5, 572.0,
            text = "Amount",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        canvas.create_text(
            215.0, 277.0,
            text = "Add money",
            fill = "#206fa5",
            font = ("None", int(20.0)))

        canvas.create_text(
            216.0, 533.0,
            text = "Withdraw",
            fill = "#206fa5",
            font = ("None", int(20.0)))

        addMoney_img = PhotoImage(file = f"img_textBoxAdd.png")
        addMoney_bg = canvas.create_image(
            215.5, 368.5,
            image = addMoney_img)

        addMoneyAdd = Entry(
            addOrWithdraw,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        addMoneyAdd.place(
            x = 52.0, y = 339,
            width = 327.0,
            height = 61)

        withDraw_img = PhotoImage(file = f"img_textBoxWithdraw.png")
        withDraw_bg = canvas.create_image(
            215.5, 624.5,
            image = withDraw_img)

        withDraw = Entry(
            addOrWithdraw,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        withDraw.place(
            x = 52.0, y = 595,
            width = 327.0,
            height = 61)

        imgBackAdd = PhotoImage(file = f"imgbackback.png")
        bBackAdd = Button(
            addOrWithdraw,
            image = imgBackAdd,
            borderwidth = 0,
            highlightthickness = 0,
            command = backAddButton,
            relief = "flat")

        bBackAdd.place(
            x = 28, y = 55,
            width = 14,
            height = 26)

        addOrWithdraw.resizable(False, False)
        addOrWithdraw.mainloop()
        
    def editClientButton():
        print("editClientButton")
        
        def saveButtonEdit():
            editAcount.destroy()
            print("saveButtonEdit")
        def backButtonEdit():
            editAcount.destroy()
            print("backButtonEdit")


        editAcount = Toplevel()

        editAcount.geometry("430x932")
        editAcount.configure(bg = "#ffffff")
        editAcount.title("Edit Client Information")
        canvas = Canvas(
            editAcount,
            bg = "#ffffff",
            height = 932,
            width = 430,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        background1 = os.path.join(os.path.dirname(__file__), "background1.png"  )
        backgroundEdit_img = PhotoImage(file =background1)
        backgroundEdit = canvas.create_image(
            215.0, 466.0,
            image=backgroundEdit_img)

        canvas.create_rectangle(
            22, 93, 22+386, 93+772,
            fill = "#ffffff",
            outline = "#36b1d2")

        canvas.create_text(
            214.0, 130.5,
            text = "Edit client information",
            fill = "#206fa5",
            font = ("Arial", int(22.0)))


        fullNameEdit = canvas.create_text(
            96.5, 182.0,
            text = "Full name",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        img_textBox2 = os.path.join(os.path.dirname(__file__), "img_textBox2.png"  )
        fullNameEdit_img = PhotoImage(file = img_textBox2)
        fullNameEdit_bg = canvas.create_image(
            215.5, 234.5,
            image = fullNameEdit_img)

        fullNameEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        fullNameEdit.place(
            x = 52.0, y = 205,
            width = 327.0,
            height = 61)

        gmailtxt = canvas.create_text(
            72.5, 287.0,
            text = "Gmail",
            fill = "#206fa5",
            font = ("None", int(18.0)))
        img_textBox3 = os.path.join(os.path.dirname(__file__), "img_textBox3.png"  )
        gmailEdit_img = PhotoImage(file = img_textBox3)
        gmailEdit_bg = canvas.create_image(
            215.5, 339.5,
            image = gmailEdit_img)

        gmailEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        gmailEdit.place(
            x = 52.0, y = 310,
            width = 327.0,
            height = 61)

        passEdittxt = canvas.create_text(
            96.5, 392.0,
            text = "Password",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        canvas.create_text(
            228.5, 392.5,
            text = "(Less than 18 characters)",
            fill = "#206fa5",
            font = ("None", int(10.0)))

        img_textBox4 = os.path.join(os.path.dirname(__file__), "img_textBox4.png"  )
        passEdit_img = PhotoImage(file = img_textBox4)
        passEdit_bg = canvas.create_image(
            215.5, 444.5,
            image = passEdit_img)

        passEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        passEdit.place(
            x = 52.0, y = 415,
            width = 327.0,
            height = 61)

        canvas.create_text(
            90.0, 497.0,
            text = "Address",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        img_textBox5 = os.path.join(os.path.dirname(__file__), "img_textBox5.png"  )
        addressEdit_img = PhotoImage(file = img_textBox5)
        addressEdit_bg = canvas.create_image(
            215.5, 549.5,
            image = addressEdit_img)

        addressEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        addressEdit.place(
            x = 52.0, y = 520,
            width = 327.0,
            height = 61)


        canvas.create_text(
            68.0, 602.0,
            text = "Age",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        canvas.create_text(
            220.0, 602.0,
            text = "Gender",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        img_textBox6 = os.path.join(os.path.dirname(__file__), "img_textBox6.png"  )
        phoneNumEdit_img = PhotoImage(file = img_textBox6)
        phoneNumEdit_bg = canvas.create_image(
            215.5, 759.5,
            image = phoneNumEdit_img)

        phoneNumEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        phoneNumEdit.place(
            x = 52.0, y = 730,
            width = 327.0,
            height = 61)

        img_textBox7 = os.path.join(os.path.dirname(__file__), "img_textBox7.png"  )
        ageEdit_img = PhotoImage(file =img_textBox7)
        ageEdit_bg = canvas.create_image(
            96.5, 654.5,
            image = ageEdit_img)

        ageEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        ageEdit.place(
            x = 52.0, y = 625,
            width = 89.0,
            height = 61)


        canvas.create_text(
            124.5, 707.0,
            text = "Phone number",
            fill = "#206fa5",
            font = ("None", int(18.0)))

        img_textBox8 = os.path.join(os.path.dirname(__file__), "img_textBox8.png"  )
        genderEdit_img = PhotoImage(file = img_textBox8)
        genderEdit_bg = canvas.create_image(
            282.5, 654.5,
            image = genderEdit_img)

        genderEdit = Entry(editAcount,
            font=("Arial", int(16.0)),
            fg = "#206fa5",
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        genderEdit.place(
            x = 186.0, y = 625,
            width = 193.0,
            height = 61)


        saveimg = os.path.join(os.path.dirname(__file__), "savebutton.png"  )
        imgSaveButton = PhotoImage(file = saveimg)
        bSaveButton = Button(
            editAcount,
            image = imgSaveButton,
            borderwidth = 0,
            highlightthickness = 0,
            command = saveButtonEdit,
            relief = "flat")

        bSaveButton.place(
            
            x = 136, y = 806,
            width = 158,
            height = 42)

        backim = os.path.join(os.path.dirname(__file__), "backim.png"  )
        imgbackEdit = PhotoImage(file = f"backim.png")
        bbackEdit = Button(
            editAcount,
            image = imgbackEdit,
            borderwidth = 0,
            highlightthickness = 0,
            command = backButtonEdit,
            relief = "flat")

        bbackEdit.place(
            x = 28, y = 55,
            width = 14,
            height = 26)
            
        editAcount.resizable(False, False)
        editAcount.mainloop()

    global background3
    global addAndWithim
    global editCliIm
    profileGuest = Toplevel()

    profileGuest.geometry("430x932")
    profileGuest.title("Profile Customer")
    profileGuest.configure(bg = "#ffffff")
    canvas = Canvas(
        profileGuest,
        bg = "#ffffff",
        height = 932,
        width = 430,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background3 = os.path.join(os.path.dirname(__file__), "background3.png"  )
    backgroundGuest_img = PhotoImage(file = background3)
    backgroundGuest = canvas.create_image(
        215.0, 466.0,
        image=backgroundGuest_img)


    canvas.create_rectangle(
        23, 103, 23+386, 103+106,
        fill = "#ffffff",
        outline = "#36b1d2")

    canvas.create_text(
        82.0, 129.5,
        text = "Client",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    guestNameFile = canvas.create_text(
        170.5, 173.5,
        text = "Nguyen Hong Minh",
        fill = "#206fa5",
        font = ("None", int(22.0)))


    canvas.create_rectangle(
        23, 228, 23+130, 228+70,
        fill = "#ffffff",
        outline = "#36b1d2")


    canvas.create_rectangle(
        171, 228, 171+238, 228+70,
        fill = "#ffffff",
        outline = "#36b1d2")

    canvas.create_text(
        72.0, 258.5,
        text = "Age:",
        fill = "#206fa5",
        font = ("None", int(22.0)))

    ageGuestFile = canvas.create_text(
        120.0, 259.5,
        text = "21",
        fill = "#206fa5",
        font = ("None", int(22.0)))

    canvas.create_text(
        244.0, 259.5,
        text = "Gender:",
        fill = "#206fa5",
        font = ("None", int(22.0)))

    genderGuestFile = canvas.create_text(
        354.5, 259.5,
        text = "Male",
        fill = "#206fa5",
        font = ("None", int(22.0)))

    addAndWithim = os.path.join(os.path.dirname(__file__), "addAndWith.png"  )
    imgaddAndWith = PhotoImage(file = addAndWithim)
    baddAndWith = Button(
        profileGuest,
        image = imgaddAndWith,
        borderwidth = 0,
        highlightthickness = 0,
        command = addAndWithButton,
        relief = "flat")

    baddAndWith.place(
        x = 23, y = 573,
        width = 385,
        height = 67)

    editCliIm = os.path.join(os.path.dirname(__file__), "editClient.png"  )
    imgeditCli = PhotoImage(file = editCliIm)
    beditClient = Button(
        profileGuest,
        image = imgeditCli,
        borderwidth = 0,
        highlightthickness = 0,
        command = editClientButton,
        relief = "flat")

    beditClient.place(
        x = 71, y = 660,
        width = 288,
        height = 42)


    canvas.create_rectangle(
        23, 317, 23+386, 317+224,
        fill = "#ffffff",
        outline = "#36b1d2")

    canvas.create_text(
        207.0, 340.5,
        text = "Client information",
        fill = "#206fa5",
        font = ("None", int(18.0)))


    canvas.create_rectangle(
        23, 374, 23+386, 374+70,
        fill = "#ffffff",
        outline = "#36b1d2")


    canvas.create_rectangle(
        23, 444, 23+386, 446+70,
        fill = "#ffffff",
        outline = "#36b1d2")

    canvas.create_text(
        133.0, 391.5,
        text = "Account number",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    acountNumFile = canvas.create_text(
        120.5, 424.5,
        text = "4702 3671",
        fill = "#206fa5",
        font = ("None", int(24.0)))

    canvas.create_text(
        86.0, 463.5,
        text = "Balance",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    amountMoneyFile = canvas.create_text(
        78.5, 496.5,
        text = "9600",
        fill = "#206fa5",
        font = ("None", int(24.0)))
    
    backim = os.path.join(os.path.dirname(__file__), "backim.png"  )
    imgbackFile = PhotoImage(file = f"backim.png")
    bbackFile = Button(
        profileGuest,
        image = imgbackFile,
        borderwidth = 0,
        highlightthickness = 0,
        command = backButtonFile,
        relief = "flat")

    bbackFile.place(
        x = 28, y = 55,
        width = 14,
        height = 26)

    profileGuest.resizable(False, False)
    profileGuest.mainloop()
    
    
def createButtonLogin():
    print("createButtonLogin")
    def createButton():
        register.destroy()
        print("createButton")
    def backButton():
        register.destroy()
        print("backButton")


    register = Toplevel()

    register.geometry("430x932")
    register.configure(bg = "#ffffff")
    register.title("New Client Register")
    canvas = Canvas(
        register,
        bg = "#ffffff",
        height = 932,
        width = 430,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    background1 = os.path.join(os.path.dirname(__file__), "background1.png"  )
    backgroundReg_img = PhotoImage(file =background1)
    backgroundReg = canvas.create_image(
        215.0, 466.0,
        image=backgroundReg_img)

    canvas.create_rectangle(
        22, 93, 22+386, 93+772,
        fill = "#ffffff",
        outline = "#36b1d2")

    canvas.create_text(
        214.0, 130.5,
        text = "Register new client",
        fill = "#206fa5",
        font = ("Arial", int(22.0)))


    fullNameReg = canvas.create_text(
        96.5, 182.0,
        text = "Full name",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox2 = os.path.join(os.path.dirname(__file__), "img_textBox2.png"  )
    fullName_img = PhotoImage(file = img_textBox2)
    fullName_bg = canvas.create_image(
        215.5, 234.5,
        image = fullName_img)

    fullName = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    fullName.place(
        x = 52.0, y = 205,
        width = 327.0,
        height = 61)

    gmailLog = canvas.create_text(
        72.5, 287.0,
        text = "Gmail",
        fill = "#206fa5",
        font = ("None", int(18.0)))
    img_textBox3 = os.path.join(os.path.dirname(__file__), "img_textBox3.png"  )
    gmail_img = PhotoImage(file = img_textBox3)
    gmail_bg = canvas.create_image(
        215.5, 339.5,
        image = gmail_img)

    gmail = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    gmail.place(
        x = 52.0, y = 310,
        width = 327.0,
        height = 61)

    passRegister = canvas.create_text(
        96.5, 392.0,
        text = "Password",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    canvas.create_text(
        228.5, 392.5,
        text = "(Less than 18 characters)",
        fill = "#206fa5",
        font = ("None", int(10.0)))

    img_textBox4 = os.path.join(os.path.dirname(__file__), "img_textBox4.png"  )
    passReg_img = PhotoImage(file = img_textBox4)
    passReg_bg = canvas.create_image(
        215.5, 444.5,
        image = passReg_img)

    passReg = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    passReg.place(
        x = 52.0, y = 415,
        width = 327.0,
        height = 61)

    canvas.create_text(
        90.0, 497.0,
        text = "Address",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox5 = os.path.join(os.path.dirname(__file__), "img_textBox5.png"  )
    address_img = PhotoImage(file = img_textBox5)
    address_bg = canvas.create_image(
        215.5, 549.5,
        image = address_img)

    address = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    address.place(
        x = 52.0, y = 520,
        width = 327.0,
        height = 61)


    canvas.create_text(
        68.0, 602.0,
        text = "Age",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    canvas.create_text(
        220.0, 602.0,
        text = "Gender",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox6 = os.path.join(os.path.dirname(__file__), "img_textBox6.png"  )
    phoneNum_img = PhotoImage(file = img_textBox6)
    phoneNum_bg = canvas.create_image(
        215.5, 759.5,
        image = phoneNum_img)

    phoneNum = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    phoneNum.place(
        x = 52.0, y = 730,
        width = 327.0,
        height = 61)

    img_textBox7 = os.path.join(os.path.dirname(__file__), "img_textBox7.png"  )
    age_img = PhotoImage(file =img_textBox7)
    age_bg = canvas.create_image(
        96.5, 654.5,
        image = age_img)

    age = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    age.place(
        x = 52.0, y = 625,
        width = 89.0,
        height = 61)


    canvas.create_text(
        124.5, 707.0,
        text = "Phone number",
        fill = "#206fa5",
        font = ("None", int(18.0)))

    img_textBox8 = os.path.join(os.path.dirname(__file__), "img_textBox8.png"  )
    gender_img = PhotoImage(file = img_textBox8)
    gender_bg = canvas.create_image(
        282.5, 654.5,
        image = gender_img)

    gender = Entry(register,
        font=("Arial", int(16.0)),
        fg = "#206fa5",
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    gender.place(
        x = 186.0, y = 625,
        width = 193.0,
        height = 61)


    createim = os.path.join(os.path.dirname(__file__), "createim.png"  )
    imgcreateReg = PhotoImage(file = createim)
    bcreateReg = Button(
        register,
        image = imgcreateReg,
        borderwidth = 0,
        highlightthickness = 0,
        command = createButton,
        relief = "flat")

    bcreateReg.place(
        
        x = 136, y = 806,
        width = 158,
        height = 42)

    backim = os.path.join(os.path.dirname(__file__), "backim.png"  )
    imgbackReg = PhotoImage(file = f"backim.png")
    bbackReg = Button(
        register,
        image = imgbackReg,
        borderwidth = 0,
        highlightthickness = 0,
        command = backButton,
        relief = "flat")

    bbackReg.place(
        x = 28, y = 55,
        width = 14,
        height = 26)
        
    register.resizable(False, False)
    register.mainloop()

login = Tk()

login.geometry("430x932")
login.title("Bank Manager Login")
login.configure(bg = "#ffffff")
canvas = Canvas(
    login,
    bg = "#ffffff",
    height = 932,
    width = 430,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

BackgroundFile = os.path.join(os.path.dirname(__file__), "background.png"  )
backgroundLogin_img = PhotoImage(file = BackgroundFile)
backgroundLogin = canvas.create_image(
    215.0, 466.0,
    image=backgroundLogin_img)

title = canvas.create_text(
    214.5, 109.5,
    text = "Banking Information\nManagement System",
    fill = "#105c90",
    font = ("Arial", int(24.0)))

canvas.create_text(
    215.0, 624.5,
    text = "or",
    fill = "#ffffff",
    font = ("Arial", int(24.0)))


canvas.create_rectangle(
    22, 183, 22+386, 183+393,
    fill = "#ffffff",
    outline = "#36b1d2")


access = canvas.create_text(
    214.5, 221.5,
    text = "Access Client Information",
    fill = "#206fa5",
    font = ("Arial", int(20.0)))


askName = canvas.create_text(
    72.5, 264.0,
    text = "Name",
    fill = "#206fa5",
    font = ("Arial", int(18.0)))

img_textBox0 = os.path.join(os.path.dirname(__file__), "img_textBox0.png"  )
nameGuest_img = PhotoImage(file = img_textBox0)
nameGuest_bg = canvas.create_image(
    214.5, 324.0,
    image = nameGuest_img)

nameGuest = Entry(
    font=("Arial", int(16.0)),
    fg = "#206fa5",
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

nameGuest.place(
    x = 51.0, y = 291,
    width = 327.0,
    height = 66)

askPhone = canvas.create_text(
    118.5, 394.0,
    text = "Phone number",
    fill = "#206fa5",
    font = ("Arial", int(18.0)))

img_textBox1 = os.path.join(os.path.dirname(__file__), "img_textBox1.png"  )
phoneGuest_img = PhotoImage(file = img_textBox1)
phoneGuest_bg = canvas.create_image(
    214.5, 453.5,
    image = phoneGuest_img)

phoneGuest = Entry(
    font=("Arial", int(16.0)),
    fg = "#206fa5",
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

phoneGuest.place(
    x = 51.0, y = 422,
    width = 327.0,
    height = 65)

img0 = os.path.join(os.path.dirname(__file__), "img0.png"  )
imgFind = PhotoImage(file = img0)
bFind = Button(
    image = imgFind,
    borderwidth = 0,
    highlightthickness = 0,
    command = findButton,
    relief = "flat")

bFind.place(
    x = 131, y = 510,
    width = 168,
    height = 56)

img1 = os.path.join(os.path.dirname(__file__), "img1.png"  )
imgCreate = PhotoImage(file = img1)
bCreate = Button(
    image = imgCreate,
    borderwidth = 0,
    highlightthickness = 0,
    command = createButtonLogin,
    relief = "flat")

bCreate.place(
    x = 135, y = 662,
    width = 158,
    height = 42)

login.resizable(False, False)
login.mainloop()
