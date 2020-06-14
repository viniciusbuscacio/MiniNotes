"""
MiniNotes - by Vinicius Buscacio
This is a very basic application for a python student
Based in the project of TEJAS - available at some sites like:
https://programtuts.com/notepadusingtkinter/notepadusing_tkinter.php
https://www.trycatchclasses.com/make-notepad-using-tkinter/
"""

# Importing the necessary tkinter module.
from tkinter.filedialog import *
from tkinter.messagebox import *

# Defining Global Variables
mnApplicationName = "MiniNotes"

# Languages available
PORTUGUES = ["Sem título", "Novo", "Abrir", "Salvar", "Sair", "Arquivo", "Cortar", "Copiar", "Colar", "Editar", "Sobre o", "Ajuda"]
ENGLISH = ["Untitled", "New", "Open", "Save", "Exit", "File", "Cut", "Copy", "Paste", "Edit", "About", "Help"]

# Set default language to ENGLISH
LANGUAGE = ENGLISH
LANGUAGE_SELECTION = "ENG"

# Check if the language configuration file exist
configFileExist = os.path.exists('config.txt')

# if the language configuration file exist, read the content
if configFileExist == True:
    with open("config.txt", "r") as myfile:
        data = myfile.read().split('=')
        myfile.close()
        LANGUAGE_SELECTION = (data[1])
        if LANGUAGE_SELECTION == "ENG":
            LANGUAGE = ENGLISH
        elif LANGUAGE_SELECTION == "POR":
            LANGUAGE = PORTUGUES


# Defining the main Class "Mininotes", where the main application will run.
class MiniNotes:
    __root = Tk()
    __mnWindowWidth = 300
    __mnWindowHeight = 300
    __mnTextArea = Text(__root)
    __mnMenuBar = Menu(__root)
    __mnFileMenu = Menu(__mnMenuBar, tearoff=0)
    __mnEditMenu = Menu(__mnMenuBar, tearoff=0)
    __mnLanguageMenu = Menu(__mnMenuBar, tearoff=0)
    __nmHelpMenu = Menu(__mnMenuBar, tearoff=0)
    __mnScrollBar = Scrollbar(__mnTextArea)
    __mnFile = None




    # Defining the application init.
    def __init__(self, **kwargs):

        # Try to load the icon "MiniNote.ico"; if it doesn't exist, it will load the Python icon.
        try:
            self.__root.wm_iconbitmap("MiniNotes.ico")
        except:
            pass

        # Try to calculate the application width.
        try:
            self.__mnWindowWidth = kwargs['width']
        except KeyError:
            pass

        # Try to calculate the application height.
        try:
            self.__mnWindowHeight = kwargs['height']
        except KeyError:
            pass

        # Set the application title.
        self.__root.title(LANGUAGE[0] + " - " + mnApplicationName)

        # In this part, the application will calculate where it should
        # appear on the screen, based on the screen resolution.
        mnScreenWidth = self.__root.winfo_screenwidth()

        mnScreenHeight = self.__root.winfo_screenheight()

        left = (mnScreenWidth / 2) - (self.__mnWindowWidth / 2)

        top = (mnScreenHeight / 2) - (self.__mnWindowHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__mnWindowWidth,
                                              self.__mnWindowHeight,
                                              left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__mnTextArea.grid(sticky=N + E + S + W)

        # Creating the File Menu.
        # option NEW FILE
        self.__mnFileMenu.add_command(label=LANGUAGE[1],
                                      command=self.__mnNewFile)
        # option OPEN FILE
        self.__mnFileMenu.add_command(label=LANGUAGE[2],
                                      command=self.__mnOpenFile)
        # option SAVE FILE
        self.__mnFileMenu.add_command(label=LANGUAGE[3],
                                      command=self.__mnSaveFile)
        # Add a menu separator
        self.__mnFileMenu.add_separator()

        # option to EXIT the application
        self.__mnFileMenu.add_command(label=LANGUAGE[4],
                                      command=self.__mnExit)

        # Create the Menu cascade with options above (__mnFileMenu)
        self.__mnMenuBar.add_cascade(label=LANGUAGE[5],
                                     menu=self.__mnFileMenu)

        # Creating the Edit Menu
        # option CUT
        self.__mnEditMenu.add_command(label=LANGUAGE[6],
                                      command=self.__mnCut)
        # option COPY
        self.__mnEditMenu.add_command(label=LANGUAGE[7],
                                      command=self.__mnCopy)
        # option PASTE
        self.__mnEditMenu.add_command(label=LANGUAGE[8],
                                      command=self.__mnPaste)

        # Create the Menu cascade with options above (_mnEditMenu)
        self.__mnMenuBar.add_cascade(label=LANGUAGE[9],
                                     menu=self.__mnEditMenu)

        # Creating the language menu
        self.__mnLanguageMenu.add_command(label="English",
                                      command=self.__mnSetEnglish)

        self.__mnLanguageMenu.add_command(label="Português",
                                      command=self.__mnSetPortugues)

        self.__mnMenuBar.add_cascade(label="Language",
                                     menu=self.__mnLanguageMenu)

        # Creating the Help Menu
        # option ABOUT
        self.__nmHelpMenu.add_command(label=LANGUAGE[10] + " " + mnApplicationName,
                                      command=self.__mnAbout)

        # Create the Menu cascade with options above (__nmHelpMenu)
        self.__mnMenuBar.add_cascade(label=LANGUAGE[11],
                                     menu=self.__nmHelpMenu)

        # Creating the Main Menu
        self.__root.config(menu=self.__mnMenuBar)

        self.__mnScrollBar.pack(side=RIGHT, fill=Y)

        self.__mnScrollBar.config(command=self.__mnTextArea.yview)

        self.__mnTextArea.config(yscrollcommand=self.__mnScrollBar.set)

    # Creating functions

    # Function to EXIT the application
    def __mnExit(self):
        self.__root.destroy()

    # Function to show the ABOUT window
    def __mnAbout(self):
        showinfo(mnApplicationName, "Vinicius Buscacio - vinicius@buscacio.net")

    # Function to show the OPEN FILE window
    def __mnOpenFile(self):
        self.__mnFile = askopenfilename(defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

        # if there's no file, set the file opened as None
        if self.__mnFile == "":
            self.__mnFile = None

        else:
            # if a file is selected, change the application title to the filename
            self.__root.title(os.path.basename(self.__mnFile) + " - " + mnApplicationName)
            self.__mnTextArea.delete(1.0, END)

            # open the file in the __mnTextArea
            file = open(self.__mnFile, "r")
            self.__mnTextArea.insert(1.0, file.read())
            file.close()

    # Function to create a NEW FILE
    def __mnNewFile(self):
        self.__root.title(LANGUAGE[0] + " - " + mnApplicationName)
        self.__mnFile = None
        self.__mnTextArea.delete(1.0, END)

    # Function to SAVE FILE
    def __mnSaveFile(self):

        if self.__mnFile == None:
            self.__mnFile = asksaveasfilename(initialfile=LANGUAGE[0] + '.txt',
                                              defaultextension=".txt",
                                              filetypes=[("All Files", "*.*"),
                                                         ("Text Documents", "*.txt")])
            if self.__mnFile == "":
                self.__mnFile = None
            else:
                file = open(self.__mnFile, "w")
                file.write(self.__mnTextArea.get(1.0, END))
                file.close()

                self.__root.title(os.path.basename(self.__mnFile) + " - " + mnApplicationName)

        else:
            file = open(self.__mnFile, "w")
            file.write(self.__mnTextArea.get(1.0, END))
            file.close()

    # Function to CUT
    def __mnCut(self):
        self.__mnTextArea.event_generate("<<Cut>>")

    # Function to COPY
    def __mnCopy(self):
        self.__mnTextArea.event_generate("<<Copy>>")

    # Function to PASTE
    def __mnPaste(self):
        self.__mnTextArea.event_generate("<<Paste>>")

    # Function to set language to English
    def __mnSetEnglish(self):
        f = open("config.txt", "w")
        f.write("LANGUAGE=ENG")
        f.close()
        showinfo("Language", "Restart application to changes to take effect.")

    # Function to set language to Portuguese
    def __mnSetPortugues(self):
        f = open("config.txt", "w")
        f.write("LANGUAGE=POR")
        f.close()
        showinfo("Idioma", "Reinicie a aplicação para as alterações surtirem efeito.")

    # Function to start the application as loop
    def start(self):
        self.__root.mainloop()


# calling the function to start
MiniNotes = MiniNotes(width=600, height=600)
MiniNotes.start()
