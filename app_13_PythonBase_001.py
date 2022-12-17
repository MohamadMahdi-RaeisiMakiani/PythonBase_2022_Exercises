# complex values
#Dar coding meqdare i neveshte nemishe va faqat j ro minevisim
first_place = +1j
second_place = 2+3j
print(first_place,second_place)
X = second_place-first_place
X_TYPE = type(X)
print(X,X_TYPE)
Adad_Elmi = 12e7 #12 ba 7 ta sefr
Adad_Elmi_TYPE = type(Adad_Elmi)
print(Adad_Elmi,Adad_Elmi_TYPE)
#Manfi ---> [ta:az]
#Mosbat ---> [az:ta]
a = "Motherboard"
print(a[-8:-1],a[0:3])
#chr(a) ---> a ===> ascii code
print("Character is : {}".format(chr(98)))
print("ASCII Code is : {}".format(ord("b")))
#ord(b) ---> b ===> character
print(a[::-1])
#Sarotah kardane reshte

# Python Keywords :
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not
# ------------------------------------------------------------------------------
# Python Moudles :
# DictObject          chardet             mmapfile            ssl
# PIL                 chunk               mmsystem            sspi
# PyInstaller         click               modulefinder        sspicon
# PyQt5               cmath               mouseinfo           stackviewer
# __future__          cmd                 msilib              stat
# __main__            code                msvcrt              statistics
# _abc                codecontext         multicall           statusbar
# _ast                codecs              multiprocessing     string
# _asyncio            codeop              netbios             stringprep
# _bisect             collections         netrc               struct
# _blake2             colorama            nntplib             subprocess
# _bootlocale         colorful            nt                  sunau
# _bz2                colorizer           ntpath              symbol
# _cffi_backend       colorsys            ntsecuritycon       symtable
# _codecs             commctrl            nturl2path          sys
# _codecs_cn          compileall          numbers             sysconfig
# _codecs_hk          concurrent          odbc                tabnanny
# _codecs_iso2022     config              opcode              tarfile
# _codecs_jp          config_key          operator            telegram
# _codecs_kr          configdialog        optparse            telnetlib
# _codecs_tw          configparser        ordlookup           tempfile
# _collections        contextlib          os                  test
# _collections_abc    contextvars         outwin              textview
# _compat_pickle      copy                paragraph           textwrap
# _compression        copyreg             parenmatch          this
# _contextvars        crypt               parser              threading
# _csv                cryptography        past                time
# _ctypes             csv                 pathbrowser         timeit
# _ctypes_test        ctypes              pathlib             timer
# _datetime           curses              pdb                 tkinter
# _decimal            dataclasses         pefile              token
# _dummy_thread       datetime            percolator          tokenize
# _elementtree        dbi                 perfmon             tooltip
# _functools          dbm                 peutils             trace
# _hashlib            dde                 pickle              traceback
# _heapq              debugger            pickletools         tracemalloc
# _imp                debugger_r          pip                 tree
# _io                 debugobj            pipes               tty
# _json               debugobj_r          pkg_resources       turtle
# _locale             decimal             pkgutil             turtledemo
# _lsprof             delegator           platform            types
# _lzma               difflib             plistlib            typing
# _markupbase         dis                 poplib              undo
# _md5                distutils           posixpath           unicodedata
# _msi                doctest             pprint              unittest
# _multibytecodec     docutils            profile             urllib
# _multiprocessing    dotenv              pstats              urllib3
# _opcode             dummy_threading     pty                 uu
# _operator           dynoption           py2exe              uuid
# _osx_support        easy_install        py_compile          venv
# _overlapped         editor              pyaes               virtualenv
# _pickle             email               pyautogui           virtualenv_support
# _py_abc             emoji               pyclbr              warnings
# _pydecimal          encodings           pycparser           wave
# _pyio               ensurepip           pydoc               weakref
# _queue              enum                pydoc_data          webbrowser
# _random             errno               pyexpat             win2kras
# _sha1               faulthandler        pygetwindow         win32api
# _sha256             filecmp             pygments            win32clipboard
# _sha3               fileinput           pymsgbox            win32com
# _sha512             filelist            pyparse             win32con
# _signal             fnmatch             pyperclip           win32console
# _sitebuiltins       formatter           pyqt5_tools         win32cred
# _socket             fractions           pyrect              win32crypt
# _sqlite3            ftplib              pyrogram            win32cryptcon
# _sre                functools           pyscreeze           win32ctypes
# _ssl                future              pyshell             win32event
# _stat               garden              pythoncom           win32evtlog
# _string             gc                  pyttsx              win32evtlogutil
# _strptime           genericpath         pyttsx3             win32file
# _struct             getopt              pytweening          win32gui
# _symtable           getpass             pywin               win32gui_struct
# _testbuffer         gettext             pywin32_testutil    win32help
# _testcapi           glob                pywintypes          win32inet
# _testconsole        grep                query               win32inetcon
# _testimportmultiple gtts                queue               win32job
# _testmultiphase     gtts_token          quopri              win32lz
# _thread             gzip                random              win32net
# _threading_local    hashlib             rasutil             win32netcon
# _tkinter            heapq               re                  win32pdh
# _tracemalloc        help                redirector          win32pdhquery
# _warnings           help_about          regcheck            win32pdhutil
# _weakref            history             regutil             win32pipe
# _weakrefset         hmac                replace             win32print
# _win32sysloader     html                reprlib             win32process
# _winapi             http                requests            win32profile
# _winxptheme         hyperparser         rlcompleter         win32ras
# abc                 idle                rpc                 win32rcparser
# adodbapi            idle_test           rstrip              win32security
# afxres              idlelib             run                 win32service
# aifc                idna                runpy               win32serviceutil
# altgraph            imaplib             runscript           win32timezone
# antigravity         imghdr              sched               win32trace
# argparse            imp                 schedule            win32traceutil
# array               importlib           scrolledlist        win32transaction
# asn1crypto          inspect             search              win32ts
# ast                 io                  searchbase          win32ui
# asynchat            iomenu              searchengine        win32uiole
# asyncio             ipaddress           secrets             win32verstamp
# asyncore            isapi               select              win32wnet
# atexit              itertools           selectors           window
# audioop             json                servicemanager      winerror
# autocomplete        keyword             setuptools          winioctlcon
# autocomplete_w      kivy                shelve              winnt
# autoexpand          lib2to3             shlex               winperf
# base64              libfuturize         shutil              winreg
# bdb                 libpasteurize       signal              winsound
# binascii            linecache           site                winxpgui
# binhex              locale              six                 winxptheme
# bisect              logging             smtpd               wsgiref
# browser             luckydonaldUtils    smtplib             xdrlib
# bs4                 lzma                sndhdr              xml
# builtins            macholib            socket              xmlrpc
# bz2                 macosx              socketserver        xxsubtype
# cProfile            macpath             socks               yaspin
# calendar            mailbox             sockshandler        zipapp
# calltip             mailcap             soupsieve           zipextimporter
# calltip_w           mainmenu            sqlite3             zipfile
# certifi             marshal             squeezer            zipimport
# cffi                math                sre_compile         zlib
# cgi                 mimetypes           sre_constants       zoomheight
# cgitb               mmap                sre_parse           zzdummy
# ------------------------------------------------------------------------------
# Python Operators :
# !=                  +                   <=                  __
# "                   +=                  <>                  `
# """                 ,                   ==                  b"
# %                   -                   >                   b'
# %=                  -=                  >=                  f"
# &                   .                   >>                  f'
# &=                  ...                 >>=                 j
# '                   /                   @                   r"
# '''                 //                  J                   r'
# (                   //=                 [                   u"
# )                   /=                  \                   u'
# *                   :                   ]                   |
# **                  <                   ^                   |=
# **=                 <<                  ^=                  ~
# *=                  <<=                 _
# ------------------------------------------------------------------------------
# Python --- :
# ASSERTION           DELETION            LOOPING             SHIFTING
# ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
# ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
# ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
# AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
# BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
# BINARY              EXECUTION           NONE                STRINGS
# BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
# BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
# CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
# CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
# CLASSES             FRAMES              PACKAGES            TUPLES
# CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
# COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
# COMPLEX             IMPORTING           PRIVATENAMES        UNARY
# CONDITIONAL         INTEGER             RETURNING           UNICODE
# CONTEXTMANAGERS     LISTLITERALS        SCOPING
# CONVERSIONS         LISTS               SEQUENCEMETHODS
# DEBUGGING           LITERALS            SEQUENCES
# ------------------------------------------------------------------------------
# Python Str_Functions :
# capitalize|          casefold|        center|      count|
# encode              endswith|        expandtabs|  find|
# format|              format_map      index|       isalnum|
# isalpha|             isascii         isdecimal   isdigit|
# isidentifier        islower|         isnumeric   isprintable
# isspace             istitle         isupper     join|
# ljust|               lower|           lstrip|      makertrans
# partition           replace|         rfind       rindex
# rjust|               rpartition      rsplit      rstrip|
# split|               splitlines|      startswith|  strip
# swapcase|            title|           translate   upper|
# zfill|

My_STR_1 = "hello world"
My_STR_2 = "HELLO"
My_STR_3 = "world"
My_STR_4 = "pYtHoN"
My_STR_5 = "I Like Python Programming"
My_STR_6 = "I+Don't+Like+Python+Programming"
My_STR_7 = "I\nWant\nSome\nCheese."
My_STR_8 = "Sausage"
My_STR_9 = "Pink\tPanther"
My_STR_10 = "        Tom&Jerry        "
My_STR_11 = "                "
My_STR_12 = "2a"
My_STR_13 = " a"
My_STR_14 = "5412368"
print(My_STR_1.capitalize())
# Hello world
print(My_STR_1.upper())
# HELLO WORLD
print(My_STR_2.lower())
# hello
print(My_STR_1.title())#Avale har kalame bozorg
# Hello World
print(My_STR_1.find("l"))
# 2
print(My_STR_4.swapcase())
# PyThOn
print(My_STR_3.replace("l","-"))
# wor-d
print(My_STR_1.count("l"))
# 3
print(My_STR_4.count("Y",3,5))
# 0
print(My_STR_2.casefold())#Mese lower
# hello
print(My_STR_2.index("L"))#Peyda kardan shomare khoone
# 2
print(My_STR_1.startswith("i"))
# False
print(My_STR_1.endswith("d"))
# True
print(My_STR_5.split())#Jodasazi har ja space bashe ba khorooji list
# ['I', 'Like', 'Python', 'Programming']
print(My_STR_6.split("+"))#Jodasazi har ja + bashe ba khorooji list
# ['I', "Don't", 'Like', 'Python', 'Programming']
print(My_STR_7.splitlines())#Jodasazi har ja \n bashe(Yani har ja bere khat bad) ba khorooji list
# ['I', 'Want', 'Some', 'Cheese.']
print(My_STR_8.zfill(15))#Andaze 15 char kole string har cheqad kam oomad 0 mizare
#00000000Sausage
print(My_STR_9)
print(My_STR_9.expandtabs(16))#B andaze 16 space tab mikhore(1 tab va nesf adad)
print(My_STR_10.lstrip())#Pak kardane space az samte chap
print(My_STR_10.rstrip())#Pak kardane space az samte rast
print(My_STR_8.center(25))#Kole Reshte 25 My_STR_8 dar vasat baqiash jaye khali
print(My_STR_8.center(25,"$"))#Kole Reshte 25 My_STR_8 dar vasat baqiash $
print(My_STR_8.ljust(15,"R"))#Kole Reshte 15 My_STR_8 dar chap baqiash $
print(My_STR_8.rjust(15,"R"))#Kole Reshte 15 My_STR_8 dar rast baqiash $
print("/".join(My_STR_8))# / Bein hame khanehaye My_STR_8 qarar migire
print(My_STR_11.isspace())#Just spaces
print(My_STR_12.isidentifier())
print(My_STR_13.isidentifier())
print(My_STR_8.isidentifier())
print(My_STR_2.isupper())#Just Big Alphabet
print(My_STR_3.islower())#Just Small Alphabet
print(My_STR_2.isalpha())#Just alphabet
print(My_STR_12.isalnum())#Alphabet and Numbers
print(My_STR_14.isdigit())#Just number
Name__1 = "Patrik"
print(Name__1)
del Name__1
try:
    print(Name__1)
except:
    Error_Message = "This string."
    print("We don't have {}".format(Error_Message))

os.listdir(r"C:\Users\DeadGhost\Desktop\PythonScripts\HTML")
# ['First_Page.html', 'MySecondPage.htm', 'My_Pic_For_HTMLPage.jpg']
