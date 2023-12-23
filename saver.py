#!/usr/bin/python
import os;
import glob;
import shutil;
from datetime import datetime;

from tkinter import *;
from tkinter import messagebox;

class Saver:
    def __init__(self):
        self.data_path = os.path.expanduser('~') + '/.crawl/saves/';
        if not os.path.isdir(self.data_path):
            print('Dungeon Crawl Stone Stone Soup not installed?');
            return;
        self.save_path = self.data_path + 'dcss_saver/';
        if not os.path.isdir(self.save_path): 
            os.makedirs(self.save_path);
    
        self.app = Tk();
        try:
            self.app.iconphoto(False, PhotoImage(file = os.getcwd() + '/saver.png'));
        except TclError as ex:
            print(ex);
        self.app.title('DCSS Dummy Saver v0.1')
        self.characterbox = Listbox();
        self.characterbox.pack(side = LEFT);
        self.characterscroll = Scrollbar(command = self.characterbox.yview);
        self.characterscroll.pack(side = LEFT, fill = Y);
        self.characterbox.config(yscrollcommand = self.characterscroll.set);
    
        self.savebox = Listbox();
        self.savebox.pack(side = RIGHT);
        self.savesscroll = Scrollbar(command = self.savebox.yview);
        self.savesscroll.pack(side = RIGHT, fill = Y);
        self.savebox.config(yscrollcommand = self.savesscroll.set);

        self.frame = Frame();
        self.frame.pack(side = TOP, padx = 10);

        Button(self.frame, text="Save character->", command = self.save_character).pack(fill = X);
        Button(self.frame, text="< - Load save", command = self.load_save).pack(fill = X);
        Button(self.frame, text="Delete save ->", command = self.delete_save).pack(fill = X);
        Button(self.frame, text="<- Delete character", command = self.delete_character).pack(fill = X);
    
        self.reload_characters(); self.reload_saves();

    def reload_saves(self):
        self.savebox.delete(0, END);
        for save in glob.glob(self.save_path + '*.cs'):
            self.savebox.insert(END, os.path.basename(save));
        return;

    def reload_characters(self):
        self.characterbox.delete(0, END);
        for charachter in glob.glob(self.data_path + '*.cs'):
            self.characterbox.insert(END, os.path.basename(charachter));
        return;
 
    def save_character(self):
        index = self.characterbox.curselection();
        if index != ():
            charachter = self.characterbox.get(index);
            # if self.question('Saving character ' + charachter):
            shutil.copy2(self.data_path + charachter, self.save_path + self.charachtertosave(charachter));
        self.reload_saves();
        return;
    
    def load_save(self):
        index = self.savebox.curselection();
        if index != ():
            save = self.savebox.get(index);
            if self.question('Load save ' + save + ' ?'):
                shutil.copy2(self.save_path + save, self.data_path + self.savetocharacter(save));
        self.reload_characters();
        return;
    
    def delete_save(self):
        index = self.savebox.curselection();
        if index != ():
            save = self.savebox.get(index);
            if self.question('Delete save ' + save + ' ? This can\'t be undo'):
                os.remove(self.save_path + save);
        self.reload_saves();
        return;

    def delete_character(self):
        index = self.characterbox.curselection();
        if index != ():
            chatacter = self.characterbox.get(index);
            if self.question('Delete character ' + chatacter + ' ? This can\'t be undo'):
                os.remove(self.data_path + chatacter);
        self.reload_characters();
        return;

    def question(self, text:str):
        answer = messagebox.askquestion('Are you sure?', text, icon = 'question');
        return answer == 'yes';

    def charachtertosave(self, text:str):
        return datetime.now().strftime(text.removesuffix('.cs') + '.%m-%d-%Y_%H-%M-%S.cs');

    def savetocharacter(self, text:str):
        return text.split('.')[0] + '.cs';

saver = Saver();
saver.app.mainloop();