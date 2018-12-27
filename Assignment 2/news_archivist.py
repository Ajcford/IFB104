
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9967729
#    Student name: Andrew Ford
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen
from urllib.error import URLError

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd, listdir

# An operating system-specific function for 'normalising' a
# path to a file to the path-naming conventions used on this
# computer.  Apply this function to the full name of your
# HTML document so that your program will work on any
# operating system.
from os.path import *
    
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
import sqlite3

# Import the date and time function.
from datetime import date

# Import this to substitute strings in the rss feed
from re import sub

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################
pass

# This function analyses the html from the archives and uses regular expressions
# to construct a new HTML document

#Connect to database
conn = sqlite3.connect('event_log.db')
c = conn.cursor()
# Initiate event log counter
k = 0

# This function is called when the 'extract news' button is pressed, and it retrieves the code
# from the archives and constructs an HTML document to view  the RSS feed in a website.
def extract_news():
    if listbox.curselection() != (): # Do function when item in listbox is selected
        archive_dir = 'InternetArchive/' + listbox.get(ACTIVE)
        archive_dir = normpath(archive_dir)
        # Open and read the archive
        webpage = open(archive_dir, encoding="utf-8")
        data = webpage.read()
        webpage.close()
        # Replace these funny instances with <, > and & to make regular expressions easier
        data = data.replace('&lt;' , '<') 
        data = data.replace('&gt;', '>')
        data = data.replace('&amp;', '&')
        data = sub('<div id.*</div>', ' ', data) # removes issue with html layout
        
        # Regular expressions to extract useful data from RSS
        article_titles = findall('<title>(.*)</title>', data)
        del article_titles[0] # Title tag was used before article entries in RSS feed
        date_published = findall('<published>(.*)</published>', data)
        link_to_article = findall('<link.*href="([^"]+)".*/>', data)
        del link_to_article[0] # Title tag was used before article entries in RSS feed
        article_names = findall('<name>(.*)</name>', data)
        content = findall('<content type="html">(.*?)</content>', data, flags = DOTALL)
        
        # HTML code used to view news archives
        template = """
        <!doctype html>
        <html>
        <head>
                <meta charset="utf-8">
                <title>The Verge News Feed</title>
                <link href="main.css" rel="stylesheet" type="text/css">
        </head>
        <body>
        <style>
        img {width:85%;margin-left: 7.5%;}
        </style>
            <div style="font-family:arial;max-width: 900px;min-width: 460px;margin-left: auto;
            margin-right: auto;background-color: #d6d4db;border: solid black;">
            <header style="text-align: center;">
                <br>
                <img style="margin:0;" src="logo.gif"/>
                <h1 style="font-size:300%;margin:15px;">News Archive</h1>
                <h1 style="font-size:110%;">News Source: https://www.theverge.com/rss/index.xml</h3>
                <h1 style="font-size:110%;">Archivist: Andrew Ford</h3>
            </header>
                <br>"""
        # Write out each article entry with a for loop (x10) into a string (connect them later
        # with string addition)
        # Initiate counter
        n = 0
        for this_doesnt_matter in range(10):
            # Make date and time look more readable on the webpage
            time = date_published[n][8:10]+'/'+date_published[n][5:7]+'/'+date_published[n][0:4]+', '+date_published[n][11:25]
            template_articles = """
                        <article style="border-top: solid black;padding-left: 7.5%; padding-right: 7.5%;">
                                <h2 style="text-align:center;margin-left:5%;margin-right:5%;">"""+article_titles[n]+"""</h2>
                                """+content[n]+"""
                                <h4>Author: """+article_names[n]+"""</h4>
                                <h4>Date Published: """+time+"""</h4>
                        </article>"""
            # Above, 'content' and 'article_titles' are lists of data from each entry in the RSS.
            template += template_articles # Append each article (string) onto the end of the last
            n = n + 1
        # Join HTML strings to complete HTML code.
        template = template + '</div></body></html>'
        
        # Create/overwrite file and write the HTML to it
        temp = open('temp.html', 'w', encoding = 'UTF-8')
        temp.write(template)
        temp.close()
        # Update text label in the GUI
        instruction['text'] = ("News extracted, ready to display")
        # Update datebase if event logger is ticked
        global k
        if box_ticked.get():
            k = k + 1
            c.execute("INSERT INTO Event_Log (Event_Number, Description) VALUES ("+str(k)+", 'Archive extracted')")
            conn.commit()
    else:
        instruction['text'] = ("Please select news to extract")

## ==========================================================================================

# This function (tied to the 'display news' button) when called, opens the extracted archive
# in the computers default browser.
def display_news():
    if listbox.curselection() != ():
        webopen('temp.html', new = 2)
        # Update text label in GUI
        instruction['text'] = ("News displayed, extract to display another")
        # Update datebase if event logger is ticked
        global k
        if box_ticked.get():
            k = k + 1
            c.execute("INSERT INTO Event_Log (Event_Number, Description) VALUES ("+str(k)+", 'Extracted archive displayed')")
            conn.commit()
    else:
        instruction['text'] = ("Please extract news first")

## ==========================================================================================

# This function reads the RSS feed from The Verge and archives it.
def archiver():
    try:
        # Address of RSS feed
        url = 'https://www.theverge.com/rss/index.xml'
        # Open the web document for reading
        web_page = urlopen(url)
        # Read its contents as a Unicode string
        web_page_contents = web_page.read().decode('UTF-8')
        # Write the contents to a text file appended with the date(overwriting the file if it
        # already exists!)
        filename = 'InternetArchive/Archive_{}.html'.format(date.today())
        filename = normpath(filename)
        html_file = open(filename, 'w', encoding = 'UTF-8')
        html_file.write(web_page_contents)
        html_file.close()
        #Update text in GUI
        instruction['text'] = ("News archived, extract to display")
        update_archive_list()
        # Update datebase if event logger is ticked
        global k
        if box_ticked.get():
            k = k + 1
            c.execute("INSERT INTO Event_Log (Event_Number, Description) VALUES ("+str(k)+", 'Latest news archived')")
            conn.commit()
    # Error handling for when connection isn't made
    except URLError as e:
        ResponseData = e.reason
        instruction['text'] = ("Connection error, please try again later")

## ==========================================================================================

# Create tkinter window 
window = Tk()
window.title("News Archivist")
window.geometry("645x470")
window.configure(background='#c5caed')

# Display title/image in GUI
title_verge = PhotoImage(file="title_verge.gif")
heading = Label(image=title_verge, bd=0, highlightthickness=0, relief='ridge')
heading.grid(row = 0, columnspan = 5, padx = 15, pady = 15)

# Subheading label
text = Label(window, text = 'News Archive', font = ('weight bold', 18), background='#c5caed')
text.grid(row = 1, column = 2)

# Create listbox to contain archive directory
listbox = Listbox(window, width = 30, bd = 4)

# Create function which is called to update the items in the listbox.
# This function is called when ever the 'archive latest' button is pressed.
def update_archive_list():
    directory = getcwd() + '\\InternetArchive'
    directory = normpath(directory)
    archive_list = listdir(directory)
    #Add archives to the listbox
    listbox.delete(0,END)
    n = 0
    for hello in range(len(archive_list)):
        listbox.insert(END, archive_list[n])
        n = n + 1

# Run above function
update_archive_list()

# Function below logs when the Event Logger check box is toggled.
def box_ticked_log():
    global k
    k = k + 1
    c.execute("INSERT INTO Event_Log (Event_Number, Description) VALUES ("+str(k)+", 'Event Logger toggled')")
    conn.commit()

# Configure and place listbox in specified grid
listbox.config(font=(50))
listbox.grid(row = 2, column = 1, columnspan = 3, pady = 5)

# Create checkbutton that allows events to be logged in the datebase
box_ticked = BooleanVar()
event_logger = Checkbutton(window, text="Event Logger", variable = box_ticked, font = (10), background='#c5caed', command = box_ticked_log)
event_logger.grid(row = 2, column = 3, columnspan = 2)

# Create label that tells user how to operate GUI
instruction = Label(window, text = 'Select news to extract', font = ('weight bold', 16), background='#c5caed')
instruction.grid(row = 3, column = 1, pady = 2, columnspan = 3)

# Create button that extracs news from archive
extract = Button(window, text = 'Extract News', command = extract_news)
extract.grid(row = 4, column = 1, sticky = E, pady = 10)

# Create button that opens extracted news in browser
display = Button(window, text = 'Display News', command = display_news)
display.grid(row = 4, column = 2, pady = 10)

# Create button that downloads latest news archive
archive_latest = Button(window, text = 'Archive Latest', command = archiver)
archive_latest.grid(row = 4, column = 3, sticky = W, pady = 10)

window.mainloop()

