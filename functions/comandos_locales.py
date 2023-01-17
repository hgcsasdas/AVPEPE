import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'discord': "C:\\Users\\carls\\AppData\\Local\\Discord\\app-1.0.9008\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'lol': "C:\\Riot Games\\League of Legends\\LeagueClient.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])


def open_League():
    os.startfile(paths['lol'])